"""
RA-MARS v4 Improved Sequence Model Training

Key improvements over v3:
1. Hierarchical classification: binary (attack/normal) + 7-class attack type
   - Binary model targets >=85% macro F1 (operationally meaningful)
   - Fine-grained model retained for research completeness
2. Deeper architecture: 2 LSTM layers, hidden=128, dropout=0.4
3. More epochs with early stopping (patience=10)
4. Focal loss to handle class imbalance better than weighted CE
5. Label smoothing (0.1) to prevent overconfidence
6. Gradient clipping (max_norm=1.0)
7. Train/val/test split: 70/15/15 (stratified)
8. Best model checkpoint saved by val F1

Input:  simulations/datasets/uav_sequence_windows_v4.npz
Output: simulations/results/model_performance_v4_*.csv
"""

import os
import random
import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import torch.nn.functional as F

from torch.utils.data import DataLoader, TensorDataset
from sklearn.model_selection import train_test_split
from sklearn.metrics import (accuracy_score, precision_score,
                              recall_score, f1_score,
                              classification_report, confusion_matrix)
from sklearn.preprocessing import StandardScaler

DATA_PATH  = "simulations/datasets/uav_sequence_windows_v4.npz"
OUTPUT_DIR = "simulations/results"
os.makedirs(OUTPUT_DIR, exist_ok=True)

RANDOM_SEED   = 42
BATCH_SIZE    = 128
EPOCHS        = 50
LR            = 0.001
HIDDEN_SIZE   = 128
NUM_LAYERS    = 2
DROPOUT       = 0.40
PATIENCE      = 10       # early stopping
GRAD_CLIP     = 1.0
LABEL_SMOOTH  = 0.1


def set_seed(seed=RANDOM_SEED):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)


# ── Focal Loss ────────────────────────────────────────────────────
class FocalLoss(nn.Module):
    """
    Focal Loss for class imbalance.
    FL(p) = -alpha * (1 - p)^gamma * log(p)
    gamma=2 focuses training on hard/misclassified examples.
    """
    def __init__(self, gamma=2.0, weight=None, label_smoothing=0.0):
        super().__init__()
        self.gamma = gamma
        self.weight = weight
        self.label_smoothing = label_smoothing

    def forward(self, inputs, targets):
        ce = F.cross_entropy(inputs, targets, weight=self.weight,
                             label_smoothing=self.label_smoothing,
                             reduction='none')
        pt = torch.exp(-ce)
        focal = (1 - pt) ** self.gamma * ce
        return focal.mean()


# ── Models ────────────────────────────────────────────────────────
class LSTMClassifier(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, num_classes, dropout):
        super().__init__()
        self.lstm = nn.LSTM(input_size, hidden_size, num_layers,
                            batch_first=True, dropout=dropout if num_layers > 1 else 0)
        self.bn   = nn.LayerNorm(hidden_size)
        self.drop = nn.Dropout(dropout)
        self.fc   = nn.Linear(hidden_size, num_classes)

    def forward(self, x):
        _, (h, _) = self.lstm(x)
        out = self.bn(h[-1])
        out = self.drop(out)
        return self.fc(out)


class GRUClassifier(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, num_classes, dropout):
        super().__init__()
        self.gru  = nn.GRU(input_size, hidden_size, num_layers,
                           batch_first=True, dropout=dropout if num_layers > 1 else 0)
        self.bn   = nn.LayerNorm(hidden_size)
        self.drop = nn.Dropout(dropout)
        self.fc   = nn.Linear(hidden_size, num_classes)

    def forward(self, x):
        _, h = self.gru(x)
        out = self.bn(h[-1])
        out = self.drop(out)
        return self.fc(out)


# ── Data loading ──────────────────────────────────────────────────
def load_data():
    data   = np.load(DATA_PATH, allow_pickle=True)
    X      = data["X"].astype(np.float32)
    y      = data["y"].astype(np.int64)
    labels = list(data["labels"])
    return X, y, labels


def make_binary_labels(y, labels):
    """Convert 8-class labels to binary: 0=normal, 1=attack."""
    normal_idx = labels.index("normal")
    return (y != normal_idx).astype(np.int64)


def make_splits(X, y):
    """70/15/15 stratified split."""
    X_tv, X_test, y_tv, y_test = train_test_split(
        X, y, test_size=0.15, random_state=RANDOM_SEED, stratify=y)
    X_train, X_val, y_train, y_val = train_test_split(
        X_tv, y_tv, test_size=0.15/0.85, random_state=RANDOM_SEED, stratify=y_tv)
    return X_train, X_val, X_test, y_train, y_val, y_test



def scale_splits_train_only(X_train, X_val, X_test):
    """
    Fit StandardScaler only on the training split to avoid preprocessing leakage.
    The same train-fitted scaler is applied to validation and test splits.
    """
    n_train, seq_len, n_feat = X_train.shape

    scaler = StandardScaler()
    X_train_2d = X_train.reshape(-1, n_feat)
    scaler.fit(X_train_2d)

    def transform(X):
        n = X.shape[0]
        X_2d = X.reshape(-1, n_feat)
        X_scaled = scaler.transform(X_2d)
        return X_scaled.reshape(n, seq_len, n_feat).astype(np.float32)

    return transform(X_train), transform(X_val), transform(X_test), scaler


def make_loaders(X_train, X_val, X_test, y_train, y_val, y_test):
    def loader(X, y, shuffle):
        return DataLoader(
            TensorDataset(torch.tensor(X), torch.tensor(y)),
            batch_size=BATCH_SIZE, shuffle=shuffle)
    return (loader(X_train, y_train, True),
            loader(X_val,   y_val,   False),
            loader(X_test,  y_test,  False))


def class_weights_tensor(y_train, num_classes):
    counts  = np.bincount(y_train, minlength=num_classes)
    weights = counts.sum() / (num_classes * np.maximum(counts, 1))
    return torch.tensor(weights, dtype=torch.float32)


# ── Training ──────────────────────────────────────────────────────
def train_model(model, train_loader, val_loader, device, criterion, model_name):
    optimizer  = torch.optim.Adam(model.parameters(), lr=LR, weight_decay=1e-4)
    scheduler  = torch.optim.lr_scheduler.ReduceLROnPlateau(
        optimizer, mode='max', factor=0.5, patience=5)

    best_val_f1   = -1.0
    best_state    = None
    patience_ctr  = 0

    for epoch in range(1, EPOCHS + 1):
        # Train
        model.train()
        total_loss = 0.0
        for Xb, yb in train_loader:
            Xb, yb = Xb.to(device), yb.to(device)
            optimizer.zero_grad()
            loss = criterion(model(Xb), yb)
            loss.backward()
            nn.utils.clip_grad_norm_(model.parameters(), GRAD_CLIP)
            optimizer.step()
            total_loss += loss.item()

        # Validate
        model.eval()
        val_preds, val_true = [], []
        with torch.no_grad():
            for Xb, yb in val_loader:
                val_preds.extend(torch.argmax(model(Xb.to(device)), dim=1).cpu().numpy())
                val_true.extend(yb.numpy())
        val_f1 = f1_score(val_true, val_preds, average='macro', zero_division=0)
        scheduler.step(val_f1)

        if epoch % 5 == 0 or epoch == 1:
            print(f"  [{model_name}] Ep {epoch:02d}/{EPOCHS} "
                  f"loss={total_loss/len(train_loader):.4f} val_F1={val_f1:.4f}")

        if val_f1 > best_val_f1:
            best_val_f1 = val_f1
            best_state  = {k: v.clone() for k, v in model.state_dict().items()}
            patience_ctr = 0
        else:
            patience_ctr += 1
            if patience_ctr >= PATIENCE:
                print(f"  [{model_name}] Early stop at epoch {epoch} (best val F1={best_val_f1:.4f})")
                break

    model.load_state_dict(best_state)
    return model


def evaluate(name, model, test_loader, y_test, labels, device):
    model.eval()
    preds = []
    with torch.no_grad():
        for Xb, _ in test_loader:
            preds.extend(torch.argmax(model(Xb.to(device)), dim=1).cpu().numpy())
    preds = np.array(preds)

    perf = {
        "model":              name,
        "accuracy":           accuracy_score(y_test, preds),
        "precision_macro":    precision_score(y_test, preds, average="macro",    zero_division=0),
        "recall_macro":       recall_score(y_test, preds, average="macro",       zero_division=0),
        "f1_macro":           f1_score(y_test, preds, average="macro",           zero_division=0),
        "precision_weighted": precision_score(y_test, preds, average="weighted", zero_division=0),
        "recall_weighted":    recall_score(y_test, preds, average="weighted",    zero_division=0),
        "f1_weighted":        f1_score(y_test, preds, average="weighted",        zero_division=0),
    }

    report = classification_report(y_test, preds, target_names=labels,
                                    output_dict=True, zero_division=0)
    per_class = [{"model": name, "class": lbl,
                  "precision": report[lbl]["precision"],
                  "recall":    report[lbl]["recall"],
                  "f1_score":  report[lbl]["f1-score"],
                  "support":   report[lbl]["support"]} for lbl in labels]

    cm_df = pd.DataFrame(confusion_matrix(y_test, preds),
                         index=labels, columns=labels)
    return perf, per_class, cm_df


# ── Main ──────────────────────────────────────────────────────────
def main():
    set_seed()
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Device: {device}\n")

    X, y, labels = load_data()
    print(f"Loaded: {X.shape[0]:,} windows | {X.shape[2]} features | {len(labels)} classes")
    print(f"Classes: {labels}\n")

    # ── TASK 1: Binary classifier (attack / normal) ───────────────
    print("=" * 60)
    print("TASK 1: Binary classification (normal vs. attack)")
    print("=" * 60)

    y_bin    = make_binary_labels(y, labels)
    bin_lbls = ["normal", "attack"]

    Xtr, Xvl, Xte, ytr, yvl, yte = make_splits(X, y_bin)
    Xtr, Xvl, Xte, bin_scaler = scale_splits_train_only(Xtr, Xvl, Xte)
    print("Applied train-only feature standardization for binary LSTM/GRU task.")
    tr_l, vl_l, te_l = make_loaders(Xtr, Xvl, Xte, ytr, yvl, yte)
    w_bin = class_weights_tensor(ytr, 2)

    bin_results, bin_per_class, bin_cms = [], [], {}

    for name, ModelCls in [("Binary LSTM", LSTMClassifier),
                            ("Binary GRU",  GRUClassifier)]:
        print(f"\nTraining {name}...")
        model = ModelCls(X.shape[2], HIDDEN_SIZE, NUM_LAYERS, 2, DROPOUT).to(device)
        crit  = FocalLoss(gamma=2.0, weight=w_bin.to(device), label_smoothing=LABEL_SMOOTH)
        model = train_model(model, tr_l, vl_l, device, crit, name)
        perf, pc, cm = evaluate(name, model, te_l, yte, bin_lbls, device)
        print(f"  Test macro F1: {perf['f1_macro']:.4f} | Accuracy: {perf['accuracy']:.4f}")
        bin_results.append(perf)
        bin_per_class.extend(pc)
        bin_cms[name] = cm
        # Save each binary model
        model_path = os.path.join(OUTPUT_DIR, f"best_model_v4_{name.replace(' ','_').lower()}.pt")
        torch.save({'model_state_dict': model.state_dict(),
                    'input_size': X.shape[2],
                    'hidden_size': HIDDEN_SIZE,
                    'num_layers': NUM_LAYERS,
                    'num_classes': 2,
                    'model_name': name}, model_path)
        print(f"  Saved: {model_path}")

    # ── TASK 2: Fine-grained 8-class (retained from v3) ──────────
    print("\n" + "=" * 60)
    print("TASK 2: Fine-grained 8-class classification")
    print("=" * 60)

    Xtr, Xvl, Xte, ytr, yvl, yte = make_splits(X, y)
    Xtr, Xvl, Xte, fg_scaler = scale_splits_train_only(Xtr, Xvl, Xte)
    print("Applied train-only feature standardization for fine-grained LSTM/GRU task.")
    tr_l, vl_l, te_l = make_loaders(Xtr, Xvl, Xte, ytr, yvl, yte)
    w8 = class_weights_tensor(ytr, len(labels))

    fg_results, fg_per_class, fg_cms = [], [], {}
    best_f1 = -1

    for name, ModelCls in [("Weighted LSTM v4", LSTMClassifier),
                            ("Weighted GRU v4",  GRUClassifier)]:
        print(f"\nTraining {name}...")
        model = ModelCls(X.shape[2], HIDDEN_SIZE, NUM_LAYERS, len(labels), DROPOUT).to(device)
        crit  = FocalLoss(gamma=2.0, weight=w8.to(device), label_smoothing=LABEL_SMOOTH)
        model = train_model(model, tr_l, vl_l, device, crit, name)
        perf, pc, cm = evaluate(name, model, te_l, yte, labels, device)
        print(f"  Test macro F1: {perf['f1_macro']:.4f} | Accuracy: {perf['accuracy']:.4f}")
        fg_results.append(perf)
        fg_per_class.extend(pc)
        if perf['f1_macro'] > best_f1:
            best_f1 = perf['f1_macro']
            fg_cms['best'] = cm

    # ── Save results ──────────────────────────────────────────────
    # Save best binary model for adversarial robustness testing
    best_bin_f1 = max(bin_results, key=lambda x: x['f1_macro'])
    best_bin_name = best_bin_f1['model']
    print(f"\nSaving best binary model: {best_bin_name} (F1={best_bin_f1['f1_macro']:.4f})")

    pd.DataFrame(bin_results).to_csv(
        os.path.join(OUTPUT_DIR, "model_performance_v4_binary.csv"), index=False)
    pd.DataFrame(bin_per_class).to_csv(
        os.path.join(OUTPUT_DIR, "per_class_metrics_v4_binary.csv"), index=False)
    for name, cm in bin_cms.items():
        safe = name.replace(" ", "_").lower()
        cm.to_csv(os.path.join(OUTPUT_DIR, f"confusion_matrix_v4_{safe}.csv"))

    pd.DataFrame(fg_results).to_csv(
        os.path.join(OUTPUT_DIR, "model_performance_v4_finegrained.csv"), index=False)
    pd.DataFrame(fg_per_class).to_csv(
        os.path.join(OUTPUT_DIR, "per_class_metrics_v4_finegrained.csv"), index=False)
    if 'best' in fg_cms:
        fg_cms['best'].to_csv(
            os.path.join(OUTPUT_DIR, "confusion_matrix_v4_finegrained_best.csv"))

    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print("\nBinary (attack/normal):")
    for r in bin_results:
        print(f"  {r['model']:20s}: F1={r['f1_macro']:.4f}  Acc={r['accuracy']:.4f}")
    print("\nFine-grained (8-class):")
    for r in fg_results:
        print(f"  {r['model']:20s}: F1={r['f1_macro']:.4f}  Acc={r['accuracy']:.4f}")
    print("\nAll results saved to:", OUTPUT_DIR)


if __name__ == "__main__":
    main()

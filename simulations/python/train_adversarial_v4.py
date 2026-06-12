"""
RA-MARS v4 Adversarial Training

Retrains the binary LSTM with PGD-augmented examples mixed into
each training batch. This hardens the classifier against white-box
adversarial perturbations (FGSM, PGD) that currently drop F1 to 0.307.

Target: F1 >= 0.80 at FGSM ε=0.01 (up from 0.307)

Method: PGD adversarial training (Madry et al. 2018)
- Mix ratio: 50% clean + 50% adversarial per batch
- PGD steps: 7, step size α=0.01, ε=0.03
- Same architecture as clean model (hidden=128, 2-layer, dropout=0.4)
- Saves: best_model_v4_adversarial.pt

Input:  simulations/datasets/uav_sequence_windows_v4.npz
Output: simulations/results/adversarial_training_results_v4.csv
        simulations/results/best_model_v4_adversarial.pt
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
from sklearn.metrics import f1_score, accuracy_score

DATA_PATH  = "simulations/datasets/uav_sequence_windows_v4.npz"
OUTPUT_DIR = "simulations/results"
os.makedirs(OUTPUT_DIR, exist_ok=True)

RANDOM_SEED  = 42
BATCH_SIZE   = 128
EPOCHS       = 40
LR           = 0.001
HIDDEN_SIZE  = 128
NUM_LAYERS   = 2
DROPOUT      = 0.40
PATIENCE     = 8
GRAD_CLIP    = 1.0

# Adversarial training parameters
ADV_EPS      = 0.03    # training perturbation budget
ADV_ALPHA    = 0.007   # PGD step size
ADV_STEPS    = 7       # PGD iterations
ADV_MIX      = 0.5     # fraction of adversarial examples per batch

# Evaluation perturbation budgets
EVAL_EPS_FGSM = [0.01, 0.05, 0.10, 0.20, 0.30]
EVAL_EPS_PGD  = [0.05, 0.10, 0.20]

def set_seed(seed=RANDOM_SEED):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)

class LSTMClassifier(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, num_classes, dropout):
        super().__init__()
        self.lstm = nn.LSTM(input_size, hidden_size, num_layers,
                            batch_first=True,
                            dropout=dropout if num_layers > 1 else 0)
        self.bn   = nn.LayerNorm(hidden_size)
        self.drop = nn.Dropout(dropout)
        self.fc   = nn.Linear(hidden_size, num_classes)

    def forward(self, x):
        _, (h, _) = self.lstm(x)
        return self.fc(self.drop(self.bn(h[-1])))

class FocalLoss(nn.Module):
    def __init__(self, gamma=2.0, weight=None, label_smoothing=0.1):
        super().__init__()
        self.gamma = gamma
        self.weight = weight
        self.label_smoothing = label_smoothing

    def forward(self, inputs, targets):
        ce  = F.cross_entropy(inputs, targets, weight=self.weight,
                              label_smoothing=self.label_smoothing, reduction='none')
        pt  = torch.exp(-ce)
        return ((1 - pt) ** self.gamma * ce).mean()

def pgd_attack(model, X, y, epsilon, alpha, n_steps, criterion):
    """PGD adversarial example generation."""
    model.train()  # Required for cuDNN RNN backward during PGD
    X_adv = X.clone().detach() + torch.empty_like(X).uniform_(-epsilon, epsilon)
    X_adv = torch.clamp(X_adv, X - epsilon, X + epsilon).detach()
    for _ in range(n_steps):
        X_adv.requires_grad_(True)
        loss = criterion(model(X_adv), y)
        loss.backward()
        with torch.no_grad():
            X_adv = X_adv + alpha * X_adv.grad.sign()
            X_adv = torch.clamp(X_adv, X - epsilon, X + epsilon).detach()
    model.train()
    return X_adv

def fgsm_attack(model, X, y, epsilon, criterion):
    """FGSM adversarial example generation."""
    model.train()
    X_adv = X.clone().detach().requires_grad_(True)
    loss = criterion(model(X_adv), y)
    loss.backward()
    return (X_adv + epsilon * X_adv.grad.sign()).detach()

def evaluate_clean(model, loader, device):
    model.eval()
    preds, trues = [], []
    with torch.no_grad():
        for Xb, yb in loader:
            preds.extend(torch.argmax(model(Xb.to(device)), 1).cpu().numpy())
            trues.extend(yb.numpy())
    return (f1_score(trues, preds, average='macro', zero_division=0),
            accuracy_score(trues, preds))

def evaluate_adversarial(model, loader, device, attack_fn, criterion):
    model.eval()
    preds, trues = [], []
    for Xb, yb in loader:
        Xb, yb = Xb.to(device), yb.to(device)
        X_adv  = attack_fn(model, Xb, yb, criterion)
        model.eval()
        with torch.no_grad():
            preds.extend(torch.argmax(model(X_adv), 1).cpu().numpy())
            trues.extend(yb.cpu().numpy())
    return f1_score(trues, preds, average='macro', zero_division=0)

def main():
    set_seed()
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Device: {device}")

    # Load data
    data   = np.load(DATA_PATH, allow_pickle=True)
    X      = data["X"].astype(np.float32)
    y      = data["y"].astype(np.int64)
    labels = list(data["labels"])

    # Binary labels
    normal_idx = labels.index("normal")
    y_bin = (y != normal_idx).astype(np.int64)

    print(f"Loaded: {X.shape[0]:,} windows | {X.shape[2]} features")
    print(f"Binary class distribution: normal={np.sum(y_bin==0):,} attack={np.sum(y_bin==1):,}")

    # 70/15/15 split
    X_tv, X_test, y_tv, y_test = train_test_split(
        X, y_bin, test_size=0.15, random_state=RANDOM_SEED, stratify=y_bin)
    X_train, X_val, y_train, y_val = train_test_split(
        X_tv, y_tv, test_size=0.15/0.85, random_state=RANDOM_SEED, stratify=y_tv)

    def loader(Xa, ya, shuffle):
        return DataLoader(TensorDataset(torch.tensor(Xa), torch.tensor(ya)),
                          batch_size=BATCH_SIZE, shuffle=shuffle)

    train_loader = loader(X_train, y_train, True)
    val_loader   = loader(X_val,   y_val,   False)
    test_loader  = loader(X_test,  y_test,  False)

    # Class weights
    counts  = np.bincount(y_train, minlength=2)
    weights = torch.tensor(counts.sum() / (2 * np.maximum(counts, 1)),
                           dtype=torch.float32).to(device)

    # Model
    model     = LSTMClassifier(X.shape[2], HIDDEN_SIZE, NUM_LAYERS, 2, DROPOUT).to(device)
    criterion = FocalLoss(gamma=2.0, weight=weights, label_smoothing=0.1)
    optimizer = torch.optim.Adam(model.parameters(), lr=LR, weight_decay=1e-4)
    scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(
        optimizer, mode='max', factor=0.5, patience=4)

    best_val_f1  = -1.0
    best_state   = None
    patience_ctr = 0

    print(f"\nAdversarial training: ε={ADV_EPS}, α={ADV_ALPHA}, steps={ADV_STEPS}, mix={ADV_MIX}")
    print(f"Epochs: {EPOCHS}, patience: {PATIENCE}\n")

    for epoch in range(1, EPOCHS + 1):
        model.train()
        total_loss = 0.0

        for Xb, yb in train_loader:
            Xb, yb = Xb.to(device), yb.to(device)

            # Generate adversarial examples for half the batch
            n_adv = int(len(Xb) * ADV_MIX)
            if n_adv > 0:
                Xb_adv = pgd_attack(model, Xb[:n_adv], yb[:n_adv],
                                    ADV_EPS, ADV_ALPHA, ADV_STEPS, criterion)
                Xb_mix = torch.cat([Xb[n_adv:], Xb_adv], dim=0)
                yb_mix = torch.cat([yb[n_adv:], yb[:n_adv]], dim=0)
            else:
                Xb_mix, yb_mix = Xb, yb

            model.train()
            optimizer.zero_grad()
            loss = criterion(model(Xb_mix), yb_mix)
            loss.backward()
            nn.utils.clip_grad_norm_(model.parameters(), GRAD_CLIP)
            optimizer.step()
            total_loss += loss.item()

        # Validate on clean data
        val_f1, val_acc = evaluate_clean(model, val_loader, device)
        scheduler.step(val_f1)

        if epoch % 5 == 0 or epoch == 1:
            print(f"  Ep {epoch:02d}/{EPOCHS} loss={total_loss/len(train_loader):.4f} "
                  f"val_F1={val_f1:.4f} val_acc={val_acc:.4f}")

        if val_f1 > best_val_f1:
            best_val_f1  = val_f1
            best_state   = {k: v.clone() for k, v in model.state_dict().items()}
            patience_ctr = 0
        else:
            patience_ctr += 1
            if patience_ctr >= PATIENCE:
                print(f"  Early stop at epoch {epoch} (best val F1={best_val_f1:.4f})")
                break

    model.load_state_dict(best_state)

    # Save model
    model_path = os.path.join(OUTPUT_DIR, "best_model_v4_adversarial.pt")
    torch.save(model.state_dict(), model_path)
    print(f"\n✓ Saved adversarially trained model: {model_path}")

    # Evaluate clean
    clean_f1, clean_acc = evaluate_clean(model, test_loader, device)
    print(f"\nClean performance: F1={clean_f1:.4f} Acc={clean_acc:.4f}")

    results = []

    # FGSM evaluation
    print("\nFGSM robustness:")
    for eps in EVAL_EPS_FGSM:
        f1 = evaluate_adversarial(
            model, test_loader, device,
            lambda m, X, y, c: fgsm_attack(m, X, y, eps, c),
            criterion)
        drop = (clean_f1 - f1) * 100
        results.append({'attack': 'FGSM', 'epsilon': eps,
                        'clean_f1': clean_f1, 'adv_f1': f1, 'f1_drop_pct': drop})
        print(f"  ε={eps:.2f}: F1={f1:.4f} (drop={drop:.1f}%)")

    # PGD evaluation
    print("\nPGD robustness:")
    for eps in EVAL_EPS_PGD:
        f1 = evaluate_adversarial(
            model, test_loader, device,
            lambda m, X, y, c: pgd_attack(m, X, y, eps, ADV_ALPHA, 20, c),
            criterion)
        drop = (clean_f1 - f1) * 100
        results.append({'attack': 'PGD', 'epsilon': eps,
                        'clean_f1': clean_f1, 'adv_f1': f1, 'f1_drop_pct': drop})
        print(f"  ε={eps:.2f}: F1={f1:.4f} (drop={drop:.1f}%)")

    df = pd.DataFrame(results)
    df.to_csv(os.path.join(OUTPUT_DIR, "adversarial_training_results_v4.csv"), index=False)

    print(f"\n{'='*50}")
    print("ADVERSARIAL TRAINING SUMMARY")
    print(f"{'='*50}")
    print(f"Clean F1:           {clean_f1:.4f}")
    print(f"FGSM ε=0.01 F1:     {df[df['epsilon']==0.01]['adv_f1'].values[0]:.4f}")
    print(f"FGSM ε=0.05 F1:     {df[(df['attack']=='FGSM') & (df['epsilon']==0.05)]['adv_f1'].values[0]:.4f}")
    print(f"PGD  ε=0.05 F1:     {df[(df['attack']=='PGD')  & (df['epsilon']==0.05)]['adv_f1'].values[0]:.4f}")
    print(f"\n✓ Results saved to {OUTPUT_DIR}/adversarial_training_results_v4.csv")

if __name__ == "__main__":
    main()

"""
RA-MARS v4 1D-CNN Temporal Baseline

Purpose:
- Adds a non-recurrent temporal deep-learning baseline for reviewer rigor.
- Uses raw v4 sequence windows.
- Fits StandardScaler only on the training split to avoid preprocessing leakage.
- Evaluates both binary attack-vs-normal and fine-grained 8-class classification.
"""

import os
import random
import numpy as np
import pandas as pd
import torch
import torch.nn as nn

from torch.utils.data import DataLoader, TensorDataset
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.preprocessing import StandardScaler

DATA_PATH = "simulations/datasets/uav_sequence_windows_v4.npz"
OUTPUT_DIR = "simulations/results"
os.makedirs(OUTPUT_DIR, exist_ok=True)

RANDOM_SEED = 42
BATCH_SIZE = 128
EPOCHS = 35
LR = 0.001
PATIENCE = 7


def set_seed(seed=RANDOM_SEED):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)


class CNN1DClassifier(nn.Module):
    def __init__(self, input_features, num_classes):
        super().__init__()
        self.net = nn.Sequential(
            nn.Conv1d(input_features, 64, kernel_size=3, padding=1),
            nn.BatchNorm1d(64),
            nn.ReLU(),
            nn.Dropout(0.25),

            nn.Conv1d(64, 128, kernel_size=3, padding=1),
            nn.BatchNorm1d(128),
            nn.ReLU(),
            nn.Dropout(0.25),

            nn.AdaptiveAvgPool1d(1),
        )
        self.fc = nn.Linear(128, num_classes)

    def forward(self, x):
        x = x.transpose(1, 2)
        x = self.net(x).squeeze(-1)
        return self.fc(x)


def load_data():
    data = np.load(DATA_PATH, allow_pickle=True)
    X = data["X"].astype(np.float32)
    y = data["y"].astype(np.int64)
    labels = list(data["labels"])
    return X, y, labels


def make_binary_labels(y, labels):
    normal_idx = labels.index("normal")
    return (y != normal_idx).astype(np.int64)


def split_and_scale(X, y):
    X_tv, X_test, y_tv, y_test = train_test_split(
        X, y, test_size=0.15, random_state=RANDOM_SEED, stratify=y
    )
    X_train, X_val, y_train, y_val = train_test_split(
        X_tv, y_tv, test_size=0.15 / 0.85, random_state=RANDOM_SEED, stratify=y_tv
    )

    _, seq_len, n_feat = X_train.shape
    scaler = StandardScaler()
    scaler.fit(X_train.reshape(-1, n_feat))

    def transform(A):
        n = A.shape[0]
        return scaler.transform(A.reshape(-1, n_feat)).reshape(n, seq_len, n_feat).astype(np.float32)

    return transform(X_train), transform(X_val), transform(X_test), y_train, y_val, y_test


def make_loader(X, y, shuffle):
    return DataLoader(
        TensorDataset(torch.tensor(X), torch.tensor(y)),
        batch_size=BATCH_SIZE,
        shuffle=shuffle,
    )


def train_model(model, train_loader, val_loader, device, criterion):
    optimizer = torch.optim.Adam(model.parameters(), lr=LR, weight_decay=1e-4)
    best_state = None
    best_f1 = -1
    patience = 0

    for epoch in range(1, EPOCHS + 1):
        model.train()
        for xb, yb in train_loader:
            xb, yb = xb.to(device), yb.to(device)
            optimizer.zero_grad()
            loss = criterion(model(xb), yb)
            loss.backward()
            optimizer.step()

        model.eval()
        preds, truth = [], []
        with torch.no_grad():
            for xb, yb in val_loader:
                out = model(xb.to(device))
                preds.extend(torch.argmax(out, dim=1).cpu().numpy())
                truth.extend(yb.numpy())

        val_f1 = f1_score(truth, preds, average="macro", zero_division=0)

        if epoch == 1 or epoch % 5 == 0:
            print(f"  epoch={epoch:02d} val_macro_f1={val_f1:.4f}")

        if val_f1 > best_f1:
            best_f1 = val_f1
            best_state = {k: v.detach().cpu().clone() for k, v in model.state_dict().items()}
            patience = 0
        else:
            patience += 1
            if patience >= PATIENCE:
                print(f"  early stop at epoch {epoch}, best_val_f1={best_f1:.4f}")
                break

    model.load_state_dict(best_state)
    return model


def evaluate_model(model, X_test, y_test, device):
    loader = make_loader(X_test, y_test, False)
    model.eval()
    preds = []
    with torch.no_grad():
        for xb, _ in loader:
            out = model(xb.to(device))
            preds.extend(torch.argmax(out, dim=1).cpu().numpy())

    return {
        "accuracy": accuracy_score(y_test, preds),
        "precision_macro": precision_score(y_test, preds, average="macro", zero_division=0),
        "recall_macro": recall_score(y_test, preds, average="macro", zero_division=0),
        "f1_macro": f1_score(y_test, preds, average="macro", zero_division=0),
        "precision_weighted": precision_score(y_test, preds, average="weighted", zero_division=0),
        "recall_weighted": recall_score(y_test, preds, average="weighted", zero_division=0),
        "f1_weighted": f1_score(y_test, preds, average="weighted", zero_division=0),
    }


def run_task(task_name, X, y, labels, num_classes, device):
    print(f"\\nRunning 1D-CNN baseline: {task_name}")
    X_train, X_val, X_test, y_train, y_val, y_test = split_and_scale(X, y)

    train_loader = make_loader(X_train, y_train, True)
    val_loader = make_loader(X_val, y_val, False)

    model = CNN1DClassifier(input_features=X.shape[2], num_classes=num_classes).to(device)

    counts = np.bincount(y_train, minlength=num_classes)
    weights = counts.sum() / (num_classes * np.maximum(counts, 1))
    criterion = nn.CrossEntropyLoss(weight=torch.tensor(weights, dtype=torch.float32).to(device))

    model = train_model(model, train_loader, val_loader, device, criterion)
    perf = evaluate_model(model, X_test, y_test, device)
    perf["model"] = f"1D-CNN {task_name}"

    print(perf)
    return perf


def main():
    set_seed()
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Device: {device}")

    X, y, labels = load_data()
    print(f"Loaded X={X.shape}, classes={labels}")

    binary_y = make_binary_labels(y, labels)

    results = []
    results.append(run_task("Binary", X, binary_y, ["normal", "attack"], 2, device))
    results.append(run_task("Fine-Grained", X, y, labels, len(labels), device))

    out = os.path.join(OUTPUT_DIR, "model_performance_v4_cnn_baseline.csv")
    pd.DataFrame(results).to_csv(out, index=False)
    print(f"Saved: {out}")


if __name__ == "__main__":
    main()

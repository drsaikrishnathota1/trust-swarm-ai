#!/usr/bin/env python3
"""
Train TRUST-Swarm Graph-Temporal Transformer.

Expected input:
    data/processed/graph_windows.pt

The tensor file should contain:
    x: [num_windows, window_size, num_uavs, num_features]
    y: [num_windows]
"""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Dict, Tuple

import numpy as np
import pandas as pd
import torch
import torch.nn as nn
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
from sklearn.model_selection import train_test_split
from torch.utils.data import DataLoader, TensorDataset

from trust_swarm.models.graph_temporal_transformer import GraphTemporalTransformer


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Train Graph-Temporal Transformer.")
    parser.add_argument("--data", type=str, default="data/processed/graph_windows.pt")
    parser.add_argument("--output-dir", type=str, default="results")
    parser.add_argument("--epochs", type=int, default=20)
    parser.add_argument("--batch-size", type=int, default=32)
    parser.add_argument("--lr", type=float, default=3e-4)
    parser.add_argument("--hidden-dim", type=int, default=128)
    parser.add_argument("--num-heads", type=int, default=4)
    parser.add_argument("--graph-layers", type=int, default=2)
    parser.add_argument("--temporal-layers", type=int, default=2)
    parser.add_argument("--dropout", type=float, default=0.25)
    parser.add_argument("--seed", type=int, default=42)
    return parser.parse_args()


def set_seed(seed: int) -> None:
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)


def load_data(path: str) -> Tuple[torch.Tensor, torch.Tensor]:
    payload = torch.load(path, map_location="cpu")
    x = payload["x"].float()
    y = payload["y"].long()
    return x, y


def make_loaders(
    x: torch.Tensor,
    y: torch.Tensor,
    batch_size: int,
    seed: int,
) -> Tuple[DataLoader, DataLoader, DataLoader]:
    idx = np.arange(len(y))

    train_idx, temp_idx = train_test_split(
        idx,
        test_size=0.30,
        random_state=seed,
        stratify=y.numpy(),
    )
    val_idx, test_idx = train_test_split(
        temp_idx,
        test_size=0.50,
        random_state=seed,
        stratify=y[temp_idx].numpy(),
    )

    train_ds = TensorDataset(x[train_idx], y[train_idx])
    val_ds = TensorDataset(x[val_idx], y[val_idx])
    test_ds = TensorDataset(x[test_idx], y[test_idx])

    train_loader = DataLoader(train_ds, batch_size=batch_size, shuffle=True)
    val_loader = DataLoader(val_ds, batch_size=batch_size, shuffle=False)
    test_loader = DataLoader(test_ds, batch_size=batch_size, shuffle=False)

    return train_loader, val_loader, test_loader


def run_epoch(
    model: nn.Module,
    loader: DataLoader,
    optimizer: torch.optim.Optimizer | None,
    criterion: nn.Module,
    device: torch.device,
) -> Tuple[float, Dict[str, float]]:
    is_train = optimizer is not None
    model.train(is_train)

    total_loss = 0.0
    preds = []
    targets = []

    for xb, yb in loader:
        xb = xb.to(device)
        yb = yb.to(device)

        with torch.set_grad_enabled(is_train):
            logits = model(xb)
            loss = criterion(logits, yb)

            if is_train:
                optimizer.zero_grad()
                loss.backward()
                nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
                optimizer.step()

        total_loss += loss.item() * xb.size(0)
        preds.extend(torch.argmax(logits, dim=1).detach().cpu().numpy().tolist())
        targets.extend(yb.detach().cpu().numpy().tolist())

    avg_loss = total_loss / len(loader.dataset)
    metrics = compute_metrics(np.array(targets), np.array(preds))
    return avg_loss, metrics


def compute_metrics(y_true: np.ndarray, y_pred: np.ndarray) -> Dict[str, float]:
    return {
        "accuracy": accuracy_score(y_true, y_pred),
        "macro_f1": f1_score(y_true, y_pred, average="macro", zero_division=0),
        "macro_precision": precision_score(y_true, y_pred, average="macro", zero_division=0),
        "macro_recall": recall_score(y_true, y_pred, average="macro", zero_division=0),
    }


def main() -> None:
    args = parse_args()
    set_seed(args.seed)

    output_dir = Path(args.output_dir)
    (output_dir / "csv").mkdir(parents=True, exist_ok=True)
    (output_dir / "models").mkdir(parents=True, exist_ok=True)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print("Device:", device)

    x, y = load_data(args.data)
    print("Loaded x:", tuple(x.shape), "y:", tuple(y.shape))

    num_features = x.shape[-1]
    num_classes = int(y.unique().numel())

    train_loader, val_loader, test_loader = make_loaders(
        x=x,
        y=y,
        batch_size=args.batch_size,
        seed=args.seed,
    )

    model = GraphTemporalTransformer(
        num_features=num_features,
        hidden_dim=args.hidden_dim,
        num_graph_layers=args.graph_layers,
        num_temporal_layers=args.temporal_layers,
        num_heads=args.num_heads,
        num_classes=num_classes,
        dropout=args.dropout,
    ).to(device)

    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.AdamW(model.parameters(), lr=args.lr, weight_decay=1e-4)

    best_val_f1 = -1.0
    best_path = output_dir / "models" / "graph_temporal_transformer.pt"
    history = []

    for epoch in range(1, args.epochs + 1):
        train_loss, train_metrics = run_epoch(model, train_loader, optimizer, criterion, device)
        val_loss, val_metrics = run_epoch(model, val_loader, None, criterion, device)

        row = {
            "epoch": epoch,
            "train_loss": train_loss,
            "val_loss": val_loss,
            **{f"train_{k}": v for k, v in train_metrics.items()},
            **{f"val_{k}": v for k, v in val_metrics.items()},
        }
        history.append(row)

        print(
            f"Epoch {epoch:03d} | "
            f"train_loss={train_loss:.4f} val_loss={val_loss:.4f} "
            f"val_f1={val_metrics['macro_f1']:.4f}"
        )

        if val_metrics["macro_f1"] > best_val_f1:
            best_val_f1 = val_metrics["macro_f1"]
            torch.save(model.state_dict(), best_path)

    model.load_state_dict(torch.load(best_path, map_location=device))
    test_loss, test_metrics = run_epoch(model, test_loader, None, criterion, device)

    history_df = pd.DataFrame(history)
    history_df.to_csv(output_dir / "csv" / "graph_temporal_training_history.csv", index=False)

    test_df = pd.DataFrame(
        [
            {
                "model": "GraphTemporalTransformer",
                "test_loss": test_loss,
                **test_metrics,
            }
        ]
    )
    test_df.to_csv(output_dir / "csv" / "graph_temporal_test_metrics.csv", index=False)

    print("Best model saved to:", best_path)
    print("Test metrics:")
    print(test_df.to_string(index=False))


if __name__ == "__main__":
    main()


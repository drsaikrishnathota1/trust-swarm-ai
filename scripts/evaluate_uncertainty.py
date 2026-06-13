#!/usr/bin/env python3
"""
Evaluate TRUST-Swarm uncertainty using Monte Carlo dropout.

Inputs:
- graph_windows.pt
- trained graph_temporal_transformer.pt

Outputs:
- results/csv/uncertainty_metrics.csv

Metrics:
- Accuracy
- Macro F1
- Expected Calibration Error
- Brier score
- Mean confidence
- Mean predictive entropy
"""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd
import torch
import torch.nn.functional as F
from sklearn.metrics import accuracy_score, f1_score, brier_score_loss
from sklearn.model_selection import train_test_split

from trust_swarm.models.graph_temporal_transformer import GraphTemporalTransformer


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Evaluate MC-dropout uncertainty.")
    parser.add_argument("--data", type=str, default="data/processed/graph_windows.pt")
    parser.add_argument("--model", type=str, default="results/models/graph_temporal_transformer.pt")
    parser.add_argument("--output", type=str, default="results/csv/uncertainty_metrics.csv")
    parser.add_argument("--mc-samples", type=int, default=20)
    parser.add_argument("--batch-size", type=int, default=64)
    parser.add_argument("--seed", type=int, default=42)
    return parser.parse_args()


def expected_calibration_error(
    confidences: np.ndarray,
    predictions: np.ndarray,
    labels: np.ndarray,
    n_bins: int = 10,
) -> float:
    bins = np.linspace(0.0, 1.0, n_bins + 1)
    ece = 0.0

    for i in range(n_bins):
        lower, upper = bins[i], bins[i + 1]
        mask = (confidences > lower) & (confidences <= upper)

        if mask.sum() == 0:
            continue

        bin_acc = (predictions[mask] == labels[mask]).mean()
        bin_conf = confidences[mask].mean()
        ece += (mask.sum() / len(labels)) * abs(bin_acc - bin_conf)

    return float(ece)


def predictive_entropy(probs: np.ndarray) -> np.ndarray:
    return -np.sum(probs * np.log(probs + 1e-12), axis=1)


def enable_dropout(model: torch.nn.Module) -> None:
    for module in model.modules():
        if isinstance(module, torch.nn.Dropout):
            module.train()


def load_test_split(data_path: str, seed: int):
    payload = torch.load(data_path, map_location="cpu")
    x = payload["x"].float()
    y = payload["y"].long()

    idx = np.arange(len(y))
    _, temp_idx = train_test_split(
        idx,
        test_size=0.30,
        random_state=seed,
        stratify=y.numpy(),
    )
    _, test_idx = train_test_split(
        temp_idx,
        test_size=0.50,
        random_state=seed,
        stratify=y[temp_idx].numpy(),
    )

    return x[test_idx], y[test_idx]


def mc_dropout_predict(
    model: torch.nn.Module,
    x: torch.Tensor,
    device: torch.device,
    mc_samples: int,
    batch_size: int,
) -> np.ndarray:
    model.eval()
    enable_dropout(model)

    all_mc_probs = []

    for _ in range(mc_samples):
        sample_probs = []

        for start in range(0, len(x), batch_size):
            xb = x[start : start + batch_size].to(device)

            with torch.no_grad():
                logits = model(xb)
                probs = F.softmax(logits, dim=1)

            sample_probs.append(probs.cpu())

        all_mc_probs.append(torch.cat(sample_probs, dim=0).numpy())

    return np.mean(np.stack(all_mc_probs, axis=0), axis=0)


def main() -> None:
    args = parse_args()
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print("Device:", device)

    x_test, y_test = load_test_split(args.data, args.seed)

    num_features = x_test.shape[-1]
    num_classes = int(y_test.unique().numel())

    model = GraphTemporalTransformer(
        num_features=num_features,
        num_classes=num_classes,
    ).to(device)

    model.load_state_dict(torch.load(args.model, map_location=device))

    probs = mc_dropout_predict(
        model=model,
        x=x_test,
        device=device,
        mc_samples=args.mc_samples,
        batch_size=args.batch_size,
    )

    preds = probs.argmax(axis=1)
    labels = y_test.numpy()
    confidences = probs.max(axis=1)
    entropy = predictive_entropy(probs)

    # Multiclass Brier score approximation: mean squared error over one-hot vectors.
    one_hot = np.eye(num_classes)[labels]
    brier = float(np.mean(np.sum((probs - one_hot) ** 2, axis=1)))

    metrics = {
        "mc_samples": args.mc_samples,
        "accuracy": accuracy_score(labels, preds),
        "macro_f1": f1_score(labels, preds, average="macro", zero_division=0),
        "expected_calibration_error": expected_calibration_error(confidences, preds, labels),
        "brier_score": brier,
        "mean_confidence": float(confidences.mean()),
        "mean_predictive_entropy": float(entropy.mean()),
    }

    df = pd.DataFrame([metrics])
    df.to_csv(output_path, index=False)

    print("Saved:", output_path)
    print(df.to_string(index=False))


if __name__ == "__main__":
    main()

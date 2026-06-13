#!/usr/bin/env python3
"""
TRUST-Swarm feature-importance explanation script.

This starter XAI script uses perturbation importance:
1. Compute baseline macro F1.
2. Replace one feature at a time with its dataset mean.
3. Measure macro-F1 drop.
4. Larger drop = more important feature.

Input:
    data/processed/graph_windows.pt
    results/models/graph_temporal_transformer.pt

Outputs:
    results/csv/feature_importance.csv
    results/figures/feature_importance.png
"""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Dict, List

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import torch
import torch.nn.functional as F
from sklearn.metrics import f1_score
from sklearn.model_selection import train_test_split

from src.trust_swarm.models.graph_temporal_transformer import GraphTemporalTransformer


DEFAULT_FEATURES = [
    "packet_loss_rate",
    "latency_ms",
    "route_deviation_m",
    "gps_jump_m",
    "velocity_inconsistency",
    "battery_level",
    "mission_progress",
    "zone_coverage",
    "energy_consumption",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Explain feature importance by perturbation.")
    parser.add_argument("--data", type=str, default="data/processed/graph_windows.pt")
    parser.add_argument("--model", type=str, default="results/models/graph_temporal_transformer.pt")
    parser.add_argument("--output-csv", type=str, default="results/csv/feature_importance.csv")
    parser.add_argument("--output-fig", type=str, default="results/figures/feature_importance.png")
    parser.add_argument("--batch-size", type=int, default=64)
    parser.add_argument("--seed", type=int, default=42)
    return parser.parse_args()


def load_test_split(data_path: str, seed: int):
    payload = torch.load(data_path, map_location="cpu")
    x = payload["x"].float()
    y = payload["y"].long()
    features = payload.get("features", DEFAULT_FEATURES)

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

    return x[test_idx], y[test_idx], features


def predict(
    model: torch.nn.Module,
    x: torch.Tensor,
    device: torch.device,
    batch_size: int,
) -> np.ndarray:
    model.eval()
    preds = []

    for start in range(0, len(x), batch_size):
        xb = x[start : start + batch_size].to(device)

        with torch.no_grad():
            logits = model(xb)
            probs = F.softmax(logits, dim=1)
            pred = torch.argmax(probs, dim=1)

        preds.append(pred.cpu())

    return torch.cat(preds, dim=0).numpy()


def macro_f1(model, x, y, device, batch_size) -> float:
    preds = predict(model, x, device, batch_size)
    return float(f1_score(y.numpy(), preds, average="macro", zero_division=0))


def plot_feature_importance(df: pd.DataFrame, output_fig: Path) -> None:
    output_fig.parent.mkdir(parents=True, exist_ok=True)

    df_sorted = df.sort_values("macro_f1_drop", ascending=True)

    plt.figure(figsize=(9, 5))
    plt.barh(df_sorted["feature"], df_sorted["macro_f1_drop"])
    plt.xlabel("Macro F1 drop after perturbation")
    plt.ylabel("Telemetry feature")
    plt.title("TRUST-Swarm feature importance by perturbation")
    plt.tight_layout()
    plt.savefig(output_fig, dpi=300)
    plt.close()


def main() -> None:
    args = parse_args()

    output_csv = Path(args.output_csv)
    output_fig = Path(args.output_fig)
    output_csv.parent.mkdir(parents=True, exist_ok=True)
    output_fig.parent.mkdir(parents=True, exist_ok=True)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print("Device:", device)

    x_test, y_test, features = load_test_split(args.data, args.seed)

    model = GraphTemporalTransformer(
        num_features=x_test.shape[-1],
        num_classes=int(y_test.unique().numel()),
    ).to(device)

    model.load_state_dict(torch.load(args.model, map_location=device))

    baseline_f1 = macro_f1(model, x_test, y_test, device, args.batch_size)

    rows: List[Dict[str, float | str]] = []

    for feature_idx, feature_name in enumerate(features):
        x_perturbed = x_test.clone()

        # Replace feature with mean over dataset/time/uav dimensions.
        feature_mean = x_test[..., feature_idx].mean()
        x_perturbed[..., feature_idx] = feature_mean

        perturbed_f1 = macro_f1(model, x_perturbed, y_test, device, args.batch_size)
        f1_drop = baseline_f1 - perturbed_f1

        rows.append(
            {
                "feature": feature_name,
                "baseline_macro_f1": baseline_f1,
                "perturbed_macro_f1": perturbed_f1,
                "macro_f1_drop": f1_drop,
            }
        )

    df = pd.DataFrame(rows).sort_values("macro_f1_drop", ascending=False)
    df.to_csv(output_csv, index=False)
    plot_feature_importance(df, output_fig)

    print("Saved:", output_csv)
    print("Saved:", output_fig)
    print(df.to_string(index=False))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Evaluate TRUST-Swarm OOD / unseen attack behavior.

Input:
    data/processed/graph_windows.pt
    results/models/graph_temporal_transformer.pt

Output:
    results/csv/ood_unseen_attack_results.csv

This is a starter OOD evaluator. It creates synthetic OOD shifts from
existing graph windows to test whether confidence drops and entropy rises.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd
import torch
import torch.nn.functional as F
from sklearn.metrics import accuracy_score, f1_score
from sklearn.model_selection import train_test_split

from trust_swarm.models.graph_temporal_transformer import GraphTemporalTransformer


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Evaluate OOD unseen attack behavior.")
    parser.add_argument("--data", type=str, default="data/processed/graph_windows.pt")
    parser.add_argument("--model", type=str, default="results/models/graph_temporal_transformer.pt")
    parser.add_argument("--output", type=str, default="results/csv/ood_unseen_attack_results.csv")
    parser.add_argument("--batch-size", type=int, default=64)
    parser.add_argument("--seed", type=int, default=42)
    return parser.parse_args()


def predictive_entropy(probs: np.ndarray) -> np.ndarray:
    return -np.sum(probs * np.log(probs + 1e-12), axis=1)


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


def make_ood_variant(x: torch.Tensor, mode: str, seed: int) -> torch.Tensor:
    """
    Feature order:
    0 packet_loss_rate
    1 latency_ms
    2 route_deviation_m
    3 gps_jump_m
    4 velocity_inconsistency
    5 battery_level
    6 mission_progress
    7 zone_coverage
    8 energy_consumption
    """
    torch.manual_seed(seed)
    x_ood = x.clone()

    if mode == "stealth_jammer":
        x_ood[..., 0] = torch.clamp(x_ood[..., 0] + 0.08, 0, 1)
        x_ood[..., 1] = x_ood[..., 1] + 35.0

    elif mode == "slow_gps_drift":
        drift = torch.linspace(0, 40, x_ood.shape[1]).view(1, -1, 1)
        x_ood[..., 2] = x_ood[..., 2] + drift
        x_ood[..., 3] = x_ood[..., 3] + drift * 0.45
        x_ood[..., 4] = x_ood[..., 4] + drift * 0.05

    elif mode == "intermittent_tampering":
        mask = torch.zeros_like(x_ood[..., 8])
        mask[:, ::3, :] = 1.0
        x_ood[..., 8] = torch.clamp(x_ood[..., 8] + 0.12 * mask, 0, 1)
        x_ood[..., 7] = torch.clamp(x_ood[..., 7] - 12.0 * mask, 0, 100)

    elif mode == "delayed_combined":
        half = x_ood.shape[1] // 2
        x_ood[:, half:, :, 0] = torch.clamp(x_ood[:, half:, :, 0] + 0.15, 0, 1)
        x_ood[:, half:, :, 1] = x_ood[:, half:, :, 1] + 75.0
        x_ood[:, half:, :, 2] = x_ood[:, half:, :, 2] + 60.0
        x_ood[:, half:, :, 3] = x_ood[:, half:, :, 3] + 35.0
        x_ood[:, half:, :, 8] = torch.clamp(x_ood[:, half:, :, 8] + 0.08, 0, 1)

    elif mode == "unseen_swarm_noise":
        noise = torch.randn_like(x_ood) * 0.03
        x_ood = x_ood + noise
        x_ood[..., 0] = torch.clamp(x_ood[..., 0], 0, 1)
        x_ood[..., 5] = torch.clamp(x_ood[..., 5], 0, 1)
        x_ood[..., 6] = torch.clamp(x_ood[..., 6], 0, 100)
        x_ood[..., 7] = torch.clamp(x_ood[..., 7], 0, 100)
        x_ood[..., 8] = torch.clamp(x_ood[..., 8], 0, 1)

    else:
        raise ValueError(f"Unknown OOD mode: {mode}")

    return x_ood


def predict_probs(
    model: torch.nn.Module,
    x: torch.Tensor,
    device: torch.device,
    batch_size: int,
) -> np.ndarray:
    model.eval()
    probs_all = []

    for start in range(0, len(x), batch_size):
        xb = x[start : start + batch_size].to(device)

        with torch.no_grad():
            logits = model(xb)
            probs = F.softmax(logits, dim=1)

        probs_all.append(probs.cpu())

    return torch.cat(probs_all, dim=0).numpy()


def summarize_condition(name: str, probs: np.ndarray, labels: np.ndarray) -> dict:
    preds = probs.argmax(axis=1)
    confidence = probs.max(axis=1)
    entropy = predictive_entropy(probs)

    return {
        "condition": name,
        "accuracy": accuracy_score(labels, preds),
        "macro_f1": f1_score(labels, preds, average="macro", zero_division=0),
        "mean_confidence": float(confidence.mean()),
        "mean_entropy": float(entropy.mean()),
        "low_confidence_rate_lt_0_70": float((confidence < 0.70).mean()),
    }


def main() -> None:
    args = parse_args()

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print("Device:", device)

    x_test, y_test = load_test_split(args.data, args.seed)
    labels = y_test.numpy()

    model = GraphTemporalTransformer(
        num_features=x_test.shape[-1],
        num_classes=int(y_test.unique().numel()),
    ).to(device)

    model.load_state_dict(torch.load(args.model, map_location=device))

    rows = []

    in_dist_probs = predict_probs(model, x_test, device, args.batch_size)
    rows.append(summarize_condition("in_distribution_test", in_dist_probs, labels))

    for mode in [
        "stealth_jammer",
        "slow_gps_drift",
        "intermittent_tampering",
        "delayed_combined",
        "unseen_swarm_noise",
    ]:
        x_ood = make_ood_variant(x_test, mode=mode, seed=args.seed)
        probs = predict_probs(model, x_ood, device, args.batch_size)
        rows.append(summarize_condition(mode, probs, labels))

    df = pd.DataFrame(rows)
    df.to_csv(output_path, index=False)

    print("Saved:", output_path)
    print(df.to_string(index=False))


if __name__ == "__main__":
    main()

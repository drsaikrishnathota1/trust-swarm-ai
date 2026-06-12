#!/usr/bin/env python3
"""
Build TRUST-Swarm graph-temporal datasets from UAV telemetry CSV.

This script converts telemetry rows into graph-temporal windows:

    [num_windows, window_size, num_uavs, num_features]

It uses run-level grouping to reduce temporal leakage risk.
"""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import List, Tuple

import numpy as np
import pandas as pd
import torch


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
    parser = argparse.ArgumentParser(description="Build TRUST-Swarm graph-temporal tensors.")
    parser.add_argument("--input", type=str, required=True, help="Input telemetry CSV path.")
    parser.add_argument("--output-dir", type=str, default="data/processed", help="Output directory.")
    parser.add_argument("--window-size", type=int, default=20, help="Temporal window size.")
    parser.add_argument("--run-col", type=str, default="run_id")
    parser.add_argument("--uav-col", type=str, default="uav_id")
    parser.add_argument("--time-col", type=str, default="timestep")
    parser.add_argument("--label-col", type=str, default="attack_label")
    parser.add_argument(
        "--features",
        type=str,
        nargs="*",
        default=DEFAULT_FEATURES,
        help="Feature columns to use.",
    )
    return parser.parse_args()


def validate_columns(df: pd.DataFrame, required: List[str]) -> None:
    missing = [col for col in required if col not in df.columns]
    if missing:
        raise ValueError(
            "Missing required columns: "
            + ", ".join(missing)
            + "\nAvailable columns: "
            + ", ".join(df.columns)
        )


def build_windows_for_run(
    run_df: pd.DataFrame,
    features: List[str],
    window_size: int,
    uav_col: str,
    time_col: str,
    label_col: str,
) -> Tuple[List[np.ndarray], List[object]]:
    windows: List[np.ndarray] = []
    labels: List[object] = []

    run_df = run_df.sort_values([time_col, uav_col])
    times = sorted(run_df[time_col].unique())
    uavs = sorted(run_df[uav_col].unique())

    tensor_by_time = []
    label_by_time = []

    for t in times:
        slice_t = run_df[run_df[time_col] == t].sort_values(uav_col)

        if list(slice_t[uav_col]) != uavs:
            continue

        x_t = slice_t[features].to_numpy(dtype=np.float32)
        y_t = slice_t[label_col].mode().iloc[0]

        tensor_by_time.append(x_t)
        label_by_time.append(y_t)

    for idx in range(window_size - 1, len(tensor_by_time)):
        window = np.stack(tensor_by_time[idx - window_size + 1 : idx + 1], axis=0)
        windows.append(window)
        labels.append(label_by_time[idx])

    return windows, labels


def main() -> None:
    args = parse_args()
    input_path = Path(args.input)
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(input_path)

    required = [args.run_col, args.uav_col, args.time_col, args.label_col] + args.features
    validate_columns(df, required)

    all_windows: List[np.ndarray] = []
    all_labels: List[object] = []
    all_run_ids: List[object] = []

    for run_id, run_df in df.groupby(args.run_col):
        windows, labels = build_windows_for_run(
            run_df=run_df,
            features=args.features,
            window_size=args.window_size,
            uav_col=args.uav_col,
            time_col=args.time_col,
            label_col=args.label_col,
        )
        all_windows.extend(windows)
        all_labels.extend(labels)
        all_run_ids.extend([run_id] * len(windows))

    if not all_windows:
        raise RuntimeError("No graph-temporal windows were created. Check column names and data format.")

    label_series = pd.Series(all_labels).astype("category")
    label_mapping = dict(enumerate(label_series.cat.categories))

    x = torch.tensor(np.stack(all_windows), dtype=torch.float32)
    y = torch.tensor(label_series.cat.codes.to_numpy(), dtype=torch.long)

    torch.save(
        {
            "x": x,
            "y": y,
            "run_ids": all_run_ids,
            "features": args.features,
            "label_mapping": label_mapping,
            "window_size": args.window_size,
            "shape_note": "[num_windows, window_size, num_uavs, num_features]",
        },
        output_dir / "graph_windows.pt",
    )

    summary = pd.DataFrame(
        {
            "num_windows": [x.shape[0]],
            "window_size": [x.shape[1]],
            "num_uavs": [x.shape[2]],
            "num_features": [x.shape[3]],
            "num_classes": [int(y.unique().numel())],
        }
    )
    summary.to_csv(output_dir / "graph_dataset_summary.csv", index=False)

    label_table = pd.DataFrame(
        [{"class_id": int(k), "class_name": str(v)} for k, v in label_mapping.items()]
    )
    label_table.to_csv(output_dir / "label_mapping.csv", index=False)

    print("Saved:", output_dir / "graph_windows.pt")
    print(summary.to_string(index=False))
    print(label_table.to_string(index=False))


if __name__ == "__main__":
    main()

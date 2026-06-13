#!/usr/bin/env python3
"""
Generate tiny synthetic UAV telemetry for TRUST-Swarm pipeline testing.

This is NOT final research data.
It only verifies that:
1. CSV generation works.
2. graph dataset builder works.
3. Graph-Temporal Transformer training script runs end-to-end.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd


ATTACK_LABELS = {
    0: "normal",
    1: "jamming",
    2: "spoofing",
    3: "tampering",
    4: "jamming_spoofing",
    5: "jamming_tampering",
    6: "spoofing_tampering",
    7: "combined",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate tiny TRUST-Swarm telemetry CSV.")
    parser.add_argument("--output", type=str, default="data/raw/tiny_telemetry.csv")
    parser.add_argument("--runs", type=int, default=16)
    parser.add_argument("--timesteps", type=int, default=80)
    parser.add_argument("--uavs", type=int, default=10)
    parser.add_argument("--seed", type=int, default=42)
    return parser.parse_args()


def make_features(label: int, rng: np.random.Generator) -> dict:
    packet_loss_rate = rng.normal(0.03, 0.01)
    latency_ms = rng.normal(45, 8)
    route_deviation_m = rng.normal(5, 2)
    gps_jump_m = rng.normal(2, 1)
    velocity_inconsistency = rng.normal(1, 0.4)
    battery_level = rng.uniform(0.45, 1.0)
    mission_progress = rng.uniform(0, 100)
    zone_coverage = rng.uniform(30, 100)
    energy_consumption = rng.uniform(0.02, 0.18)

    if label in [1, 4, 5, 7]:
        packet_loss_rate += rng.uniform(0.25, 0.55)
        latency_ms += rng.uniform(80, 240)

    if label in [2, 4, 6, 7]:
        route_deviation_m += rng.uniform(50, 180)
        gps_jump_m += rng.uniform(35, 120)
        velocity_inconsistency += rng.uniform(8, 30)

    if label in [3, 5, 6, 7]:
        energy_consumption += rng.uniform(0.03, 0.10)
        zone_coverage -= rng.uniform(5, 25)

    return {
        "packet_loss_rate": float(np.clip(packet_loss_rate, 0, 1)),
        "latency_ms": float(max(latency_ms, 1)),
        "route_deviation_m": float(max(route_deviation_m, 0)),
        "gps_jump_m": float(max(gps_jump_m, 0)),
        "velocity_inconsistency": float(max(velocity_inconsistency, 0)),
        "battery_level": float(np.clip(battery_level, 0, 1)),
        "mission_progress": float(np.clip(mission_progress, 0, 100)),
        "zone_coverage": float(np.clip(zone_coverage, 0, 100)),
        "energy_consumption": float(np.clip(energy_consumption, 0, 1)),
    }


def main() -> None:
    args = parse_args()
    rng = np.random.default_rng(args.seed)

    rows = []

    for run_id in range(args.runs):
        label = run_id % len(ATTACK_LABELS)

        for timestep in range(args.timesteps):
            active_label = 0 if timestep < 20 else label

            for uav_id in range(args.uavs):
                features = make_features(active_label, rng)

                rows.append(
                    {
                        "run_id": run_id,
                        "timestep": timestep,
                        "uav_id": uav_id,
                        "attack_label": active_label,
                        "attack_name": ATTACK_LABELS[active_label],
                        "x_position": float(rng.uniform(0, 5000)),
                        "y_position": float(rng.uniform(0, 5000)),
                        "zone_id": int(rng.integers(0, 25)),
                        **features,
                    }
                )

    df = pd.DataFrame(rows)

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)

    print("Saved:", output_path)
    print("Shape:", df.shape)
    print(df["attack_name"].value_counts().to_string())


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Generate a larger, more realistic TRUST-Swarm telemetry dataset.

This is for journal-level experiments, not only sanity testing.

Output columns match the graph dataset builder:
- run_id
- timestep
- uav_id
- attack_label
- packet_loss_rate
- latency_ms
- route_deviation_m
- gps_jump_m
- velocity_inconsistency
- battery_level
- mission_progress
- zone_coverage
- energy_consumption

Attack labels:
0 normal
1 jamming
2 spoofing
3 tampering
4 jamming_spoofing
5 jamming_tampering
6 spoofing_tampering
7 combined
"""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd


ATTACK_NAMES = {
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
    parser = argparse.ArgumentParser(description="Generate realistic TRUST-Swarm telemetry.")
    parser.add_argument("--output", type=str, default="data/raw/realistic_telemetry.csv")
    parser.add_argument("--summary-output", type=str, default="results/tables/realistic_dataset_summary.csv")
    parser.add_argument("--runs", type=int, default=300)
    parser.add_argument("--timesteps", type=int, default=240)
    parser.add_argument("--uavs", type=int, default=20)
    parser.add_argument("--seed", type=int, default=42)
    return parser.parse_args()


def choose_attack_label(run_id: int, rng: np.random.Generator) -> int:
    # Intentional imbalance: normal/jamming/spoofing are common; combined attacks are rarer.
    labels = np.array([0, 1, 2, 3, 4, 5, 6, 7])
    probs = np.array([0.34, 0.16, 0.14, 0.12, 0.08, 0.06, 0.05, 0.05])
    return int(rng.choice(labels, p=probs))


def baseline_state(
    rng: np.random.Generator,
    timestep: int,
    timesteps: int,
    uav_id: int,
    uavs: int,
) -> dict:
    mission_progress = 100.0 * timestep / max(timesteps - 1, 1)

    # UAV-level heterogeneity.
    uav_factor = 1.0 + 0.08 * np.sin((uav_id + 1) / max(uavs, 1) * np.pi)

    packet_loss_rate = rng.normal(0.035, 0.018) * uav_factor
    latency_ms = rng.normal(48, 12) * uav_factor
    route_deviation_m = rng.normal(8, 4)
    gps_jump_m = rng.normal(2.5, 1.5)
    velocity_inconsistency = rng.normal(1.2, 0.7)
    battery_level = 1.0 - 0.55 * (timestep / max(timesteps - 1, 1)) + rng.normal(0, 0.025)
    zone_coverage = 65 + 25 * np.sin(np.pi * timestep / max(timesteps - 1, 1)) + rng.normal(0, 6)
    energy_consumption = 0.05 + 0.18 * (1.0 - battery_level) + rng.normal(0, 0.015)

    return {
        "packet_loss_rate": packet_loss_rate,
        "latency_ms": latency_ms,
        "route_deviation_m": route_deviation_m,
        "gps_jump_m": gps_jump_m,
        "velocity_inconsistency": velocity_inconsistency,
        "battery_level": battery_level,
        "mission_progress": mission_progress,
        "zone_coverage": zone_coverage,
        "energy_consumption": energy_consumption,
    }


def apply_attack_effects(
    features: dict,
    attack_label: int,
    attack_strength: float,
    rng: np.random.Generator,
    local_exposure: float,
) -> dict:
    f = dict(features)
    strength = attack_strength * local_exposure

    # Jamming component
    if attack_label in [1, 4, 5, 7]:
        f["packet_loss_rate"] += rng.uniform(0.08, 0.35) * strength
        f["latency_ms"] += rng.uniform(25, 150) * strength
        f["zone_coverage"] -= rng.uniform(0, 8) * strength

    # Spoofing component
    if attack_label in [2, 4, 6, 7]:
        f["route_deviation_m"] += rng.uniform(15, 120) * strength
        f["gps_jump_m"] += rng.uniform(10, 85) * strength
        f["velocity_inconsistency"] += rng.uniform(3, 22) * strength

    # Tampering component
    if attack_label in [3, 5, 6, 7]:
        f["energy_consumption"] += rng.uniform(0.015, 0.08) * strength
        f["zone_coverage"] -= rng.uniform(4, 20) * strength
        f["mission_progress"] -= rng.uniform(0, 4) * strength

    return f


def clip_features(f: dict) -> dict:
    return {
        "packet_loss_rate": float(np.clip(f["packet_loss_rate"], 0, 1)),
        "latency_ms": float(np.clip(f["latency_ms"], 1, 600)),
        "route_deviation_m": float(np.clip(f["route_deviation_m"], 0, 500)),
        "gps_jump_m": float(np.clip(f["gps_jump_m"], 0, 300)),
        "velocity_inconsistency": float(np.clip(f["velocity_inconsistency"], 0, 80)),
        "battery_level": float(np.clip(f["battery_level"], 0, 1)),
        "mission_progress": float(np.clip(f["mission_progress"], 0, 100)),
        "zone_coverage": float(np.clip(f["zone_coverage"], 0, 100)),
        "energy_consumption": float(np.clip(f["energy_consumption"], 0, 1)),
    }


def main() -> None:
    args = parse_args()
    rng = np.random.default_rng(args.seed)

    rows = []

    for run_id in range(args.runs):
        attack_label = choose_attack_label(run_id, rng)

        onset = int(rng.integers(low=max(20, args.timesteps // 5), high=max(21, args.timesteps // 2)))
        duration = int(rng.integers(low=args.timesteps // 5, high=max(args.timesteps // 5 + 1, args.timesteps // 2)))
        end = min(args.timesteps, onset + duration)

        jammer_x = rng.uniform(0, 5000)
        jammer_y = rng.uniform(0, 5000)

        for timestep in range(args.timesteps):
            active = onset <= timestep < end and attack_label != 0

            if active:
                attack_progress = (timestep - onset) / max(end - onset, 1)
                attack_strength = 0.35 + 0.65 * attack_progress
                current_label = attack_label
            else:
                attack_strength = 0.0
                current_label = 0

            for uav_id in range(args.uavs):
                x_position = rng.uniform(0, 5000)
                y_position = rng.uniform(0, 5000)
                distance_to_jammer = np.sqrt((x_position - jammer_x) ** 2 + (y_position - jammer_y) ** 2)
                local_exposure = float(np.clip(1.2 - distance_to_jammer / 5000, 0.25, 1.25))

                f = baseline_state(
                    rng=rng,
                    timestep=timestep,
                    timesteps=args.timesteps,
                    uav_id=uav_id,
                    uavs=args.uavs,
                )

                if active:
                    f = apply_attack_effects(
                        features=f,
                        attack_label=current_label,
                        attack_strength=attack_strength,
                        rng=rng,
                        local_exposure=local_exposure,
                    )

                f = clip_features(f)

                rows.append(
                    {
                        "run_id": run_id,
                        "timestep": timestep,
                        "uav_id": uav_id,
                        "attack_label": current_label,
                        "attack_name": ATTACK_NAMES[current_label],
                        "x_position": float(x_position),
                        "y_position": float(y_position),
                        "zone_id": int(rng.integers(0, 25)),
                        "distance_to_jammer": float(distance_to_jammer),
                        "attack_onset": onset,
                        "attack_end": end,
                        **f,
                    }
                )

    df = pd.DataFrame(rows)

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)

    summary = (
        df.groupby(["attack_label", "attack_name"])
        .size()
        .reset_index(name="rows")
        .sort_values("attack_label")
    )

    summary_path = Path(args.summary_output)
    summary_path.parent.mkdir(parents=True, exist_ok=True)
    summary.to_csv(summary_path, index=False)

    print("Saved:", output_path)
    print("Shape:", df.shape)
    print("Saved summary:", summary_path)
    print(summary.to_string(index=False))


if __name__ == "__main__":
    main()

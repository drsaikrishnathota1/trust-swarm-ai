"""
RA-MARS v4 Sequence Window Creator

Converts v4 telemetry CSV into sliding time-series windows for LSTM/GRU training.
Identical logic to v3 but uses v4 dataset with SINR column added.

Leakage prevention: derived MAI scores excluded from classifier input features.
Only raw telemetry features are used (no mission_assurance_index, communication_score etc.)

Input:  simulations/datasets/uav_mission_telemetry_v4_sample.csv
Output: simulations/datasets/uav_sequence_windows_v4.npz
"""

import os
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder

RANDOM_SEED  = 42
SEQ_LEN      = 20       # 20 timesteps per window
STRIDE       = 1        # step between windows
DATA_PATH    = "simulations/datasets/uav_mission_telemetry_v4_sample.csv"
OUTPUT_PATH  = "simulations/datasets/uav_sequence_windows_v4.npz"

# Raw non-leakage features only (no derived MAI scores)
FEATURES = [
    "packet_loss_rate",
    "latency_ms",
    "route_deviation",
    "gps_jump",
    "velocity_inconsistency",
    "log_integrity_status",
    "energy_consumption",
    "zone_coverage",
    "sinr_db",              # NEW in v4 — physics-based SINR
]

GROUP_COLS = ["seed", "scenario", "attack_intensity", "uav_count", "uav_id"]

np.random.seed(RANDOM_SEED)


def create_windows(group_df: pd.DataFrame, features: list,
                   seq_len: int, stride: int):
    """Sliding window over a single UAV time series."""
    arr = group_df[features].values
    labels = group_df["actual_attack_type"].values
    windows, window_labels = [], []

    for start in range(0, len(arr) - seq_len + 1, stride):
        end = start + seq_len
        windows.append(arr[start:end])
        # Label = majority class in window
        window_label = pd.Series(labels[start:end]).mode()[0]
        window_labels.append(window_label)

    return windows, window_labels


def main():
    print(f"Loading {DATA_PATH}...")
    df = pd.read_csv(DATA_PATH)
    print(f"  Loaded {len(df):,} rows | {df['actual_attack_type'].nunique()} classes")

    # Fill any missing SINR column (compatibility with v3 data)
    if "sinr_db" not in df.columns:
        print("  sinr_db not found — adding placeholder (run generate_dataset_v4.py first)")
        df["sinr_db"] = 39.9  # normal link SINR

    # Drop rows with NaN in features
    df = df.dropna(subset=FEATURES + ["actual_attack_type"])
    print(f"  After dropna: {len(df):,} rows")

    all_windows, all_labels = [], []

    groups = df.groupby(GROUP_COLS)
    n_groups = len(groups)
    print(f"  Processing {n_groups:,} UAV time-series groups...")

    for i, (_, group_df) in enumerate(groups):
        group_df = group_df.sort_values("timestamp").reset_index(drop=True)
        if len(group_df) < SEQ_LEN:
            continue
        windows, labels = create_windows(group_df, FEATURES, SEQ_LEN, STRIDE)
        all_windows.extend(windows)
        all_labels.extend(labels)

        if (i + 1) % 500 == 0:
            print(f"  {i+1}/{n_groups} groups processed | {len(all_windows):,} windows so far")

    X = np.array(all_windows, dtype=np.float32)
    print(f"\nRaw windows: {X.shape}")

    # Encode labels
    le = LabelEncoder()
    y = le.fit_transform(all_labels).astype(np.int64)
    labels_arr = le.classes_

    print(f"Classes ({len(labels_arr)}): {list(labels_arr)}")
    print(f"Class distribution:")
    for lbl, idx in zip(labels_arr, range(len(labels_arr))):
        print(f"  {lbl:25s}: {(y == idx).sum():,}")

    # Do NOT standardise here.
    # Scaling is fitted only on the training split inside train_sequence_models_v4.py
    # to prevent train/test preprocessing leakage.
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    np.savez_compressed(OUTPUT_PATH,
                        X=X, y=y, labels=labels_arr,
                        feature_names=np.array(FEATURES))

    print(f"\n✓ Saved: {OUTPUT_PATH}")
    print(f"  X shape: {X.shape}")
    print(f"  y shape: {y.shape}")
    print(f"  Features: {FEATURES}")
    print("  Scaling: deferred to training split only")
    print(f"  Sequence length: {SEQ_LEN} steps")


if __name__ == "__main__":
    main()

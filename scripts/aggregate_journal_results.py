#!/usr/bin/env python3
"""
Aggregate TRUST-Swarm journal experiment results across multiple seeds.

Expected structure:
results/journal/
  seed_42/
  seed_123/
  seed_2026/

Outputs:
results/journal/summary/
  model_comparison_summary.csv
  uncertainty_summary.csv
  ood_summary.csv
  feature_importance_summary.csv
"""

from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Aggregate TRUST-Swarm journal results.")
    parser.add_argument("--input-dir", type=str, default="results/journal")
    parser.add_argument("--output-dir", type=str, default="results/journal/summary")
    return parser.parse_args()


def read_seed_csv(seed_dir: Path, relative_path: str) -> pd.DataFrame | None:
    path = seed_dir / relative_path
    if not path.exists():
        print(f"Missing: {path}")
        return None

    df = pd.read_csv(path)
    df["seed"] = seed_dir.name.replace("seed_", "")
    return df


def summarize_numeric(df: pd.DataFrame, group_cols: list[str]) -> pd.DataFrame:
    numeric_cols = df.select_dtypes(include="number").columns.tolist()
    numeric_cols = [c for c in numeric_cols if c not in ["seed"]]

    summary = (
        df.groupby(group_cols)[numeric_cols]
        .agg(["mean", "std"])
        .reset_index()
    )

    summary.columns = [
        "_".join(col).strip("_") if isinstance(col, tuple) else col
        for col in summary.columns
    ]

    return summary


def main() -> None:
    args = parse_args()
    input_dir = Path(args.input_dir)
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    seed_dirs = sorted([p for p in input_dir.glob("seed_*") if p.is_dir()])

    if not seed_dirs:
        raise RuntimeError(f"No seed directories found in {input_dir}")

    baseline_rows = []
    graph_rows = []
    uncertainty_rows = []
    ood_rows = []
    feature_rows = []

    for seed_dir in seed_dirs:
        baseline = read_seed_csv(seed_dir, "csv/baseline_model_results.csv")
        if baseline is not None:
            baseline_rows.append(baseline)

        graph = read_seed_csv(seed_dir, "csv/graph_temporal_test_metrics.csv")
        if graph is not None:
            graph_rows.append(graph)

        uncertainty = read_seed_csv(seed_dir, "csv/uncertainty_metrics.csv")
        if uncertainty is not None:
            uncertainty["model"] = "GraphTemporalTransformer"
            uncertainty_rows.append(uncertainty)

        ood = read_seed_csv(seed_dir, "csv/ood_unseen_attack_results.csv")
        if ood is not None:
            ood_rows.append(ood)

        feature = read_seed_csv(seed_dir, "csv/feature_importance.csv")
        if feature is not None:
            feature_rows.append(feature)

    if baseline_rows or graph_rows:
        combined_models = []

        if baseline_rows:
            combined_models.append(pd.concat(baseline_rows, ignore_index=True))

        if graph_rows:
            combined_models.append(pd.concat(graph_rows, ignore_index=True))

        model_df = pd.concat(combined_models, ignore_index=True)
        model_df.to_csv(output_dir / "model_comparison_all_seeds.csv", index=False)

        model_summary = summarize_numeric(model_df, group_cols=["model"])
        model_summary.to_csv(output_dir / "model_comparison_summary.csv", index=False)

        print("\nModel comparison summary:")
        print(model_summary.to_string(index=False))

    if uncertainty_rows:
        uncertainty_df = pd.concat(uncertainty_rows, ignore_index=True)
        uncertainty_df.to_csv(output_dir / "uncertainty_all_seeds.csv", index=False)

        uncertainty_summary = summarize_numeric(uncertainty_df, group_cols=["model"])
        uncertainty_summary.to_csv(output_dir / "uncertainty_summary.csv", index=False)

        print("\nUncertainty summary:")
        print(uncertainty_summary.to_string(index=False))

    if ood_rows:
        ood_df = pd.concat(ood_rows, ignore_index=True)
        ood_df.to_csv(output_dir / "ood_all_seeds.csv", index=False)

        ood_summary = summarize_numeric(ood_df, group_cols=["condition"])
        ood_summary.to_csv(output_dir / "ood_summary.csv", index=False)

        print("\nOOD summary:")
        print(ood_summary.to_string(index=False))

    if feature_rows:
        feature_df = pd.concat(feature_rows, ignore_index=True)
        feature_df.to_csv(output_dir / "feature_importance_all_seeds.csv", index=False)

        feature_summary = summarize_numeric(feature_df, group_cols=["feature"])
        feature_summary = feature_summary.sort_values(
            "macro_f1_drop_mean",
            ascending=False,
        )
        feature_summary.to_csv(output_dir / "feature_importance_summary.csv", index=False)

        print("\nFeature importance summary:")
        print(feature_summary.to_string(index=False))

    print(f"\nSaved summary files to: {output_dir}")


if __name__ == "__main__":
    main()

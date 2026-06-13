from pathlib import Path
import argparse
import pandas as pd
import matplotlib.pyplot as plt

def pick_col(df, candidates, contains=None):
    for c in candidates:
        if c in df.columns:
            return c
    if contains:
        for c in df.columns:
            low = c.lower()
            if all(x in low for x in contains):
                return c
    raise KeyError(f"Could not find column. Available columns: {list(df.columns)}")

def save_bar(df, x_col, y_col, title, ylabel, out_path, top_n=None, rotate=30):
    data = df.copy()
    if top_n:
        data = data.sort_values(y_col, ascending=False).head(top_n)

    plt.figure(figsize=(10, 6))
    plt.bar(data[x_col].astype(str), data[y_col])
    plt.title(title)
    plt.ylabel(ylabel)
    plt.xticks(rotation=rotate, ha="right")
    plt.tight_layout()
    plt.savefig(out_path, dpi=300)
    plt.close()
    print(f"Saved: {out_path}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--summary-dir",
        default=str(Path.home() / "Documents/TRUST-Swarm-Results/journal-run-01/results/journal/summary"),
    )
    parser.add_argument("--out-dir", default="figures/manuscript")
    args = parser.parse_args()

    summary_dir = Path(args.summary_dir)
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    model = pd.read_csv(summary_dir / "model_comparison_summary.csv")
    uncertainty = pd.read_csv(summary_dir / "uncertainty_summary.csv")
    ood = pd.read_csv(summary_dir / "ood_summary.csv")
    feature = pd.read_csv(summary_dir / "feature_importance_summary.csv")

    print("OOD columns:", list(ood.columns))
    print("Feature columns:", list(feature.columns))

    entropy_col = pick_col(
        ood,
        candidates=["entropy_mean", "mean_entropy_mean", "predictive_entropy_mean", "mean_predictive_entropy"],
        contains=["entropy", "mean"],
    )

    feature_name_col = "feature" if "feature" in feature.columns else feature.columns[0]
    importance_col = pick_col(
        feature,
        candidates=["importance_mean", "macro_f1_drop_mean", "f1_drop_mean", "drop_mean"],
        contains=["mean"],
    )

    save_bar(
        model,
        x_col="model",
        y_col="macro_f1_mean",
        title="Model Comparison by Mean Macro F1",
        ylabel="Mean Macro F1",
        out_path=out_dir / "fig_01_model_comparison_macro_f1.png",
    )

    save_bar(
        model,
        x_col="model",
        y_col="accuracy_mean",
        title="Model Comparison by Mean Accuracy",
        ylabel="Mean Accuracy",
        out_path=out_dir / "fig_02_model_comparison_accuracy.png",
    )

    save_bar(
        uncertainty,
        x_col="model",
        y_col="expected_calibration_error_mean",
        title="Uncertainty Calibration: Expected Calibration Error",
        ylabel="Mean ECE",
        out_path=out_dir / "fig_03_uncertainty_ece.png",
    )

    save_bar(
        uncertainty,
        x_col="model",
        y_col="brier_score_mean",
        title="Uncertainty Calibration: Brier Score",
        ylabel="Mean Brier Score",
        out_path=out_dir / "fig_04_uncertainty_brier.png",
    )

    save_bar(
        ood,
        x_col="condition",
        y_col="macro_f1_mean",
        title="OOD Stress Test by Mean Macro F1",
        ylabel="Mean Macro F1",
        out_path=out_dir / "fig_05_ood_macro_f1.png",
        rotate=45,
    )

    save_bar(
        ood,
        x_col="condition",
        y_col=entropy_col,
        title="OOD Stress Test by Predictive Entropy",
        ylabel="Mean Entropy",
        out_path=out_dir / "fig_06_ood_entropy.png",
        rotate=45,
    )

    save_bar(
        feature,
        x_col=feature_name_col,
        y_col=importance_col,
        title="Perturbation-Based Feature Importance",
        ylabel="Mean Macro-F1 Drop",
        out_path=out_dir / "fig_07_feature_importance.png",
        top_n=9,
        rotate=45,
    )

    print("\nAll manuscript figures generated successfully.")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re

ROOT = Path(".")
SUMMARY = ROOT / "runpod_artifacts/extracted/trust-swarm-journal-results/results/journal/summary"
HCC = ROOT / "results/hcc"
FIG = ROOT / "figures/hcc_real_evidence"
TABLES = ROOT / "docs/tables"
RESULTS_DOC = ROOT / "docs/hcc_results_discussion_v2.md"

FIG.mkdir(parents=True, exist_ok=True)
TABLES.mkdir(parents=True, exist_ok=True)

plt.rcParams["font.family"] = "DejaVu Sans"
plt.rcParams["figure.dpi"] = 220

def norm(s):
    return re.sub(r"[^a-z0-9]+", "_", str(s).lower()).strip("_")

def find_col(df, choices):
    cols = list(df.columns)
    low = {norm(c): c for c in cols}
    for key in choices:
        key = norm(key)
        for lc, orig in low.items():
            if key in lc:
                return orig
    return None

def save(name):
    out = FIG / name
    plt.tight_layout()
    plt.savefig(out, dpi=300, bbox_inches="tight")
    plt.close()
    print("Saved", out)
    return out

def read_csv(path):
    if path.exists():
        df = pd.read_csv(path)
        print(f"Loaded {path} columns={list(df.columns)} shape={df.shape}")
        return df
    print("Missing", path)
    return None

def md_table(df, max_rows=20):
    if df is None or df.empty:
        return "_Not available._"
    return df.head(max_rows).to_markdown(index=False)

created_figures = []

model_summary = read_csv(SUMMARY / "model_comparison_summary.csv")
model_all = read_csv(SUMMARY / "model_comparison_all_seeds.csv")
ood_summary = read_csv(SUMMARY / "ood_summary.csv")
ood_all = read_csv(SUMMARY / "ood_all_seeds.csv")
unc_summary = read_csv(SUMMARY / "uncertainty_summary.csv")
unc_all = read_csv(SUMMARY / "uncertainty_all_seeds.csv")
feat_summary = read_csv(SUMMARY / "feature_importance_summary.csv")
feat_all = read_csv(SUMMARY / "feature_importance_all_seeds.csv")
abl = read_csv(HCC / "ablation_summary.csv")
runtime = read_csv(HCC / "runtime_complexity_summary.csv")

# 1. Model comparison macro F1
if model_summary is not None:
    model_col = find_col(model_summary, ["model", "classifier", "method"])
    f1_col = find_col(model_summary, ["macro_f1", "macro f1", "f1_macro", "mean_macro"])
    acc_col = find_col(model_summary, ["accuracy", "mean_accuracy", "acc"])
    if model_col and f1_col:
        df = model_summary[[model_col, f1_col]].dropna().copy()
        df = df.sort_values(f1_col, ascending=True)
        plt.figure(figsize=(8.8, 5.2))
        plt.barh(df[model_col].astype(str), df[f1_col].astype(float))
        plt.xlabel("Macro F1")
        plt.title("Fig. 3. RunPod model-comparison macro-F1 evidence")
        for i, v in enumerate(df[f1_col].astype(float)):
            plt.text(v + 0.005, i, f"{v:.4f}", va="center", fontsize=8)
        created_figures.append(("Fig. 3. RunPod model-comparison macro-F1 evidence", save("fig3_runpod_model_macro_f1.png")))
    if model_col and acc_col:
        df = model_summary[[model_col, acc_col]].dropna().copy()
        df = df.sort_values(acc_col, ascending=True)
        plt.figure(figsize=(8.8, 5.2))
        plt.barh(df[model_col].astype(str), df[acc_col].astype(float))
        plt.xlabel("Accuracy")
        plt.title("Fig. 4. RunPod model-comparison accuracy evidence")
        for i, v in enumerate(df[acc_col].astype(float)):
            plt.text(v + 0.005, i, f"{v:.4f}", va="center", fontsize=8)
        created_figures.append(("Fig. 4. RunPod model-comparison accuracy evidence", save("fig4_runpod_model_accuracy.png")))

# 2. OOD macro F1 / entropy
if ood_summary is not None:
    cond_col = find_col(ood_summary, ["condition", "attack", "ood", "scenario"])
    f1_col = find_col(ood_summary, ["macro_f1", "macro f1", "f1"])
    entropy_col = find_col(ood_summary, ["entropy"])
    if cond_col and f1_col:
        df = ood_summary[[cond_col, f1_col]].dropna().copy()
        df = df.sort_values(f1_col, ascending=True)
        plt.figure(figsize=(9.5, 5.6))
        plt.barh(df[cond_col].astype(str), df[f1_col].astype(float))
        plt.xlabel("Macro F1")
        plt.title("Fig. 5. RunPod OOD macro-F1 degradation evidence")
        for i, v in enumerate(df[f1_col].astype(float)):
            plt.text(v + 0.005, i, f"{v:.4f}", va="center", fontsize=8)
        created_figures.append(("Fig. 5. RunPod OOD macro-F1 degradation evidence", save("fig5_runpod_ood_macro_f1.png")))
    if cond_col and entropy_col:
        df = ood_summary[[cond_col, entropy_col]].dropna().copy()
        df = df.sort_values(entropy_col, ascending=True)
        plt.figure(figsize=(9.5, 5.6))
        plt.barh(df[cond_col].astype(str), df[entropy_col].astype(float))
        plt.xlabel("Predictive entropy")
        plt.title("Fig. 6. RunPod OOD uncertainty/entropy evidence")
        for i, v in enumerate(df[entropy_col].astype(float)):
            plt.text(v + 0.005, i, f"{v:.4f}", va="center", fontsize=8)
        created_figures.append(("Fig. 6. RunPod OOD uncertainty/entropy evidence", save("fig6_runpod_ood_entropy.png")))

# 3. Calibration
if unc_summary is not None:
    metric_col = find_col(unc_summary, ["metric", "uncertainty"])
    value_col = find_col(unc_summary, ["mean", "value"])
    if metric_col and value_col:
        df = unc_summary[[metric_col, value_col]].dropna().copy()
        plt.figure(figsize=(8.5, 4.8))
        plt.bar(df[metric_col].astype(str), df[value_col].astype(float))
        plt.ylabel("Value")
        plt.title("Fig. 7. RunPod calibration and uncertainty evidence")
        plt.xticks(rotation=15, ha="right")
        for i, v in enumerate(df[value_col].astype(float)):
            plt.text(i, v + max(df[value_col].astype(float))*0.03, f"{v:.4f}", ha="center", fontsize=8)
        created_figures.append(("Fig. 7. RunPod calibration and uncertainty evidence", save("fig7_runpod_calibration_uncertainty.png")))

# 4. Feature importance
if feat_summary is not None:
    feat_col = find_col(feat_summary, ["feature"])
    imp_col = find_col(feat_summary, ["importance", "mean", "score"])
    if feat_col and imp_col:
        df = feat_summary[[feat_col, imp_col]].dropna().copy()
        df = df.sort_values(imp_col, ascending=True).tail(10)
        plt.figure(figsize=(9, 5.2))
        plt.barh(df[feat_col].astype(str), df[imp_col].astype(float))
        plt.xlabel("Importance")
        plt.title("Fig. 8. RunPod feature-importance evidence")
        created_figures.append(("Fig. 8. RunPod feature-importance evidence", save("fig8_runpod_feature_importance.png")))

# 5. Ablation
if abl is not None:
    variant_col = find_col(abl, ["variant", "model", "ablation"])
    f1_col = find_col(abl, ["macro_f1", "macro f1", "f1"])
    if variant_col and f1_col:
        df = abl[[variant_col, f1_col]].dropna().copy()
        df = df.sort_values(f1_col, ascending=True)
        plt.figure(figsize=(8.8, 5.2))
        plt.barh(df[variant_col].astype(str), df[f1_col].astype(float))
        plt.xlabel("Macro F1")
        plt.title("Fig. 9. RunPod ablation evidence")
        for i, v in enumerate(df[f1_col].astype(float)):
            plt.text(v + 0.005, i, f"{v:.4f}", va="center", fontsize=8)
        created_figures.append(("Fig. 9. RunPod ablation evidence", save("fig9_runpod_ablation.png")))

# 6. Runtime
if runtime is not None:
    metric_col = find_col(runtime, ["metric", "name"])
    value_col = find_col(runtime, ["value", "mean"])
    if metric_col and value_col:
        df = runtime[[metric_col, value_col]].dropna().copy()
        numeric = pd.to_numeric(df[value_col], errors="coerce")
        df = df[numeric.notna()].copy()
        df[value_col] = pd.to_numeric(df[value_col], errors="coerce")
        plt.figure(figsize=(9.2, 5.2))
        plt.barh(df[metric_col].astype(str), df[value_col].astype(float))
        plt.xlabel("Value")
        plt.title("Fig. 10. RunPod runtime-complexity evidence")
        created_figures.append(("Fig. 10. RunPod runtime-complexity evidence", save("fig10_runpod_runtime_complexity.png")))

# Build markdown evidence tables
tables_md = ["# Real RunPod Evidence Tables v1\n"]

tables = [
    ("Table R1. Model comparison summary from RunPod", model_summary),
    ("Table R2. Model comparison across all seeds", model_all),
    ("Table R3. OOD summary from RunPod", ood_summary),
    ("Table R4. OOD across all seeds", ood_all),
    ("Table R5. Calibration/uncertainty summary", unc_summary),
    ("Table R6. Calibration/uncertainty across all seeds", unc_all),
    ("Table R7. Feature-importance summary", feat_summary),
    ("Table R8. Ablation summary", abl),
    ("Table R9. Runtime-complexity summary", runtime),
]

for title, df in tables:
    tables_md.append(f"## {title}\n")
    tables_md.append(md_table(df, max_rows=18))
    tables_md.append("")

(TABLES / "hcc_real_runpod_evidence_tables_v1.md").write_text("\n".join(tables_md))
print("Saved docs/tables/hcc_real_runpod_evidence_tables_v1.md")

# Insert/replace evidence block in Results section
if RESULTS_DOC.exists():
    r = RESULTS_DOC.read_text()

    block = ["### 5.0. Real RunPod experimental evidence package\n"]
    block.append("This subsection consolidates the actual RunPod-generated experimental evidence used in the manuscript, including model-comparison summaries, OOD stress-test outputs, uncertainty/calibration summaries, feature-importance results, ablation evidence, and runtime-complexity profiling. Unlike conceptual architecture figures, these figures are generated directly from the extracted RunPod CSV result artifacts.\n")

    for caption, path in created_figures:
        rel = path.as_posix()
        block.append(f"![{caption}]({rel})\n")

    block.append("The corresponding publication-quality evidence tables are generated in `docs/tables/hcc_real_runpod_evidence_tables_v1.md` and should be used as the source for final manuscript tables.\n")
    block_text = "\n".join(block)

    if "### 5.0. Real RunPod experimental evidence package" in r:
        start = r.find("### 5.0. Real RunPod experimental evidence package")
        end = r.find("### 5.1. In-distribution mission-state recognition", start)
        if end != -1:
            r = r[:start] + block_text + "\n" + r[end:]
    else:
        r = r.replace("### 5.1. In-distribution mission-state recognition", block_text + "\n### 5.1. In-distribution mission-state recognition")

    RESULTS_DOC.write_text(r)
    print("Inserted real RunPod evidence package into Results section.")

print(f"Created figures: {len(created_figures)}")
for caption, path in created_figures:
    print(caption, "->", path)

#!/usr/bin/env python3
from pathlib import Path
import pandas as pd
import re

ROOT = Path(".")
SUMMARY = ROOT / "runpod_artifacts/extracted/trust-swarm-journal-results/results/journal/summary"
HCC = ROOT / "results/hcc"
RESULTS_DOC = ROOT / "docs/hcc_results_discussion_v2.md"
OUT_TABLES = ROOT / "docs/tables/hcc_real_runpod_compact_tables_v1.md"

def norm(s):
    return re.sub(r"[^a-z0-9]+", "_", str(s).lower()).strip("_")

def find_col(df, choices):
    for c in df.columns:
        lc = norm(c)
        for choice in choices:
            if norm(choice) in lc:
                return c
    return None

def read(path):
    if not path.exists():
        return None
    try:
        return pd.read_csv(path)
    except Exception:
        return None

def round_df(df):
    out = df.copy()
    for c in out.columns:
        converted = pd.to_numeric(out[c], errors="coerce")
        # Convert only if at least one value is numeric; otherwise keep text columns unchanged.
        if converted.notna().any():
            out[c] = converted
            if pd.api.types.is_float_dtype(out[c]):
                out[c] = out[c].round(4)
    return out

def md(df):
    if df is None or df.empty:
        return "_Not available._"
    return round_df(df).to_markdown(index=False)

model = read(SUMMARY / "model_comparison_summary.csv")
ood = read(SUMMARY / "ood_summary.csv")
unc = read(SUMMARY / "uncertainty_summary.csv")
feat = read(SUMMARY / "feature_importance_summary.csv")
abl = read(HCC / "ablation_summary.csv")
runtime = read(HCC / "runtime_complexity_summary.csv")

blocks = []

# Table R1: model comparison
if model is not None:
    model_col = find_col(model, ["model", "classifier", "method"])
    acc_col = find_col(model, ["accuracy", "acc"])
    f1_col = find_col(model, ["macro_f1", "f1_macro", "macro f1"])
    cols = [c for c in [model_col, acc_col, f1_col] if c]
    t = model[cols].copy() if cols else model.copy()
    blocks += [
        "### Table R1. RunPod model-comparison summary",
        md(t),
        ""
    ]

# Table R2: OOD
if ood is not None:
    cond_col = find_col(ood, ["condition", "scenario", "attack", "ood"])
    f1_col = find_col(ood, ["macro_f1", "f1"])
    ent_col = find_col(ood, ["entropy"])
    cols = [c for c in [cond_col, f1_col, ent_col] if c]
    t = ood[cols].copy() if cols else ood.copy()
    blocks += [
        "### Table R2. RunPod OOD stress-test summary",
        md(t),
        ""
    ]

# Table R3: calibration uncertainty
if unc is not None:
    blocks += [
        "### Table R3. RunPod calibration and uncertainty summary",
        md(unc),
        ""
    ]

# Table R4: feature importance
if feat is not None:
    feat_col = find_col(feat, ["feature"])
    imp_col = find_col(feat, ["importance", "mean", "score"])
    cols = [c for c in [feat_col, imp_col] if c]
    t = feat[cols].copy() if cols else feat.copy()
    if imp_col:
        t = t.sort_values(imp_col, ascending=False).head(10)
    blocks += [
        "### Table R4. RunPod top telemetry feature-importance summary",
        md(t),
        ""
    ]

# Table R5: ablation
if abl is not None:
    blocks += [
        "### Table R5. RunPod ablation summary",
        md(abl),
        ""
    ]

# Table R6: runtime
if runtime is not None:
    blocks += [
        "### Table R6. RunPod runtime-complexity summary",
        md(runtime),
        ""
    ]

table_block = "\n".join(blocks).strip()
OUT_TABLES.write_text("# Compact Real RunPod Evidence Tables v1\n\n" + table_block + "\n")
print(f"Saved {OUT_TABLES}")

if not RESULTS_DOC.exists():
    raise FileNotFoundError(RESULTS_DOC)

r = RESULTS_DOC.read_text()

insert = f"""
### 5.0.1. Compact real RunPod evidence tables

The following compact tables are generated from the real extracted RunPod CSV outputs. They provide the numerical evidence behind the model-comparison, OOD, calibration, feature-importance, ablation, and runtime claims.

{table_block}

"""

# Remove old auto preview section if present, because it is ugly and too raw.
start = r.find("### 5.9. Automatically inserted result-table previews")
if start != -1:
    r = r[:start].rstrip() + "\n"

# Insert compact evidence tables after real RunPod evidence package.
if "### 5.0.1. Compact real RunPod evidence tables" in r:
    s = r.find("### 5.0.1. Compact real RunPod evidence tables")
    e = r.find("### 5.1. In-distribution mission-state recognition", s)
    if e != -1:
        r = r[:s] + insert + "\n" + r[e:]
else:
    anchor = "### 5.1. In-distribution mission-state recognition"
    r = r.replace(anchor, insert + "\n" + anchor)

RESULTS_DOC.write_text(r)
print("Inserted compact real RunPod evidence tables into Results section.")

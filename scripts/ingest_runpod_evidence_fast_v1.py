#!/usr/bin/env python3
from pathlib import Path
import tarfile, zipfile, shutil, csv, re

ROOT = Path(".").resolve()
EXTRACT_DIR = ROOT / "runpod_artifacts" / "extracted"
FIG_DIR = ROOT / "figures" / "runpod_evidence"
DOC_DIR = ROOT / "docs" / "runpod_evidence"
RESULTS_DOC = ROOT / "docs" / "hcc_results_discussion_v2.md"

for d in [EXTRACT_DIR, FIG_DIR, DOC_DIR]:
    d.mkdir(parents=True, exist_ok=True)

archives = []
for pat in ["*trust-swarm*results*.tar.gz", "*trust*swarm*.tar.gz", "*results*.tar.gz", "*trust*swarm*.zip", "*results*.zip"]:
    archives.extend(ROOT.glob(pat))
    archives.extend((Path.home() / "Downloads").glob(pat))

archives = sorted(set([p for p in archives if p.is_file()]))
print(f"Archives found: {len(archives)}")
for a in archives:
    print(" -", a)

def safe(s):
    return re.sub(r"[^A-Za-z0-9._-]+", "_", s)[:140]

def cat(p):
    n = p.name.lower()
    if "confusion" in n or "matrix" in n: return "confusion_matrix"
    if "calibration" in n or "ece" in n or "brier" in n: return "calibration"
    if "ood" in n or "stress" in n or "drift" in n or "tamper" in n: return "ood_stress"
    if "ablation" in n: return "ablation"
    if "runtime" in n or "latency" in n or "throughput" in n: return "runtime"
    if "feature" in n or "importance" in n or "explain" in n: return "explainability"
    if "loss" in n or "train" in n or "epoch" in n: return "training_curve"
    if "baseline" in n or "cnn" in n or "lstm" in n or "gru" in n: return "baseline"
    return "other"

for a in archives:
    dest = EXTRACT_DIR / safe(a.name.replace(".tar.gz", "").replace(".zip", ""))
    dest.mkdir(parents=True, exist_ok=True)
    try:
        if a.name.endswith(".tar.gz"):
            with tarfile.open(a, "r:gz") as t:
                t.extractall(dest)
        elif a.suffix == ".zip":
            with zipfile.ZipFile(a) as z:
                z.extractall(dest)
        print(f"Extracted {a.name}")
    except Exception as e:
        print(f"FAILED {a}: {e}")

files = []
for base in [EXTRACT_DIR, ROOT / "results", ROOT / "figures"]:
    if base.exists():
        files.extend([p for p in base.rglob("*") if p.is_file()])

imgs = [p for p in files if p.suffix.lower() in [".png", ".jpg", ".jpeg"]]
csvs = [p for p in files if p.suffix.lower() == ".csv"]

rows = []
copied = []
for i, p in enumerate(sorted(imgs), 1):
    c = cat(p)
    out = FIG_DIR / f"runpod_fig_{i:02d}_{c}_{safe(p.stem)}{p.suffix.lower()}"
    shutil.copy2(p, out)
    copied.append((c, out))
    rows.append([c, "image", str(p), str(out)])

for p in sorted(csvs):
    rows.append([cat(p), "csv", str(p), ""])

with (DOC_DIR / "runpod_evidence_inventory_v1.csv").open("w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["category", "type", "source_path", "paper_path"])
    w.writerows(rows)

md = ["# RunPod Evidence Inventory v1", "", f"Archives found: **{len(archives)}**", f"Images copied: **{len(copied)}**", f"CSV files found: **{len(csvs)}**", ""]
for i, (c, out) in enumerate(copied, 1):
    rel = out.relative_to(ROOT)
    cap = c.replace("_", " ").title()
    md += [f"## RunPod Fig. R{i}. {cap}", f"![RunPod Fig. R{i}. {cap}]({rel})", ""]
(DOC_DIR / "runpod_evidence_inventory_v1.md").write_text("\n".join(md))

if RESULTS_DOC.exists() and copied:
    r = RESULTS_DOC.read_text()
    block = ["\n### 5.0. RunPod-generated experimental evidence\n", "The following figures are copied from the RunPod experimental artifact archive and provide direct evidence from the executed pipeline.\n"]
    for i, (c, out) in enumerate(copied, 1):
        rel = out.relative_to(ROOT)
        cap = c.replace("_", " ").title()
        block.append(f"![RunPod Fig. R{i}. {cap}]({rel})\n")
    if "### 5.0. RunPod-generated experimental evidence" not in r:
        r = r.replace("### 5.1. In-distribution mission-state recognition", "\n".join(block) + "\n### 5.1. In-distribution mission-state recognition")
        RESULTS_DOC.write_text(r)

print(f"Copied images: {len(copied)}")
print(f"CSV files: {len(csvs)}")
print("Saved inventory in docs/runpod_evidence/")

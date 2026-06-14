# HCC RunPod Final Commands

## Purpose

Use this file on RunPod GPU to generate final High-Confidence Computing evidence:

1. Final ablation study
2. Final runtime and complexity profiling
3. Final HCC reports

## Step 1: Enter Project

```bash
cd /workspace/trust-swarm-ai
source .venv/bin/activate
git pull
```

## Step 2: Check GPU

```bash
nvidia-smi

python - <<'PY'
import torch
print("Torch:", torch.__version__)
print("CUDA available:", torch.cuda.is_available())
if torch.cuda.is_available():
    print("GPU:", torch.cuda.get_device_name(0))
PY
```

## Step 3: Confirm Dataset Exists

```bash
find data results /workspace -name "graph_windows.pt" 2>/dev/null
```

Expected path:

```bash
data/processed/seed_42/graph_windows.pt
```

If missing, generate it:

```bash
mkdir -p data/raw/seed_42 data/processed/seed_42

python scripts/generate_realistic_telemetry.py \
  --runs 300 \
  --timesteps 240 \
  --uavs 20 \
  --seed 42 \
  --output data/raw/seed_42/telemetry.csv

python scripts/build_graph_dataset.py \
  --input data/raw/seed_42/telemetry.csv \
  --output-dir data/processed/seed_42 \
  --window-size 20
```

## Step 4: Run Final HCC Ablation Study

```bash
python scripts/run_hcc_ablation_study.py \
  --data data/processed/seed_42/graph_windows.pt \
  --epochs 30 \
  --batch-size 128 \
  --device cuda
```

Expected outputs:

```bash
results/hcc/ablation_summary.csv
docs/hcc_ablation_report.md
```

Check:

```bash
cat docs/hcc_ablation_report.md
head -10 results/hcc/ablation_summary.csv
```

## Step 5: Run Final Runtime and Complexity Profiling

```bash
python scripts/profile_runtime_complexity.py \
  --batch-size 128 \
  --warmup 10 \
  --iters 50 \
  --device cuda
```

Expected outputs:

```bash
results/hcc/runtime_complexity_summary.csv
docs/hcc_runtime_complexity_report.md
```

Check:

```bash
cat docs/hcc_runtime_complexity_report.md
head -10 results/hcc/runtime_complexity_summary.csv
```

## Step 6: Rebuild HCC Manuscript v1

```bash
python scripts/build_hcc_manuscript_v1.py
python scripts/check_hcc_manuscript_quality.py

cat docs/hcc_manuscript_quality_check.md
```

## Step 7: Commit Only Code and Reports

Do not commit generated raw/processed dataset folders.

```bash
git status

git add \
  docs/hcc_ablation_report.md \
  docs/hcc_runtime_complexity_report.md \
  docs/hcc_manuscript_quality_check.md \
  results/hcc/ablation_summary.csv \
  results/hcc/runtime_complexity_summary.csv \
  manuscript/TRUST-Swarm-HCC-manuscript-v1.md

git commit -m "Add final HCC ablation and runtime evidence"
git push
git status
```

## Important Warning

Do not run full 30-epoch ablation on Mac. Use RunPod GPU only.

Mac is okay only for this quick sanity command:

```bash
python scripts/run_hcc_ablation_study.py \
  --data data/processed/seed_42/graph_windows.pt \
  --epochs 1 \
  --batch-size 64 \
  --max-samples 5000
```


# TRUST-Swarm Final Journal RunPod Commands

## Purpose

Run final journal-grade experiments for TRUST-Swarm using realistic telemetry, temporal baselines, Graph-Temporal Transformer, uncertainty, OOD, explainability, and multi-seed aggregation.

## Recommended Pod

Use H200 or RTX 4090.

Preferred:
- H200 for faster multi-seed run.
- RTX 4090 if cost is priority.

## Setup on RunPod

git clone https://github.com/drsaikrishnathota1/trust-swarm-ai.git
cd trust-swarm-ai

python -m venv .venv
source .venv/bin/activate

python -m pip install --upgrade pip
python -m pip install numpy pandas scikit-learn matplotlib pyyaml tqdm gymnasium stable-baselines3
python -m pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu128
python -m pip install -e . --no-deps

## Check GPU

python - <<'PY'
import torch
print("Torch:", torch.__version__)
print("CUDA available:", torch.cuda.is_available())
if torch.cuda.is_available():
    print("GPU:", torch.cuda.get_device_name(0))
PY

Do not continue unless CUDA available is True.

## Small Validation Run

RUNS=10 TIMESTEPS=80 UAVS=10 EPOCHS=1 BATCH_SIZE=32 SEEDS="42" ./scripts/run_journal_experiments.sh
python scripts/aggregate_journal_results.py

If validation works, remove validation outputs:

rm -rf data/raw/realistic_seed_42.csv
rm -rf data/processed/seed_42
rm -rf results/journal

## Final Journal Run

RUNS=300 TIMESTEPS=240 UAVS=20 EPOCHS=30 BATCH_SIZE=128 SEEDS="42 123 2026" ./scripts/run_journal_experiments.sh
python scripts/aggregate_journal_results.py

## Expected Outputs

results/journal/seed_42/
results/journal/seed_123/
results/journal/seed_2026/
results/journal/summary/

Important summary files:

results/journal/summary/model_comparison_summary.csv
results/journal/summary/uncertainty_summary.csv
results/journal/summary/ood_summary.csv
results/journal/summary/feature_importance_summary.csv

## Package Results

tar -czf trust-swarm-journal-results.tar.gz results/journal
ls -lh trust-swarm-journal-results.tar.gz

## Download From Mac

No custom port:

scp root@HOST:/workspace/trust-swarm-ai/trust-swarm-journal-results.tar.gz ~/Downloads/

With custom port:

scp -P PORT root@HOST:/workspace/trust-swarm-ai/trust-swarm-journal-results.tar.gz ~/Downloads/

Replace HOST and PORT from the RunPod Connect tab.

## Stop Pod

Stop the pod only after confirming the .tar.gz file is downloaded to your Mac.

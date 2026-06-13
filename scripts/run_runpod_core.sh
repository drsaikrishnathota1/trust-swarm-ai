#!/usr/bin/env bash
set -e

echo "=== TRUST-Swarm RunPod Core Pipeline ==="

echo "[0/6] Checking GPU..."
python - <<'PY'
import torch
print("CUDA available:", torch.cuda.is_available())
if torch.cuda.is_available():
    print("GPU:", torch.cuda.get_device_name(0))
PY

echo "[1/6] Generating tiny telemetry sanity dataset..."
python scripts/generate_tiny_telemetry.py \
  --output data/raw/tiny_telemetry.csv \
  --runs 24 \
  --timesteps 100 \
  --uavs 10

echo "[2/6] Building graph-temporal dataset..."
python scripts/build_graph_dataset.py \
  --input data/raw/tiny_telemetry.csv \
  --output-dir data/processed

echo "[3/6] Training Graph-Temporal Transformer..."
PYTHONPATH=. python scripts/train_graph_transformer.py \
  --data data/processed/graph_windows.pt \
  --epochs 20 \
  --batch-size 64

echo "[4/6] Evaluating uncertainty calibration..."
PYTHONPATH=. python scripts/evaluate_uncertainty.py \
  --data data/processed/graph_windows.pt \
  --model results/models/graph_temporal_transformer.pt \
  --mc-samples 20

echo "[5/6] Evaluating OOD unseen attacks..."
PYTHONPATH=. python scripts/evaluate_ood.py \
  --data data/processed/graph_windows.pt \
  --model results/models/graph_temporal_transformer.pt

echo "[6/6] Generating explainability feature importance..."
PYTHONPATH=. python scripts/explain_feature_importance.py \
  --data data/processed/graph_windows.pt \
  --model results/models/graph_temporal_transformer.pt

echo "=== TRUST-Swarm RunPod core pipeline completed ==="


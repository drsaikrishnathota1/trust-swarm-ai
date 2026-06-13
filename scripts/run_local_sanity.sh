#!/usr/bin/env bash
set -e

echo "=== TRUST-Swarm Local Sanity Test ==="

echo "[1/5] Generating tiny telemetry..."
python scripts/generate_tiny_telemetry.py \
  --output data/raw/tiny_telemetry.csv \
  --runs 16 \
  --timesteps 80 \
  --uavs 10

echo "[2/5] Building graph dataset..."
python scripts/build_graph_dataset.py \
  --input data/raw/tiny_telemetry.csv \
  --output-dir data/processed

echo "[3/5] Training Graph-Temporal Transformer for 2 epochs..."
PYTHONPATH=. python scripts/train_graph_transformer.py \
  --data data/processed/graph_windows.pt \
  --epochs 2 \
  --batch-size 16

echo "[4/5] Evaluating uncertainty..."
PYTHONPATH=. python scripts/evaluate_uncertainty.py \
  --data data/processed/graph_windows.pt \
  --model results/models/graph_temporal_transformer.pt \
  --mc-samples 5

echo "[5/5] Evaluating OOD behavior..."
PYTHONPATH=. python scripts/evaluate_ood.py \
  --data data/processed/graph_windows.pt \
  --model results/models/graph_temporal_transformer.pt

echo "=== Local sanity test completed successfully ==="

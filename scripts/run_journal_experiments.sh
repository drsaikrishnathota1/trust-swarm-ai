#!/usr/bin/env bash
set -e

echo "=== TRUST-Swarm Journal-Level Experiment Runner ==="

# Default values. Override like:
# RUNS=300 TIMESTEPS=240 UAVS=20 EPOCHS=30 BATCH_SIZE=128 ./scripts/run_journal_experiments.sh

RUNS=${RUNS:-300}
TIMESTEPS=${TIMESTEPS:-240}
UAVS=${UAVS:-20}
EPOCHS=${EPOCHS:-30}
BATCH_SIZE=${BATCH_SIZE:-128}
SEEDS=${SEEDS:-"42 123 2026"}

echo "Runs: $RUNS"
echo "Timesteps: $TIMESTEPS"
echo "UAVs: $UAVS"
echo "Epochs: $EPOCHS"
echo "Batch size: $BATCH_SIZE"
echo "Seeds: $SEEDS"

mkdir -p results/journal

for SEED in $SEEDS; do
  echo ""
  echo "======================================"
  echo "Running TRUST-Swarm journal seed: $SEED"
  echo "======================================"

  RAW_CSV="data/raw/realistic_seed_${SEED}.csv"
  SUMMARY_CSV="results/journal/dataset_summary_seed_${SEED}.csv"
  PROCESSED_DIR="data/processed/seed_${SEED}"
  OUTPUT_DIR="results/journal/seed_${SEED}"

  mkdir -p "$PROCESSED_DIR"
  mkdir -p "$OUTPUT_DIR"

  echo "[1/7] Generating realistic telemetry..."
  python scripts/generate_realistic_telemetry.py \
    --output "$RAW_CSV" \
    --summary-output "$SUMMARY_CSV" \
    --runs "$RUNS" \
    --timesteps "$TIMESTEPS" \
    --uavs "$UAVS" \
    --seed "$SEED"

  echo "[2/7] Building graph windows..."
  python scripts/build_graph_dataset.py \
    --input "$RAW_CSV" \
    --output-dir "$PROCESSED_DIR"

  echo "[3/7] Training LSTM/GRU/1D-CNN baselines..."
  python scripts/train_baselines.py \
    --data "$PROCESSED_DIR/graph_windows.pt" \
    --output-dir "$OUTPUT_DIR" \
    --epochs "$EPOCHS" \
    --batch-size "$BATCH_SIZE" \
    --seed "$SEED"

  echo "[4/7] Training Graph-Temporal Transformer..."
  python scripts/train_graph_transformer.py \
    --data "$PROCESSED_DIR/graph_windows.pt" \
    --output-dir "$OUTPUT_DIR" \
    --epochs "$EPOCHS" \
    --batch-size "$BATCH_SIZE" \
    --seed "$SEED"

  echo "[5/7] Evaluating uncertainty..."
  python scripts/evaluate_uncertainty.py \
    --data "$PROCESSED_DIR/graph_windows.pt" \
    --model "$OUTPUT_DIR/models/graph_temporal_transformer.pt" \
    --output "$OUTPUT_DIR/csv/uncertainty_metrics.csv" \
    --mc-samples 20 \
    --seed "$SEED"

  echo "[6/7] Evaluating OOD unseen attacks..."
  python scripts/evaluate_ood.py \
    --data "$PROCESSED_DIR/graph_windows.pt" \
    --model "$OUTPUT_DIR/models/graph_temporal_transformer.pt" \
    --output "$OUTPUT_DIR/csv/ood_unseen_attack_results.csv" \
    --seed "$SEED"

  echo "[7/7] Generating explainability feature importance..."
  python scripts/explain_feature_importance.py \
    --data "$PROCESSED_DIR/graph_windows.pt" \
    --model "$OUTPUT_DIR/models/graph_temporal_transformer.pt" \
    --output-csv "$OUTPUT_DIR/csv/feature_importance.csv" \
    --output-fig "$OUTPUT_DIR/figures/feature_importance.png" \
    --seed "$SEED"

  echo "Completed seed: $SEED"
done

echo ""
echo "=== TRUST-Swarm journal experiments completed ==="
echo "Results saved under: results/journal/"

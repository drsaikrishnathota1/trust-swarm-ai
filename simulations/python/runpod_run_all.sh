#!/bin/bash
# RA-MARS v4 RunPod Master Script
# Runs all 9 steps in sequence on a single GPU pod
# Expected runtime: ~45-90 mins on RTX 4090/A6000-class GPU

set -e

echo "=============================================="
echo "RA-MARS v4 Full Pipeline — RunPod"
echo "=============================================="
echo "Started: $(date)"
echo ""

cd /workspace

if [ ! -d "ra-mars-defence-technology" ]; then
    git clone https://github.com/drsaikrishnathota1/ra-mars-defence-technology.git
fi

cd ra-mars-defence-technology

echo "Installing dependencies..."
pip install numpy pandas scikit-learn torch scipy matplotlib seaborn foolbox --quiet

mkdir -p simulations/datasets simulations/results

echo ""
echo "STEP 1/9: Generating v4 physics-based dataset..."
python simulations/python/generate_dataset_v4.py
echo "✓ Step 1 complete"

echo ""
echo "STEP 2/9: Creating raw sequence windows for LSTM/GRU/CNN..."
python simulations/python/create_sequence_windows_v4.py
echo "✓ Step 2 complete"

echo ""
echo "STEP 3/9: Training v4 binary + fine-grained LSTM/GRU models..."
python simulations/python/train_sequence_models_v4.py
echo "✓ Step 3 complete"

echo ""
echo "STEP 4/9: Training classical baseline models..."
python simulations/python/train_classical_baselines_v4.py
echo "✓ Step 4 complete"

echo ""
echo "STEP 5/9: Training 1D-CNN temporal baseline..."
python simulations/python/train_cnn_baseline_v4.py
echo "✓ Step 5 complete"

echo ""
echo "STEP 6/9: Running mission assurance, ablation, scalability, intensity, and SINR evaluation..."
python simulations/python/evaluate_ablation_v4.py
echo "✓ Step 6 complete"

echo ""
echo "STEP 7/9: Running FGSM + PGD adversarial robustness tests..."
ls simulations/results/best_model_v4_*.pt 2>/dev/null && echo "Model files found" || echo "No model files found"
python simulations/python/adversarial_robustness_v4.py
echo "✓ Step 7 complete"

echo ""
echo "STEP 8/9: Computing latency budget analysis..."
python simulations/python/latency_budget_v4.py
echo "✓ Step 8 complete"

echo ""
echo "STEP 9/9: Running PGD-augmented adversarial training..."
python simulations/python/train_adversarial_v4.py
echo "✓ Step 9 complete"

echo ""
echo "=============================================="
echo "ALL 9 STEPS COMPLETE"
echo "Finished: $(date)"
echo ""
echo "Results generated:"
ls -lh simulations/results/*.csv 2>/dev/null | awk '{print "  "$5, $9}'
echo ""
echo "Important outputs:"
echo "  simulations/results/model_performance_v4_binary.csv"
echo "  simulations/results/model_performance_v4_finegrained.csv"
echo "  simulations/results/model_performance_v4_cnn_baseline.csv"
echo "  simulations/results/model_performance_v4_classical.csv"
echo "  simulations/results/adversarial_training_results_v4.csv"
echo "  simulations/results/best_model_v4_adversarial.pt"
echo "  simulations/datasets/uav_mission_telemetry_v4_sample.csv"
echo "  simulations/datasets/uav_sequence_windows_v4.npz"
echo ""
echo "Before terminating RunPod, archive results with:"
echo "  tar -czf ra_mars_results_v4_final.tar.gz simulations/results simulations/datasets/uav_mission_telemetry_v4_sample.csv simulations/datasets/uav_sequence_windows_v4.npz"
echo "=============================================="

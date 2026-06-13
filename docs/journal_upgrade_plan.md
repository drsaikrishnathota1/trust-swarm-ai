# TRUST-Swarm Journal Upgrade Plan

## Current Status

The RunPod validation run confirmed that the full TRUST-Swarm scaffold works end-to-end:

- Graph-Temporal Transformer training completed.
- Uncertainty calibration completed.
- OOD/unseen attack evaluation completed.
- Feature-importance explainability completed.
- PPO/DRL recovery completed.
- Results were downloaded and verified locally.

## Validation Results Summary

### Graph-Temporal Transformer

- Accuracy: 0.9897
- Macro F1: 0.9896
- Macro Precision: 0.9900
- Macro Recall: 0.9896

### Uncertainty Calibration

- Expected Calibration Error: 0.0465
- Brier Score: 0.0174
- Mean Confidence: 0.9467
- Mean Predictive Entropy: 0.2374

### OOD / Unseen Attack Behavior

The model performed strongly on in-distribution and moderate OOD conditions, while entropy increased under harder unseen attacks.

Key observation:

- In-distribution entropy: 0.1991
- Slow GPS drift entropy: 0.4234
- Delayed combined attack entropy: 0.6596

This supports the claim that TRUST-Swarm can expose higher uncertainty under harder cyber-physical shifts.

### Explainability

Top important features by macro-F1 drop:

1. zone_coverage
2. latency_ms
3. route_deviation_m
4. gps_jump_m

This supports an interpretable mission-assurance story.

### PPO / DRL Recovery

- Mission success: 0.99
- Initial MAI: approximately 0.617
- Final MAI: approximately 0.693
- MAI improvement: approximately 0.076

However, the policy mostly selected Return to Base, so the DRL reward/action design must be improved for journal-level contribution.

## Why Current Results Are Not Final Journal Results

The current validation used a small synthetic scaffold dataset. The results prove the pipeline works, but reviewers may consider the task too easy.

For journal submission, the following upgrades are required:

1. Larger realistic dataset.
2. Multiple baseline models.
3. Repeated runs with multiple seeds.
4. Stronger OOD attack scenarios.
5. Improved PPO reward design.
6. More balanced recovery action distribution.
7. Final paper-quality figures and tables.

## Required Journal-Level Experiments

### Experiment 1 — Larger Dataset

Create a larger TRUST-Swarm dataset with:

- 10, 20, and 40 UAV swarm sizes.
- Longer missions.
- Multiple mission zones.
- Mixed attack timing.
- More realistic noise.
- Class imbalance.

Target size:

- Minimum: 100,000 windows.
- Preferred: 300,000+ windows.

### Experiment 2 — Baseline Model Comparison

Compare:

- LSTM
- GRU
- 1D-CNN
- GAT-LSTM
- Graph Transformer
- Graph-Temporal Transformer

Metrics:

- Accuracy
- Macro F1
- Macro Precision
- Macro Recall
- False positive rate
- False negative rate
- Inference latency

### Experiment 3 — Repeated Seeds

Run final results using:

- seed 42
- seed 123
- seed 2026

Report:

- mean
- standard deviation

### Experiment 4 — Uncertainty and Calibration

Report:

- Expected Calibration Error
- Brier Score
- Reliability diagram
- Mean confidence
- Predictive entropy
- False high-confidence error rate

### Experiment 5 — OOD / Unseen Attacks

Test:

- stealth low-power jammer
- slow GPS drift
- intermittent tampering
- unseen jammer location
- delayed combined attack
- unseen swarm size
- mixed attack with delayed onset

Report:

- OOD macro F1
- entropy shift
- confidence drop
- low-confidence rate
- OOD AUROC if available

### Experiment 6 — Explainability

Generate:

- feature importance table
- feature importance figure
- UAV-node attention heatmap
- attack-specific explanation examples

### Experiment 7 — PPO / DRL Recovery Upgrade

Improve reward design so policy does not overuse Return to Base.

Add penalties for:

- unnecessary Return to Base
- coverage loss
- excessive energy use
- unsafe continuation under high uncertainty

Report:

- mission success
- MAI improvement
- recovery time
- energy cost
- action distribution
- unsafe-action rate

## Required Manuscript Tables

1. Comparison with RA-MARS baseline.
2. Dataset configuration table.
3. Model comparison table.
4. Uncertainty and calibration table.
5. OOD unseen attack table.
6. Explainability feature-importance table.
7. DRL recovery table.
8. Ablation study table.

## Required Manuscript Figures

1. TRUST-Swarm architecture.
2. Dynamic UAV graph construction.
3. Graph-Temporal Transformer architecture.
4. Training curves.
5. Reliability diagram.
6. OOD confidence/entropy shift.
7. Feature-importance heatmap.
8. PPO recovery action distribution.

## Next Technical Tasks

1. Add realistic dataset generator.
2. Add baseline models.
3. Add multi-seed runner.
4. Add final results aggregation script.
5. Improve PPO reward and action balance.
6. Generate final manuscript-ready figures.

# TRUST-Swarm RunPod Roadmap

## Target GPU Budget

Recommended: 85–100 RTX 4090 GPU hours.

Full differentiation with PPO/DRL recovery: 110–130 GPU hours.

Hard stop: 150 GPU hours.

## Phase 0 — Local Prep

GPU hours: 0

Tasks:
- Confirm baseline RA-MARS CSVs are available.
- Confirm raw telemetry source path.
- Push latest repo before renting GPU.
- Do not use RunPod for writing or folder cleanup.

## Phase 1 — RunPod Setup

GPU hours: 4–6

Commands:
- Clone repo.
- Create Python virtual environment.
- Install requirements.
- Confirm CUDA works.
- Run one mini training sanity check.

Exit criteria:
- CUDA works.
- PyTorch Geometric imports correctly.
- One tiny model run completes.

## Phase 2 — Graph Dataset

GPU hours: 3–5

Goal:
Convert UAV telemetry into graph-temporal tensors:

20 timesteps x N UAV nodes x 9 features

Outputs:
- data/processed/graph_train.pt
- data/processed/graph_val.pt
- data/processed/graph_test.pt
- data/processed/graph_ood.pt

## Phase 3 — Graph-Temporal AI Training

GPU hours: 25–35

Train:
- GAT-LSTM
- Graph Transformer
- Graph-Temporal Transformer

Compare against:
- LSTM
- GRU
- 1D-CNN
- RA-MARS baseline

Metrics:
- Accuracy
- Macro F1
- FPR/FNR
- Detection delay
- Inference latency

## Phase 4 — Uncertainty

GPU hours: 10–15

Use:
- MC dropout first
- Optional conformal prediction

Metrics:
- Expected Calibration Error
- Brier score
- Confidence under known attacks
- Confidence under OOD attacks

## Phase 5 — OOD Attacks

GPU hours: 8–12

OOD cases:
- Stealth low-power jammer
- Slow GPS drift
- Intermittent tampering
- Unseen jammer location
- Delayed combined attack
- Unseen swarm size

## Phase 6 — Explainability

GPU hours: 5–8

Use:
- Attention heatmaps
- Captum Integrated Gradients
- SHAP-style attribution if feasible

Figures:
- Feature importance by attack type
- UAV-node attention map
- Combined-attack explanation

## Optional Phase 7 — PPO/DRL Recovery

GPU hours: 25–35

State:
MAI components + attack label + uncertainty + SINR + battery + coverage

Actions:
Continue, Monitor, Reroute, Reassign, Isolate Node, Return to Base

Reward:
Mission success + coverage - energy penalty - recovery delay - unsafe action penalty

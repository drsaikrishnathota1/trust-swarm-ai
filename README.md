# TRUST-Swarm

**Trustworthy Graph-Temporal AI for High-Confidence Multi-UAV Mission Assurance Under Cyber-Physical Attacks**

TRUST-Swarm is an AI-first research workspace for developing a new high-confidence intelligent-computing manuscript on multi-UAV mission assurance under cyber-physical attacks.

This project uses the RA-MARS simulation foundation as a baseline, but the new paper will focus on graph-temporal AI, uncertainty-aware prediction, explainable AI, out-of-distribution attack detection, and reinforcement-learning-based recovery.

## Planned Manuscript Title

**TRUST-Swarm: Trustworthy Graph-Temporal AI for High-Confidence Multi-UAV Mission Assurance Under Cyber-Physical Attacks**

## Core Differentiation

| Dimension | RA-MARS Baseline | TRUST-Swarm Target |
|---|---|---|
| Primary framing | Mission-assurance digital twin | Trustworthy graph-temporal AI |
| Detector | LSTM / GRU / 1D-CNN | GAT-LSTM / Graph Transformer / Graph-Temporal Transformer |
| Recovery logic | One-step projected MAI action selector | PPO / DRL recovery policy |
| Trust layer | Hash-chain provenance | Uncertainty + explainability + OOD trust |
| Robustness | FGSM/PGD classifier robustness | OOD, calibration, unseen attacks |
| Journal fit | Defence Technology | High-Confidence Computing |

## Planned Experiments

1. Build graph-temporal UAV telemetry tensors.
2. Train GAT-LSTM, Graph Transformer, and Graph-Temporal Transformer.
3. Compare against LSTM, GRU, and 1D-CNN baselines.
4. Add uncertainty metrics: ECE, Brier score, MC dropout confidence.
5. Add OOD tests: stealth jammer, slow GPS drift, intermittent tampering, unseen jammer location, delayed combined attack, unseen swarm size.
6. Add explainability: attention maps, Captum Integrated Gradients, or SHAP-style attribution.
7. Add PPO/DRL recovery policy and compare against deterministic action selection.

## GPU Plan

Recommended: **85–100 RTX 4090 GPU hours**.  
Full differentiation with DRL: **110–130 GPU hours**.

## Status

Initial TRUST-Swarm AI repo created.

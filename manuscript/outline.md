# TRUST-Swarm Manuscript Outline

## Title

TRUST-Swarm: Trustworthy Graph-Temporal AI for High-Confidence Multi-UAV Mission Assurance Under Cyber-Physical Attacks

## Target Journal

High-Confidence Computing

## Paper Identity

TRUST-Swarm is an AI-first extension of the multi-UAV mission-assurance research direction.

The paper should not present itself as a repeat of RA-MARS. RA-MARS should be used only as a baseline and simulation foundation.

## Core Contributions

1. A graph-temporal AI framework for modelling multi-UAV cyber-physical mission states.
2. A Graph-Temporal Transformer that jointly learns spatial swarm dependencies and temporal attack signatures.
3. An uncertainty-aware prediction layer using calibration and confidence estimation.
4. Explainable AI maps identifying influential UAV nodes and telemetry features.
5. OOD and unseen-attack detection under stealth and delayed attack conditions.
6. A PPO/DRL mission recovery agent compared with deterministic action selection.

## Proposed Sections

1. Introduction
2. Related Work
   - Trustworthy AI for cyber-physical systems
   - Graph neural networks for UAV swarms
   - Uncertainty and calibration
   - Explainable AI
   - Reinforcement learning for mission recovery
3. System and Threat Model
4. TRUST-Swarm Framework
5. Graph-Temporal AI Architecture
6. Uncertainty and Explainability Layer
7. PPO-Based Mission Recovery
8. Experimental Setup
9. Results and Discussion
10. Limitations
11. Conclusion

## Required New Results

- Model comparison: LSTM/GRU/1D-CNN vs GAT-LSTM/Graph Transformer/Graph-Temporal Transformer.
- OOD results.
- Calibration results.
- Explainability figures.
- DRL recovery comparison.

## Expected New Figures

1. TRUST-Swarm architecture.
2. Dynamic UAV graph construction.
3. Graph-Temporal Transformer model.
4. Uncertainty calibration / reliability diagram.
5. OOD uncertainty shift.
6. Explainability heatmap.
7. PPO recovery comparison.

## Expected New Tables

1. Difference from RA-MARS baseline.
2. Dataset and graph construction parameters.
3. Model comparison.
4. Calibration and uncertainty metrics.
5. OOD attack results.
6. DRL recovery results.
7. Ablation of graph, temporal, uncertainty, and explainability modules.

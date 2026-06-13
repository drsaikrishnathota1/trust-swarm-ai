# TRUST-Swarm Information Fusion Figure Plan

## Purpose

This document defines the figures needed to make the TRUST-Swarm manuscript look stronger for an Information Fusion-style journal submission.

The figures should emphasize TRUST-Swarm as a trustworthy graph-temporal multi-source information fusion framework, not only as a classifier.

---

## Figure 1. TRUST-Swarm Overall Multi-Source Information Fusion Architecture

### Goal

Show the full TRUST-Swarm pipeline from distributed UAV telemetry to mission-assurance decisions.

### Main blocks

1. Multi-UAV swarm mission environment
2. Multi-source telemetry streams

   * communication telemetry
   * navigation telemetry
   * energy telemetry
   * mission-progress telemetry
   * coverage telemetry
3. Graph-temporal fusion-window construction
4. Graph-Temporal Transformer
5. Confidence-aware calibration
6. OOD-aware stress testing
7. Fusion-driver explainability
8. PPO-based recovery reasoning
9. Mission-assurance action output

### Message

TRUST-Swarm fuses distributed UAV telemetry across nodes and time to support high-confidence mission assurance.

---

## Figure 2. Graph-Temporal Fusion-Window Construction

### Goal

Show how raw UAV telemetry becomes a graph-temporal tensor.

### Main visual idea

Raw telemetry table → temporal sliding window → UAV nodes → graph-temporal fusion tensor.

### Include notation

X ∈ R^(T × N × F)

Where:

* T = temporal window length
* N = UAV nodes
* F = telemetry features

### Final experiment values

* T = 20
* N = 20
* F = 9

### Message

Each mission sample preserves temporal structure, UAV-node structure, and multi-source telemetry feature structure.

---

## Figure 3. Graph-Temporal Fusion Model Architecture

### Goal

Show the internal Graph-Temporal Transformer pipeline.

### Main blocks

1. Input graph-temporal fusion window
2. Feature projection layer
3. UAV-node attention
4. Temporal transformer encoder
5. Fusion embedding
6. Mission-state classifier
7. Output class probabilities

### Message

The model learns UAV-node relationships and mission-time evolution from fused telemetry windows.

---

## Figure 4. Confidence-Aware Fusion Pipeline

### Goal

Show how TRUST-Swarm estimates prediction confidence.

### Main blocks

1. Graph-temporal fusion model
2. Monte Carlo dropout inference
3. Class probability distribution
4. Confidence score
5. Predictive entropy
6. Expected Calibration Error
7. Brier score
8. Mission-assurance trust decision

### Message

TRUST-Swarm evaluates whether a fused mission-state prediction should be trusted, monitored, or escalated.

---

## Figure 5. OOD-Aware Mission Risk Evaluation Pipeline

### Goal

Show the OOD stress-testing workflow.

### Main blocks

1. In-distribution test windows
2. OOD perturbation engine
3. OOD scenarios:

   * stealth jamming
   * slow GPS drift
   * intermittent tampering
   * delayed combined attack
   * unseen swarm noise
4. Model prediction
5. Macro F1 / confidence / entropy / low-confidence rate
6. Mission-risk interpretation

### Message

OOD stress testing exposes vulnerability under unseen cyber-physical shifts.

---

## Figure 6. Fusion-Driver Explainability Workflow

### Goal

Show how feature importance is computed.

### Main blocks

1. Baseline graph-temporal test set
2. Baseline macro F1
3. Feature perturbation one feature at a time
4. Recompute macro F1
5. Macro-F1 drop
6. Ranked fusion drivers

### Top drivers from final experiment

1. latency_ms
2. zone_coverage
3. route_deviation_m
4. mission_progress
5. gps_jump_m

### Message

TRUST-Swarm identifies which telemetry sources drive the fused mission-state decision.

---

## Figure 7. Recovery-Oriented Fusion Decision Loop

### Goal

Show how fused mission-state prediction connects to recovery reasoning.

### Main blocks

1. Fused mission-state output
2. Confidence and uncertainty signals
3. Mission-risk indicators
4. PPO recovery policy
5. Possible actions:

   * continue
   * monitor
   * reroute
   * reassign
   * isolate node
   * return to base
6. Updated mission state

### Message

TRUST-Swarm connects trustworthy fusion outputs to recovery-oriented mission reasoning.

---

## Figure 8. Model Comparison Result Figure

### Existing file

figures/manuscript/fig_01_model_comparison_macro_f1.png

### Message

The 1D-CNN baseline achieved the strongest in-distribution macro F1, while the Graph-Temporal Transformer supports the broader trustworthy fusion framework.

---

## Figure 9. OOD Stress-Test Result Figure

### Existing file

figures/manuscript/fig_05_ood_macro_f1.png

### Message

Severe unseen cyber-physical shifts substantially degrade mission-state recognition, proving the need for OOD-aware fusion evaluation.

---

## Figure 10. Fusion-Driver Feature Importance Result Figure

### Existing file

figures/manuscript/fig_07_feature_importance.png

### Message

Latency, zone coverage, route deviation, mission progress, and GPS jump are important mission-relevant fusion drivers.

---

## Priority Order for Manuscript

High priority:

1. Overall architecture
2. Graph-temporal fusion-window construction
3. Graph-Temporal Transformer architecture
4. OOD-aware mission-risk evaluation
5. Fusion-driver explainability

Medium priority:

6. Confidence-aware fusion pipeline
7. Recovery-oriented fusion decision loop

Already generated:

8. Model comparison result figure
9. OOD macro F1 figure
10. Feature-importance figure

## Final Recommendation

For journal submission, the manuscript should include at least 7 figures:

1. TRUST-Swarm architecture
2. Graph-temporal fusion-window construction
3. Graph-Temporal Transformer architecture
4. Model comparison results
5. OOD stress-test results
6. Feature-importance results
7. Recovery-oriented fusion decision loop

The architecture figures should be clean, academic, and not overly colorful. The goal is to make the paper look like a serious information-fusion framework rather than only a machine-learning experiment.


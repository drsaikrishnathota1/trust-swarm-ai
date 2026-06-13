# Information Fusion Methodology v2

## 3. Methodology

This section presents the TRUST-Swarm methodology as a trustworthy graph-temporal multi-source information fusion framework for UAV swarm mission assurance under cyber-physical attacks. The framework fuses distributed UAV telemetry across mission time, UAV nodes, and heterogeneous telemetry sources to estimate mission state and support high-confidence decision-making.

## 3.1 TRUST-Swarm Framework Overview

TRUST-Swarm treats UAV swarm mission assurance as a graph-temporal information fusion problem. Each UAV contributes telemetry streams related to communication, navigation, energy, mission progress, and coverage. These heterogeneous telemetry sources are fused across time and across UAV nodes to infer whether the mission is operating normally or under cyber-physical attack.

The framework includes the following components:

1. multi-source mission telemetry generation
2. graph-temporal fusion-window construction
3. temporal baseline modeling
4. graph-temporal fusion modeling
5. confidence-aware fusion calibration
6. OOD-aware fusion stress testing
7. fusion-driver explainability
8. recovery-oriented mission reasoning

The goal is not only to classify mission state, but also to estimate confidence, evaluate behavior under unseen cyber-physical shifts, explain which telemetry sources drive the fused decision, and connect fused mission-state outputs to recovery reasoning.

## 3.2 Multi-Source Mission Telemetry Generation

A controlled simulation-based telemetry generator was developed to create multi-UAV cyber-physical mission scenarios. Each mission contains a swarm of UAVs operating over time under normal or adversarial conditions. For each UAV and timestep, the generator produces telemetry features representing multiple mission information sources.

The telemetry sources include:

1. communication telemetry
2. navigation telemetry
3. energy telemetry
4. mission-progress telemetry
5. coverage telemetry

The nine telemetry features are:

1. packet_loss_rate
2. latency_ms
3. route_deviation_m
4. gps_jump_m
5. velocity_inconsistency
6. battery_level
7. mission_progress
8. zone_coverage
9. energy_consumption

These features represent mission-relevant information streams. Packet loss and latency describe communication degradation. Route deviation, GPS jump, and velocity inconsistency describe navigation integrity. Battery level and energy consumption describe energy state. Mission progress and zone coverage describe mission-level effectiveness.

The mission-state classes are:

1. normal
2. jamming
3. spoofing
4. tampering
5. jamming-spoofing
6. jamming-tampering
7. spoofing-tampering
8. combined attack

The telemetry generator introduces random attack onset, attack duration, UAV-level variation, jammer proximity, and local attack exposure. This allows the framework to evaluate multi-source fusion under controlled cyber-physical mission degradation.

## 3.3 Graph-Temporal Fusion-Window Construction

Raw UAV telemetry is converted into graph-temporal fusion windows. Each fusion window represents a short mission segment in which UAV nodes evolve over time with heterogeneous telemetry features.

Each sample is represented as:

X ∈ R^(T × N × F)

where:

* T is the temporal window length
* N is the number of UAV nodes
* F is the number of telemetry features

In the final experiment:

* T = 20 timesteps
* N = 20 UAV nodes
* F = 9 telemetry features

Each seed produced 66,300 graph-temporal fusion windows.

This representation supports multi-source mission fusion because it preserves three forms of structure:

1. temporal structure across mission time
2. relational structure across UAV nodes
3. feature-level structure across heterogeneous telemetry sources

## 3.4 Temporal Baseline Models

Three temporal baseline models were evaluated:

1. LSTM
2. GRU
3. 1D-CNN

The LSTM and GRU baselines model sequential telemetry patterns across time. The 1D-CNN baseline captures local temporal signatures in the graph-window telemetry. These baselines are included to determine how much of the mission-state information can be captured using conventional temporal models.

The final results show that the 1D-CNN baseline achieves the strongest in-distribution classification performance. This result is important because it shows that raw classification accuracy alone should not be the only measure of contribution. TRUST-Swarm is therefore positioned as a broader trustworthy information-fusion framework.

## 3.5 Graph-Temporal Fusion Model

The Graph-Temporal Transformer is used as the main graph-temporal fusion model. The model receives an input tensor of shape:

batch_size × window_size × num_uavs × num_features

The model first projects telemetry features into a hidden representation. It then applies UAV-node attention to model relationships across UAV nodes. A temporal transformer encoder is used to model mission evolution across time. The final fused representation is passed to a classifier to estimate mission-state class.

The graph-temporal fusion model learns:

1. UAV-node interaction patterns
2. temporal mission evolution
3. cyber-physical attack signatures
4. communication-navigation-energy-coverage interactions
5. mission-state degradation patterns

This design allows TRUST-Swarm to operationalize multi-source mission telemetry fusion through graph-temporal learning.

## 3.6 Confidence-Aware Fusion Calibration

High-confidence mission assurance requires calibrated confidence, not only accurate predictions. TRUST-Swarm evaluates whether fused model predictions are probabilistically reliable using:

1. Expected Calibration Error
2. Brier score
3. mean predictive confidence
4. predictive entropy

Monte Carlo dropout is used during uncertainty evaluation to estimate predictive uncertainty. This allows the mission-assurance layer to assess whether a fused prediction should be trusted, monitored, or escalated.

## 3.7 OOD-Aware Fusion Stress Testing

Real UAV missions may encounter cyber-physical shifts not observed during training. TRUST-Swarm therefore evaluates OOD-aware fusion behavior under unseen stress conditions.

The OOD scenarios are:

1. stealth jamming
2. slow GPS drift
3. intermittent tampering
4. delayed combined attack
5. unseen swarm noise

These conditions test whether the fused model remains reliable when mission telemetry is shifted or corrupted in unfamiliar ways. The evaluation reports accuracy, macro F1, confidence, entropy, and low-confidence rate.

The purpose is not to claim perfect OOD detection. Instead, OOD-aware fusion evaluation exposes mission-risk conditions where performance degrades or confidence becomes unreliable.

## 3.8 Fusion-Driver Explainability

TRUST-Swarm uses perturbation-based feature importance to identify which telemetry sources drive the fused decision. The method first computes baseline macro F1. Then, each feature is replaced by its mean value, and the resulting macro-F1 drop is measured.

A larger macro-F1 drop indicates that the feature is more important to the fused mission-state prediction.

This analysis identifies fusion drivers such as:

1. latency
2. zone coverage
3. route deviation
4. mission progress
5. GPS jump

These drivers are operationally meaningful because they represent communication degradation, mission coverage loss, navigation disruption, mission-progress interruption, and spoofing-related displacement.

## 3.9 Recovery-Oriented Mission Fusion Reasoning

TRUST-Swarm includes a PPO-based recovery-reasoning scaffold. The recovery module connects fused mission-state indicators, confidence signals, and mission-risk features to possible recovery actions.

The recovery action space includes:

1. continue
2. monitor
3. reroute
4. reassign
5. isolate node
6. return to base

This module should be interpreted as an initial recovery-reasoning layer, not as a complete operational UAV controller. Its purpose is to demonstrate how trustworthy information-fusion outputs can support downstream mission-assurance decisions.

## 3.10 Experimental Protocol

The final evaluation used three seeds: 42, 123, and 2026. For each seed, the telemetry generator produced:

* 300 mission runs
* 240 timesteps per mission
* 20 UAVs per mission
* 1,440,000 raw telemetry rows
* 66,300 graph-temporal fusion windows

Models were trained for 30 epochs with a batch size of 128. Results were aggregated across seeds using mean and standard deviation.

## 3.11 Summary

TRUST-Swarm reframes UAV swarm mission assurance as a graph-temporal multi-source information fusion problem. The framework fuses communication, navigation, energy, coverage, and mission-progress telemetry across UAV nodes and mission time. It then evaluates fused mission-state predictions using classification metrics, calibration metrics, OOD stress tests, explainability, and recovery reasoning.

This methodology supports the central claim that high-confidence UAV mission assurance requires trustworthy fusion mechanisms beyond raw classification accuracy.


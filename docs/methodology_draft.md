# TRUST-Swarm Methodology Draft

## 3. Methodology

This section presents the TRUST-Swarm methodology for high-confidence multi-UAV mission assurance under cyber-physical attacks. The framework consists of seven major components: synthetic mission telemetry generation, graph-temporal window construction, temporal baseline modeling, Graph-Temporal Transformer modeling, uncertainty calibration, OOD stress testing, explainability analysis, and recovery-oriented decision support.

## 3.1 TRUST-Swarm Framework Overview

TRUST-Swarm is designed as a trustworthy AI pipeline for multi-UAV swarm mission assurance. The system receives UAV mission telemetry over time and converts it into graph-temporal windows. Each window represents the state of a UAV swarm across a fixed temporal horizon, where UAVs are treated as nodes and telemetry features describe communication, navigation, energy, and mission-progress conditions.

The framework evaluates whether the swarm is operating normally or under cyber-physical attack conditions such as jamming, spoofing, tampering, or combined attacks. Unlike a pure classifier, TRUST-Swarm also evaluates prediction confidence, stress-tests the model under unseen attack shifts, identifies mission-relevant decision drivers, and supports recovery-oriented reasoning.

## 3.2 Synthetic Multi-UAV Telemetry Generation

A controlled telemetry generator was developed to simulate multi-UAV mission behavior under normal and adversarial conditions. Each mission run includes a swarm of UAVs operating across mission time. For each UAV and timestep, the generator produces telemetry features representing communication reliability, navigation consistency, mission coverage, battery state, energy consumption, and mission progress.

The generated telemetry includes the following features:

1. packet_loss_rate
2. latency_ms
3. route_deviation_m
4. gps_jump_m
5. velocity_inconsistency
6. battery_level
7. mission_progress
8. zone_coverage
9. energy_consumption

The attack classes include:

1. normal
2. jamming
3. spoofing
4. tampering
5. jamming-spoofing
6. jamming-tampering
7. spoofing-tampering
8. combined attack

The generator introduces mission-level variation through random attack onset, attack duration, UAV-level heterogeneity, jammer proximity, and local exposure intensity. This creates a large-scale controlled benchmark for evaluating cyber-physical mission assurance.

## 3.3 Graph-Temporal Window Construction

The raw telemetry stream is converted into graph-temporal windows. Each graph-temporal sample is represented as:

X ∈ R^(T × N × F)

where T is the temporal window length, N is the number of UAV nodes, and F is the number of telemetry features.

In the final journal experiment, the window length was 20 timesteps, the swarm size was 20 UAVs, and each UAV had 9 telemetry features. Each seed produced 66,300 graph-temporal windows.

The graph-temporal representation preserves both temporal mission evolution and UAV-node structure. This is important because multi-UAV mission assurance depends not only on individual telemetry values, but also on how swarm behavior evolves across time and across UAV nodes.

## 3.4 Temporal Baseline Models

Three temporal baseline models were implemented for comparison:

1. LSTM
2. GRU
3. 1D-CNN

The LSTM and GRU baselines process flattened UAV telemetry over time. The 1D-CNN baseline applies temporal convolution over graph-window sequences. These baselines evaluate whether the dataset can be classified effectively using conventional temporal learning methods.

The final results show that the 1D-CNN baseline achieves the strongest in-distribution classification performance. Therefore, these baselines are important for preventing overclaiming and for positioning TRUST-Swarm as a trustworthy mission-assurance framework rather than only a classifier.

## 3.5 Graph-Temporal Transformer

The Graph-Temporal Transformer is used as the main graph-temporal learning model in TRUST-Swarm. The model receives an input tensor with shape:

batch_size × window_size × num_uavs × num_features

The architecture first projects UAV telemetry features into a hidden representation. It then applies graph-node attention to model UAV-level relationships within each temporal window. A temporal transformer encoder is then used to model mission evolution across time. The final representation is passed to a classifier that predicts the mission-state class.

The model is designed to jointly learn:

1. UAV-node interactions
2. temporal mission evolution
3. cyber-physical attack signatures
4. mission-state degradation patterns

This graph-temporal structure supports the high-confidence mission-assurance objective because it models both relational and temporal structure in swarm telemetry.

## 3.6 Uncertainty Calibration

TRUST-Swarm evaluates uncertainty calibration to determine whether the model’s predicted confidence is reliable. The following metrics are used:

1. Expected Calibration Error
2. Brier score
3. mean predictive confidence
4. mean predictive entropy

Monte Carlo dropout is used during uncertainty evaluation to estimate predictive uncertainty. This supports high-confidence decision-making by helping the mission-assurance layer evaluate whether a prediction should be trusted, monitored, or escalated.

## 3.7 OOD and Unseen Attack Stress Testing

OOD stress testing evaluates whether the trained model remains reliable under unseen cyber-physical shifts. The OOD scenarios include:

1. stealth jamming
2. slow GPS drift
3. intermittent tampering
4. delayed combined attack
5. unseen swarm noise

These perturbations are applied to the test windows to simulate distribution shifts that were not directly represented in the standard test condition. OOD evaluation reports accuracy, macro F1, mean confidence, predictive entropy, and low-confidence rate.

The purpose of this stage is not to claim perfect OOD detection. Instead, it exposes mission-risk conditions where the model becomes unreliable or where performance drops sharply under unseen attack patterns.

## 3.8 Explainability Through Perturbation-Based Feature Importance

TRUST-Swarm uses perturbation-based feature importance to identify which telemetry features most influence model decisions. The method first computes the baseline macro F1 score on the test set. Then, one feature at a time is replaced with its mean value across the dataset. The drop in macro F1 is measured.

A larger macro-F1 drop indicates that the feature is more important for model prediction.

This method provides an interpretable link between model behavior and mission-relevant telemetry factors. In the final experiment, the most important features included latency, zone coverage, route deviation, mission progress, and GPS jump.

## 3.9 PPO-Based Mission Recovery Scaffold

TRUST-Swarm includes a PPO-based recovery environment for mission-recovery reasoning. The recovery environment represents mission state using communication, navigation, coverage, integrity, recovery, energy, attack class, and uncertainty indicators.

The available recovery actions include:

1. continue
2. monitor
3. reroute
4. reassign
5. isolate node
6. return to base

The PPO recovery module is included as a recovery-reasoning scaffold. It demonstrates how prediction, confidence, and mission-state indicators can be connected to recovery decisions. However, it should be described as an initial recovery layer rather than a fully operational control policy.

## 3.10 Experimental Protocol

The final experiment used three seeds: 42, 123, and 2026. For each seed, the telemetry generator produced 300 mission runs with 240 timesteps and 20 UAVs. Each seed produced 1,440,000 raw telemetry rows and 66,300 graph-temporal windows.

Each model was trained for 30 epochs with a batch size of 128. The evaluation included temporal baselines, Graph-Temporal Transformer classification, uncertainty calibration, OOD stress testing, and explainability analysis.

The final results were aggregated across seeds using mean and standard deviation.

## 3.11 Summary

The TRUST-Swarm methodology combines graph-temporal learning, temporal baseline comparison, uncertainty calibration, OOD stress testing, explainability, and recovery reasoning. This integrated design supports the paper’s central claim that UAV swarm mission assurance requires more than raw classification accuracy. It requires trustworthy AI mechanisms that can evaluate confidence, expose unseen-shift vulnerability, explain mission-relevant decision factors, and support recovery-oriented reasoning.


# High-Confidence Computing Experimental Setup v1

## 4. Experimental Setup

This section describes the experimental setup used to evaluate TRUST-Swarm as a high-confidence graph-temporal intelligent computing framework for secure multi-UAV mission assurance. The evaluation is designed to test mission-state recognition, baseline comparison, confidence calibration, OOD vulnerability, traceable explanation, and recovery-oriented reasoning.

## 4.1 Computing Environment

The final experiment was executed in a GPU-based RunPod environment using Python and PyTorch. The implementation used pandas, NumPy, scikit-learn, matplotlib, Gymnasium, and Stable-Baselines3. Neural-network training was performed with GPU acceleration.

The experiment used three random seeds:

* 42
* 123
* 2026

Using multiple seeds reduces dependence on a single telemetry generation run or train-test split and supports more reliable performance reporting.

## 4.2 Synthetic Multi-UAV Mission Telemetry

A controlled simulation-based telemetry generator was used to evaluate cyber-physical mission assurance under repeatable conditions. Each seed generated:

* 300 mission runs
* 240 timesteps per mission
* 20 UAVs per mission
* 1,440,000 raw telemetry rows per seed
* 66,300 graph-temporal mission windows per seed

The simulation includes normal mission operation and cyber-physical attack states. The purpose of this dataset is to provide a controlled high-confidence benchmark for evaluating secure mission-state prediction and uncertainty-aware mission reasoning.

## 4.3 Mission-State Classes

The mission-state labels include eight classes:

1. normal
2. jamming
3. spoofing
4. tampering
5. jamming-spoofing
6. jamming-tampering
7. spoofing-tampering
8. combined attack

These classes represent communication disruption, navigation manipulation, telemetry integrity attack, and combined cyber-physical mission degradation.

## 4.4 Telemetry Features

Each UAV is represented using nine telemetry features:

1. packet_loss_rate
2. latency_ms
3. route_deviation_m
4. gps_jump_m
5. velocity_inconsistency
6. battery_level
7. mission_progress
8. zone_coverage
9. energy_consumption

These features capture communication reliability, navigation integrity, energy state, mission progress, and coverage quality.

## 4.5 Graph-Temporal Mission Windows

Raw telemetry is transformed into graph-temporal mission windows using a sliding temporal window. Each mission-window sample is represented as:

X ∈ R^(T × N × F)

where:

* T = 20 timesteps
* N = 20 UAV nodes
* F = 9 telemetry features

Thus, each graph-temporal mission window has the final shape:

X ∈ R^(20 × 20 × 9)

This representation preserves mission-time evolution, UAV-node structure, and telemetry-feature structure.

## 4.6 Evaluated Models

The evaluation includes the proposed Graph-Temporal Transformer and three temporal baseline models:

1. LSTM
2. GRU
3. 1D-CNN
4. Graph-Temporal Transformer

The LSTM and GRU baselines evaluate recurrent temporal learning. The 1D-CNN baseline evaluates local temporal pattern extraction. The Graph-Temporal Transformer evaluates graph-temporal mission reasoning across UAV nodes and mission time.

## 4.7 Training Configuration

Each model was trained under the following configuration:

* epochs: 30
* batch size: 128
* seeds: 42, 123, 2026

Results were aggregated across the three seeds using mean and standard deviation.

## 4.8 In-Distribution Classification Metrics

The mission-state recognition task was evaluated using:

* test loss
* accuracy
* macro precision
* macro recall
* macro F1

Macro-averaged metrics were emphasized because the cyber-physical attack classes are imbalanced.

## 4.9 Confidence Calibration Metrics

The confidence-aware reliability layer was evaluated using:

* Expected Calibration Error
* Brier score
* mean predictive confidence
* predictive entropy

Monte Carlo dropout with 20 stochastic samples was used during uncertainty evaluation. The goal was to evaluate whether the Graph-Temporal Transformer produced reliable in-distribution confidence estimates.

## 4.10 OOD Cyber-Physical Stress Testing

OOD stress testing evaluated model behavior under unseen cyber-physical mission shifts. The OOD conditions were:

1. in-distribution test
2. stealth jammer
3. slow GPS drift
4. intermittent tampering
5. delayed combined attack
6. unseen swarm noise

Each OOD condition was evaluated using:

* accuracy
* macro F1
* mean confidence
* predictive entropy
* low-confidence rate

The purpose of this evaluation is not to claim perfect OOD detection. Instead, it identifies mission-risk conditions where model performance degrades or confidence becomes unreliable.

## 4.11 Traceable Explanation Evaluation

Traceability was evaluated using perturbation-based feature importance. First, the baseline macro F1 was computed. Then, each telemetry feature was replaced by its mean value, and macro F1 was recomputed.

Feature importance was calculated as:

Feature importance = baseline macro F1 − perturbed macro F1

A larger macro-F1 drop indicates that the feature is more important for mission-state prediction.

## 4.12 Recovery-Oriented Reasoning Evaluation

The PPO-based recovery module was evaluated as a recovery-reasoning scaffold. The action space included:

1. continue
2. monitor
3. reroute
4. reassign
5. isolate node
6. return to base

This module is included to demonstrate how prediction, confidence, entropy, and mission-risk indicators can support mission-response reasoning. It is not claimed as a deployment-ready UAV controller.

## 4.13 Current Experimental Limitation

The current evaluation uses controlled synthetic telemetry rather than field-collected UAV telemetry. This design allows repeatable testing across attack states, OOD conditions, and multiple seeds, but real-world validation remains future work.

To better match High-Confidence Computing standards, two additional analyses should be added before final submission:

1. ablation study
2. runtime and complexity analysis

These analyses will strengthen the practical high-confidence computing contribution.


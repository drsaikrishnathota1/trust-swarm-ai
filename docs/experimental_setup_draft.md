# TRUST-Swarm Experimental Setup Draft

## 4. Experimental Setup

This section describes the experimental configuration used to evaluate TRUST-Swarm. The evaluation was designed to test in-distribution classification, uncertainty calibration, out-of-distribution attack behavior, explainability, and mission-assurance relevance under multi-UAV cyber-physical attack conditions.

## 4.1 Computing Environment

The final journal experiment was executed on a GPU-based RunPod environment. The training pipeline used Python, PyTorch, pandas, scikit-learn, matplotlib, Gymnasium, and Stable-Baselines3. CUDA was enabled during the final experiment, and all neural-network training was executed using GPU acceleration.

The full experiment was run using three random seeds: 42, 123, and 2026. The final experiment completed the full pipeline, including realistic telemetry generation, graph-window construction, baseline model training, Graph-Temporal Transformer training, uncertainty evaluation, OOD stress testing, explainability analysis, and results aggregation.

## 4.2 Dataset Configuration

A synthetic multi-UAV telemetry generator was used to create controlled mission scenarios under normal and adversarial conditions. For each random seed, the generator produced:

* 300 mission runs
* 240 timesteps per mission
* 20 UAVs per mission
* 1,440,000 raw telemetry rows
* 66,300 graph-temporal windows

Each graph-temporal window used:

* temporal window length: 20
* UAV nodes: 20
* telemetry features: 9
* mission-state classes: 8

The mission-state classes were:

1. normal
2. jamming
3. spoofing
4. tampering
5. jamming-spoofing
6. jamming-tampering
7. spoofing-tampering
8. combined attack

## 4.3 Telemetry Features

Each UAV was represented using nine telemetry features:

1. packet_loss_rate
2. latency_ms
3. route_deviation_m
4. gps_jump_m
5. velocity_inconsistency
6. battery_level
7. mission_progress
8. zone_coverage
9. energy_consumption

These features were selected because they represent communication degradation, navigation disruption, mission progress, mission coverage, and energy state.

## 4.4 Model Configuration

The evaluation compared the Graph-Temporal Transformer against three temporal baseline models:

1. LSTM
2. GRU
3. 1D-CNN

All models were trained using the same graph-window dataset for each seed. The training configuration was:

* epochs: 30
* batch size: 128
* seeds: 42, 123, 2026

The Graph-Temporal Transformer used UAV-node attention followed by temporal transformer encoding. The LSTM and GRU baselines processed flattened UAV telemetry across time. The 1D-CNN baseline used temporal convolution over windowed telemetry sequences.

## 4.5 Evaluation Metrics

The in-distribution classification metrics were:

* accuracy
* macro F1
* macro precision
* macro recall
* test loss

Macro-averaged metrics were emphasized because the dataset contained imbalanced attack classes.

## 4.6 Uncertainty Calibration Metrics

Uncertainty calibration was evaluated using:

* Expected Calibration Error
* Brier score
* mean predictive confidence
* mean predictive entropy

Monte Carlo dropout with 20 samples was used during uncertainty evaluation. The goal was to determine whether the Graph-Temporal Transformer produced reliable confidence estimates under in-distribution test conditions.

## 4.7 OOD Stress-Test Conditions

The OOD evaluation tested the model under unseen cyber-physical shifts. The evaluated conditions were:

1. in-distribution test
2. stealth jammer
3. slow GPS drift
4. intermittent tampering
5. delayed combined attack
6. unseen swarm noise

For each OOD condition, the following metrics were reported:

* accuracy
* macro F1
* mean confidence
* mean entropy
* low-confidence rate below 0.70

The purpose of OOD testing was to expose model behavior under unseen mission-risk conditions, not to claim perfect OOD detection.

## 4.8 Explainability Evaluation

Explainability was evaluated using perturbation-based feature importance. The baseline macro F1 score was first computed on the test set. Then, each telemetry feature was replaced with its dataset mean value, and the resulting macro-F1 drop was measured.

The feature-importance score was defined as:

macro-F1 drop = baseline macro F1 - perturbed macro F1

A larger drop indicates that the feature had greater influence on model predictions.

## 4.9 Results Aggregation

All final metrics were aggregated across the three random seeds. The aggregation reported mean and standard deviation for model comparison, uncertainty calibration, OOD stress testing, and feature importance.

This multi-seed design improves the reliability of the reported results by reducing dependence on a single random train-test split or telemetry generation seed.

## 4.10 Summary

The experimental setup was designed to evaluate TRUST-Swarm as a high-confidence mission-assurance framework. The evaluation included not only in-distribution classification but also calibration, OOD behavior, explainability, and recovery-oriented reasoning. This design supports the central claim that trustworthy UAV swarm mission assurance requires more than raw attack-classification accuracy.


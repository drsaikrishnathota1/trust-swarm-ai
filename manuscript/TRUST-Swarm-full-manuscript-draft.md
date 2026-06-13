# TRUST-Swarm Full Manuscript Draft

**Title:** TRUST-Swarm: Trustworthy Graph-Temporal AI for High-Confidence Multi-UAV Mission Assurance Under Cyber-Physical Attacks

---

# TRUST-Swarm Abstract and Contributions Draft

## Proposed Title

TRUST-Swarm: Trustworthy Graph-Temporal AI for High-Confidence Multi-UAV Mission Assurance Under Cyber-Physical Attacks

## Abstract

Multi-UAV swarm missions are increasingly exposed to cyber-physical disruptions such as communication jamming, GPS spoofing, telemetry tampering, and combined attack conditions. Existing mission-assurance approaches often emphasize attack classification or rule-based resilience, but they provide limited support for calibrated confidence estimation, out-of-distribution stress testing, explainability, and recovery-oriented decision support. This paper presents TRUST-Swarm, a trustworthy graph-temporal AI framework for high-confidence multi-UAV mission assurance under cyber-physical attacks.

TRUST-Swarm models UAV swarms as dynamic graph-temporal telemetry windows, where UAV nodes evolve over mission time under normal and adversarial conditions. The framework integrates graph-temporal learning, uncertainty calibration, OOD attack evaluation, perturbation-based explainability, and reinforcement-learning-based recovery reasoning. A large-scale simulation study was conducted using three random seeds, 300 mission runs per seed, 240 timesteps per mission, 20 UAVs per mission, and 66,300 graph-temporal windows per seed. The Graph-Temporal Transformer achieved a mean accuracy of 0.9647 and a mean macro F1 score of 0.8750 across three seeds, while also producing strong calibration with an Expected Calibration Error of 0.0088 and a Brier score of 0.0531.

The results show that severe unseen cyber-physical shifts substantially degrade model performance, with delayed combined attacks and stealth jamming producing the largest reductions. Explainability analysis identified latency, zone coverage, route deviation, mission progress, and GPS jump as the most influential telemetry factors. Although a 1D-CNN baseline achieved stronger in-distribution classification performance, TRUST-Swarm provides a broader high-confidence mission-assurance framework by combining graph-temporal modeling, calibrated uncertainty, OOD stress testing, explainability, and recovery reasoning. These findings demonstrate the importance of trustworthy AI mechanisms for resilient autonomous swarm operations under cyber-physical uncertainty.

## Main Contributions

1. A trustworthy graph-temporal AI framework is proposed for multi-UAV mission assurance under cyber-physical attacks.

2. A dynamic graph-temporal telemetry representation is developed to model UAV swarm behavior across mission time, UAV nodes, and attack conditions.

3. A Graph-Temporal Transformer is evaluated for multi-class cyber-physical mission-state recognition under jamming, spoofing, tampering, and combined attack scenarios.

4. A three-seed large-scale simulation study is conducted using 300 mission runs per seed, 240 timesteps per mission, 20 UAVs, and 66,300 graph-temporal windows per seed.

5. A baseline comparison is performed against LSTM, GRU, and 1D-CNN models to evaluate in-distribution classification performance.

6. Uncertainty calibration is evaluated using Expected Calibration Error, Brier score, predictive confidence, and predictive entropy.

7. OOD and unseen attack stress tests are conducted for stealth jamming, slow GPS drift, intermittent tampering, delayed combined attacks, and unseen swarm noise.

8. Perturbation-based explainability is used to identify the mission-relevant telemetry features most responsible for model decisions.

9. The results show that TRUST-Swarm should be interpreted as a high-confidence mission-assurance framework rather than only a raw classification model.

## Correct Positioning Statement

The manuscript should not claim that the Graph-Temporal Transformer outperforms all baselines in standard in-distribution classification. The 1D-CNN baseline achieved the strongest in-distribution classification performance. Instead, the manuscript should claim that TRUST-Swarm provides a broader trustworthy AI framework by integrating graph-temporal learning, calibration, OOD stress testing, explainability, and recovery reasoning for resilient multi-UAV mission assurance.

## Keywords

Multi-UAV swarms; graph-temporal AI; mission assurance; cyber-physical attacks; jamming; spoofing; telemetry tampering; uncertainty calibration; out-of-distribution detection; explainable AI; reinforcement learning; high-confidence computing.


---

# TRUST-Swarm Introduction Draft

## 1. Introduction

Multi-UAV swarm systems are becoming increasingly important for reconnaissance, surveillance, disaster response, border monitoring, logistics, and defense-oriented autonomous missions. Compared with single-UAV platforms, coordinated UAV swarms provide wider spatial coverage, redundancy, distributed sensing, and adaptive mission execution. However, these advantages also introduce new cyber-physical vulnerabilities. A swarm mission can be degraded not only by individual UAV failures, but also by communication jamming, GPS spoofing, telemetry tampering, node compromise, route disruption, and coordinated combined attacks.

In contested environments, cyber-physical attacks can affect mission assurance at multiple levels. Jamming can increase packet loss and latency, reducing inter-UAV coordination. GPS spoofing can produce route deviation, localization jumps, and velocity inconsistency. Telemetry tampering can distort mission-state reporting, energy consumption, or coverage information. Combined attacks can simultaneously degrade communication, navigation, and mission integrity. These disruptions make it difficult for conventional monitoring systems to determine whether a swarm is still operating safely, whether mission progress remains trustworthy, and whether recovery actions should be triggered.

Existing UAV security and resilience studies often focus on attack detection, secure communication, intrusion detection, or rule-based recovery. While these methods are useful, many of them remain limited in four important ways. First, they often treat UAV telemetry as independent time-series data and do not fully model the graph-like relationships among UAV nodes in a swarm. Second, they emphasize classification accuracy but provide limited confidence calibration. Third, they rarely evaluate performance under out-of-distribution or unseen attack shifts. Fourth, they often provide limited explainability and limited connection between attack detection and mission recovery.

These limitations are critical for high-confidence autonomous systems. In safety-sensitive swarm missions, a model should not only classify attack states but also indicate how reliable its prediction is, how it behaves under unseen cyber-physical shifts, which telemetry features influenced the decision, and how the mission-assurance layer can use the output for recovery reasoning. Therefore, trustworthy UAV mission assurance requires more than a high-performing classifier. It requires an integrated framework that combines graph-temporal modeling, uncertainty calibration, OOD stress testing, explainability, and recovery-oriented decision support.

To address this need, this paper presents TRUST-Swarm, a trustworthy graph-temporal AI framework for high-confidence multi-UAV mission assurance under cyber-physical attacks. TRUST-Swarm models swarm telemetry as graph-temporal mission windows in which UAV nodes evolve over time under normal and adversarial conditions. The framework evaluates a Graph-Temporal Transformer for mission-state recognition and integrates uncertainty calibration, OOD attack stress testing, perturbation-based explainability, and recovery reasoning.

The experimental study uses a large-scale synthetic telemetry environment with three random seeds, 300 mission runs per seed, 240 timesteps per mission, 20 UAVs per mission, and 66,300 graph-temporal windows per seed. The evaluation includes jamming, spoofing, tampering, combined cyber-physical attack states, and unseen OOD attack variants. Temporal baseline models, including LSTM, GRU, and 1D-CNN, are also evaluated for comparison.

The final results show that the Graph-Temporal Transformer achieves strong in-distribution performance and calibration, while OOD stress testing reveals significant degradation under severe unseen cyber-physical shifts. The 1D-CNN baseline achieves the highest in-distribution classification accuracy, indicating that the current synthetic telemetry setting contains strong local temporal signatures. Therefore, the contribution of TRUST-Swarm is not framed as simply outperforming every baseline in raw classification accuracy. Instead, TRUST-Swarm is positioned as a high-confidence mission-assurance framework that integrates graph-temporal learning, calibration, OOD evaluation, explainability, and recovery reasoning.

The main contributions of this paper are as follows:

1. A trustworthy graph-temporal AI framework is introduced for multi-UAV mission assurance under cyber-physical attacks.

2. A graph-temporal telemetry representation is developed to model UAV node interactions and mission evolution across time.

3. A Graph-Temporal Transformer is evaluated for multi-class cyber-physical mission-state recognition under jamming, spoofing, tampering, and combined attacks.

4. A three-seed large-scale simulation study is conducted using 300 mission runs per seed, 240 timesteps, 20 UAVs, and 66,300 graph-temporal windows per seed.

5. Baseline comparisons are performed against LSTM, GRU, and 1D-CNN models.

6. Uncertainty calibration is evaluated using Expected Calibration Error, Brier score, predictive confidence, and predictive entropy.

7. OOD stress testing is conducted under unseen attack variants, including stealth jamming, slow GPS drift, intermittent tampering, delayed combined attacks, and unseen swarm noise.

8. Perturbation-based explainability is used to identify mission-relevant telemetry drivers such as latency, zone coverage, route deviation, mission progress, and GPS jump.

9. The study provides a careful trustworthy-AI framing for UAV mission assurance, showing that high-confidence reasoning requires more than raw classifier accuracy.

The remainder of this paper is organized as follows. Section 2 reviews related work on UAV mission assurance, cyber-physical attacks, graph-temporal learning, uncertainty calibration, OOD evaluation, explainability, and recovery reasoning. Section 3 presents the TRUST-Swarm methodology. Section 4 describes the experimental setup. Section 5 reports and discusses the results. Section 6 presents limitations and future work. Section 7 concludes the paper.


---

# TRUST-Swarm Related Work Draft

## 2. Related Work

### 2.1 UAV Mission Assurance and Swarm Resilience

Multi-UAV systems are increasingly used for surveillance, reconnaissance, mapping, disaster response, and defense-oriented autonomous operations. Compared with single-UAV missions, swarm systems provide distributed coverage, redundancy, and adaptive coordination. However, these benefits also create new mission-assurance challenges. A swarm can fail due to communication disruption, navigation errors, energy depletion, node compromise, route deviation, or coordinated cyber-physical attacks.

Mission assurance for UAV swarms requires more than detecting a single attack or failure. It requires continuous evaluation of whether the mission remains operational, whether the swarm can maintain coverage, whether UAV nodes can coordinate reliably, and whether recovery actions should be triggered. Existing approaches often use rule-based monitoring, anomaly detection, secure communication protocols, or resilience-oriented control strategies. While useful, many of these approaches do not provide an integrated high-confidence AI framework that combines prediction, uncertainty, explainability, OOD stress testing, and recovery reasoning.

### 2.2 Cyber-Physical Attacks on UAV Swarms

UAV swarms are exposed to both cyber and physical attack surfaces. Communication jamming can increase packet loss, latency, and coordination failures. GPS spoofing can manipulate localization, navigation, velocity consistency, and route tracking. Telemetry tampering can distort mission progress, coverage status, battery state, or energy-consumption reporting. Combined attacks can simultaneously affect communication, navigation, and mission-integrity signals.

Many prior studies focus on detecting specific attacks, such as jamming or spoofing. However, real missions may involve mixed or delayed attacks, intermittent effects, stealthy low-intensity disruption, or unseen attack patterns. This creates a need for evaluation beyond standard in-distribution classification. TRUST-Swarm addresses this gap by including OOD and unseen attack stress tests such as stealth jamming, slow GPS drift, intermittent tampering, delayed combined attacks, and unseen swarm noise.

### 2.3 Temporal Deep Learning for UAV Telemetry

Temporal models such as LSTM, GRU, and 1D-CNN are commonly used for sequential telemetry analysis. LSTM and GRU models are effective for learning time-dependent patterns, while 1D-CNN models can capture local temporal signatures efficiently. In the TRUST-Swarm experiments, these models serve as important baselines for evaluating in-distribution mission-state classification.

The final results show that the 1D-CNN baseline achieves the strongest in-distribution classification performance. This suggests that the synthetic telemetry environment contains strong local temporal patterns. However, high in-distribution accuracy alone does not provide uncertainty calibration, OOD stress analysis, graph-based mission reasoning, explainability, or recovery-oriented decision support. Therefore, temporal baselines are important for classification comparison, but they do not fully satisfy the broader high-confidence mission-assurance objective.

### 2.4 Graph-Temporal AI for Swarm Systems

UAV swarms naturally form dynamic graph systems. UAVs can be treated as nodes, while communication, proximity, coordination, or shared mission context can define edges. Graph-temporal learning is suitable for this setting because it can model both spatial relationships among UAV nodes and temporal evolution across mission windows.

Graph neural networks and graph attention mechanisms provide a way to learn relational dependencies among nodes, while temporal transformers can capture long-range sequence behavior. TRUST-Swarm uses this idea by modeling multi-UAV telemetry as graph-temporal windows with UAV nodes, mission time, and telemetry features. The Graph-Temporal Transformer is used to learn mission-state patterns under normal, jamming, spoofing, tampering, and combined attack conditions.

### 2.5 Uncertainty Calibration and High-Confidence AI

For safety-critical autonomous systems, prediction confidence is as important as prediction accuracy. A model that is accurate in-distribution but poorly calibrated may be unsafe when deployed in unfamiliar mission conditions. Uncertainty calibration evaluates whether predicted probabilities reflect actual correctness likelihood.

TRUST-Swarm evaluates uncertainty using Expected Calibration Error, Brier score, predictive confidence, and predictive entropy. The final three-seed experiment shows strong in-distribution calibration for the Graph-Temporal Transformer. This supports the high-confidence computing direction because calibrated confidence can help a mission-assurance layer decide when to trust, monitor, or escalate a model prediction.

### 2.6 OOD and Unseen Attack Evaluation

Out-of-distribution evaluation is important because real cyber-physical missions may differ from training conditions. Attackers may use unseen jammer locations, stealthy low-power attacks, slow GPS drift, delayed combined effects, or intermittent tampering. Models that perform well on in-distribution test data may fail when the input distribution shifts.

TRUST-Swarm explicitly evaluates unseen attack stress conditions. The final results show major degradation under stealth jamming, slow GPS drift, and delayed combined attacks. This finding is important because it shows that even calibrated in-distribution models can struggle under severe unseen cyber-physical shifts. Therefore, OOD stress testing should be treated as a core part of mission-assurance evaluation rather than an optional robustness check.

### 2.7 Explainable AI for Mission Assurance

Explainability helps determine whether a model is relying on mission-relevant telemetry or arbitrary artifacts. In UAV mission assurance, useful explanations should identify operationally meaningful drivers such as latency, packet loss, route deviation, GPS jump, mission progress, zone coverage, battery state, or energy consumption.

TRUST-Swarm uses perturbation-based feature importance to identify the most influential telemetry features. The final results show that latency, zone coverage, route deviation, mission progress, and GPS jump are the dominant decision drivers. These features are consistent with communication degradation, mission coverage loss, navigation disruption, and mission-progress interruption, supporting the operational credibility of the model.

### 2.8 Recovery Reasoning and Reinforcement Learning

Mission assurance should not stop at attack recognition. Once a risk is detected, the system should support recovery-oriented decisions such as continuing the mission, monitoring, rerouting, reassigning tasks, isolating compromised nodes, or returning to base. Reinforcement learning provides a mechanism for learning such policies through reward-based interaction with a mission environment.

TRUST-Swarm includes a PPO-based recovery environment as a recovery-reasoning layer. The current recovery module demonstrates feasibility, but it should be interpreted as an initial scaffold rather than a complete operational recovery system. Future work should improve reward design, action diversity, safety constraints, and integration with realistic mission simulators.

### 2.9 Research Gap

The literature contains strong work on UAV attack detection, secure communication, anomaly detection, graph learning, uncertainty estimation, explainability, and reinforcement learning. However, these areas are often studied separately. Few frameworks integrate graph-temporal mission modeling, uncertainty calibration, OOD stress testing, explainability, and recovery reasoning into one high-confidence mission-assurance pipeline for multi-UAV cyber-physical operations.

TRUST-Swarm addresses this gap by presenting an integrated trustworthy AI framework for multi-UAV mission assurance. The goal is not only to classify attack states, but also to evaluate confidence, expose OOD vulnerability, explain decision drivers, and support recovery-oriented reasoning.


---

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


---

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


---

# TRUST-Swarm Manuscript Results Tables

These tables summarize the final three-seed RunPod journal experiment.

Configuration: 300 runs, 240 timesteps, 20 UAVs, 30 epochs, seeds 42, 123, and 2026.

## Table 1. Model Comparison Summary

| model                    |   test_loss_mean |   test_loss_std |   accuracy_mean |   accuracy_std |   macro_f1_mean |   macro_f1_std |   macro_precision_mean |   macro_precision_std |   macro_recall_mean |   macro_recall_std |
|:-------------------------|-----------------:|----------------:|----------------:|---------------:|----------------:|---------------:|-----------------------:|----------------------:|--------------------:|-------------------:|
| GraphTemporalTransformer |           0.0933 |          0.0214 |          0.9647 |         0.0065 |          0.875  |         0.0143 |                 0.8935 |                0.0284 |              0.87   |             0.016  |
| cnn1d                    |           0.0042 |          0.0009 |          0.9987 |         0.0003 |          0.9971 |         0.0008 |                 0.9971 |                0.0017 |              0.9971 |             0.0017 |
| gru                      |           0.054  |          0.0211 |          0.9796 |         0.0107 |          0.9288 |         0.0471 |                 0.9469 |                0.0349 |              0.917  |             0.0534 |
| lstm                     |           0.0374 |          0.004  |          0.9871 |         0.0022 |          0.9608 |         0.0072 |                 0.9627 |                0.011  |              0.9597 |             0.005  |



## Table 2. Uncertainty Calibration Summary

| model                    |   mc_samples_mean |   mc_samples_std |   accuracy_mean |   accuracy_std |   macro_f1_mean |   macro_f1_std |   expected_calibration_error_mean |   expected_calibration_error_std |   brier_score_mean |   brier_score_std |   mean_confidence_mean |   mean_confidence_std |   mean_predictive_entropy_mean |   mean_predictive_entropy_std |
|:-------------------------|------------------:|-----------------:|----------------:|---------------:|----------------:|---------------:|----------------------------------:|---------------------------------:|-------------------:|------------------:|-----------------------:|----------------------:|-------------------------------:|------------------------------:|
| GraphTemporalTransformer |                20 |                0 |          0.9655 |         0.0076 |          0.8808 |         0.0122 |                            0.0088 |                           0.0024 |             0.0531 |            0.0129 |                 0.9601 |                0.0056 |                         0.0986 |                        0.0117 |



## Table 3. OOD / Unseen Attack Summary

| condition              |   accuracy_mean |   accuracy_std |   macro_f1_mean |   macro_f1_std |   mean_confidence_mean |   mean_confidence_std |   mean_entropy_mean |   mean_entropy_std |   low_confidence_rate_lt_0_70_mean |   low_confidence_rate_lt_0_70_std |
|:-----------------------|----------------:|---------------:|----------------:|---------------:|-----------------------:|----------------------:|--------------------:|-------------------:|-----------------------------------:|----------------------------------:|
| delayed_combined       |          0.0305 |         0.0046 |          0.0521 |         0.0242 |                 0.9194 |                0.0289 |              0.231  |             0.0862 |                             0.0651 |                            0.0086 |
| in_distribution_test   |          0.9647 |         0.0065 |          0.875  |         0.0143 |                 0.9631 |                0.0076 |              0.0928 |             0.0188 |                             0.0422 |                            0.0148 |
| intermittent_tampering |          0.691  |         0.0309 |          0.5965 |         0.0518 |                 0.8916 |                0.0141 |              0.2486 |             0.0207 |                             0.1434 |                            0.0318 |
| slow_gps_drift         |          0.1253 |         0.0138 |          0.1701 |         0.051  |                 0.8875 |                0.0328 |              0.2721 |             0.0766 |                             0.1434 |                            0.0509 |
| stealth_jammer         |          0.0651 |         0.0197 |          0.0779 |         0.0236 |                 0.8652 |                0.0263 |              0.3449 |             0.0091 |                             0.1208 |                            0.1275 |
| unseen_swarm_noise     |          0.9645 |         0.0066 |          0.8744 |         0.0147 |                 0.9631 |                0.0076 |              0.0928 |             0.0189 |                             0.0422 |                            0.0147 |



## Table 4. Feature Importance Summary

| feature                |   baseline_macro_f1_mean |   baseline_macro_f1_std |   perturbed_macro_f1_mean |   perturbed_macro_f1_std |   macro_f1_drop_mean |   macro_f1_drop_std |
|:-----------------------|-------------------------:|------------------------:|--------------------------:|-------------------------:|---------------------:|--------------------:|
| latency_ms             |                    0.875 |                  0.0143 |                    0.1856 |                   0.0218 |               0.6894 |              0.0311 |
| zone_coverage          |                    0.875 |                  0.0143 |                    0.4749 |                   0.0331 |               0.4001 |              0.044  |
| route_deviation_m      |                    0.875 |                  0.0143 |                    0.5694 |                   0.1021 |               0.3056 |              0.0897 |
| mission_progress       |                    0.875 |                  0.0143 |                    0.576  |                   0.0533 |               0.299  |              0.0416 |
| gps_jump_m             |                    0.875 |                  0.0143 |                    0.5816 |                   0.0329 |               0.2934 |              0.0215 |
| velocity_inconsistency |                    0.875 |                  0.0143 |                    0.8654 |                   0.0275 |               0.0096 |              0.0142 |
| energy_consumption     |                    0.875 |                  0.0143 |                    0.8726 |                   0.0144 |               0.0024 |              0.0014 |
| packet_loss_rate       |                    0.875 |                  0.0143 |                    0.8747 |                   0.0145 |               0.0003 |              0.0002 |
| battery_level          |                    0.875 |                  0.0143 |                    0.8756 |                   0.0148 |              -0.0006 |              0.0009 |



## Key Interpretation

- CNN1D achieved the strongest in-distribution classification performance.

- Graph-Temporal Transformer achieved strong calibrated performance and supports the trustworthy mission-assurance framing.

- OOD stress tests show severe degradation under stealth jamming, slow GPS drift, and delayed combined attacks.

- Feature importance highlights latency, zone coverage, route deviation, mission progress, and GPS jump as major decision drivers.

---

# Results and Discussion Draft

## Experimental Configuration

The TRUST-Swarm experiment was evaluated using a three-seed journal-grade configuration with seeds 42, 123, and 2026. For each seed, the telemetry generator produced 300 mission runs with 240 timesteps and 20 UAVs per mission. The graph-window builder generated 66,300 graph-temporal windows per seed using a 20-step temporal window, 20 UAV nodes, and 9 telemetry features.

The evaluation included temporal baselines, a graph-temporal model, uncertainty calibration, out-of-distribution attack evaluation, and perturbation-based feature-importance analysis. The baseline models included LSTM, GRU, and 1D-CNN. The proposed TRUST-Swarm model used a Graph-Temporal Transformer to jointly reason over UAV-node interactions and temporal mission evolution.

## In-Distribution Classification Performance

The Graph-Temporal Transformer achieved a mean accuracy of 0.9647 and a mean macro F1 score of 0.8750 across the three seeds. This confirms that the proposed graph-temporal architecture can learn meaningful mission-state patterns from multi-UAV telemetry under cyber-physical attack conditions.

The 1D-CNN baseline achieved the strongest in-distribution classification performance, with a mean accuracy of 0.9987 and a mean macro F1 score of 0.9971. The LSTM and GRU baselines achieved mean macro F1 scores of 0.9608 and 0.9288, respectively.

These results indicate that the current synthetic telemetry setting contains strong local temporal signatures that can be captured effectively by convolutional temporal models. Therefore, the contribution of TRUST-Swarm should not be framed as outperforming every baseline in standard classification accuracy. Instead, the correct contribution is the integration of graph-temporal learning with uncertainty calibration, OOD stress testing, explainability, and mission-recovery reasoning.

## Uncertainty Calibration

The Graph-Temporal Transformer demonstrated strong in-distribution calibration. Across the three seeds, the model achieved a mean Expected Calibration Error of 0.0088 and a mean Brier score of 0.0531. The mean predictive confidence was 0.9601, while the mean predictive entropy was 0.0986.

These results support the high-confidence computing framing of TRUST-Swarm. The model is not only capable of producing accurate predictions under in-distribution conditions, but it also provides calibrated confidence estimates that can be used by a mission-assurance layer.

## OOD and Unseen Attack Stress Testing

OOD evaluation revealed that unseen cyber-physical shifts cause substantial degradation in model performance. The in-distribution macro F1 score was 0.8750, while intermittent tampering reduced macro F1 to 0.5965. More severe shifts produced larger degradation: slow GPS drift achieved a macro F1 of 0.1701, stealth jamming achieved 0.0779, and delayed combined attacks achieved 0.0521.

These results show that unseen attack conditions can significantly alter mission telemetry distributions. The findings support the need for OOD-aware monitoring in safety-critical multi-UAV systems. However, the model should not be described as perfectly detecting all OOD conditions. Some severe OOD cases retained high confidence, indicating that confidence alone is not sufficient for reliable OOD rejection. Instead, the results motivate the combined use of uncertainty monitoring, OOD stress testing, explainability, and recovery policies.

## Explainability Analysis

Perturbation-based feature importance showed that the most influential telemetry features were latency, zone coverage, route deviation, mission progress, and GPS jump. These features align with the operational meaning of the attack scenarios. Latency reflects communication degradation, zone coverage reflects mission-level impact, route deviation and GPS jump reflect navigation disruption, and mission progress reflects task completion under cyber-physical interference.

This explainability result improves the interpretability of TRUST-Swarm because the model’s most important features correspond to mission-relevant risk factors rather than arbitrary telemetry artifacts.

## Discussion

The final results show that TRUST-Swarm should be positioned as a high-confidence mission-assurance framework rather than only a classifier. Although the 1D-CNN baseline achieved stronger in-distribution classification accuracy, it does not provide the same integrated framework for graph-temporal mission modeling, calibration, OOD evaluation, explainability, and recovery reasoning.

The Graph-Temporal Transformer provides a structured representation of multi-UAV mission state by incorporating both UAV-node interactions and temporal evolution. Its calibrated uncertainty metrics support high-confidence decision-making under normal conditions, while the OOD stress tests expose vulnerability under unseen attack shifts. These findings are important because real-world UAV operations rarely remain fully in-distribution. Mission-assurance systems must identify not only what class is predicted, but also how trustworthy the prediction is and which telemetry factors contributed to the decision.

The feature-importance results further support the operational relevance of the model. The strongest decision drivers were latency, zone coverage, route deviation, mission progress, and GPS jump, all of which are meaningful indicators of cyber-physical mission degradation. This improves the credibility of the model for defense and autonomous-systems applications.

## Manuscript Claim to Use

The final manuscript should claim that TRUST-Swarm provides an integrated trustworthy AI framework for multi-UAV mission assurance under cyber-physical attacks. The framework combines graph-temporal learning, calibration, OOD stress testing, explainability, and recovery reasoning.

The manuscript should not claim that the Graph-Temporal Transformer is the best in-distribution classifier across all baselines. Instead, it should state that the proposed framework adds trust, interpretability, OOD awareness, and recovery support beyond raw classification performance.

## Limitations

The current dataset is synthetically generated and should be described as a controlled simulation-based evaluation. Although it includes multiple attack types, multiple seeds, and large-scale telemetry generation, it does not replace field-tested UAV data. The OOD results also show that severe unseen shifts can produce major performance degradation, and in some cases the model remains highly confident under OOD conditions. This limitation should be acknowledged clearly.

Future work should include more realistic communication-channel simulation, physics-based UAV mobility, larger swarm-size variation, field telemetry, and stronger OOD detection mechanisms.

## Final Interpretation

The results provide a strong foundation for a journal manuscript if the contribution is framed correctly. TRUST-Swarm should be presented as a high-confidence mission-assurance framework rather than a pure classifier. The strongest contribution is the combined evaluation of graph-temporal learning, uncertainty calibration, OOD stress testing, explainability, and recovery reasoning for resilient multi-UAV operations under cyber-physical attacks.


---

# TRUST-Swarm Conclusion and Limitations Draft

## 6. Limitations and Future Work

Although the final TRUST-Swarm experiment provides a strong foundation for high-confidence multi-UAV mission assurance, several limitations should be acknowledged.

First, the evaluation is based on synthetic telemetry generation. The synthetic environment allows controlled testing across multiple attack types, mission runs, seeds, and OOD stress conditions, but it does not fully replace field-collected UAV telemetry. Real-world UAV operations may include more complex mobility patterns, communication-channel effects, environmental interference, sensor noise, weather conditions, hardware constraints, and operator-driven mission changes.

Second, the current graph structure is based on graph-temporal telemetry windows rather than a fully physics-based UAV communication graph. Future work should integrate distance-aware communication links, RF propagation models, UAV mobility constraints, line-of-sight disruption, and dynamic edge construction based on mission context.

Third, the OOD results show that severe unseen cyber-physical shifts can substantially degrade model performance. This is important because it reveals operational vulnerability under stealth jamming, slow GPS drift, and delayed combined attacks. However, some severe OOD cases may still produce high model confidence. Therefore, future work should include stronger OOD detection methods, ensemble uncertainty, conformal prediction, energy-based OOD scoring, and hybrid statistical monitoring.

Fourth, the 1D-CNN baseline achieved the strongest in-distribution classification performance. This indicates that the current synthetic telemetry contains strong local temporal signatures. The Graph-Temporal Transformer should therefore not be framed as the best raw classifier. Instead, TRUST-Swarm should be framed as a trustworthy mission-assurance framework that integrates graph-temporal modeling, uncertainty calibration, OOD stress testing, explainability, and recovery reasoning.

Fifth, the PPO-based mission recovery module is currently a recovery-reasoning scaffold. Although it demonstrates the feasibility of connecting mission-state indicators to recovery actions, it should not be interpreted as a complete operational UAV controller. Future work should improve the reward function, enforce safety constraints, encourage balanced recovery actions, integrate realistic mission simulators, and evaluate recovery policies under dynamic swarm conditions.

Future research will extend TRUST-Swarm in five directions: field-realistic UAV telemetry, physics-informed communication modeling, stronger OOD detection, safety-constrained recovery policies, and hardware-in-the-loop or simulator-in-the-loop validation.

## 7. Conclusion

This paper presented TRUST-Swarm, a trustworthy graph-temporal AI framework for high-confidence multi-UAV mission assurance under cyber-physical attacks. The framework models UAV swarm telemetry as graph-temporal mission windows and integrates graph-temporal learning, uncertainty calibration, OOD stress testing, perturbation-based explainability, and recovery-oriented reasoning.

The final three-seed experiment evaluated TRUST-Swarm using 300 mission runs per seed, 240 timesteps per mission, 20 UAVs per mission, and 66,300 graph-temporal windows per seed. The Graph-Temporal Transformer achieved strong in-distribution performance and calibration, with a mean accuracy of 0.9647, mean macro F1 of 0.8750, Expected Calibration Error of 0.0088, and Brier score of 0.0531.

The results also showed that the 1D-CNN baseline achieved stronger in-distribution classification performance than the Graph-Temporal Transformer. This finding is important because it prevents overclaiming and supports a more accurate interpretation of TRUST-Swarm. The contribution of TRUST-Swarm is not simply raw classification superiority. Its contribution is the integration of classification, calibration, OOD stress testing, explainability, and recovery reasoning into a high-confidence mission-assurance pipeline.

OOD stress tests revealed that unseen cyber-physical shifts, especially stealth jamming, slow GPS drift, and delayed combined attacks, can severely degrade model performance. These findings show that UAV swarm mission assurance must include OOD-aware evaluation rather than relying only on in-distribution test accuracy.

Explainability analysis identified latency, zone coverage, route deviation, mission progress, and GPS jump as the most influential telemetry features. These features align with operationally meaningful mission-risk indicators, supporting the interpretability and mission relevance of the TRUST-Swarm framework.

Overall, TRUST-Swarm provides a strong foundation for trustworthy AI-enabled multi-UAV mission assurance. The framework demonstrates how graph-temporal learning, calibrated confidence, OOD stress testing, explainability, and recovery reasoning can be combined to support resilient autonomous swarm operations under cyber-physical uncertainty.


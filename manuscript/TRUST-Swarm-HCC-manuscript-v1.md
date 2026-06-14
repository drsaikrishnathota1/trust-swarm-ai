# TRUST-Swarm: A High-Confidence Graph-Temporal Intelligent Computing Framework for Secure Multi-UAV Mission Assurance Under Cyber-Physical Attacks

**Target journal:** High-Confidence Computing


## Abstract

Multi-UAV swarm systems are increasingly used in cyber-physical missions that require secure, reliable, and intelligent decision support under dynamic adversarial conditions. However, communication jamming, GPS spoofing, telemetry tampering, and combined attacks can corrupt mission telemetry, degrade coordination, and reduce the reliability of autonomous mission-state prediction. Existing UAV security and resilience methods often emphasize attack classification or communication protection, but they provide limited support for calibrated confidence estimation, out-of-distribution stress testing, traceable decision evidence, and recovery-oriented mission reasoning.

This paper presents TRUST-Swarm, a high-confidence graph-temporal intelligent computing framework for secure multi-UAV mission assurance under cyber-physical attacks. TRUST-Swarm models distributed UAV telemetry as graph-temporal mission windows and integrates mission-state recognition, uncertainty calibration, OOD stress testing, perturbation-based explainability, and recovery-oriented reasoning. The framework is designed to support high-confidence decision-making by evaluating not only what mission state is predicted, but also how reliable the prediction is, how the model behaves under unseen cyber-physical shifts, which telemetry factors influence the decision, and how prediction outputs can support mission recovery.

A three-seed simulation study was conducted using 300 mission runs per seed, 240 timesteps per mission, 20 UAVs per mission, and 66,300 graph-temporal windows per seed. The Graph-Temporal Transformer achieved a mean accuracy of 0.9647 and a mean macro F1 score of 0.8750, while producing strong in-distribution calibration with an Expected Calibration Error of 0.0088 and a Brier score of 0.0531. OOD stress testing revealed substantial degradation under severe unseen cyber-physical shifts, especially delayed combined attacks, stealth jamming, and slow GPS drift. Explainability analysis identified latency, zone coverage, route deviation, mission progress, and GPS jump as mission-relevant decision drivers.

Although the 1D-CNN baseline achieved stronger in-distribution classification performance, TRUST-Swarm is not proposed as a raw classifier alone. Instead, it provides a high-confidence secure intelligent computing framework that integrates prediction, calibration, OOD vulnerability analysis, traceable explanation, and recovery-oriented mission reasoning. The results demonstrate that secure UAV swarm mission assurance requires more than high classification accuracy; it requires high-confidence computing mechanisms that can evaluate reliability, expose unseen-shift risk, explain decisions, and support resilient mission response.

## Contributions

| High-Confidence Computing Requirement | TRUST-Swarm Component                                                                   | Manuscript Evidence                                                                                  |
| ------------------------------------- | --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| Secure computing                      | Cyber-physical attack modeling under jamming, spoofing, tampering, and combined attacks | Attack-state simulation and multi-class mission-state recognition                                    |
| Intelligent computing                 | Graph-Temporal Transformer for UAV mission-state recognition                            | Graph-temporal learning over UAV nodes, mission time, and telemetry features                         |
| Precise computing                     | Calibrated prediction confidence                                                        | Expected Calibration Error, Brier score, confidence, and entropy                                     |
| Traceable computing                   | Perturbation-based explainability                                                       | Feature-importance ranking using macro-F1 drop                                                       |
| Robustness under uncertainty          | OOD stress testing                                                                      | Stealth jamming, slow GPS drift, intermittent tampering, delayed combined attack, unseen swarm noise |
| Active defense support                | Recovery-oriented reasoning scaffold                                                    | PPO-based recovery action space: continue, monitor, reroute, reassign, isolate node, return to base  |
| Mission assurance                     | End-to-end high-confidence decision support                                             | Prediction + confidence + OOD behavior + explanation + recovery loop                                 |

## 1. Introduction

Multi-UAV swarm systems are increasingly used in surveillance, reconnaissance, disaster response, infrastructure monitoring, logistics, and cyber-physical mission operations. Compared with single-UAV platforms, UAV swarms provide distributed sensing, wider coverage, redundancy, and adaptive mission execution. However, these advantages depend on the reliability of communication, navigation, telemetry integrity, energy awareness, and mission-progress monitoring. When these information streams are disrupted, autonomous mission decisions may become unreliable.

Cyber-physical attacks create a major challenge for secure UAV swarm mission assurance. Communication jamming can increase latency and packet loss, reducing coordination among UAV nodes. GPS spoofing can cause route deviation, GPS jumps, and velocity inconsistency. Telemetry tampering can distort battery state, mission progress, energy consumption, or zone coverage. Combined attacks can simultaneously degrade communication, navigation, and mission integrity. These disruptions create a high-confidence computing problem: the system must not only predict mission state, but also evaluate whether the prediction can be trusted.

Existing UAV security and resilience methods often focus on attack detection, secure communication, intrusion detection, or rule-based recovery. Although these methods are valuable, many of them remain limited in four ways. First, they often treat mission telemetry as ordinary time-series data rather than modeling UAV-node relationships and mission evolution together. Second, they emphasize classification accuracy without calibrated confidence estimation. Third, they rarely evaluate model behavior under unseen out-of-distribution cyber-physical shifts. Fourth, they provide limited traceability and limited connection between prediction outputs and recovery-oriented mission response.

These limitations are critical for high-confidence intelligent systems. In secure autonomous missions, a prediction is not sufficient by itself. A mission-assurance framework should answer five questions: what mission state is predicted, how reliable the prediction is, how the system behaves under unseen cyber-physical shifts, which telemetry factors influenced the decision, and how the output can support recovery reasoning. Therefore, secure UAV swarm mission assurance should be framed as a high-confidence intelligent computing problem rather than only an attack-classification problem.

To address this need, this paper presents TRUST-Swarm, a high-confidence graph-temporal intelligent computing framework for secure multi-UAV mission assurance under cyber-physical attacks. TRUST-Swarm represents distributed UAV telemetry as graph-temporal mission windows and evaluates a Graph-Temporal Transformer for mission-state recognition. The framework further integrates uncertainty calibration, OOD stress testing, perturbation-based explainability, and recovery-oriented reasoning.

The final evaluation uses a controlled simulation-based telemetry environment with three random seeds, 300 mission runs per seed, 240 timesteps per mission, 20 UAVs per mission, and 66,300 graph-temporal windows per seed. The evaluated mission states include normal operation, jamming, spoofing, tampering, and combined cyber-physical attack scenarios. The OOD evaluation includes stealth jamming, slow GPS drift, intermittent tampering, delayed combined attacks, and unseen swarm noise.

The results show that the Graph-Temporal Transformer achieves strong in-distribution mission-state recognition and strong calibration. However, the 1D-CNN baseline achieves the strongest raw in-distribution classification performance. Therefore, TRUST-Swarm is not positioned as the best raw classifier. Instead, it is positioned as a high-confidence secure intelligent computing framework that integrates prediction, calibration, OOD vulnerability analysis, traceable explanation, and recovery-oriented mission reasoning.

The main contributions of this paper are as follows:

1. A high-confidence graph-temporal intelligent computing framework is proposed for secure multi-UAV mission assurance under cyber-physical attacks.

2. A graph-temporal mission-window representation is developed to model UAV-node relationships, mission-time evolution, and heterogeneous telemetry features.

3. A Graph-Temporal Transformer is evaluated for mission-state recognition under normal, jamming, spoofing, tampering, and combined attack conditions.

4. A three-seed simulation study is conducted using 300 mission runs per seed, 240 timesteps per mission, 20 UAVs per mission, and 66,300 graph-temporal windows per seed.

5. Temporal baseline comparisons are performed against LSTM, GRU, and 1D-CNN models.

6. Calibrated confidence is evaluated using Expected Calibration Error, Brier score, predictive confidence, and predictive entropy.

7. OOD stress testing is performed under stealth jamming, slow GPS drift, intermittent tampering, delayed combined attacks, and unseen swarm noise.

8. Perturbation-based explainability is used to identify traceable mission-risk drivers, including latency, zone coverage, route deviation, mission progress, and GPS jump.

9. A PPO-based recovery-reasoning scaffold is included to connect mission-state prediction, confidence, and risk indicators to mission-assurance response actions.

The remainder of this paper is organized as follows. Section 2 reviews related work on UAV cyber-physical security, high-confidence intelligent computing, graph-temporal learning, uncertainty calibration, OOD evaluation, explainability, and recovery reasoning. Section 3 presents the TRUST-Swarm methodology. Section 4 describes the experimental setup. Section 5 reports and discusses the results. Section 6 presents limitations and future work. Section 7 concludes the paper.

## 2. Related Work

This section reviews prior work related to secure UAV swarm mission assurance, high-confidence intelligent computing, graph-temporal learning, uncertainty calibration, OOD robustness, explainable AI, and recovery-oriented reinforcement learning. The goal is to position TRUST-Swarm as a high-confidence secure intelligent computing framework rather than only a UAV attack-classification model.

## 2.1 Secure UAV Swarm Mission Assurance

Multi-UAV swarms provide distributed sensing, redundancy, wide-area mission coverage, and cooperative autonomy. These properties make them useful for surveillance, reconnaissance, infrastructure monitoring, disaster response, logistics, and cyber-physical mission operations. However, UAV swarms also introduce mission-assurance challenges because mission success depends on communication reliability, navigation integrity, telemetry correctness, energy state, node coordination, and mission-progress consistency.

Prior UAV security and mission-assurance studies have examined UAV cyber risks, UAS traffic-management security, sensor-channel threats, GPS spoofing, jamming, and secure communication [1–4, 34–47]. These studies show that UAV missions can be degraded through both cyber and physical channels. However, many existing methods focus on individual attack detection or communication protection rather than end-to-end high-confidence mission assurance.

TRUST-Swarm builds on this literature by treating secure UAV swarm operation as a high-confidence computing problem. The framework evaluates mission-state prediction, calibrated confidence, unseen-shift behavior, decision traceability, and recovery reasoning together.

## 2.2 Cyber-Physical Attack Detection and Secure Intelligent Systems

Cyber-physical attacks against UAV swarms can corrupt the information required for autonomous mission decisions. Communication jamming increases packet loss and latency. GPS spoofing produces route deviation, GPS jumps, and velocity inconsistency. Telemetry tampering can distort battery state, mission progress, energy consumption, or zone coverage. Combined attacks can simultaneously affect communication, navigation, and mission integrity.

Existing cyber-physical security approaches often use intrusion detection, anomaly detection, secure communication, rule-based monitoring, or machine-learning classification. These methods are valuable but often remain static, fragmented, or focused on one attack family. High-confidence secure intelligent systems require a more unified design, where detection, confidence estimation, OOD behavior, explanation, and recovery are evaluated in one pipeline.

TRUST-Swarm addresses this need by integrating graph-temporal mission-state recognition with confidence-aware and OOD-aware evaluation. This supports secure intelligent decision-making under cyber-physical uncertainty.

## 2.3 High-Confidence Computing and Trustworthy Intelligent Frameworks

High-confidence computing emphasizes secure, reliable, precise, traceable, and intelligent system behavior. In security-critical environments, a model should not only make predictions, but also provide evidence about reliability, robustness, uncertainty, and decision traceability.

Recent High-Confidence Computing-style papers commonly present unified frameworks that combine multiple capabilities rather than isolated models. For example, accepted works in this journal use structures such as privacy-aware adaptive IDS pipelines, hybrid cybersecurity assessment frameworks, federated learning with zero-trust mechanisms, denoising, feature fusion, and multi-benchmark validation. This style motivates TRUST-Swarm’s unified design.

TRUST-Swarm follows this direction by combining:

1. secure cyber-physical attack modeling,
2. graph-temporal intelligent prediction,
3. calibrated confidence estimation,
4. OOD stress testing,
5. traceable feature-level explanation,
6. recovery-oriented mission reasoning.

This makes the framework closer to a high-confidence intelligent computing system than to a standalone classifier.

## 2.4 Graph-Temporal Learning for Multi-UAV Telemetry

UAV swarms naturally produce structured telemetry over time. Each UAV can be treated as a node, and the mission state emerges from relationships among UAVs, telemetry features, and temporal mission evolution. Graph neural networks, graph attention, transformers, and time-series models provide foundations for learning such relational and temporal dependencies [5–13].

Graph-temporal learning is suitable for UAV swarm mission assurance because it can jointly capture:

1. UAV-node relationships,
2. temporal attack progression,
3. mission degradation patterns,
4. heterogeneous telemetry interactions.

TRUST-Swarm uses a Graph-Temporal Transformer to model graph-temporal mission windows. This design enables the framework to reason over UAV nodes, mission time, and telemetry features simultaneously.

## 2.5 Temporal Deep Learning Baselines

Temporal deep learning models such as LSTM, GRU, and 1D-CNN are widely used for sequence modeling and telemetry classification [14–17]. LSTM and GRU models capture recurrent temporal dependencies, while 1D-CNN models efficiently capture local temporal signatures.

In TRUST-Swarm, these models are used as baselines to evaluate whether standard temporal learning can classify mission states from the same telemetry windows. The final results show that 1D-CNN achieves the strongest in-distribution classification performance. This finding is important because it prevents overclaiming. TRUST-Swarm should not be presented as the best raw classifier, but as a high-confidence framework that adds calibration, OOD evaluation, explanation, and recovery reasoning beyond standard accuracy.

## 2.6 Uncertainty Calibration for High-Confidence Prediction

In high-confidence computing, prediction reliability is as important as prediction accuracy. A UAV mission-assurance system must know not only which mission state is predicted, but also whether the prediction is trustworthy. Neural networks can be poorly calibrated, especially under distribution shift, so calibration and uncertainty evaluation are critical for secure autonomous systems [18–24].

TRUST-Swarm evaluates confidence using Expected Calibration Error, Brier score, predictive confidence, and predictive entropy. Monte Carlo dropout is used to estimate uncertainty. These metrics allow the framework to evaluate whether mission-state predictions are reliable under in-distribution conditions.

This confidence-aware layer is important for mission assurance because uncertain predictions may require monitoring, escalation, or recovery-oriented response.

## 2.7 OOD Robustness and Cyber-Physical Distribution Shift

Autonomous UAV missions may encounter unseen attack behaviors that differ from training conditions. Attackers may use stealth jamming, slow GPS drift, intermittent tampering, delayed combined attacks, or other low-observable cyber-physical shifts. Prior OOD and distribution-shift studies show that models can fail under shifted inputs even when they perform well on in-distribution data [22, 25–28, 54, 55].

TRUST-Swarm includes OOD stress testing to evaluate mission-state recognition under unseen attack shifts. The purpose is not to claim perfect OOD detection. Instead, the goal is to expose mission-risk conditions where performance degrades or confidence becomes unreliable.

This is strongly aligned with high-confidence computing because systems operating in adversarial environments must be evaluated under uncertainty, distribution shift, and evolving threat conditions.

## 2.8 Explainability and Traceable Mission-Risk Evidence

Traceability is a key requirement for high-confidence intelligent systems. A mission-assurance framework should explain which telemetry factors influenced its prediction. Explainable AI methods such as LIME, SHAP, saliency analysis, and perturbation-based feature importance provide tools for interpreting model behavior [29–32].

TRUST-Swarm uses perturbation-based feature importance to identify traceable mission-risk drivers. The final analysis identifies latency, zone coverage, route deviation, mission progress, and GPS jump as major decision drivers. These features are operationally meaningful because they correspond to communication degradation, mission coverage loss, navigation disruption, mission-progress interruption, and spoofing-related displacement.

This supports the claim that TRUST-Swarm provides traceable decision evidence rather than opaque classification alone.

## 2.9 Recovery-Oriented Reinforcement Learning and Active Defense

Mission assurance should not stop after prediction. Once a mission risk is detected, a UAV swarm may need to continue, monitor, reroute, reassign, isolate a compromised node, or return to base. Reinforcement learning, PPO, and multi-agent reinforcement-learning methods provide foundations for adaptive planning and recovery-oriented response [33, 48–53].

TRUST-Swarm includes a PPO-based recovery-reasoning scaffold to connect mission-state prediction, confidence, entropy, and mission-risk indicators to possible recovery actions. The recovery layer is not claimed as a deployment-ready UAV controller. Instead, it demonstrates how high-confidence prediction outputs can support active-defense-style mission reasoning.

## 2.10 Research Gap

The literature includes strong work on UAV cybersecurity, graph learning, temporal modeling, uncertainty calibration, OOD detection, explainability, and reinforcement learning. However, these areas are often studied separately. Existing UAV security frameworks may classify attacks or detect anomalies, but they often do not jointly provide calibrated confidence, OOD stress testing, traceable decision evidence, and recovery-oriented reasoning.

TRUST-Swarm addresses this gap by presenting a high-confidence graph-temporal intelligent computing framework for secure UAV swarm mission assurance. The framework evaluates not only mission-state prediction, but also prediction reliability, unseen-shift vulnerability, feature-level traceability, and recovery-oriented decision support.

This positioning aligns TRUST-Swarm with High-Confidence Computing because the central contribution is not raw classification superiority, but integrated secure, intelligent, calibrated, traceable, and recovery-aware mission assurance.

## 3. Methodology

This section presents TRUST-Swarm as a high-confidence graph-temporal intelligent computing framework for secure multi-UAV mission assurance under cyber-physical attacks. The framework is designed to support secure prediction, calibrated confidence, OOD vulnerability analysis, traceable explanation, and recovery-oriented reasoning.

## 3.1 Framework Overview

TRUST-Swarm contains six main layers:

1. Secure multi-UAV telemetry generation
2. Graph-temporal mission-window construction
3. Graph-temporal intelligent prediction
4. Confidence-aware reliability evaluation
5. OOD-aware cyber-physical stress testing
6. Traceable explanation and recovery-oriented reasoning

The purpose of the framework is not only to classify cyber-physical mission states, but also to evaluate whether predictions are trustworthy, whether unseen attack shifts degrade reliability, which telemetry factors influence decisions, and how mission-risk outputs can support recovery reasoning.

## 3.2 Secure Multi-UAV Telemetry Generation

A controlled simulation-based telemetry generator is used to create multi-UAV cyber-physical mission scenarios. Each mission contains a swarm of UAVs operating across mission time under normal or adversarial conditions.

The telemetry sources include:

1. Communication telemetry
2. Navigation telemetry
3. Energy telemetry
4. Mission-progress telemetry
5. Coverage telemetry

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

The mission-state classes are:

1. normal
2. jamming
3. spoofing
4. tampering
5. jamming-spoofing
6. jamming-tampering
7. spoofing-tampering
8. combined attack

The generator introduces random attack onset, attack duration, UAV-level variation, jammer proximity, and local exposure intensity. This creates a controlled high-confidence benchmark for evaluating secure mission-state prediction under cyber-physical uncertainty.

## 3.3 Graph-Temporal Mission-Window Construction

Raw UAV telemetry is converted into graph-temporal mission windows. Each sample is represented as:

X ∈ R^(T × N × F)

where:

* T is the temporal window length
* N is the number of UAV nodes
* F is the number of telemetry features

In the final experiment:

* T = 20 timesteps
* N = 20 UAV nodes
* F = 9 telemetry features

This representation preserves three types of structure:

1. temporal mission evolution
2. UAV-node structure
3. heterogeneous telemetry-feature structure

The graph-temporal mission window allows TRUST-Swarm to reason over mission degradation across nodes, time, and telemetry sources.

## 3.4 Graph-Temporal Intelligent Prediction Layer

The Graph-Temporal Transformer is used as the main intelligent prediction model. The model receives an input tensor with shape:

batch_size × window_size × num_uavs × num_features

The model contains:

1. telemetry feature projection
2. UAV-node attention
3. temporal transformer encoding
4. fused mission embedding
5. mission-state classifier

The model learns UAV-node relationships, temporal attack progression, and mission-state degradation patterns. Its output is a probability distribution over mission-state classes.

## 3.5 Temporal Baseline Models

Three temporal baseline models are evaluated:

1. LSTM
2. GRU
3. 1D-CNN

These baselines evaluate whether conventional temporal models can classify mission states from the same graph-window telemetry. The 1D-CNN baseline achieved the strongest in-distribution classification performance, so TRUST-Swarm is not framed as the best raw classifier. Instead, the framework is evaluated as a high-confidence computing pipeline that adds calibration, OOD testing, explanation, and recovery reasoning.

## 3.6 Confidence-Aware Reliability Evaluation

High-confidence computing requires reliable prediction confidence. TRUST-Swarm evaluates prediction reliability using:

1. Expected Calibration Error
2. Brier score
3. mean predictive confidence
4. predictive entropy

Monte Carlo dropout is used during uncertainty evaluation to estimate predictive uncertainty. This reliability layer helps determine whether a mission-state prediction should be trusted, monitored, escalated, or passed to the recovery-reasoning layer.

## 3.7 OOD-Aware Cyber-Physical Stress Testing

Operational UAV swarms may face unseen cyber-physical shifts not represented during training. TRUST-Swarm evaluates OOD behavior under five stress conditions:

1. stealth jamming
2. slow GPS drift
3. intermittent tampering
4. delayed combined attack
5. unseen swarm noise

For each condition, the framework reports:

1. accuracy
2. macro F1
3. confidence
4. entropy
5. low-confidence rate

This stage is designed to expose mission-risk conditions where predictions degrade or confidence becomes unreliable. The goal is not to claim complete OOD reliability, but to evaluate vulnerability under unseen cyber-physical conditions.

## 3.8 Traceable Explanation Layer

TRUST-Swarm uses perturbation-based feature importance to provide traceable mission-risk evidence. First, baseline macro F1 is computed. Then, each telemetry feature is replaced with its mean value, and macro F1 is recomputed.

Feature importance is calculated as:

Feature importance = baseline macro F1 − perturbed macro F1

A larger macro-F1 drop indicates that the feature has greater influence on the mission-state prediction.

The most influential telemetry drivers include:

1. latency_ms
2. zone_coverage
3. route_deviation_m
4. mission_progress
5. gps_jump_m

These features correspond to operationally meaningful cyber-physical mission risks, including communication degradation, coverage loss, navigation disruption, mission-progress interruption, and spoofing-related displacement.

## 3.9 Recovery-Oriented Reasoning Layer

TRUST-Swarm includes a PPO-based recovery-reasoning scaffold. The recovery layer receives mission-state predictions, confidence scores, entropy, and mission-risk indicators.

The action space includes:

1. continue
2. monitor
3. reroute
4. reassign
5. isolate node
6. return to base

This module is not claimed as a operationally deployable UAV controller. It is included to demonstrate how high-confidence prediction outputs can support recovery-oriented mission reasoning.

## 3.10 Experimental Protocol

The final evaluation uses three random seeds:

* 42
* 123
* 2026

For each seed, the telemetry generator produces:

* 300 mission runs
* 240 timesteps per mission
* 20 UAVs per mission
* 1,440,000 raw telemetry rows
* 66,300 graph-temporal mission windows

Each model is trained for 30 epochs using a batch size of 128. Results are aggregated across seeds using mean and standard deviation.

## 3.11 Summary

TRUST-Swarm operationalizes high-confidence computing for secure UAV swarm mission assurance through six integrated layers: secure telemetry modeling, graph-temporal prediction, confidence calibration, OOD stress testing, traceable explanation, and recovery-oriented reasoning.

This methodology follows the High-Confidence Computing style of presenting a unified framework rather than an isolated model.

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

## 5. Results and Discussion

This section evaluates TRUST-Swarm as a high-confidence graph-temporal intelligent computing framework for secure multi-UAV mission assurance. The evaluation focuses on five questions:

1. Can TRUST-Swarm recognize cyber-physical mission states?
2. How does the Graph-Temporal Transformer compare with temporal baselines?
3. Are its predictions well calibrated?
4. How does the model behave under unseen OOD cyber-physical shifts?
5. Can the framework provide traceable evidence and recovery-oriented reasoning?

## 5.1 In-Distribution Mission-State Recognition

Across three random seeds, the Graph-Temporal Transformer achieved a mean accuracy of 0.9647 and a mean macro F1 score of 0.8750. The mean macro precision was 0.8935, and the mean macro recall was 0.8700.

These results show that the graph-temporal prediction layer can learn meaningful mission-state patterns from UAV telemetry under cyber-physical attack conditions. The model captures mission-time evolution, UAV-node structure, and telemetry-feature interactions across communication, navigation, energy, mission-progress, and coverage signals.

From a High-Confidence Computing perspective, this result demonstrates the intelligent computing component of TRUST-Swarm. However, mission-state recognition alone is not sufficient for high-confidence autonomous operation. The framework must also evaluate reliability, uncertainty, OOD behavior, traceability, and recovery support.

## 5.2 Baseline Comparison

The baseline comparison included LSTM, GRU, and 1D-CNN models. The 1D-CNN baseline achieved the strongest in-distribution classification performance, with a mean accuracy of 0.9987 and a mean macro F1 score of 0.9971. The LSTM and GRU baselines achieved mean macro F1 scores of 0.9608 and 0.9288, respectively.

This result shows that the synthetic telemetry benchmark contains strong local temporal signatures that are effectively captured by convolutional temporal learning. Therefore, the Graph-Temporal Transformer should not be claimed as the best raw classifier.

The correct interpretation is that TRUST-Swarm contributes a high-confidence secure intelligent computing pipeline. Unlike a pure classifier, the framework integrates prediction, calibration, OOD stress testing, traceable explanation, and recovery-oriented reasoning. This broader framework-level contribution is more aligned with High-Confidence Computing than a single accuracy comparison.

## 5.3 Confidence Calibration Results

The Graph-Temporal Transformer produced strong in-distribution calibration. Across three seeds, the model achieved a mean Expected Calibration Error of 0.0088 and a mean Brier score of 0.0531. The mean predictive confidence was 0.9601, and the mean predictive entropy was 0.0986.

These results support the high-confidence computing objective because the model provides not only mission-state probabilities but also reliability evidence. A low Expected Calibration Error indicates that predicted confidence is well aligned with empirical correctness under in-distribution conditions.

For secure UAV swarm mission assurance, calibrated confidence is important because uncertain or low-confidence predictions may require monitoring, escalation, or recovery-oriented response. This makes calibration a core component of TRUST-Swarm rather than an optional evaluation metric.

## 5.4 OOD Cyber-Physical Stress Testing

OOD stress testing revealed substantial performance degradation under unseen cyber-physical shifts. The in-distribution macro F1 score was 0.8750. Intermittent tampering reduced macro F1 to 0.5965. More severe shifts caused larger reductions: slow GPS drift achieved a macro F1 score of 0.1701, stealth jamming achieved 0.0779, and delayed combined attacks achieved 0.0521.

These findings show that cyber-physical distribution shifts can significantly degrade mission-state recognition even when in-distribution performance is strong. This is an important high-confidence computing result because it exposes failure modes that standard test accuracy would hide.

The OOD results should not be interpreted as complete OOD reliability. Some severe OOD cases may still produce high confidence. Therefore, confidence alone is not sufficient for secure mission assurance. TRUST-Swarm uses OOD stress testing to reveal mission-risk conditions and motivate stronger monitoring, escalation, and recovery mechanisms.

## 5.5 Traceable Mission-Risk Explanation

Perturbation-based feature importance identified latency, zone coverage, route deviation, mission progress, and GPS jump as the most influential mission-risk drivers.

These features are operationally meaningful:

* latency reflects communication degradation and possible jamming;
* zone coverage reflects mission effectiveness and coverage loss;
* route deviation reflects navigation disruption;
* mission progress reflects task completion under attack;
* GPS jump reflects spoofing-related displacement.

This improves decision traceability. In high-confidence computing, a framework should provide evidence explaining why a decision was produced. TRUST-Swarm supports this through feature-level traceability, linking mission-state predictions to interpretable cyber-physical telemetry drivers.

## 5.6 Recovery-Oriented Reasoning

TRUST-Swarm includes a PPO-based recovery-reasoning scaffold. The recovery layer receives mission-state prediction, confidence, entropy, and mission-risk indicators. It maps these inputs to recovery actions such as continue, monitor, reroute, reassign, isolate node, and return to base.

This module is not claimed as a operationally deployable UAV controller. Instead, it demonstrates how high-confidence prediction outputs can support mission-response reasoning. This is important because secure mission assurance should not stop at detection. It should connect risk recognition to response planning.

## 5.7 Discussion Against High-Confidence Computing Standards

The results show that TRUST-Swarm is better framed as a high-confidence intelligent computing framework than as a pure classification model.

The accepted High-Confidence Computing papers commonly emphasize unified frameworks, multiple evaluation metrics, practical validation, and system-level reasoning. For example, the SDN-IoT DRAFT paper combines traffic prediction, federated learning, zero-trust mechanisms, denoising, and real-world dataset evaluation. The HTTPS assessment paper proposes a unified methodology with testing, examination, interviewing, and real-world website case-study validation. The critical-infrastructure IDS paper integrates detection, classification, privacy preservation, adaptation, and multi-benchmark validation. TRUST-Swarm follows the same framework-oriented direction, but its current limitation is that validation remains synthetic.

Therefore, the current results are strong enough to justify a manuscript foundation, but two additional analyses are needed before final HCC submission:

1. Ablation study to show the value of each TRUST-Swarm module.
2. Runtime and complexity analysis to show practical computing feasibility.

## 5.8 Safe Final Interpretation

The safe interpretation is:

TRUST-Swarm provides a high-confidence graph-temporal intelligent computing framework for secure multi-UAV mission assurance by integrating mission-state recognition, calibrated confidence, OOD cyber-physical stress testing, traceable explanation, and recovery-oriented reasoning.

The manuscript should not claim:

* the Graph-Temporal Transformer is superior to all baselines;
* OOD behavior is fully solved;
* the recovery module is operationally operationally deployable;
* synthetic telemetry replaces field UAV validation.

The results support TRUST-Swarm as a secure, intelligent, calibrated, traceable, and recovery-aware mission-assurance framework.

## 6. Limitations and Future Work

This study has several limitations. First, the current evaluation uses controlled synthetic multi-UAV telemetry rather than field-collected UAV swarm data. The controlled benchmark enables repeatable evaluation across cyber-physical attack states, OOD stress conditions, confidence metrics, and multiple random seeds, but real-world deployment validation remains necessary.

Second, the OOD stress tests reveal that severe unseen cyber-physical shifts can substantially reduce mission-state recognition performance. This finding is important for high-confidence computing because it exposes hidden mission risk, but it also shows that additional OOD detection and uncertainty-monitoring mechanisms are needed.

Third, the PPO-based recovery component is evaluated as a recovery-reasoning scaffold rather than a operationally deployable UAV controller. Future work should connect the recovery layer to high-fidelity UAV swarm simulators, hardware-in-the-loop validation, and mission-level safety constraints.

Fourth, the current framework uses a fixed set of telemetry features and attack classes. Future research should include richer sensor streams, adversarial attack adaptation, communication-topology changes, multi-agent coordination constraints, and real UAV logs.

Finally, future work should extend TRUST-Swarm with privacy-preserving learning, formal safety constraints, online adaptation, and human-in-the-loop mission assurance.

## 7. Conclusion

This paper presented TRUST-Swarm, a high-confidence graph-temporal intelligent computing framework for secure multi-UAV mission assurance under cyber-physical attacks. The framework integrates graph-temporal mission-state recognition, confidence calibration, OOD cyber-physical stress testing, perturbation-based traceability, and recovery-oriented reasoning.

The results show that the Graph-Temporal Transformer achieves strong mission-state recognition and strong in-distribution calibration. However, the 1D-CNN baseline achieves stronger raw in-distribution classification performance, so TRUST-Swarm is not positioned as the best standalone classifier. Instead, its contribution is a high-confidence secure intelligent computing pipeline that evaluates prediction reliability, exposes unseen-shift risk, explains mission-relevant telemetry drivers, and links risk outputs to recovery reasoning.

The study demonstrates that secure UAV swarm mission assurance requires more than accuracy. It requires high-confidence computing mechanisms that can evaluate trustworthiness, uncertainty, robustness, traceability, and recovery support under cyber-physical mission risk.

## HCC Final Submission Items Still Needed

Before submission, complete the following:

1. Add final ablation results from RunPod GPU.
2. Add final runtime and complexity results from RunPod GPU.
3. Clean and verify all references.
4. Convert this Markdown manuscript into journal-style Word/PDF.
5. Prepare cover letter, highlights, declaration of interest, and data/code availability statement.

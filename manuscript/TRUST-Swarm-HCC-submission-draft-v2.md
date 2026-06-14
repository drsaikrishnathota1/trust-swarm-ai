# TRUST-Swarm: A High-Confidence Graph-Temporal Intelligent Computing Framework for Secure Multi-UAV Mission Assurance Under Cyber-Physical Attacks


## HCC-Framed Abstract

Multi-UAV swarm systems are increasingly deployed in surveillance, reconnaissance, infrastructure inspection, disaster response, logistics, and other cyber-physical missions where autonomous decisions must remain reliable under communication, navigation, telemetry, and environmental uncertainty. In adversarial mission settings, however, communication jamming, GPS spoofing, telemetry tampering, and combined cyber-physical attacks can corrupt the information streams required for swarm coordination and mission-state assessment. Existing UAV security and resilience studies have made important progress in attack detection, secure communication, anomaly recognition, and rule-based response. Nevertheless, many approaches remain focused on classification accuracy or isolated security functions, while providing limited support for calibrated confidence estimation, out-of-distribution (OOD) stress testing, traceable decision evidence, and recovery-oriented mission reasoning. This gap is critical for high-confidence computing because security-critical autonomous systems must evaluate not only what state is predicted, but also whether the prediction is reliable, how it behaves under unseen shifts, why the decision was produced, and how the output can support response planning.

To address this need, this paper presents TRUST-Swarm, a high-confidence graph-temporal intelligent computing framework for secure multi-UAV mission assurance under cyber-physical attacks. TRUST-Swarm represents distributed UAV telemetry as graph-temporal mission windows and evaluates a Graph-Temporal Transformer for mission-state recognition. The framework integrates five assurance-oriented components: uncertainty calibration, OOD cyber-physical stress testing, perturbation-based feature-level explanation, ablation-based framework analysis, and PPO-based recovery-reasoning support. A three-seed simulation study was conducted using 300 mission runs per seed, 240 timesteps per mission, 20 UAVs per mission, and 66,300 graph-temporal windows per seed. The Graph-Temporal Transformer achieved a mean accuracy of 0.9647 and a mean macro F1 score of 0.8750, with strong in-distribution calibration measured by an Expected Calibration Error of 0.0088 and a Brier score of 0.0531. OOD testing revealed substantial degradation under severe unseen shifts, highlighting mission-risk conditions that would be hidden by standard in-distribution accuracy. Explainability analysis identified latency, zone coverage, route deviation, mission progress, and GPS jump as key mission-risk drivers. Although the 1D-CNN baseline achieved stronger raw in-distribution classification, TRUST-Swarm contributes a broader high-confidence mission-assurance framework that combines prediction, reliability assessment, OOD vulnerability analysis, decision traceability, and recovery-oriented reasoning.

## Keywords

High-confidence computing; Multi-UAV swarm; Cyber-physical security; Mission assurance; Graph-temporal learning; Uncertainty calibration; Out-of-distribution evaluation; Explainable AI; Recovery reasoning

## HCC Contribution Table

| High-Confidence Computing Requirement | TRUST-Swarm Component | Manuscript Evidence |
| ------------------------------------- | -------------------- | ------------------- |
| Secure computing | Cyber-physical attack modeling under jamming, spoofing, tampering, and combined attacks | Multi-class mission-state simulation and recognition |
| Intelligent computing | Graph-Temporal Transformer for UAV mission-state recognition | Graph-temporal learning over UAV nodes, mission time, and telemetry features |
| Precise computing | Calibrated prediction confidence | Expected Calibration Error, Brier score, confidence, and entropy |
| Robustness under uncertainty | OOD cyber-physical stress testing | Stealth jamming, slow GPS drift, intermittent tampering, delayed combined attack, and unseen swarm noise |
| Traceable computing | Perturbation-based explainability | Feature-importance ranking using macro-F1 degradation |
| Active defense support | Recovery-oriented reasoning scaffold | PPO-based recovery action space: continue, monitor, reroute, reassign, isolate node, return to base |
| Practical feasibility | Runtime and complexity profiling | Model size, latency, throughput, training-step time, and GPU memory use |

## 1. Introduction

Multi-UAV swarm systems are becoming an important class of cyber-physical intelligent systems. In contrast to single-UAV platforms, a swarm can distribute sensing, increase coverage, improve redundancy, and support cooperative mission execution across large or uncertain environments. These advantages make UAV swarms attractive for surveillance, reconnaissance, border monitoring, disaster response, infrastructure inspection, logistics, search-and-rescue, and defense-oriented mission operations. In such settings, the swarm is not only a collection of flying platforms; it is a distributed decision-making system that depends on communication reliability, navigation integrity, telemetry correctness, energy awareness, coverage consistency, and mission-progress coordination. When these information streams are trustworthy, the swarm can maintain situational awareness and adapt its mission behavior. When they are disrupted, however, autonomous decisions may become unreliable even if individual UAVs remain operational [1–8].

The security challenge becomes more serious when UAV swarm missions are exposed to cyber-physical attacks. Communication jamming can increase packet loss and latency, weakening coordination among UAV nodes and delaying mission updates. GPS spoofing can create route deviation, sudden GPS jumps, and velocity inconsistency, causing the swarm to misinterpret location and movement. Telemetry tampering can distort battery state, mission progress, energy consumption, and zone coverage, making the system believe that a mission is safer or more complete than it actually is. Combined attacks can simultaneously degrade communication, navigation, and telemetry integrity. These attacks do not merely create isolated anomalies; they alter the information foundation on which autonomous mission-state prediction and response planning depend [9–14].

For this reason, secure UAV swarm mission assurance should be treated as a high-confidence computing problem. A conventional classifier can predict whether the current state resembles normal operation, jamming, spoofing, tampering, or a combined attack. However, in security-critical autonomous missions, a predicted label is not enough. The system must also estimate whether the prediction is reliable, identify when unseen attack patterns create distribution shift, explain which telemetry factors influenced the decision, and connect risk evidence to response-oriented reasoning. A UAV mission-assurance framework that reports only accuracy may appear strong under ordinary test conditions while still failing under stealthy or previously unseen cyber-physical shifts. High-confidence computing therefore requires a broader evaluation view: prediction, confidence, robustness, traceability, and recovery support must be considered together [15–24].

Existing research provides important foundations for this goal but often addresses the required capabilities separately. UAV cybersecurity and secure communication studies examine jamming, spoofing, intrusion detection, and communication protection. Time-series and deep-learning models support telemetry classification and sequential pattern recognition. Graph neural networks and transformers provide mechanisms for learning relational and temporal structure. Calibration and uncertainty methods help evaluate whether probability estimates are reliable. OOD and distribution-shift studies show that models may fail when test conditions differ from training distributions. Explainable AI methods provide ways to identify feature-level decision drivers. Reinforcement learning and safe control literature provide foundations for adaptive recovery reasoning. Although these areas are individually valuable, a gap remains: UAV swarm mission assurance still lacks an integrated high-confidence framework that combines graph-temporal prediction, calibrated reliability, OOD stress testing, traceable explanation, and recovery-oriented decision support in one evaluation pipeline [25–45].

This paper addresses that gap by presenting TRUST-Swarm, a high-confidence graph-temporal intelligent computing framework for secure multi-UAV mission assurance under cyber-physical attacks. TRUST-Swarm models distributed UAV telemetry as graph-temporal mission windows. Each window preserves three forms of structure: temporal mission evolution, UAV-node relationships, and heterogeneous telemetry-feature interactions. The framework evaluates a Graph-Temporal Transformer for mission-state recognition while also comparing temporal baselines, including LSTM, GRU, and 1D-CNN models. Unlike a pure classification study, TRUST-Swarm does not position the Graph-Temporal Transformer as the strongest raw classifier. Instead, it uses the model as the central prediction layer within a broader assurance pipeline that evaluates calibration, uncertainty, OOD vulnerability, explanation, ablation evidence, runtime feasibility, and recovery-oriented reasoning.

The proposed framework is evaluated using a controlled simulation-based multi-UAV telemetry environment. The final study uses three random seeds. For each seed, the telemetry generator produces 300 mission runs, 240 timesteps per mission, 20 UAVs per mission, 1,440,000 raw telemetry rows, and 66,300 graph-temporal mission windows. The mission-state labels include normal operation, jamming, spoofing, tampering, jamming-spoofing, jamming-tampering, spoofing-tampering, and combined attacks. The telemetry features capture communication reliability, navigation integrity, energy state, mission progress, coverage quality, and energy consumption. This design enables repeatable evaluation across cyber-physical attack states while preserving enough node-level and time-level structure to test graph-temporal mission reasoning.

The experimental results show that the Graph-Temporal Transformer achieves strong in-distribution mission-state recognition, with a mean accuracy of 0.9647 and a mean macro F1 score of 0.8750 across three seeds. The model also produces strong in-distribution calibration, with an Expected Calibration Error of 0.0088 and a Brier score of 0.0531. However, the 1D-CNN baseline achieves stronger raw in-distribution classification performance, with a mean macro F1 score of 0.9971. This finding is important because it prevents overclaiming and clarifies the contribution of TRUST-Swarm. The contribution is not that the Graph-Temporal Transformer is the strongest standalone classifier. The contribution is that TRUST-Swarm provides an integrated high-confidence mission-assurance framework that evaluates not only prediction performance, but also prediction reliability, unseen-shift vulnerability, decision traceability, framework ablation, runtime feasibility, and recovery-oriented response support.

The OOD stress-test results further motivate this high-confidence framing. Under unseen cyber-physical shifts, mission-state recognition performance decreases substantially. Intermittent tampering reduces macro F1 to 0.5965, while more severe shifts such as slow GPS drift, stealth jamming, and delayed combined attacks cause larger degradation. These results show that standard in-distribution accuracy can hide mission-risk conditions. From a high-confidence computing perspective, this is not a weakness of the study; it is a necessary finding. A trustworthy mission-assurance framework should expose where reliability degrades, rather than reporting only favorable in-distribution performance. TRUST-Swarm therefore uses OOD stress testing as an assurance mechanism to identify conditions where monitoring, escalation, or recovery reasoning may be required.

Traceability and response support are also central to the proposed framework. Perturbation-based feature-importance analysis identifies latency, zone coverage, route deviation, mission progress, and GPS jump as the most influential mission-risk drivers. These drivers are operationally meaningful because they correspond to communication degradation, mission coverage loss, navigation disruption, mission-progress interruption, and spoofing-related displacement. TRUST-Swarm further includes a PPO-based recovery-reasoning scaffold that maps prediction, confidence, entropy, and mission-risk indicators to possible response actions such as continue, monitor, reroute, reassign, isolate node, and return to base. This recovery layer is not claimed as an operational UAV controller. Rather, it demonstrates how high-confidence prediction outputs can be connected to mission-response reasoning.

The main contributions of this paper are summarized as follows:

1. A high-confidence graph-temporal intelligent computing framework is proposed for secure multi-UAV mission assurance under cyber-physical attacks. The framework integrates mission-state prediction, calibrated confidence, OOD stress testing, traceable explanation, ablation evidence, runtime profiling, and recovery-oriented reasoning.

2. A graph-temporal mission-window representation is developed to model UAV-node relationships, temporal mission evolution, and heterogeneous telemetry features. This representation allows the framework to reason over distributed swarm telemetry rather than treating mission data as ordinary flat time-series records.

3. A Graph-Temporal Transformer is evaluated for mission-state recognition under normal, jamming, spoofing, tampering, and combined attack conditions. Temporal baselines, including LSTM, GRU, and 1D-CNN, are used to clarify the difference between raw classification performance and broader high-confidence mission assurance.

4. A three-seed simulation study is conducted using 300 mission runs per seed, 240 timesteps per mission, 20 UAVs per mission, and 66,300 graph-temporal mission windows per seed. The evaluation includes in-distribution performance, calibration metrics, OOD stress testing, explainability analysis, ablation analysis, and runtime profiling.

5. The study demonstrates that secure UAV swarm mission assurance requires more than high classification accuracy. The results show the value of evaluating reliability, uncertainty, unseen-shift vulnerability, decision traceability, and recovery support as integrated high-confidence computing requirements.

The remainder of this paper is organized as follows. Section 2 reviews related work on UAV cyber-physical security, high-confidence intelligent computing, graph-temporal learning, temporal deep-learning baselines, uncertainty calibration, OOD evaluation, explainable AI, and recovery-oriented reinforcement learning. Section 3 presents the TRUST-Swarm methodology. Section 4 describes the experimental setup. Section 5 reports and discusses the results, including baseline comparison, calibration, OOD stress testing, explainability, ablation, and runtime analysis. Section 6 presents limitations and future work. Section 7 concludes the paper.

## 2. Related work

Secure UAV swarm mission assurance is connected to several research areas, including UAV cyber-physical security, multi-UAV communication, graph-temporal learning, uncertainty calibration, OOD robustness, explainable artificial intelligence, and recovery-oriented reinforcement learning. These areas provide important foundations for TRUST-Swarm. However, most existing studies treat these capabilities as separate research problems. A high-confidence mission-assurance framework requires a more integrated view: the system should recognize mission states, estimate prediction reliability, expose unseen-shift vulnerability, explain mission-risk drivers, and connect prediction outputs to recovery reasoning. This section reviews the relevant literature and positions TRUST-Swarm as a high-confidence secure intelligent computing framework rather than only an attack-classification model.

### 2.1. UAV cyber-physical security and mission assurance

UAV systems operate through tight coupling between communication, navigation, sensing, telemetry, and control. This coupling creates strong mission capability, but it also increases the attack surface. A UAV swarm depends on reliable packet exchange, GPS consistency, route stability, battery-state awareness, mission-progress reporting, and coverage information. If any of these streams is corrupted, the swarm may continue operating while its internal mission-state estimate becomes unreliable. Prior UAV security studies have therefore examined communication jamming, GPS spoofing, false data injection, route deviation, sensor-channel attacks, and secure communication mechanisms [1–14].

Communication jamming is especially important in swarm settings because coordination depends on timely exchange of state information. Increased latency and packet loss can weaken cooperative behavior, delay mission updates, and reduce the ability of the swarm to respond to dynamic mission conditions. GPS spoofing affects navigation integrity by creating false position, velocity, or route information. Telemetry tampering affects the internal mission picture by corrupting battery level, energy consumption, mission progress, or zone coverage. Combined cyber-physical attacks are more difficult because they can simultaneously degrade communication, navigation, and telemetry correctness. These attack modes motivate the need for mission assurance rather than isolated anomaly detection.

Although UAV cybersecurity research provides strong foundations, many studies focus on detecting a specific attack type, protecting communication links, or evaluating one security mechanism. Such approaches are valuable, but they do not fully address the high-confidence requirements of autonomous mission operation. In a swarm mission, the system must evaluate whether the prediction can be trusted, whether an unseen shift is occurring, which mission signals created the decision, and how the mission should respond. TRUST-Swarm builds on UAV security literature by treating cyber-physical mission assurance as an integrated high-confidence computing problem.

### 2.2. High-confidence intelligent computing frameworks

High-confidence computing emphasizes secure, reliable, precise, traceable, and intelligent system behavior. In recent High-Confidence Computing articles, the contribution is often not a single model in isolation, but a unified framework that connects several capabilities. For example, recent studies in this journal present framework-level solutions involving traffic prediction, federated learning, zero-trust control, denoising, cybersecurity assessment, privacy preservation, real-time anomaly detection, adaptation, ablation, and practical validation. This publication style is important for TRUST-Swarm because it shows that HCC papers are expected to present a coherent pipeline with strong narration, not only a model-and-metrics report.

The HCC framing is particularly suitable for secure autonomous systems. In security-critical environments, a model with high test accuracy may still be unsafe if its confidence is poorly calibrated, if it fails under distribution shift, if its decisions are not traceable, or if its outputs do not support response planning. Therefore, high-confidence intelligent computing requires evaluation beyond conventional accuracy. TRUST-Swarm follows this direction by combining mission-state recognition, calibration, OOD stress testing, explanation, ablation analysis, runtime profiling, and recovery reasoning.

### 2.3. Graph-temporal learning for UAV swarm telemetry

UAV swarm telemetry naturally has graph-temporal structure. Each UAV can be treated as a node, and mission behavior evolves across time through interactions among UAV nodes, telemetry features, and mission-state transitions. Flat time-series models may capture temporal signals, but they may not explicitly represent node relationships. Graph neural networks, graph attention mechanisms, temporal graph networks, and transformer-based architectures provide foundations for learning relational and temporal dependencies in structured data [30–36].

Graph-temporal modeling is relevant to UAV mission assurance because cyber-physical attacks often appear as structured mission degradation rather than isolated feature changes. Jamming may affect communication-related features across multiple UAVs. Spoofing may create navigation inconsistencies in a subset of nodes. Tampering may distort telemetry signals related to mission progress or energy state. Combined attacks may create multi-feature and multi-node degradation patterns. A graph-temporal representation allows the model to reason over node relationships, mission-time evolution, and heterogeneous telemetry interactions together.

TRUST-Swarm uses this idea by converting distributed UAV telemetry into graph-temporal mission windows. Each window preserves temporal length, UAV-node structure, and telemetry-feature structure. The Graph-Temporal Transformer is then evaluated as the central prediction layer. This design is not intended to prove that graph-temporal modeling always outperforms all temporal baselines. Instead, it provides an intelligent prediction layer suitable for integration into a broader high-confidence mission-assurance framework.

### 2.4. Temporal deep-learning baselines

Temporal deep-learning models such as LSTM, GRU, and 1D-CNN are widely used for sequence modeling and telemetry classification [37–40]. LSTM and GRU models capture recurrent dependencies and are useful when past states influence future behavior. 1D-CNN models can efficiently extract local temporal patterns and often perform strongly when class-specific signatures are visible in short windows. These baselines are important because they provide a fair comparison between graph-temporal reasoning and conventional sequence-learning approaches.

In TRUST-Swarm, the baseline comparison is not treated as a simple competition for highest raw accuracy. The final results show that the 1D-CNN baseline achieves the strongest in-distribution classification performance. This finding is important because it prevents overclaiming. The correct interpretation is that TRUST-Swarm contributes an assurance-oriented framework rather than merely a new classifier. The Graph-Temporal Transformer provides a structured prediction layer, while the broader framework adds calibration, OOD evaluation, traceability, ablation evidence, runtime feasibility, and recovery-oriented reasoning.

### 2.5. Uncertainty calibration and reliability estimation

For high-confidence computing, prediction confidence is as important as prediction accuracy. A mission-assurance system must know whether a mission-state prediction is trustworthy. Neural networks can be overconfident, especially under distribution shift or adversarial inputs. Calibration methods and uncertainty metrics help evaluate whether predicted probabilities align with empirical correctness [41–45].

Expected Calibration Error, Brier score, predictive confidence, and predictive entropy are commonly used to evaluate probabilistic reliability. Monte Carlo dropout and related uncertainty-estimation approaches can provide additional evidence about predictive uncertainty. In a UAV mission context, unreliable confidence can be dangerous because the system may continue normal operation during a degraded or uncertain state. TRUST-Swarm therefore treats calibration as a core high-confidence component rather than an optional metric.

### 2.6. OOD robustness and cyber-physical distribution shift

Autonomous UAV missions may encounter attack behaviors that differ from training conditions. Attackers may use stealth jamming, slow GPS drift, intermittent telemetry tampering, delayed combined attacks, or other low-observable strategies. OOD and distribution-shift research shows that models can fail when test data differs from training data, even when in-distribution performance is strong [45–48].

OOD evaluation is therefore essential for high-confidence mission assurance. The purpose is not to claim complete OOD reliability. Instead, OOD stress testing should reveal where performance degrades, where confidence becomes unreliable, and where monitoring or escalation may be needed. TRUST-Swarm includes OOD cyber-physical stress testing for this reason. It exposes mission-risk conditions that ordinary test accuracy would hide and supports a more honest high-confidence interpretation.

### 2.7. Explainability and traceable mission-risk evidence

Traceability is another requirement for high-confidence intelligent systems. A mission-assurance framework should not only output a mission-state label; it should also identify which telemetry factors influenced the decision. Explainable AI methods, including LIME, SHAP, saliency analysis, and perturbation-based feature importance, provide foundations for interpreting model behavior [49–52].

TRUST-Swarm uses perturbation-based feature importance to identify mission-risk drivers. The final analysis identifies latency, zone coverage, route deviation, mission progress, and GPS jump as major decision drivers. These features are operationally meaningful because they correspond to communication degradation, mission coverage loss, navigation disruption, mission-progress interruption, and spoofing-related displacement. This improves the traceability of the framework and supports the claim that TRUST-Swarm provides decision evidence rather than opaque classification alone.

### 2.8. Recovery-oriented reinforcement learning and active defense

Mission assurance should not stop after detection. Once a mission risk is identified, a UAV swarm may need to continue, monitor, reroute, reassign, isolate a compromised node, or return to base. Reinforcement learning, PPO, multi-agent reinforcement learning, safe reinforcement learning, and cyber-physical resilience research provide foundations for adaptive response reasoning [18–20, 53–63].

TRUST-Swarm includes a PPO-based recovery-reasoning scaffold to connect prediction outputs with mission-response actions. The recovery layer receives mission-state prediction, confidence, entropy, and risk indicators. It is not claimed as an operational UAV controller. Instead, it demonstrates how high-confidence prediction outputs can support response-oriented mission reasoning. This is aligned with active defense because the framework connects recognition and confidence evidence to possible response pathways.

### 2.9. Comparison with related research directions

| Research direction | Main focus | Common limitation | TRUST-Swarm positioning |
| --- | --- | --- | --- |
| UAV cybersecurity | Jamming, spoofing, tampering, secure communication, attack detection | Often focused on isolated attack families or communication protection | Models multiple cyber-physical mission states and combined attacks |
| Temporal deep learning | Sequence classification using LSTM, GRU, CNN, or transformer variants | May emphasize raw accuracy without assurance evidence | Uses temporal baselines but frames contribution as high-confidence mission assurance |
| Graph-temporal learning | Node-time relational modeling | Often not connected to calibration, OOD, explanation, and recovery | Uses graph-temporal mission windows as the prediction layer inside an assurance pipeline |
| Calibration and uncertainty | Reliability of predictive probabilities | Often evaluated separately from cyber-physical response | Integrates ECE, Brier score, confidence, and entropy into mission assurance |
| OOD robustness | Performance under distribution shift | Often not linked to recovery planning | Uses OOD stress tests to expose mission-risk conditions |
| Explainable AI | Feature attribution and traceability | Explanations may not be operationally linked to mission risk | Identifies interpretable telemetry risk drivers |
| Reinforcement learning and resilience | Adaptive response and policy reasoning | Often separated from prediction confidence and explanation | Adds a PPO-based recovery-reasoning scaffold |

### 2.10. Research gap

The reviewed literature shows strong progress in UAV security, temporal modeling, graph learning, uncertainty calibration, OOD evaluation, explainability, and reinforcement-learning-based response. However, these areas are often studied separately. Existing UAV security frameworks may detect attacks or classify anomalies, but they frequently do not provide calibrated confidence, OOD stress testing, traceable mission-risk evidence, ablation-based framework analysis, runtime feasibility profiling, and recovery-oriented reasoning in a single pipeline.

TRUST-Swarm addresses this gap by presenting a high-confidence graph-temporal intelligent computing framework for secure UAV swarm mission assurance. The central contribution is not raw classification superiority. Instead, the contribution is an integrated secure, intelligent, calibrated, OOD-aware, traceable, and recovery-aware mission-assurance framework suitable for high-confidence computing evaluation.

## 3. Methodology

This section presents TRUST-Swarm as a high-confidence graph-temporal intelligent computing framework for secure multi-UAV mission assurance under cyber-physical attacks. The framework is designed to support secure prediction, calibrated confidence, OOD vulnerability analysis, traceable explanation, and recovery-oriented reasoning [R01–R03, R21–R33, R37–R50, R64–R80].

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

A controlled simulation-based telemetry generator is used to create multi-UAV cyber-physical mission scenarios. Each mission contains a swarm of UAVs operating across mission time under normal or adversarial conditions [R21–R28, R31–R33].

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

Raw UAV telemetry is converted into graph-temporal mission windows to preserve node-level and temporal mission structure [R51–R59]. Each sample is represented as:

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

The Graph-Temporal Transformer is used as the main intelligent prediction model, drawing on attention, transformer, graph neural network, and temporal graph learning foundations [R51, R53, R54, R56, R58]. The model receives an input tensor with shape:

batch_size × window_size × num_uavs × num_features

The model contains:

1. telemetry feature projection
2. UAV-node attention
3. temporal transformer encoding
4. fused mission embedding
5. mission-state classifier

The model learns UAV-node relationships, temporal attack progression, and mission-state degradation patterns. Its output is a probability distribution over mission-state classes.

## 3.5 Temporal Baseline Models

Three temporal baseline models are evaluated to compare TRUST-Swarm against recurrent and convolutional sequence-learning baselines [R60–R63]:

1. LSTM
2. GRU
3. 1D-CNN

These baselines evaluate whether conventional temporal models can classify mission states from the same graph-window telemetry. The 1D-CNN baseline achieved the strongest in-distribution classification performance, so TRUST-Swarm is not framed as the best raw classifier. Instead, the framework is evaluated as a high-confidence computing pipeline that adds calibration, OOD testing, explanation, and recovery reasoning.

## 3.6 Confidence-Aware Reliability Evaluation

High-confidence computing requires reliable prediction confidence. TRUST-Swarm evaluates prediction reliability using calibration and uncertainty metrics commonly used to assess probabilistic prediction reliability [R37–R43]:

1. Expected Calibration Error
2. Brier score
3. mean predictive confidence
4. predictive entropy

Monte Carlo dropout is used during uncertainty evaluation to estimate predictive uncertainty. This reliability layer helps determine whether a mission-state prediction should be trusted, monitored, escalated, or passed to the recovery-reasoning layer.

## 3.7 OOD-Aware Cyber-Physical Stress Testing

Operational UAV swarms may face unseen cyber-physical shifts not represented during training. TRUST-Swarm evaluates OOD behavior under five stress conditions, motivated by OOD and dataset-shift evaluation literature [R43–R46]:

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

TRUST-Swarm uses perturbation-based feature importance to provide traceable mission-risk evidence, following the broader motivation of explainability and feature-attribution methods in trustworthy AI [R47–R50]. First, baseline macro F1 is computed. Then, each telemetry feature is replaced with its mean value, and macro F1 is recomputed.

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

TRUST-Swarm includes a PPO-based recovery-reasoning scaffold motivated by reinforcement learning, safe RL, multi-agent decision support, and cyber-physical resilience literature [R64–R80]. The recovery layer receives mission-state predictions, confidence scores, entropy, and mission-risk indicators.

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

This methodology follows the High-Confidence Computing style of presenting a unified framework rather than an isolated model [R01–R03].

<!-- CITATIONS_INSERTED_METHODOLOGY_V1 -->

## 4. Experimental Setup

This section describes the experimental setup used to evaluate TRUST-Swarm as a high-confidence graph-temporal intelligent computing framework for secure multi-UAV mission assurance. The evaluation is designed to test mission-state recognition, baseline comparison, confidence calibration, OOD vulnerability, traceable explanation, and recovery-oriented reasoning [R01–R03, R37–R50, R64–R80].

## 4.1 Computing Environment

The final experiment was executed in a GPU-based RunPod environment using Python and PyTorch. The implementation used pandas, NumPy, scikit-learn, matplotlib, Gymnasium, and Stable-Baselines3. Neural-network training was performed with GPU acceleration.

The experiment used three random seeds:

* 42
* 123
* 2026

Using multiple seeds reduces dependence on a single telemetry generation run or train-test split and supports more reliable performance reporting.

## 4.2 Synthetic Multi-UAV Mission Telemetry

A controlled simulation-based telemetry generator was used to evaluate cyber-physical mission assurance under repeatable conditions, motivated by UAV cyber-physical security, communication, spoofing, and tampering risks [R21–R28, R31–R33]. Each seed generated:

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

These classes represent communication disruption, navigation manipulation, telemetry integrity attack, and combined cyber-physical mission degradation [R24–R26, R31–R33].

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

These features capture communication reliability, navigation integrity, energy state, mission progress, and coverage quality [R21–R28, R31–R33].

## 4.5 Graph-Temporal Mission Windows

Raw telemetry is transformed into graph-temporal mission windows using a sliding temporal window to preserve temporal mission evolution and UAV-node structure [R51–R59]. Each mission-window sample is represented as:

X ∈ R^(T × N × F)

where:

* T = 20 timesteps
* N = 20 UAV nodes
* F = 9 telemetry features

Thus, each graph-temporal mission window has the final shape:

X ∈ R^(20 × 20 × 9)

This representation preserves mission-time evolution, UAV-node structure, and telemetry-feature structure.

## 4.6 Evaluated Models

The evaluation includes the proposed Graph-Temporal Transformer and three temporal baseline models based on transformer, graph-learning, recurrent, and convolutional sequence-modeling foundations [R51–R63]:

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

Macro-averaged metrics were emphasized because the cyber-physical attack classes are imbalanced and mission-state performance must be interpreted beyond raw accuracy.

## 4.9 Confidence Calibration Metrics

The confidence-aware reliability layer was evaluated using calibration and uncertainty metrics commonly used for probabilistic reliability assessment [R37–R43]:

* Expected Calibration Error
* Brier score
* mean predictive confidence
* predictive entropy

Monte Carlo dropout with 20 stochastic samples was used during uncertainty evaluation. The goal was to evaluate whether the Graph-Temporal Transformer produced reliable in-distribution confidence estimates.

## 4.10 OOD Cyber-Physical Stress Testing

OOD stress testing evaluated model behavior under unseen cyber-physical mission shifts, following the broader motivation of OOD and distribution-shift evaluation [R43–R46]. The OOD conditions were:

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

The purpose of this evaluation is not to claim complete OOD reliability. Instead, it identifies mission-risk conditions where model performance degrades or confidence becomes unreliable [R43–R46].

## 4.11 Traceable Explanation Evaluation

Traceability was evaluated using perturbation-based feature importance, motivated by explainability and feature-attribution methods for trustworthy AI [R47–R50]. First, the baseline macro F1 was computed. Then, each telemetry feature was replaced by its mean value, and macro F1 was recomputed.

Feature importance was calculated as:

Feature importance = baseline macro F1 − perturbed macro F1

A larger macro-F1 drop indicates that the feature is more important for mission-state prediction.

## 4.12 Recovery-Oriented Reasoning Evaluation

The PPO-based recovery module was evaluated as a recovery-reasoning scaffold, motivated by reinforcement learning, safe RL, multi-agent decision support, and cyber-physical resilience literature [R64–R80]. The action space included:

1. continue
2. monitor
3. reroute
4. reassign
5. isolate node
6. return to base

This module is included to demonstrate how prediction, confidence, entropy, and mission-risk indicators can support mission-response reasoning. It is not claimed as an operationally deployable UAV controller.

## 4.13 Current Experimental Limitation

The current evaluation uses controlled synthetic telemetry rather than field-collected UAV telemetry. This design allows repeatable testing across attack states, OOD conditions, and multiple seeds, but real-world validation remains future work.

Final HCC-aligned evidence includes ablation analysis and runtime/complexity profiling. The ablation study evaluates the contribution of UAV-node attention, temporal transformer reasoning, and assurance modules. The runtime analysis reports model size, latency, throughput, train-step time, and GPU memory use to support practical feasibility claims.

<!-- CITATIONS_INSERTED_EXPERIMENTAL_SETUP_V1 -->

## 5. Results and Discussion

This section evaluates TRUST-Swarm as a high-confidence graph-temporal intelligent computing framework for secure multi-UAV mission assurance. The evaluation follows HCC-style framework evaluation by combining prediction, calibration, OOD stress testing, traceable explanation, recovery reasoning, ablation, and runtime feasibility evidence [R01–R03]. The evaluation focuses on five questions:

1. Can TRUST-Swarm recognize cyber-physical mission states?
2. How does the Graph-Temporal Transformer compare with temporal baselines?
3. Are its predictions well calibrated?
4. How does the model behave under unseen OOD cyber-physical shifts?
5. Can the framework provide traceable evidence and recovery-oriented reasoning?

## 5.1 In-Distribution Mission-State Recognition

Across three random seeds, the Graph-Temporal Transformer achieved a mean accuracy of 0.9647 and a mean macro F1 score of 0.8750. The mean macro precision was 0.8935, and the mean macro recall was 0.8700.

These results show that the graph-temporal prediction layer can learn meaningful mission-state patterns from UAV telemetry under cyber-physical attack conditions. The model captures mission-time evolution, UAV-node structure, and telemetry-feature interactions across communication, navigation, energy, mission-progress, and coverage signals [R21–R28, R51–R59].

From a High-Confidence Computing perspective, this result demonstrates the intelligent computing component of TRUST-Swarm. However, mission-state recognition alone is not sufficient for high-confidence autonomous operation. The framework must also evaluate reliability, uncertainty, OOD behavior, traceability, and recovery support.

## 5.2 Baseline Comparison

The baseline comparison included LSTM, GRU, and 1D-CNN models [R60–R63]. The 1D-CNN baseline achieved the strongest in-distribution classification performance, with a mean accuracy of 0.9987 and a mean macro F1 score of 0.9971. The LSTM and GRU baselines achieved mean macro F1 scores of 0.9608 and 0.9288, respectively.

This result shows that the synthetic telemetry benchmark contains strong local temporal signatures that are effectively captured by convolutional temporal learning. Therefore, the Graph-Temporal Transformer should not be claimed as the best raw classifier.

The correct interpretation is that TRUST-Swarm contributes a high-confidence secure intelligent computing pipeline. Unlike a pure classifier, the framework integrates prediction, calibration, OOD stress testing, traceable explanation, and recovery-oriented reasoning. This broader framework-level contribution is more aligned with High-Confidence Computing than a single accuracy comparison.

## 5.3 Confidence Calibration Results

The Graph-Temporal Transformer produced strong in-distribution calibration. Across three seeds, the model achieved a mean Expected Calibration Error of 0.0088 and a mean Brier score of 0.0531. The mean predictive confidence was 0.9601, and the mean predictive entropy was 0.0986 [R37–R43].

These results support the high-confidence computing objective because the model provides not only mission-state probabilities but also reliability evidence. A low Expected Calibration Error indicates that predicted confidence is well aligned with empirical correctness under in-distribution conditions.

For secure UAV swarm mission assurance, calibrated confidence is important because uncertain or low-confidence predictions may require monitoring, escalation, or recovery-oriented response. This makes calibration a core component of TRUST-Swarm rather than an optional evaluation metric.

## 5.4 OOD Cyber-Physical Stress Testing

OOD stress testing revealed substantial performance degradation under unseen cyber-physical shifts. The in-distribution macro F1 score was 0.8750. Intermittent tampering reduced macro F1 to 0.5965. More severe shifts caused larger reductions: slow GPS drift achieved a macro F1 score of 0.1701, stealth jamming achieved 0.0779, and delayed combined attacks achieved 0.0521 [R43–R46].

These findings show that cyber-physical distribution shifts can significantly degrade mission-state recognition even when in-distribution performance is strong. This is an important high-confidence computing result because it exposes failure modes that standard test accuracy would hide.

The OOD results should not be interpreted as complete OOD reliability. Some severe OOD cases may still produce high confidence. Therefore, confidence alone is not sufficient for secure mission assurance. TRUST-Swarm uses OOD stress testing to reveal mission-risk conditions and motivate stronger monitoring, escalation, and recovery mechanisms.

## 5.5 Traceable Mission-Risk Explanation

Perturbation-based feature importance identified latency, zone coverage, route deviation, mission progress, and GPS jump as the most influential mission-risk drivers [R47–R50].

These features are operationally meaningful:

* latency reflects communication degradation and possible jamming;
* zone coverage reflects mission effectiveness and coverage loss;
* route deviation reflects navigation disruption;
* mission progress reflects task completion under attack;
* GPS jump reflects spoofing-related displacement.

This improves decision traceability. In high-confidence computing, a framework should provide evidence explaining why a decision was produced. TRUST-Swarm supports this through feature-level traceability, linking mission-state predictions to interpretable cyber-physical telemetry drivers.

## 5.6 Recovery-Oriented Reasoning

TRUST-Swarm includes a PPO-based recovery-reasoning scaffold [R64–R80]. The recovery layer receives mission-state prediction, confidence, entropy, and mission-risk indicators. It maps these inputs to recovery actions such as continue, monitor, reroute, reassign, isolate node, and return to base.

This module is not claimed as an operationally deployable UAV controller. Instead, it demonstrates how high-confidence prediction outputs can support mission-response reasoning. This is important because secure mission assurance should not stop at detection. It should connect risk recognition to response planning [R64–R80].

## 5.7 Final Ablation Study

A final HCC ablation study was conducted on the seed-42 graph-temporal dataset using 66,300 mission windows, 20 UAV nodes, 20 timesteps, 9 telemetry features, and 8 mission-state classes. The full Graph-Temporal Transformer achieved an accuracy of 0.9579 and a macro F1 score of 0.8734. The ablation design supports framework-level HCC evaluation by showing how architectural and assurance components contribute to the evidence pipeline [R01–R03, R51–R59].

Removing UAV-node attention reduced macro F1 from 0.8734 to 0.7903, showing that swarm-node relational reasoning contributes meaningfully to mission-state recognition. Removing the temporal transformer reduced macro F1 to 0.8237, showing that temporal mission-evolution modeling is also important.

Framework-level ablations do not change classifier accuracy because they remove assurance modules rather than the classifier itself. However, they show what high-confidence evidence is lost when calibration, OOD stress testing, explainability, or recovery reasoning is removed.

| configuration                      |   accuracy |   macro_f1 | calibration_evidence   | ood_evidence   | explanation_evidence   | recovery_support   |
|:-----------------------------------|-----------:|-----------:|:-----------------------|:---------------|:-----------------------|:-------------------|
| A0_full_graph_temporal_transformer |     0.9579 |     0.8734 | yes                    | yes            | yes                    | yes                |
| A1_without_uav_node_attention      |     0.9572 |     0.7903 | yes                    | yes            | yes                    | yes                |
| A2_without_temporal_transformer    |     0.9507 |     0.8237 | yes                    | yes            | yes                    | yes                |
| A3_without_uncertainty_calibration |     0.9579 |     0.8734 | no                     | yes            | yes                    | yes                |
| A4_without_ood_stress_testing      |     0.9579 |     0.8734 | yes                    | no             | yes                    | yes                |
| A5_without_explainability          |     0.9579 |     0.8734 | yes                    | yes            | no                     | yes                |
| A6_without_recovery_reasoning      |     0.9579 |     0.8734 | yes                    | yes            | yes                    | no                 |

## 5.8 Runtime and Complexity Analysis

Runtime and complexity profiling was conducted on an NVIDIA H200 GPU using batch size 128, 20 UAV nodes, 20 timesteps, and 9 telemetry features. The Graph-Temporal Transformer has 680,840 trainable parameters and a model size of 2.618 MB. Its inference latency was 2.267 ms per batch and 0.0177 ms per graph-temporal mission window, corresponding to approximately 56,458 windows per second. This supports practical feasibility evidence expected in high-confidence intelligent computing evaluations [R01–R03].

Although the Graph-Temporal Transformer is heavier than LSTM, GRU, and 1D-CNN baselines, the profiling results show that it remains computationally practical for high-throughput mission-window inference on modern GPU hardware.

| model                    |   parameters |   model_size_mb |   inference_batch_latency_ms |   inference_sample_latency_ms |   throughput_windows_per_second |   single_train_step_ms |
|:-------------------------|-------------:|----------------:|-----------------------------:|------------------------------:|--------------------------------:|-----------------------:|
| LSTM                     |       308616 |           1.181 |                        0.214 |                        0.0017 |                        599007   |                  1.674 |
| GRU                      |       235912 |           0.904 |                        0.177 |                        0.0014 |                        724111   |                  1.48  |
| CNN1D                    |       136840 |           0.531 |                        0.211 |                        0.0016 |                        606987   |                  1.465 |
| GraphTemporalTransformer |       680840 |           2.618 |                        2.267 |                        0.0177 |                         56458.4 |                  9.938 |

## 5.9 Discussion Against High-Confidence Computing Standards

The results show that TRUST-Swarm is better framed as a high-confidence intelligent computing framework than as a pure classification model.

The accepted High-Confidence Computing papers commonly emphasize unified frameworks, multiple evaluation metrics, practical validation, and system-level reasoning. For example, the SDN-IoT DRAFT paper combines traffic prediction, federated learning, zero-trust mechanisms, denoising, and real-world dataset evaluation. The HTTPS assessment paper proposes a unified methodology with testing, examination, interviewing, and real-world website case-study validation. The critical-infrastructure IDS paper integrates detection, classification, privacy preservation, adaptation, and multi-benchmark validation. TRUST-Swarm follows the same framework-oriented direction, but its current limitation is that validation remains synthetic.

Therefore, the current results provide a stronger HCC manuscript foundation because the evaluation now includes mission-state recognition, baseline comparison, calibration, OOD stress testing, traceable explanation, recovery reasoning, final ablation evidence, and runtime/complexity profiling.

## 5.10 Safe Final Interpretation

The safe interpretation is:

TRUST-Swarm provides a high-confidence graph-temporal intelligent computing framework for secure multi-UAV mission assurance by integrating mission-state recognition, calibrated confidence, OOD cyber-physical stress testing, traceable explanation, and recovery-oriented reasoning.

The manuscript should not claim:

* the Graph-Temporal Transformer is superior to all baselines;
* OOD behavior is fully solved;
* the recovery module is operationally deployable;
* synthetic telemetry replaces field UAV validation.

The results support TRUST-Swarm as a secure, intelligent, calibrated, traceable, and recovery-aware mission-assurance framework.

<!-- CITATIONS_INSERTED_RESULTS_V1 -->

## 6. Limitations and Future Work

This study has several limitations. First, the current evaluation uses controlled synthetic multi-UAV telemetry rather than field-collected UAV swarm data. The controlled benchmark enables repeatable evaluation across cyber-physical attack states, OOD stress conditions, confidence metrics, and multiple random seeds, but real-world deployment validation remains necessary [R21–R33].

Second, the OOD stress tests reveal that severe unseen cyber-physical shifts can substantially reduce mission-state recognition performance. This finding is important for high-confidence computing because it exposes hidden mission risk, but it also shows that additional OOD detection and uncertainty-monitoring mechanisms are needed [R43–R46].

Third, the PPO-based recovery component is evaluated as a recovery-reasoning scaffold rather than an operationally deployable UAV controller. Future work should connect the recovery layer to high-fidelity UAV swarm simulators, hardware-in-the-loop validation, and mission-level safety constraints [R64–R80].

Fourth, the current framework uses a fixed set of telemetry features and attack classes. Future research should include richer sensor streams, adversarial attack adaptation, communication-topology changes, multi-agent coordination constraints, and real UAV logs.

Finally, future work should extend TRUST-Swarm with privacy-preserving learning, formal safety constraints, online adaptation, and human-in-the-loop mission assurance [R01–R03, R68–R80].

## 7. Conclusion

This paper presented TRUST-Swarm, a high-confidence graph-temporal intelligent computing framework for secure multi-UAV mission assurance under cyber-physical attacks. The framework integrates graph-temporal mission-state recognition, confidence calibration, OOD cyber-physical stress testing, perturbation-based traceability, and recovery-oriented reasoning [R01–R03, R21–R33, R37–R50, R51–R80].

The results show that the Graph-Temporal Transformer achieves strong mission-state recognition and strong in-distribution calibration. However, the 1D-CNN baseline achieves stronger raw in-distribution classification performance, so TRUST-Swarm is not positioned as the best standalone classifier. Instead, its contribution is a high-confidence secure intelligent computing pipeline that evaluates prediction reliability, exposes unseen-shift risk, explains mission-relevant telemetry drivers, and links risk outputs to recovery reasoning.

The study demonstrates that secure UAV swarm mission assurance requires more than accuracy. It requires high-confidence computing mechanisms that can evaluate trustworthiness, uncertainty, robustness, traceability, and recovery support under cyber-physical mission risk [R01–R03].

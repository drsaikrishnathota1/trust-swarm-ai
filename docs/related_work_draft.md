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


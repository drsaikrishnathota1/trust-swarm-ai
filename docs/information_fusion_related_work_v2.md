# Information Fusion Related Work v2

## 2. Related Work

This section reviews prior work related to UAV swarm mission assurance, cyber-physical UAV attacks, graph-temporal learning, multi-source information fusion, uncertainty calibration, OOD evaluation, explainability, and recovery-oriented reinforcement learning.

## 2.1 UAV Swarm Mission Assurance

UAV swarms provide distributed sensing, wide-area coverage, redundancy, and cooperative mission execution. These properties make them attractive for surveillance, reconnaissance, disaster response, infrastructure monitoring, and defense-oriented missions. However, swarm autonomy also creates mission-assurance challenges because the mission state depends on multiple UAV nodes, communication links, navigation signals, energy constraints, coverage progress, and operator objectives.

Prior UAV security and mission-assurance studies have examined UAS risks, sensor-channel threats, UAV-enabled systems, and cyber-physical vulnerabilities [1, 2, 34–37]. These works motivate the need for resilient monitoring and assurance mechanisms. However, many existing approaches focus on individual attack detection or secure communication rather than integrated mission-state fusion across heterogeneous telemetry sources.

## 2.2 Cyber-Physical Attacks on UAV Swarms

UAV swarms are exposed to cyber-physical attacks that can corrupt or degrade mission information streams. Communication jamming can increase latency and packet loss. GPS or GNSS spoofing can distort localization, route tracking, and velocity consistency. Telemetry tampering can manipulate mission progress, energy reporting, or coverage status. Combined attacks can affect multiple information channels simultaneously.

Prior work has studied GPS spoofing detection, cooperative swarm spoofing mitigation, UAV anti-jamming communication, and adversarial UAV planning [3, 4, 38–47]. These studies show that UAV mission assurance requires reasoning over communication, navigation, and mission-integrity signals together. TRUST-Swarm builds on this direction by modeling mission assurance as a graph-temporal multi-source fusion problem rather than only a single-attack classification task.

## 2.3 Multi-Source Information Fusion for Mission Awareness

Information fusion is central to autonomous mission awareness because a single sensor or telemetry source rarely provides sufficient evidence for reliable mission-state estimation. In UAV swarms, mission state must be inferred by combining communication telemetry, navigation behavior, energy state, coverage status, and mission-progress indicators.

Traditional fusion approaches often focus on combining sensor measurements or improving state estimation. In contrast, TRUST-Swarm focuses on cyber-physical mission-assurance fusion, where telemetry streams may be adversarially corrupted or distribution-shifted. The framework operationalizes multi-source fusion by representing UAV telemetry as graph-temporal fusion windows and evaluating fused predictions using classification, calibration, OOD stress testing, explainability, and recovery reasoning.

## 2.4 Graph-Temporal Learning for UAV Swarms

UAV swarms naturally form dynamic graph systems. UAVs can be represented as nodes, while communication, proximity, coordination, or shared mission context can define relationships. Graph neural networks, graph attention models, and graph-temporal approaches are therefore well suited for learning relational dependencies in multi-agent systems [5–10].

Transformers and temporal models provide additional support for capturing long-range mission evolution and temporal dependencies [11–13]. TRUST-Swarm combines these ideas by using a Graph-Temporal Transformer to learn both UAV-node relationships and mission-time evolution from graph-temporal fusion windows.

## 2.5 Temporal Deep Learning Baselines

Temporal deep learning models such as LSTM, GRU, and 1D-CNN are common baselines for sequence classification and telemetry analysis [14–17]. LSTM and GRU models capture recurrent temporal dependencies, while 1D-CNN models capture local temporal signatures efficiently.

In TRUST-Swarm, these models are used to evaluate whether conventional temporal models can classify mission-state patterns from the same telemetry windows. The strong 1D-CNN result shows that local temporal signatures are highly informative in the current synthetic telemetry setting. This supports the need for careful claim positioning: TRUST-Swarm should be presented as a trustworthy information-fusion framework, not merely as the highest-accuracy classifier.

## 2.6 Uncertainty Calibration for High-Confidence Fusion

High-confidence mission assurance requires calibrated confidence estimates. A UAV swarm model may produce a correct or incorrect mission-state prediction, but the mission-assurance layer also needs to know whether that prediction is reliable. Prior work on neural-network calibration, MC dropout, deep ensembles, and uncertainty under dataset shift provides the foundation for confidence-aware learning [18–24].

TRUST-Swarm evaluates calibration using Expected Calibration Error, Brier score, predictive confidence, and predictive entropy. This supports confidence-aware fusion because the framework evaluates not only what mission state is predicted, but also how trustworthy the fused prediction is under in-distribution conditions.

## 2.7 OOD Evaluation and Distribution Shift

Autonomous UAV missions may encounter unseen cyber-physical conditions that differ from training data. Attackers may use stealth jamming, slow GPS drift, intermittent tampering, delayed combined attacks, or noise patterns that were not observed during model training. Prior OOD and distribution-shift studies show that models can fail under shifted inputs even when they perform well in-distribution [22, 25–28, 54, 55].

TRUST-Swarm includes OOD-aware fusion stress testing to evaluate how fused mission-state predictions behave under unseen cyber-physical shifts. This is important because high in-distribution accuracy does not guarantee reliable mission assurance under adversarial or unfamiliar operating conditions.

## 2.8 Explainability for Fusion-Driver Analysis

Explainability is important for mission assurance because operators and downstream recovery modules need to understand which telemetry sources influenced a prediction. Prior explainable AI methods such as LIME, SHAP, saliency evaluation, and XAI frameworks support interpretation of model decisions [29–32].

TRUST-Swarm uses perturbation-based feature importance to identify fusion drivers. The analysis reveals whether the model relies on operationally meaningful telemetry sources such as latency, zone coverage, route deviation, mission progress, and GPS jump. This improves trust because the fused prediction can be linked back to mission-relevant evidence.

## 2.9 Recovery-Oriented Reinforcement Learning

Mission assurance should not stop at mission-state prediction. When a risk is detected, a UAV swarm may need to continue, monitor, reroute, reassign, isolate a node, or return to base. Reinforcement learning, PPO, and multi-agent reinforcement learning provide foundations for adaptive mission planning and recovery-oriented reasoning [33, 48–53].

TRUST-Swarm includes a PPO-based recovery scaffold to demonstrate how fused mission-state predictions and confidence signals can support downstream mission-assurance decisions. The current recovery component is not a deployment-ready controller, but it provides an initial bridge between trustworthy information fusion and recovery reasoning.

## 2.10 Research Gap

The literature includes strong work on UAV security, cyber-physical attacks, graph learning, temporal modeling, uncertainty estimation, OOD detection, explainability, and reinforcement learning. However, these areas are often studied separately. Existing UAV security systems may detect attacks, but they often do not integrate multi-source telemetry fusion, graph-temporal mission modeling, calibrated confidence, OOD stress testing, fusion-driver explainability, and recovery reasoning in one pipeline.

TRUST-Swarm addresses this gap by presenting a trustworthy graph-temporal multi-source information fusion framework for UAV swarm mission assurance. The framework evaluates not only mission-state classification, but also confidence reliability, unseen-shift vulnerability, telemetry-source importance, and recovery-oriented decision support.


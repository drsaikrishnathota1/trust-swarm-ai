# Information Fusion Related Work v3

## 2. Related Work

This section reviews prior work related to UAV swarm mission assurance, cyber-physical UAV attacks, multi-source information fusion, graph-temporal learning, uncertainty calibration, OOD evaluation, explainability, and recovery-oriented reinforcement learning.

## 2.1 UAV Swarm Mission Assurance

UAV swarms provide distributed sensing, wide-area coverage, redundancy, and cooperative mission execution. These properties make them attractive for surveillance, reconnaissance, disaster response, infrastructure monitoring, border security, and defense-oriented missions. However, swarm autonomy also creates mission-assurance challenges because mission state depends on multiple UAV nodes, communication links, navigation signals, energy constraints, coverage progress, and operator objectives.

Prior UAV security and mission-assurance studies have examined UAS risks, sensor-channel threats, UAV-enabled systems, and cyber-physical vulnerabilities [1, 2, 34–37]. These works motivate the need for resilient monitoring and assurance mechanisms. However, many existing approaches focus on individual attack detection or secure communication rather than integrated mission-state fusion across heterogeneous telemetry sources.

## 2.2 Cyber-Physical Attacks on UAV Swarms

UAV swarms are exposed to cyber-physical attacks that can corrupt or degrade mission information streams. Communication jamming can increase latency and packet loss. GPS or GNSS spoofing can distort localization, route tracking, and velocity consistency. Telemetry tampering can manipulate mission progress, energy reporting, or coverage status. Combined attacks can affect multiple information channels simultaneously.

Prior work has studied GPS spoofing detection, cooperative swarm spoofing mitigation, UAV anti-jamming communication, and adversarial UAV planning [3, 4, 38–47]. These studies show that UAV mission assurance requires reasoning over communication, navigation, and mission-integrity signals together. TRUST-Swarm builds on this direction by modeling mission assurance as a graph-temporal multi-source fusion problem rather than only a single-attack classification task.

## 2.3 Multi-Source Information Fusion for Mission Awareness

Information fusion provides the foundation for combining heterogeneous data sources into decision-relevant representations. Classical multisensor fusion work has shown that combining multiple information sources can improve situational awareness, reliability, and decision support compared with isolated sensor interpretation [IF1–IF5]. High-level fusion models further emphasize the transformation of low-level measurements into mission-level awareness and decision-oriented reasoning [IF6–IF8, IF15].

In UAV swarm mission assurance, no single telemetry source is sufficient to determine mission reliability. Communication delay, packet loss, route deviation, GPS jumps, energy consumption, mission progress, and coverage loss must be interpreted jointly across UAV nodes and mission time. TRUST-Swarm operationalizes this idea by converting distributed UAV telemetry into graph-temporal fusion windows.

## 2.4 Uncertainty-Aware and Conflict-Aware Fusion

Cyber-physical mission telemetry may be noisy, incomplete, delayed, or adversarially corrupted. Therefore, trustworthy fusion requires not only combining data streams but also evaluating uncertainty and conflict among information sources. Evidence-theoretic and uncertainty-aware fusion methods provide a foundation for reasoning under uncertain or conflicting evidence [IF9–IF12].

TRUST-Swarm extends this idea into a deep graph-temporal setting by evaluating confidence, predictive entropy, Expected Calibration Error, and Brier score. This allows the framework to assess whether a fused mission-state prediction is reliable under in-distribution conditions and vulnerable under shifted conditions [18–24].

## 2.5 Multi-Source and Multi-Temporal Fusion

Multi-source and multi-temporal fusion is widely studied in domains where observations evolve over time and originate from heterogeneous sources [IF13, IF14]. UAV swarm mission assurance has a similar structure because each UAV contributes telemetry over time, and mission-level state emerges from the combined behavior of many nodes and features.

TRUST-Swarm represents this setting as a graph-temporal fusion tensor, preserving temporal structure, UAV-node structure, and feature-source structure. This enables the model to jointly reason over communication, navigation, energy, mission-progress, and coverage signals.

## 2.6 Graph-Temporal Learning for UAV Swarms

UAV swarms naturally form dynamic graph systems. UAVs can be represented as nodes, while communication, proximity, coordination, or shared mission context can define relationships. Graph neural networks, graph attention models, and graph-temporal approaches are therefore suitable for learning relational dependencies in multi-agent systems [5–10].

Transformers and temporal models provide additional support for capturing long-range mission evolution and temporal dependencies [11–13]. TRUST-Swarm combines these ideas by using a Graph-Temporal Transformer to learn both UAV-node relationships and mission-time evolution from graph-temporal fusion windows.

## 2.7 Temporal Deep Learning Baselines

Temporal deep learning models such as LSTM, GRU, and 1D-CNN are common baselines for sequence classification and telemetry analysis [14–17]. LSTM and GRU models capture recurrent temporal dependencies, while 1D-CNN models capture local temporal signatures efficiently.

In TRUST-Swarm, these models are used to evaluate whether conventional temporal models can classify mission-state patterns from the same telemetry windows. The strong 1D-CNN result shows that local temporal signatures are highly informative in the current synthetic telemetry setting. This supports careful claim positioning: TRUST-Swarm should be presented as a trustworthy information-fusion framework, not merely as the highest-accuracy classifier.

## 2.8 OOD Evaluation and Distribution Shift

Autonomous UAV missions may encounter unseen cyber-physical conditions that differ from training data. Attackers may use stealth jamming, slow GPS drift, intermittent tampering, delayed combined attacks, or noise patterns that were not observed during model training. Prior OOD and distribution-shift studies show that models can fail under shifted inputs even when they perform well in-distribution [22, 25–28, 54, 55].

TRUST-Swarm includes OOD-aware fusion stress testing to evaluate how fused mission-state predictions behave under unseen cyber-physical shifts. This is important because high in-distribution accuracy does not guarantee reliable mission assurance under adversarial or unfamiliar operating conditions.

## 2.9 Explainability for Fusion-Driver Analysis

Explainability is important for mission assurance because operators and downstream recovery modules need to understand which telemetry sources influenced a prediction. Prior explainable AI methods such as LIME, SHAP, saliency evaluation, and XAI frameworks support interpretation of model decisions [29–32]. Context-enhanced information fusion also emphasizes linking fused decisions to mission-relevant domain knowledge [IF15].

TRUST-Swarm uses perturbation-based feature importance to identify fusion drivers. The analysis reveals whether the model relies on operationally meaningful telemetry sources such as latency, zone coverage, route deviation, mission progress, and GPS jump.

## 2.10 Recovery-Oriented Reinforcement Learning

Mission assurance should not stop at mission-state prediction. When a risk is detected, a UAV swarm may need to continue, monitor, reroute, reassign, isolate a node, or return to base. Reinforcement learning, PPO, and multi-agent reinforcement learning provide foundations for adaptive mission planning and recovery-oriented reasoning [33, 48–53].

TRUST-Swarm includes a PPO-based recovery scaffold to demonstrate how fused mission-state predictions and confidence signals can support downstream mission-assurance decisions. The current recovery component is not a deployment-ready controller, but it provides an initial bridge between trustworthy information fusion and recovery reasoning.

## 2.11 Research Gap

The literature includes strong work on UAV security, cyber-physical attacks, information fusion, graph learning, temporal modeling, uncertainty estimation, OOD detection, explainability, and reinforcement learning. However, these areas are often studied separately. Existing UAV security systems may detect attacks, but they often do not integrate multi-source telemetry fusion, graph-temporal mission modeling, calibrated confidence, OOD stress testing, fusion-driver explainability, and recovery reasoning in one pipeline.

TRUST-Swarm addresses this gap by presenting a trustworthy graph-temporal multi-source information fusion framework for UAV swarm mission assurance. The framework evaluates not only mission-state classification, but also confidence reliability, unseen-shift vulnerability, telemetry-source importance, and recovery-oriented decision support.


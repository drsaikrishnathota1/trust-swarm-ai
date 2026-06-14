# High-Confidence Computing Related Work v2

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

TRUST-Swarm uses this idea by converting distributed UAV telemetry into graph-temporal mission windows. Each window preserves temporal length, UAV-node structure, and telemetry-feature structure. The Graph-Temporal Transformer is then evaluated as the central prediction layer. This design is not intended to show that graph-temporal modeling always outperforms all temporal baselines. Instead, it provides an intelligent prediction layer suitable for integration into a broader high-confidence mission-assurance framework.

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

TRUST-Swarm uses perturbation-based feature importance to identify mission-risk drivers. The final analysis identifies latency, zone coverage, route deviation, mission progress, and GPS jump as major decision drivers. These features are operationally meaningful because they correspond to communication degradation, mission coverage loss, navigation disruption, mission-progress interruption, and spoofing-related displacement. This imshows the traceability of the framework and supports the claim that TRUST-Swarm provides decision evidence rather than opaque classification alone.

### 2.8. Recovery-oriented reinforcement learning and active defense

Mission assurance should not stop after detection. Once a mission risk is identified, a UAV swarm may need to continue, monitor, reroute, reassign, isolate a compromised node, or return to base. Reinforcement learning, PPO, multi-agent reinforcement learning, safe reinforcement learning, and cyber-physical resilience research provide foundations for adaptive response reasoning [18–20, 53–63].

TRUST-Swarm includes a PPO-based recovery-reasoning scaffold to connect prediction outputs with mission-response actions. The recovery layer receives mission-state prediction, confidence, entropy, and risk indicators. It is not claimed as an operational UAV controller. Instead, it demonstrates how high-confidence prediction outputs can support response-oriented mission reasoning. This is aligned with active defense because the framework connects recognition and confidence evidence to possible response pathways.

### 2.9. Comparison with related research directions

Table 1 summarizes the positioning of TRUST-Swarm against related research directions.

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

# High-Confidence Computing Introduction v1

## 1. Introduction

Multi-UAV swarm systems are increasingly used in surveillance, reconnaissance, disaster response, infrastructure monitoring, logistics, and cyber-physical mission operations. Compared with single-UAV platforms, UAV swarms provide distributed sensing, wider coverage, redundancy, and adaptive mission execution. However, these advantages depend on the reliability of communication, navigation, telemetry integrity, energy awareness, and mission-progress monitoring. When these information streams are disrupted, autonomous mission decisions may become unreliable [R21, R23, R27, R28].

Cyber-physical attacks create a major challenge for secure UAV swarm mission assurance. Communication jamming can increase latency and packet loss, reducing coordination among UAV nodes. GPS spoofing can cause route deviation, GPS jumps, and velocity inconsistency. Telemetry tampering can distort battery state, mission progress, energy consumption, or zone coverage. Combined attacks can simultaneously degrade communication, navigation, and mission integrity. These disruptions create a high-confidence computing problem: the system must not only predict mission state, but also evaluate whether the prediction can be trusted [R24, R25, R26, R31, R32, R33].

Existing UAV security and resilience methods often focus on attack detection, secure communication, intrusion detection, or rule-based recovery. Although these methods are valuable, many of them remain limited in four ways. First, they often treat mission telemetry as ordinary time-series data rather than modeling UAV-node relationships and mission evolution together. Second, they emphasize classification accuracy without calibrated confidence estimation. Third, they rarely evaluate model behavior under unseen out-of-distribution cyber-physical shifts. Fourth, they provide limited traceability and limited connection between prediction outputs and recovery-oriented mission response [R37, R41, R43, R44, R47, R48, R64, R66, R76, R80].

These limitations are critical for high-confidence intelligent systems. In secure autonomous missions, a prediction is not sufficient by itself. A mission-assurance framework should answer five questions: what mission state is predicted, how reliable the prediction is, how the system behaves under unseen cyber-physical shifts, which telemetry factors influenced the decision, and how the output can support recovery reasoning. Therefore, secure UAV swarm mission assurance should be framed as a high-confidence intelligent computing problem rather than only an attack-classification problem [R01, R02, R03, R34, R35, R36].

To address this need, this paper presents TRUST-Swarm, a high-confidence graph-temporal intelligent computing framework for secure multi-UAV mission assurance under cyber-physical attacks. TRUST-Swarm represents distributed UAV telemetry as graph-temporal mission windows and evaluates a Graph-Temporal Transformer for mission-state recognition. The framework further integrates uncertainty calibration, OOD stress testing, perturbation-based explainability, and recovery-oriented reasoning [R51, R53, R54, R56, R58, R37, R41, R43, R44, R47, R48, R66].

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

<!-- CITATIONS_INSERTED_INTRO_V1 -->

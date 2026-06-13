# Information Fusion Introduction v2

## 1. Introduction

Multi-UAV swarm systems are increasingly used for surveillance, reconnaissance, disaster response, infrastructure monitoring, border security, logistics, and defense-oriented autonomous missions. Unlike single-UAV systems, UAV swarms provide distributed sensing, wide-area coverage, redundancy, cooperative decision-making, and adaptive mission execution. However, these advantages depend on the reliable fusion of heterogeneous mission information streams collected across UAV nodes and mission time.

A UAV swarm mission produces multiple forms of operational telemetry, including communication behavior, navigation state, energy condition, mission progress, and coverage quality. No single telemetry source is sufficient to determine mission reliability under cyber-physical stress. For example, communication latency may indicate jamming, GPS displacement may indicate spoofing, route deviation may indicate navigation disruption, zone-coverage loss may indicate mission degradation, and energy variation may indicate abnormal maneuvering or mission stress. Mission assurance therefore requires the joint interpretation of multiple information sources across both swarm topology and temporal mission evolution.

In contested cyber-physical environments, these information streams may be degraded, delayed, corrupted, or manipulated. Communication jamming can increase latency and packet loss, reducing inter-UAV coordination. GPS spoofing can cause localization jumps, route deviation, and velocity inconsistency. Telemetry tampering can distort mission-progress reporting, battery state, energy consumption, or coverage information. Combined attacks can simultaneously affect communication, navigation, and mission integrity. These disruptions create a high-confidence information-fusion problem: the system must estimate mission state while also evaluating whether its fused prediction is reliable.

Existing UAV security and resilience methods often focus on attack detection, secure communication, intrusion detection, anomaly monitoring, or rule-based recovery. While these methods are important, many of them treat mission telemetry as isolated time-series measurements or focus primarily on classification accuracy. Such approaches may not fully capture the graph-like structure of UAV swarms, the temporal evolution of mission degradation, the uncertainty of model predictions, the behavior of models under unseen distribution shifts, or the mission-relevant features driving the decision.

This limitation is critical for autonomous swarm operations. A high-confidence UAV mission-assurance system should not only classify whether the swarm is normal or under attack. It should also fuse distributed mission telemetry, estimate confidence, expose vulnerability under out-of-distribution attack shifts, explain the telemetry drivers behind the decision, and support recovery-oriented reasoning. Therefore, trustworthy UAV swarm mission assurance should be treated as a multi-source graph-temporal information-fusion problem rather than only a conventional attack-classification task.

To address this need, this paper presents TRUST-Swarm, a trustworthy graph-temporal multi-source information fusion framework for high-confidence UAV swarm mission assurance under cyber-physical attacks. TRUST-Swarm represents UAV missions as graph-temporal fusion windows, where UAVs are modeled as dynamic nodes and heterogeneous telemetry signals are fused across mission time. The framework integrates graph-temporal learning, uncertainty calibration, OOD stress evaluation, perturbation-based explainability, and PPO-based recovery reasoning.

The TRUST-Swarm evaluation uses a controlled simulation-based telemetry environment with three random seeds, 300 mission runs per seed, 240 timesteps per mission, 20 UAVs per mission, and 66,300 graph-temporal fusion windows per seed. The evaluated mission states include normal operation, jamming, spoofing, tampering, and combined cyber-physical attack scenarios. The evaluation also includes unseen OOD stress conditions, including stealth jamming, slow GPS drift, intermittent tampering, delayed combined attacks, and unseen swarm noise.

The final results show that the Graph-Temporal Transformer achieves strong in-distribution mission-state recognition and strong calibration. However, the 1D-CNN baseline achieves the strongest raw in-distribution classification performance, indicating that the synthetic telemetry environment contains strong local temporal signatures. Therefore, TRUST-Swarm is not positioned as merely the best raw classifier. Instead, it is positioned as a trustworthy information-fusion framework that combines graph-temporal mission modeling, calibrated confidence, OOD stress testing, explainability, and recovery reasoning.

The main contributions of this paper are as follows:

1. A trustworthy graph-temporal multi-source information fusion framework is proposed for UAV swarm mission assurance under cyber-physical attacks.

2. A graph-temporal fusion-window representation is developed to model distributed UAV telemetry across nodes, mission time, and heterogeneous telemetry sources.

3. A Graph-Temporal Transformer is evaluated for mission-state recognition under normal, jamming, spoofing, tampering, and combined attack conditions.

4. A three-seed large-scale simulation study is conducted using 300 mission runs per seed, 240 timesteps per mission, 20 UAVs per mission, and 66,300 graph-temporal fusion windows per seed.

5. Temporal baseline comparisons are performed against LSTM, GRU, and 1D-CNN models to evaluate in-distribution classification performance.

6. Confidence-aware fusion is evaluated using Expected Calibration Error, Brier score, predictive confidence, and predictive entropy.

7. OOD-aware fusion behavior is evaluated under unseen cyber-physical stress conditions, including stealth jamming, slow GPS drift, intermittent tampering, delayed combined attacks, and unseen swarm noise.

8. Perturbation-based explainability is used to identify the most influential mission telemetry fusion drivers, including latency, zone coverage, route deviation, mission progress, and GPS jump.

9. A PPO-based recovery-reasoning scaffold is included to connect fused mission-state outputs with mission-assurance recovery decisions.

The remainder of this paper is organized as follows. Section 2 reviews related work on UAV swarm security, cyber-physical attacks, graph-temporal learning, information fusion, uncertainty calibration, OOD evaluation, explainability, and recovery reasoning. Section 3 presents the TRUST-Swarm methodology. Section 4 describes the experimental setup. Section 5 presents the results and discussion. Section 6 discusses limitations and future work. Section 7 concludes the paper.


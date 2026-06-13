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


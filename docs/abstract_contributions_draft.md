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


# Information Fusion Abstract v2

## Reframed Title

TRUST-Swarm: Trustworthy Graph-Temporal Multi-Source Information Fusion for High-Confidence UAV Swarm Mission Assurance Under Cyber-Physical Attacks

## Abstract

Multi-UAV swarm missions depend on the continuous fusion of distributed and heterogeneous information streams, including communication telemetry, navigation behavior, energy state, mission progress, and coverage status. In contested cyber-physical environments, these information streams can be degraded or corrupted by communication jamming, GPS spoofing, telemetry tampering, and combined attack conditions. Existing UAV security and resilience studies often focus on attack detection or communication protection, but many provide limited support for confidence-aware information fusion, out-of-distribution stress testing, explainability, and recovery-oriented mission assurance.

This paper presents TRUST-Swarm, a trustworthy graph-temporal multi-source information fusion framework for high-confidence UAV swarm mission assurance under cyber-physical attacks. TRUST-Swarm represents UAV missions as graph-temporal fusion windows, where UAVs are modeled as dynamic nodes and heterogeneous telemetry signals are fused across time to estimate mission state under normal and adversarial conditions. The framework integrates graph-temporal learning, uncertainty calibration, OOD stress evaluation, perturbation-based explainability, and PPO-based recovery reasoning.

A three-seed simulation study was conducted using 300 mission runs per seed, 240 timesteps per mission, 20 UAVs per mission, and 66,300 graph-temporal fusion windows per seed. The Graph-Temporal Transformer achieved a mean accuracy of 0.9647 and a mean macro F1 score of 0.8750 across three seeds, while producing strong in-distribution calibration with an Expected Calibration Error of 0.0088 and a Brier score of 0.0531. OOD stress tests showed substantial degradation under severe unseen cyber-physical shifts, especially delayed combined attacks, stealth jamming, and slow GPS drift. Explainability analysis identified latency, zone coverage, route deviation, mission progress, and GPS jump as major fusion drivers.

Although a 1D-CNN baseline achieved stronger in-distribution classification performance, TRUST-Swarm provides a broader trustworthy information-fusion framework by combining graph-temporal mission modeling, calibrated confidence, OOD stress testing, explainability, and recovery-oriented reasoning. The results demonstrate that high-confidence UAV swarm mission assurance requires more than raw classification accuracy; it requires trustworthy fusion mechanisms that can evaluate prediction reliability, expose unseen-shift vulnerability, explain mission-relevant telemetry drivers, and support recovery decisions under cyber-physical uncertainty.

## Keywords

UAV swarms; information fusion; multi-source telemetry fusion; graph-temporal learning; mission assurance; cyber-physical attacks; jamming; GPS spoofing; telemetry tampering; uncertainty calibration; out-of-distribution evaluation; explainable AI; reinforcement learning; trustworthy AI.


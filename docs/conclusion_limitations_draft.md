# TRUST-Swarm Conclusion and Limitations Draft

## 6. Limitations and Future Work

Although the final TRUST-Swarm experiment provides a strong foundation for high-confidence multi-UAV mission assurance, several limitations should be acknowledged.

First, the evaluation is based on synthetic telemetry generation. The synthetic environment allows controlled testing across multiple attack types, mission runs, seeds, and OOD stress conditions, but it does not fully replace field-collected UAV telemetry. Real-world UAV operations may include more complex mobility patterns, communication-channel effects, environmental interference, sensor noise, weather conditions, hardware constraints, and operator-driven mission changes.

Second, the current graph structure is based on graph-temporal telemetry windows rather than a fully physics-based UAV communication graph. Future work should integrate distance-aware communication links, RF propagation models, UAV mobility constraints, line-of-sight disruption, and dynamic edge construction based on mission context.

Third, the OOD results show that severe unseen cyber-physical shifts can substantially degrade model performance. This is important because it reveals operational vulnerability under stealth jamming, slow GPS drift, and delayed combined attacks. However, some severe OOD cases may still produce high model confidence. Therefore, future work should include stronger OOD detection methods, ensemble uncertainty, conformal prediction, energy-based OOD scoring, and hybrid statistical monitoring.

Fourth, the 1D-CNN baseline achieved the strongest in-distribution classification performance. This indicates that the current synthetic telemetry contains strong local temporal signatures. The Graph-Temporal Transformer should therefore not be framed as the best raw classifier. Instead, TRUST-Swarm should be framed as a trustworthy mission-assurance framework that integrates graph-temporal modeling, uncertainty calibration, OOD stress testing, explainability, and recovery reasoning.

Fifth, the PPO-based mission recovery module is currently a recovery-reasoning scaffold. Although it demonstrates the feasibility of connecting mission-state indicators to recovery actions, it should not be interpreted as a complete operational UAV controller. Future work should improve the reward function, enforce safety constraints, encourage balanced recovery actions, integrate realistic mission simulators, and evaluate recovery policies under dynamic swarm conditions.

Future research will extend TRUST-Swarm in five directions: field-realistic UAV telemetry, physics-informed communication modeling, stronger OOD detection, safety-constrained recovery policies, and hardware-in-the-loop or simulator-in-the-loop validation.

## 7. Conclusion

This paper presented TRUST-Swarm, a trustworthy graph-temporal AI framework for high-confidence multi-UAV mission assurance under cyber-physical attacks. The framework models UAV swarm telemetry as graph-temporal mission windows and integrates graph-temporal learning, uncertainty calibration, OOD stress testing, perturbation-based explainability, and recovery-oriented reasoning.

The final three-seed experiment evaluated TRUST-Swarm using 300 mission runs per seed, 240 timesteps per mission, 20 UAVs per mission, and 66,300 graph-temporal windows per seed. The Graph-Temporal Transformer achieved strong in-distribution performance and calibration, with a mean accuracy of 0.9647, mean macro F1 of 0.8750, Expected Calibration Error of 0.0088, and Brier score of 0.0531.

The results also showed that the 1D-CNN baseline achieved stronger in-distribution classification performance than the Graph-Temporal Transformer. This finding is important because it prevents overclaiming and supports a more accurate interpretation of TRUST-Swarm. The contribution of TRUST-Swarm is not simply raw classification superiority. Its contribution is the integration of classification, calibration, OOD stress testing, explainability, and recovery reasoning into a high-confidence mission-assurance pipeline.

OOD stress tests revealed that unseen cyber-physical shifts, especially stealth jamming, slow GPS drift, and delayed combined attacks, can severely degrade model performance. These findings show that UAV swarm mission assurance must include OOD-aware evaluation rather than relying only on in-distribution test accuracy.

Explainability analysis identified latency, zone coverage, route deviation, mission progress, and GPS jump as the most influential telemetry features. These features align with operationally meaningful mission-risk indicators, supporting the interpretability and mission relevance of the TRUST-Swarm framework.

Overall, TRUST-Swarm provides a strong foundation for trustworthy AI-enabled multi-UAV mission assurance. The framework demonstrates how graph-temporal learning, calibrated confidence, OOD stress testing, explainability, and recovery reasoning can be combined to support resilient autonomous swarm operations under cyber-physical uncertainty.


# Information Fusion Conclusion and Limitations v2

## 6. Limitations and Future Work

Although TRUST-Swarm provides a strong simulation-based foundation for high-confidence UAV swarm mission assurance, several limitations should be acknowledged.

First, the evaluation is based on synthetic multi-UAV telemetry. The synthetic environment enables controlled testing across multiple seeds, mission runs, attack classes, and OOD stress conditions, but it does not fully replace field-collected UAV telemetry. Real-world UAV swarm operations may include more complex mobility patterns, communication-channel effects, RF propagation behavior, weather effects, hardware constraints, sensor drift, operator interventions, and environmental uncertainty.

Second, the current graph-temporal fusion representation models UAVs as structured mission nodes across time, but it does not yet implement a fully physics-aware dynamic communication graph. Future work should incorporate distance-aware edges, RF propagation models, line-of-sight constraints, jammer geometry, UAV mobility dynamics, and dynamic graph construction based on communication and mission context.

Third, OOD stress testing revealed substantial degradation under severe unseen cyber-physical shifts. This is an important finding because it shows that high in-distribution classification performance is not sufficient for reliable mission assurance. Some OOD conditions may still produce high confidence, indicating that confidence alone cannot fully guarantee safe operation under unseen attacks. Future work should integrate stronger OOD detection methods, conformal prediction, ensemble uncertainty, energy-based scoring, and hybrid statistical monitoring.

Fourth, the 1D-CNN baseline achieved the strongest in-distribution classification performance. This suggests that the current synthetic telemetry benchmark contains strong local temporal signatures. Therefore, TRUST-Swarm should not be framed as the best raw classifier. Instead, it should be framed as a trustworthy graph-temporal information-fusion framework that integrates mission-state recognition, calibrated confidence, OOD stress testing, fusion-driver explainability, and recovery reasoning.

Fifth, the PPO-based recovery component is currently a recovery-reasoning scaffold. It demonstrates how fused mission-state predictions and confidence signals can be connected to possible recovery actions, but it is not a complete operational UAV controller. Future work should improve reward design, add safety constraints, encourage balanced recovery actions, integrate realistic swarm simulators, and evaluate recovery policies under dynamic cyber-physical mission conditions.

Future research will extend TRUST-Swarm in five directions: field-realistic UAV telemetry, physics-aware graph construction, stronger OOD detection, safety-constrained recovery policies, and simulator-in-the-loop or hardware-in-the-loop validation.

## 7. Conclusion

This paper presented TRUST-Swarm, a trustworthy graph-temporal multi-source information fusion framework for high-confidence UAV swarm mission assurance under cyber-physical attacks. The framework represents UAV missions as graph-temporal fusion windows and jointly models communication, navigation, energy, mission-progress, and coverage telemetry across UAV nodes and mission time.

The final three-seed experiment evaluated TRUST-Swarm using 300 mission runs per seed, 240 timesteps per mission, 20 UAVs per mission, and 66,300 graph-temporal fusion windows per seed. The Graph-Temporal Transformer achieved strong in-distribution performance, with a mean accuracy of 0.9647 and a mean macro F1 score of 0.8750. It also produced strong calibration, with an Expected Calibration Error of 0.0088 and a Brier score of 0.0531.

The results also showed that the 1D-CNN baseline achieved stronger in-distribution classification performance than the Graph-Temporal Transformer. This finding is important because it supports a careful and honest interpretation of the contribution. TRUST-Swarm is not presented as the highest-performing raw classifier. Instead, its contribution is the integration of graph-temporal multi-source telemetry fusion, calibrated confidence, OOD stress testing, fusion-driver explainability, and recovery-oriented mission reasoning.

OOD stress tests demonstrated that unseen cyber-physical shifts, especially delayed combined attacks, stealth jamming, and slow GPS drift, can severely degrade mission-state recognition. These findings show that UAV swarm mission assurance must evaluate distribution-shift behavior rather than relying only on in-distribution test accuracy.

Fusion-driver explainability identified latency, zone coverage, route deviation, mission progress, and GPS jump as influential telemetry sources. These drivers are operationally meaningful because they correspond to communication degradation, mission coverage loss, navigation disruption, mission-progress interruption, and spoofing-related displacement.

Overall, TRUST-Swarm demonstrates how trustworthy graph-temporal information fusion can support high-confidence UAV swarm mission assurance under cyber-physical uncertainty. The framework provides a foundation for future research on field-realistic UAV telemetry, physics-aware swarm communication graphs, stronger OOD detection, explainable mission-risk reasoning, and safety-constrained autonomous recovery.


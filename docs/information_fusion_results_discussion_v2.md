# Information Fusion Results and Discussion v2

## 5. Results and Discussion

This section evaluates TRUST-Swarm as a graph-temporal multi-source information fusion framework for high-confidence UAV swarm mission assurance. The analysis focuses on six questions:

1. Can graph-temporal fusion recognize cyber-physical mission states?
2. How does the fusion model compare with temporal baselines?
3. Are the fused predictions calibrated?
4. How does the framework behave under unseen OOD cyber-physical shifts?
5. Which telemetry sources drive the fused decisions?
6. How can fused mission-state outputs support recovery-oriented reasoning?

## 5.1 In-Distribution Mission-State Recognition

The Graph-Temporal Transformer achieved a mean accuracy of 0.9647 and a mean macro F1 score of 0.8750 across three seeds. The mean macro precision was 0.8935, and the mean macro recall was 0.8700. These results show that graph-temporal fusion can learn meaningful mission-state patterns from distributed UAV telemetry under cyber-physical attack conditions.

The model fused heterogeneous telemetry sources across UAV nodes and mission time, including communication, navigation, energy, mission-progress, and coverage signals. This supports the central idea that mission assurance should not depend on a single telemetry variable, but instead should jointly interpret multiple mission information streams.

## 5.2 Comparison with Temporal Baselines

The temporal baselines included LSTM, GRU, and 1D-CNN models. The 1D-CNN baseline achieved the strongest in-distribution classification performance, with a mean accuracy of 0.9987 and a mean macro F1 score of 0.9971. The LSTM baseline achieved a mean macro F1 score of 0.9608, while the GRU achieved a mean macro F1 score of 0.9288.

This result indicates that the synthetic telemetry environment contains strong local temporal signatures that can be captured effectively by convolutional temporal models. Therefore, the manuscript should not claim that the Graph-Temporal Transformer is the best raw classifier.

Instead, the correct interpretation is that TRUST-Swarm provides a broader trustworthy information-fusion framework. Its contribution is not limited to in-distribution classification. It combines graph-temporal mission modeling, confidence calibration, OOD stress evaluation, fusion-driver explainability, and recovery-oriented reasoning.

## 5.3 Confidence-Aware Fusion Calibration

The Graph-Temporal Transformer produced strong in-distribution calibration. Across three seeds, it achieved a mean Expected Calibration Error of 0.0088 and a mean Brier score of 0.0531. The mean predictive confidence was 0.9601, and the mean predictive entropy was 0.0986.

These results support the high-confidence information-fusion framing of TRUST-Swarm. A mission-assurance system should not only output a predicted mission state. It should also estimate whether the fused prediction is reliable. The low Expected Calibration Error suggests that the model’s confidence estimates are well aligned with in-distribution prediction correctness.

Confidence-aware fusion is especially important for autonomous UAV swarms because mission decisions may require escalation, monitoring, rerouting, or recovery actions when model confidence is uncertain.

## 5.4 OOD-Aware Fusion Stress Testing

OOD stress testing revealed substantial degradation under unseen cyber-physical shifts. The in-distribution macro F1 score was 0.8750. However, intermittent tampering reduced macro F1 to 0.5965. More severe OOD conditions caused larger reductions: slow GPS drift achieved a macro F1 score of 0.1701, stealth jamming achieved 0.0779, and delayed combined attacks achieved 0.0521.

These results show that unseen cyber-physical shifts can significantly alter the mission telemetry distribution. In operational UAV swarm missions, attackers may not follow the same patterns represented during training. Therefore, OOD-aware fusion evaluation is necessary for high-confidence mission assurance.

The OOD results should not be interpreted as perfect OOD detection. Some severe OOD cases may still produce high confidence. This means that confidence alone is not sufficient for robust mission assurance. Instead, TRUST-Swarm motivates the combined use of calibration, OOD stress testing, explainability, and recovery reasoning.

## 5.5 Fusion-Driver Explainability

Perturbation-based feature importance identified latency, zone coverage, route deviation, mission progress, and GPS jump as major fusion drivers. These features are operationally meaningful.

Latency reflects communication degradation and possible jamming. Zone coverage reflects mission-level effectiveness. Route deviation reflects navigation disruption. Mission progress reflects task completion under cyber-physical interference. GPS jump reflects spoofing-related displacement or localization instability.

This result strengthens the interpretability of TRUST-Swarm. The model’s most influential inputs correspond to mission-relevant risk indicators rather than arbitrary telemetry artifacts. For high-confidence UAV swarm assurance, this is important because operators and downstream decision modules need to understand why a mission-state prediction was produced.

## 5.6 Recovery-Oriented Fusion Reasoning

TRUST-Swarm includes a PPO-based recovery-reasoning scaffold. The recovery layer connects fused mission-state outputs, confidence signals, and mission-risk indicators to possible recovery actions such as continue, monitor, reroute, reassign, isolate node, or return to base.

The recovery module should be interpreted as an initial mission-assurance scaffold rather than a complete operational UAV controller. Its purpose is to demonstrate how fused predictions can support downstream recovery reasoning. Future work should extend this module with richer reward functions, safety constraints, realistic swarm dynamics, and simulator-in-the-loop validation.

## 5.7 Discussion

The final results show that TRUST-Swarm should be positioned as a trustworthy graph-temporal information-fusion framework rather than only a classifier. Although the 1D-CNN baseline achieved stronger in-distribution classification performance, it does not provide the same integrated analysis of calibrated confidence, OOD behavior, explainability, and recovery-oriented decision support.

The Graph-Temporal Transformer provides a structured way to fuse UAV-node telemetry across mission time. The calibration results show that the fused predictions are reliable under in-distribution conditions. The OOD stress tests reveal that severe unseen cyber-physical shifts remain challenging. The explainability results show that the model relies on mission-relevant telemetry drivers.

Together, these findings support the main claim of TRUST-Swarm: high-confidence UAV swarm mission assurance requires trustworthy fusion mechanisms beyond raw classification accuracy. A useful mission-assurance system must evaluate what mission state is predicted, how reliable the prediction is, how the system behaves under unseen shifts, which telemetry sources influenced the decision, and how the output can support recovery.

## 5.8 Safe Interpretation

The manuscript should state that TRUST-Swarm provides an integrated trustworthy information-fusion framework for UAV swarm mission assurance.

The manuscript should not claim that the Graph-Temporal Transformer outperforms all baselines.

The safest claim is:

TRUST-Swarm demonstrates how graph-temporal multi-source telemetry fusion, calibrated confidence, OOD stress testing, fusion-driver explainability, and recovery reasoning can be integrated for high-confidence UAV swarm mission assurance under cyber-physical attacks.


# High-Confidence Computing Results and Discussion v1

## 5. Results and Discussion

This section evaluates TRUST-Swarm as a high-confidence graph-temporal intelligent computing framework for secure multi-UAV mission assurance. The evaluation focuses on five questions:

1. Can TRUST-Swarm recognize cyber-physical mission states?
2. How does the Graph-Temporal Transformer compare with temporal baselines?
3. Are its predictions well calibrated?
4. How does the model behave under unseen OOD cyber-physical shifts?
5. Can the framework provide traceable evidence and recovery-oriented reasoning?

## 5.1 In-Distribution Mission-State Recognition

Across three random seeds, the Graph-Temporal Transformer achieved a mean accuracy of 0.9647 and a mean macro F1 score of 0.8750. The mean macro precision was 0.8935, and the mean macro recall was 0.8700.

These results show that the graph-temporal prediction layer can learn meaningful mission-state patterns from UAV telemetry under cyber-physical attack conditions. The model captures mission-time evolution, UAV-node structure, and telemetry-feature interactions across communication, navigation, energy, mission-progress, and coverage signals.

From a High-Confidence Computing perspective, this result demonstrates the intelligent computing component of TRUST-Swarm. However, mission-state recognition alone is not sufficient for high-confidence autonomous operation. The framework must also evaluate reliability, uncertainty, OOD behavior, traceability, and recovery support.

## 5.2 Baseline Comparison

The baseline comparison included LSTM, GRU, and 1D-CNN models. The 1D-CNN baseline achieved the strongest in-distribution classification performance, with a mean accuracy of 0.9987 and a mean macro F1 score of 0.9971. The LSTM and GRU baselines achieved mean macro F1 scores of 0.9608 and 0.9288, respectively.

This result shows that the synthetic telemetry benchmark contains strong local temporal signatures that are effectively captured by convolutional temporal learning. Therefore, the Graph-Temporal Transformer should not be claimed as the best raw classifier.

The correct interpretation is that TRUST-Swarm contributes a high-confidence secure intelligent computing pipeline. Unlike a pure classifier, the framework integrates prediction, calibration, OOD stress testing, traceable explanation, and recovery-oriented reasoning. This broader framework-level contribution is more aligned with High-Confidence Computing than a single accuracy comparison.

## 5.3 Confidence Calibration Results

The Graph-Temporal Transformer produced strong in-distribution calibration. Across three seeds, the model achieved a mean Expected Calibration Error of 0.0088 and a mean Brier score of 0.0531. The mean predictive confidence was 0.9601, and the mean predictive entropy was 0.0986.

These results support the high-confidence computing objective because the model provides not only mission-state probabilities but also reliability evidence. A low Expected Calibration Error indicates that predicted confidence is well aligned with empirical correctness under in-distribution conditions.

For secure UAV swarm mission assurance, calibrated confidence is important because uncertain or low-confidence predictions may require monitoring, escalation, or recovery-oriented response. This makes calibration a core component of TRUST-Swarm rather than an optional evaluation metric.

## 5.4 OOD Cyber-Physical Stress Testing

OOD stress testing revealed substantial performance degradation under unseen cyber-physical shifts. The in-distribution macro F1 score was 0.8750. Intermittent tampering reduced macro F1 to 0.5965. More severe shifts caused larger reductions: slow GPS drift achieved a macro F1 score of 0.1701, stealth jamming achieved 0.0779, and delayed combined attacks achieved 0.0521.

These findings show that cyber-physical distribution shifts can significantly degrade mission-state recognition even when in-distribution performance is strong. This is an important high-confidence computing result because it exposes failure modes that standard test accuracy would hide.

The OOD results should not be interpreted as complete OOD reliability. Some severe OOD cases may still produce high confidence. Therefore, confidence alone is not sufficient for secure mission assurance. TRUST-Swarm uses OOD stress testing to reveal mission-risk conditions and motivate stronger monitoring, escalation, and recovery mechanisms.

## 5.5 Traceable Mission-Risk Explanation

Perturbation-based feature importance identified latency, zone coverage, route deviation, mission progress, and GPS jump as the most influential mission-risk drivers.

These features are operationally meaningful:

* latency reflects communication degradation and possible jamming;
* zone coverage reflects mission effectiveness and coverage loss;
* route deviation reflects navigation disruption;
* mission progress reflects task completion under attack;
* GPS jump reflects spoofing-related displacement.

This improves decision traceability. In high-confidence computing, a framework should provide evidence explaining why a decision was produced. TRUST-Swarm supports this through feature-level traceability, linking mission-state predictions to interpretable cyber-physical telemetry drivers.

## 5.6 Recovery-Oriented Reasoning

TRUST-Swarm includes a PPO-based recovery-reasoning scaffold. The recovery layer receives mission-state prediction, confidence, entropy, and mission-risk indicators. It maps these inputs to recovery actions such as continue, monitor, reroute, reassign, isolate node, and return to base.

This module is not claimed as a operationally deployable UAV controller. Instead, it demonstrates how high-confidence prediction outputs can support mission-response reasoning. This is important because secure mission assurance should not stop at detection. It should connect risk recognition to response planning.

## 5.7 Discussion Against High-Confidence Computing Standards

The results show that TRUST-Swarm is better framed as a high-confidence intelligent computing framework than as a pure classification model.

The accepted High-Confidence Computing papers commonly emphasize unified frameworks, multiple evaluation metrics, practical validation, and system-level reasoning. For example, the SDN-IoT DRAFT paper combines traffic prediction, federated learning, zero-trust mechanisms, denoising, and real-world dataset evaluation. The HTTPS assessment paper proposes a unified methodology with testing, examination, interviewing, and real-world website case-study validation. The critical-infrastructure IDS paper integrates detection, classification, privacy preservation, adaptation, and multi-benchmark validation. TRUST-Swarm follows the same framework-oriented direction, but its current limitation is that validation remains synthetic.

Therefore, the current results are strong enough to justify a manuscript foundation, but two additional analyses are needed before final HCC submission:

1. Ablation study to show the value of each TRUST-Swarm module.
2. Runtime and complexity analysis to show practical computing feasibility.

## 5.8 Safe Final Interpretation

The safe interpretation is:

TRUST-Swarm provides a high-confidence graph-temporal intelligent computing framework for secure multi-UAV mission assurance by integrating mission-state recognition, calibrated confidence, OOD cyber-physical stress testing, traceable explanation, and recovery-oriented reasoning.

The manuscript should not claim:

* the Graph-Temporal Transformer is superior to all baselines;
* OOD behavior is fully solved;
* the recovery module is operationally operationally deployable;
* synthetic telemetry replaces field UAV validation.

The results support TRUST-Swarm as a secure, intelligent, calibrated, traceable, and recovery-aware mission-assurance framework.


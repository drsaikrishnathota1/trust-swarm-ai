# High-Confidence Computing Target: Title, Abstract, and Contributions v1

## Target Journal

High-Confidence Computing

## Recommended HCC Title

TRUST-Swarm: A High-Confidence Graph-Temporal Intelligent Computing Framework for Secure Multi-UAV Mission Assurance Under Cyber-Physical Attacks

## HCC-Framed Abstract

Multi-UAV swarm systems are increasingly used in cyber-physical missions that require secure, reliable, and intelligent decision support under dynamic adversarial conditions. However, communication jamming, GPS spoofing, telemetry tampering, and combined attacks can corrupt mission telemetry, degrade coordination, and reduce the reliability of autonomous mission-state prediction. Existing UAV security and resilience methods often emphasize attack classification or communication protection, but they provide limited support for calibrated confidence estimation, out-of-distribution stress testing, traceable decision evidence, and recovery-oriented mission reasoning.

This paper presents TRUST-Swarm, a high-confidence graph-temporal intelligent computing framework for secure multi-UAV mission assurance under cyber-physical attacks. TRUST-Swarm models distributed UAV telemetry as graph-temporal mission windows and integrates mission-state recognition, uncertainty calibration, OOD stress testing, perturbation-based explainability, and recovery-oriented reasoning. The framework is designed to support high-confidence decision-making by evaluating not only what mission state is predicted, but also how reliable the prediction is, how the model behaves under unseen cyber-physical shifts, which telemetry factors influence the decision, and how prediction outputs can support mission recovery.

A three-seed simulation study was conducted using 300 mission runs per seed, 240 timesteps per mission, 20 UAVs per mission, and 66,300 graph-temporal windows per seed. The Graph-Temporal Transformer achieved a mean accuracy of 0.9647 and a mean macro F1 score of 0.8750, while producing strong in-distribution calibration with an Expected Calibration Error of 0.0088 and a Brier score of 0.0531. OOD stress testing revealed substantial degradation under severe unseen cyber-physical shifts, especially delayed combined attacks, stealth jamming, and slow GPS drift. Explainability analysis identified latency, zone coverage, route deviation, mission progress, and GPS jump as mission-relevant decision drivers.

Although the 1D-CNN baseline achieved stronger in-distribution classification performance, TRUST-Swarm is not proposed as a raw classifier alone. Instead, it provides a high-confidence secure intelligent computing framework that integrates prediction, calibration, OOD vulnerability analysis, traceable explanation, and recovery-oriented mission reasoning. The results demonstrate that secure UAV swarm mission assurance requires more than high classification accuracy; it requires high-confidence computing mechanisms that can evaluate reliability, expose unseen-shift risk, explain decisions, and support resilient mission response.

## HCC Contribution Table

| High-Confidence Computing Requirement | TRUST-Swarm Component                                                                   | Manuscript Evidence                                                                                  |
| ------------------------------------- | --------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| Secure computing                      | Cyber-physical attack modeling under jamming, spoofing, tampering, and combined attacks | Attack-state simulation and multi-class mission-state recognition                                    |
| Intelligent computing                 | Graph-Temporal Transformer for UAV mission-state recognition                            | Graph-temporal learning over UAV nodes, mission time, and telemetry features                         |
| Precise computing                     | Calibrated prediction confidence                                                        | Expected Calibration Error, Brier score, confidence, and entropy                                     |
| Traceable computing                   | Perturbation-based explainability                                                       | Feature-importance ranking using macro-F1 drop                                                       |
| Robustness under uncertainty          | OOD stress testing                                                                      | Stealth jamming, slow GPS drift, intermittent tampering, delayed combined attack, unseen swarm noise |
| Active defense support                | Recovery-oriented reasoning scaffold                                                    | PPO-based recovery action space: continue, monitor, reroute, reassign, isolate node, return to base  |
| Mission assurance                     | End-to-end high-confidence decision support                                             | Prediction + confidence + OOD behavior + explanation + recovery loop                                 |

## Correct Main Claim for HCC

TRUST-Swarm provides a high-confidence graph-temporal intelligent computing framework for secure multi-UAV mission assurance by integrating mission-state recognition, calibrated confidence, OOD stress testing, traceable explanation, and recovery-oriented reasoning.

## Claims to Avoid

Do not claim:

* Graph-Temporal Transformer is the best classifier.
* TRUST-Swarm solves all OOD attack detection.
* PPO recovery is operationally deployable.
* Synthetic telemetry fully replaces real UAV field data.
* The framework is operationally validated on real UAV hardware.

## Why This Fits High-Confidence Computing

The target journal publishes work around secure computing, intelligent computing, high-confidence security/privacy, adaptive frameworks, traceable algorithms, anomaly detection, cyber-physical systems, and practical intelligent-system evaluation. TRUST-Swarm fits this direction when framed as a high-confidence secure intelligent computing framework rather than only a UAV attack-classification model.

## Immediate Next Fixes After This File

1. Rewrite the introduction using HCC framing.
2. Add an HCC-style contribution table into the manuscript.
3. Add ablation experiments.
4. Add runtime and complexity analysis.
5. Clean references for HCC.
6. Build the final HCC manuscript version.


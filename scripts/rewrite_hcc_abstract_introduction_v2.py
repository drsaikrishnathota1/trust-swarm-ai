#!/usr/bin/env python3
from pathlib import Path

abstract_path = Path("docs/hcc_title_abstract_contributions_v2.md")
intro_path = Path("docs/hcc_introduction_v2.md")
builder_path = Path("scripts/build_hcc_manuscript_v1.py")

abstract_text = """# High-Confidence Computing Target: Title, Abstract, and Contributions v2

## HCC-Framed Abstract

Multi-UAV swarm systems are increasingly deployed in surveillance, reconnaissance, infrastructure inspection, disaster response, logistics, and other cyber-physical missions where autonomous decisions must remain reliable under communication, navigation, telemetry, and environmental uncertainty. In adversarial mission settings, however, communication jamming, GPS spoofing, telemetry tampering, and combined cyber-physical attacks can corrupt the information streams required for swarm coordination and mission-state assessment. Existing UAV security and resilience studies have made important progress in attack detection, secure communication, anomaly recognition, and rule-based response. Nevertheless, many approaches remain focused on classification accuracy or isolated security functions, while providing limited support for calibrated confidence estimation, out-of-distribution (OOD) stress testing, traceable decision evidence, and recovery-oriented mission reasoning. This gap is critical for high-confidence computing because security-critical autonomous systems must evaluate not only what state is predicted, but also whether the prediction is reliable, how it behaves under unseen shifts, why the decision was produced, and how the output can support response planning.

To address this need, this paper presents TRUST-Swarm, a high-confidence graph-temporal intelligent computing framework for secure multi-UAV mission assurance under cyber-physical attacks. TRUST-Swarm represents distributed UAV telemetry as graph-temporal mission windows and evaluates a Graph-Temporal Transformer for mission-state recognition. The framework integrates five assurance-oriented components: uncertainty calibration, OOD cyber-physical stress testing, perturbation-based feature-level explanation, ablation-based framework analysis, and PPO-based recovery-reasoning support. A three-seed simulation study was conducted using 300 mission runs per seed, 240 timesteps per mission, 20 UAVs per mission, and 66,300 graph-temporal windows per seed. The Graph-Temporal Transformer achieved a mean accuracy of 0.9647 and a mean macro F1 score of 0.8750, with strong in-distribution calibration measured by an Expected Calibration Error of 0.0088 and a Brier score of 0.0531. OOD testing revealed substantial degradation under severe unseen shifts, highlighting mission-risk conditions that would be hidden by standard in-distribution accuracy. Explainability analysis identified latency, zone coverage, route deviation, mission progress, and GPS jump as key mission-risk drivers. Although the 1D-CNN baseline achieved stronger raw in-distribution classification, TRUST-Swarm contributes a broader high-confidence mission-assurance framework that combines prediction, reliability assessment, OOD vulnerability analysis, decision traceability, and recovery-oriented reasoning.

## Keywords

High-confidence computing; Multi-UAV swarm; Cyber-physical security; Mission assurance; Graph-temporal learning; Uncertainty calibration; Out-of-distribution evaluation; Explainable AI; Recovery reasoning

## HCC Contribution Table

| High-Confidence Computing Requirement | TRUST-Swarm Component | Manuscript Evidence |
| ------------------------------------- | -------------------- | ------------------- |
| Secure computing | Cyber-physical attack modeling under jamming, spoofing, tampering, and combined attacks | Multi-class mission-state simulation and recognition |
| Intelligent computing | Graph-Temporal Transformer for UAV mission-state recognition | Graph-temporal learning over UAV nodes, mission time, and telemetry features |
| Precise computing | Calibrated prediction confidence | Expected Calibration Error, Brier score, confidence, and entropy |
| Robustness under uncertainty | OOD cyber-physical stress testing | Stealth jamming, slow GPS drift, intermittent tampering, delayed combined attack, and unseen swarm noise |
| Traceable computing | Perturbation-based explainability | Feature-importance ranking using macro-F1 degradation |
| Active defense support | Recovery-oriented reasoning scaffold | PPO-based recovery action space: continue, monitor, reroute, reassign, isolate node, return to base |
| Practical feasibility | Runtime and complexity profiling | Model size, latency, throughput, training-step time, and GPU memory use |
"""

intro_text = """# High-Confidence Computing Introduction v2

## 1. Introduction

Multi-UAV swarm systems are becoming an important class of cyber-physical intelligent systems. In contrast to single-UAV platforms, a swarm can distribute sensing, increase coverage, improve redundancy, and support cooperative mission execution across large or uncertain environments. These advantages make UAV swarms attractive for surveillance, reconnaissance, border monitoring, disaster response, infrastructure inspection, logistics, search-and-rescue, and defense-oriented mission operations. In such settings, the swarm is not only a collection of flying platforms; it is a distributed decision-making system that depends on communication reliability, navigation integrity, telemetry correctness, energy awareness, coverage consistency, and mission-progress coordination. When these information streams are trustworthy, the swarm can maintain situational awareness and adapt its mission behavior. When they are disrupted, however, autonomous decisions may become unreliable even if individual UAVs remain operational [1–8].

The security challenge becomes more serious when UAV swarm missions are exposed to cyber-physical attacks. Communication jamming can increase packet loss and latency, weakening coordination among UAV nodes and delaying mission updates. GPS spoofing can create route deviation, sudden GPS jumps, and velocity inconsistency, causing the swarm to misinterpret location and movement. Telemetry tampering can distort battery state, mission progress, energy consumption, and zone coverage, making the system believe that a mission is safer or more complete than it actually is. Combined attacks can simultaneously degrade communication, navigation, and telemetry integrity. These attacks do not merely create isolated anomalies; they alter the information foundation on which autonomous mission-state prediction and response planning depend [9–14].

For this reason, secure UAV swarm mission assurance should be treated as a high-confidence computing problem. A conventional classifier can predict whether the current state resembles normal operation, jamming, spoofing, tampering, or a combined attack. However, in security-critical autonomous missions, a predicted label is not enough. The system must also estimate whether the prediction is reliable, identify when unseen attack patterns create distribution shift, explain which telemetry factors influenced the decision, and connect risk evidence to response-oriented reasoning. A UAV mission-assurance framework that reports only accuracy may appear strong under ordinary test conditions while still failing under stealthy or previously unseen cyber-physical shifts. High-confidence computing therefore requires a broader evaluation view: prediction, confidence, robustness, traceability, and recovery support must be considered together [15–24].

Existing research provides important foundations for this goal but often addresses the required capabilities separately. UAV cybersecurity and secure communication studies examine jamming, spoofing, intrusion detection, and communication protection. Time-series and deep-learning models support telemetry classification and sequential pattern recognition. Graph neural networks and transformers provide mechanisms for learning relational and temporal structure. Calibration and uncertainty methods help evaluate whether probability estimates are reliable. OOD and distribution-shift studies show that models may fail when test conditions differ from training distributions. Explainable AI methods provide ways to identify feature-level decision drivers. Reinforcement learning and safe control literature provide foundations for adaptive recovery reasoning. Although these areas are individually valuable, a gap remains: UAV swarm mission assurance still lacks an integrated high-confidence framework that combines graph-temporal prediction, calibrated reliability, OOD stress testing, traceable explanation, and recovery-oriented decision support in one evaluation pipeline [25–45].

This paper addresses that gap by presenting TRUST-Swarm, a high-confidence graph-temporal intelligent computing framework for secure multi-UAV mission assurance under cyber-physical attacks. TRUST-Swarm models distributed UAV telemetry as graph-temporal mission windows. Each window preserves three forms of structure: temporal mission evolution, UAV-node relationships, and heterogeneous telemetry-feature interactions. The framework evaluates a Graph-Temporal Transformer for mission-state recognition while also comparing temporal baselines, including LSTM, GRU, and 1D-CNN models. Unlike a pure classification study, TRUST-Swarm does not position the Graph-Temporal Transformer as the strongest raw classifier. Instead, it uses the model as the central prediction layer within a broader assurance pipeline that evaluates calibration, uncertainty, OOD vulnerability, explanation, ablation evidence, runtime feasibility, and recovery-oriented reasoning.

The proposed framework is evaluated using a controlled simulation-based multi-UAV telemetry environment. The final study uses three random seeds. For each seed, the telemetry generator produces 300 mission runs, 240 timesteps per mission, 20 UAVs per mission, 1,440,000 raw telemetry rows, and 66,300 graph-temporal mission windows. The mission-state labels include normal operation, jamming, spoofing, tampering, jamming-spoofing, jamming-tampering, spoofing-tampering, and combined attacks. The telemetry features capture communication reliability, navigation integrity, energy state, mission progress, coverage quality, and energy consumption. This design enables repeatable evaluation across cyber-physical attack states while preserving enough node-level and time-level structure to test graph-temporal mission reasoning.

The experimental results show that the Graph-Temporal Transformer achieves strong in-distribution mission-state recognition, with a mean accuracy of 0.9647 and a mean macro F1 score of 0.8750 across three seeds. The model also produces strong in-distribution calibration, with an Expected Calibration Error of 0.0088 and a Brier score of 0.0531. However, the 1D-CNN baseline achieves stronger raw in-distribution classification performance, with a mean macro F1 score of 0.9971. This finding is important because it prevents overclaiming and clarifies the contribution of TRUST-Swarm. The contribution is not that the Graph-Temporal Transformer is the strongest standalone classifier. The contribution is that TRUST-Swarm provides an integrated high-confidence mission-assurance framework that evaluates not only prediction performance, but also prediction reliability, unseen-shift vulnerability, decision traceability, framework ablation, runtime feasibility, and recovery-oriented response support.

The OOD stress-test results further motivate this high-confidence framing. Under unseen cyber-physical shifts, mission-state recognition performance decreases substantially. Intermittent tampering reduces macro F1 to 0.5965, while more severe shifts such as slow GPS drift, stealth jamming, and delayed combined attacks cause larger degradation. These results show that standard in-distribution accuracy can hide mission-risk conditions. From a high-confidence computing perspective, this is not a weakness of the study; it is a necessary finding. A trustworthy mission-assurance framework should expose where reliability degrades, rather than reporting only favorable in-distribution performance. TRUST-Swarm therefore uses OOD stress testing as an assurance mechanism to identify conditions where monitoring, escalation, or recovery reasoning may be required.

Traceability and response support are also central to the proposed framework. Perturbation-based feature-importance analysis identifies latency, zone coverage, route deviation, mission progress, and GPS jump as the most influential mission-risk drivers. These drivers are operationally meaningful because they correspond to communication degradation, mission coverage loss, navigation disruption, mission-progress interruption, and spoofing-related displacement. TRUST-Swarm further includes a PPO-based recovery-reasoning scaffold that maps prediction, confidence, entropy, and mission-risk indicators to possible response actions such as continue, monitor, reroute, reassign, isolate node, and return to base. This recovery layer is not claimed as an operational UAV controller. Rather, it demonstrates how high-confidence prediction outputs can be connected to mission-response reasoning.

The main contributions of this paper are summarized as follows:

1. A high-confidence graph-temporal intelligent computing framework is proposed for secure multi-UAV mission assurance under cyber-physical attacks. The framework integrates mission-state prediction, calibrated confidence, OOD stress testing, traceable explanation, ablation evidence, runtime profiling, and recovery-oriented reasoning.

2. A graph-temporal mission-window representation is developed to model UAV-node relationships, temporal mission evolution, and heterogeneous telemetry features. This representation allows the framework to reason over distributed swarm telemetry rather than treating mission data as ordinary flat time-series records.

3. A Graph-Temporal Transformer is evaluated for mission-state recognition under normal, jamming, spoofing, tampering, and combined attack conditions. Temporal baselines, including LSTM, GRU, and 1D-CNN, are used to clarify the difference between raw classification performance and broader high-confidence mission assurance.

4. A three-seed simulation study is conducted using 300 mission runs per seed, 240 timesteps per mission, 20 UAVs per mission, and 66,300 graph-temporal mission windows per seed. The evaluation includes in-distribution performance, calibration metrics, OOD stress testing, explainability analysis, ablation analysis, and runtime profiling.

5. The study demonstrates that secure UAV swarm mission assurance requires more than high classification accuracy. The results show the value of evaluating reliability, uncertainty, unseen-shift vulnerability, decision traceability, and recovery support as integrated high-confidence computing requirements.

The remainder of this paper is organized as follows. Section 2 reviews related work on UAV cyber-physical security, high-confidence intelligent computing, graph-temporal learning, temporal deep-learning baselines, uncertainty calibration, OOD evaluation, explainable AI, and recovery-oriented reinforcement learning. Section 3 presents the TRUST-Swarm methodology. Section 4 describes the experimental setup. Section 5 reports and discusses the results, including baseline comparison, calibration, OOD stress testing, explainability, ablation, and runtime analysis. Section 6 presents limitations and future work. Section 7 concludes the paper.
"""

abstract_path.write_text(abstract_text)
intro_path.write_text(intro_text)

# Update manuscript builder to use v2 files.
if builder_path.exists():
    b = builder_path.read_text()
    b = b.replace('ROOT / "docs" / "hcc_title_abstract_contributions_v1.md"', 'ROOT / "docs" / "hcc_title_abstract_contributions_v2.md"')
    b = b.replace('ROOT / "docs" / "hcc_introduction_v1.md"', 'ROOT / "docs" / "hcc_introduction_v2.md"')
    b = b.replace('text = text.replace("# High-Confidence Computing Target: Title, Abstract, and Contributions v1", "")',
                  'text = text.replace("# High-Confidence Computing Target: Title, Abstract, and Contributions v1", "")\\n    text = text.replace("# High-Confidence Computing Target: Title, Abstract, and Contributions v2", "")')
    b = b.replace('text = text.replace("# High-Confidence Computing Introduction v1", "")',
                  'text = text.replace("# High-Confidence Computing Introduction v1", "")\\n    text = text.replace("# High-Confidence Computing Introduction v2", "")')
    builder_path.write_text(b)

print(f"Saved: {abstract_path}")
print(f"Saved: {intro_path}")
print("Updated manuscript builder to use v2 abstract/introduction.")

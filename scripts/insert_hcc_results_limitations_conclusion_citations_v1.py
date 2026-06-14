#!/usr/bin/env python3
from pathlib import Path

results_path = Path("docs/hcc_results_discussion_v1.md")
builder_path = Path("scripts/build_hcc_manuscript_v1.py")

if not results_path.exists():
    raise FileNotFoundError(results_path)
if not builder_path.exists():
    raise FileNotFoundError(builder_path)

results = results_path.read_text()
builder = builder_path.read_text()

results_marker = "<!-- CITATIONS_INSERTED_RESULTS_V1 -->"
builder_marker = "# CITATIONS_INSERTED_LIMITATIONS_CONCLUSION_V1"

if results_marker not in results:
    replacements = {
"""This section evaluates TRUST-Swarm as a high-confidence graph-temporal intelligent computing framework for secure multi-UAV mission assurance. The evaluation focuses on five questions:""":
"""This section evaluates TRUST-Swarm as a high-confidence graph-temporal intelligent computing framework for secure multi-UAV mission assurance. The evaluation follows HCC-style framework evaluation by combining prediction, calibration, OOD stress testing, traceable explanation, recovery reasoning, ablation, and runtime feasibility evidence [R01–R03]. The evaluation focuses on five questions:""",

"""These results show that the graph-temporal prediction layer can learn meaningful mission-state patterns from UAV telemetry under cyber-physical attack conditions. The model captures mission-time evolution, UAV-node structure, and telemetry-feature interactions across communication, navigation, energy, mission-progress, and coverage signals.""":
"""These results show that the graph-temporal prediction layer can learn meaningful mission-state patterns from UAV telemetry under cyber-physical attack conditions. The model captures mission-time evolution, UAV-node structure, and telemetry-feature interactions across communication, navigation, energy, mission-progress, and coverage signals [R21–R28, R51–R59].""",

"""The baseline comparison included LSTM, GRU, and 1D-CNN models. The 1D-CNN baseline achieved the strongest in-distribution classification performance, with a mean accuracy of 0.9987 and a mean macro F1 score of 0.9971. The LSTM and GRU baselines achieved mean macro F1 scores of 0.9608 and 0.9288, respectively.""":
"""The baseline comparison included LSTM, GRU, and 1D-CNN models [R60–R63]. The 1D-CNN baseline achieved the strongest in-distribution classification performance, with a mean accuracy of 0.9987 and a mean macro F1 score of 0.9971. The LSTM and GRU baselines achieved mean macro F1 scores of 0.9608 and 0.9288, respectively.""",

"""The Graph-Temporal Transformer produced strong in-distribution calibration. Across three seeds, the model achieved a mean Expected Calibration Error of 0.0088 and a mean Brier score of 0.0531. The mean predictive confidence was 0.9601, and the mean predictive entropy was 0.0986.""":
"""The Graph-Temporal Transformer produced strong in-distribution calibration. Across three seeds, the model achieved a mean Expected Calibration Error of 0.0088 and a mean Brier score of 0.0531. The mean predictive confidence was 0.9601, and the mean predictive entropy was 0.0986 [R37–R43].""",

"""OOD stress testing revealed substantial performance degradation under unseen cyber-physical shifts. The in-distribution macro F1 score was 0.8750. Intermittent tampering reduced macro F1 to 0.5965. More severe shifts caused larger reductions: slow GPS drift achieved a macro F1 score of 0.1701, stealth jamming achieved 0.0779, and delayed combined attacks achieved 0.0521.""":
"""OOD stress testing revealed substantial performance degradation under unseen cyber-physical shifts. The in-distribution macro F1 score was 0.8750. Intermittent tampering reduced macro F1 to 0.5965. More severe shifts caused larger reductions: slow GPS drift achieved a macro F1 score of 0.1701, stealth jamming achieved 0.0779, and delayed combined attacks achieved 0.0521 [R43–R46].""",

"""Perturbation-based feature importance identified latency, zone coverage, route deviation, mission progress, and GPS jump as the most influential mission-risk drivers.""":
"""Perturbation-based feature importance identified latency, zone coverage, route deviation, mission progress, and GPS jump as the most influential mission-risk drivers [R47–R50].""",

"""TRUST-Swarm includes a PPO-based recovery-reasoning scaffold. The recovery layer receives mission-state prediction, confidence, entropy, and mission-risk indicators. It maps these inputs to recovery actions such as continue, monitor, reroute, reassign, isolate node, and return to base.""":
"""TRUST-Swarm includes a PPO-based recovery-reasoning scaffold [R64–R80]. The recovery layer receives mission-state prediction, confidence, entropy, and mission-risk indicators. It maps these inputs to recovery actions such as continue, monitor, reroute, reassign, isolate node, and return to base.""",

"""This module is not claimed as a operationally deployable UAV controller. Instead, it demonstrates how high-confidence prediction outputs can support mission-response reasoning. This is important because secure mission assurance should not stop at detection. It should connect risk recognition to response planning.""":
"""This module is not claimed as an operationally deployable UAV controller. Instead, it demonstrates how high-confidence prediction outputs can support mission-response reasoning. This is important because secure mission assurance should not stop at detection. It should connect risk recognition to response planning [R64–R80].""",

"""A final HCC ablation study was conducted on the seed-42 graph-temporal dataset using 66,300 mission windows, 20 UAV nodes, 20 timesteps, 9 telemetry features, and 8 mission-state classes. The full Graph-Temporal Transformer achieved an accuracy of 0.9579 and a macro F1 score of 0.8734.""":
"""A final HCC ablation study was conducted on the seed-42 graph-temporal dataset using 66,300 mission windows, 20 UAV nodes, 20 timesteps, 9 telemetry features, and 8 mission-state classes. The full Graph-Temporal Transformer achieved an accuracy of 0.9579 and a macro F1 score of 0.8734. The ablation design supports framework-level HCC evaluation by showing how architectural and assurance components contribute to the evidence pipeline [R01–R03, R51–R59].""",

"""Runtime and complexity profiling was conducted on an NVIDIA H200 GPU using batch size 128, 20 UAV nodes, 20 timesteps, and 9 telemetry features. The Graph-Temporal Transformer has 680,840 trainable parameters and a model size of 2.618 MB. Its inference latency was 2.267 ms per batch and 0.0177 ms per graph-temporal mission window, corresponding to approximately 56,458 windows per second.""":
"""Runtime and complexity profiling was conducted on an NVIDIA H200 GPU using batch size 128, 20 UAV nodes, 20 timesteps, and 9 telemetry features. The Graph-Temporal Transformer has 680,840 trainable parameters and a model size of 2.618 MB. Its inference latency was 2.267 ms per batch and 0.0177 ms per graph-temporal mission window, corresponding to approximately 56,458 windows per second. This supports practical feasibility evidence expected in high-confidence intelligent computing evaluations [R01–R03].""",

"""Therefore, the current results are strong enough to justify a manuscript foundation, but two additional analyses are needed before final HCC submission:

1. Ablation study to show the value of each TRUST-Swarm module.
2. Runtime and complexity analysis to show practical computing feasibility.""":
"""Therefore, the current results provide a stronger HCC manuscript foundation because the evaluation now includes mission-state recognition, baseline comparison, calibration, OOD stress testing, traceable explanation, recovery reasoning, final ablation evidence, and runtime/complexity profiling."""
    }

    for old, new in replacements.items():
        if old not in results:
            print(f"Warning: results paragraph not found, skipped: {old[:70]}...")
        results = results.replace(old, new)

    results = results.replace("operationally operationally deployable", "operationally deployable")
    results = results.rstrip() + "\n\n" + results_marker + "\n"
    results_path.write_text(results)
    print("Updated Results citations.")
else:
    print("Results citations already inserted.")

if builder_marker not in builder:
    replacements = {
"""This study has several limitations. First, the current evaluation uses controlled synthetic multi-UAV telemetry rather than field-collected UAV swarm data. The controlled benchmark enables repeatable evaluation across cyber-physical attack states, OOD stress conditions, confidence metrics, and multiple random seeds, but real-world deployment validation remains necessary.""":
"""This study has several limitations. First, the current evaluation uses controlled synthetic multi-UAV telemetry rather than field-collected UAV swarm data. The controlled benchmark enables repeatable evaluation across cyber-physical attack states, OOD stress conditions, confidence metrics, and multiple random seeds, but real-world deployment validation remains necessary [R21–R33].""",

"""Second, the OOD stress tests reveal that severe unseen cyber-physical shifts can substantially reduce mission-state recognition performance. This finding is important for high-confidence computing because it exposes hidden mission risk, but it also shows that additional OOD detection and uncertainty-monitoring mechanisms are needed.""":
"""Second, the OOD stress tests reveal that severe unseen cyber-physical shifts can substantially reduce mission-state recognition performance. This finding is important for high-confidence computing because it exposes hidden mission risk, but it also shows that additional OOD detection and uncertainty-monitoring mechanisms are needed [R43–R46].""",

"""Third, the PPO-based recovery component is evaluated as a recovery-reasoning scaffold rather than a operationally deployable UAV controller. Future work should connect the recovery layer to high-fidelity UAV swarm simulators, hardware-in-the-loop validation, and mission-level safety constraints.""":
"""Third, the PPO-based recovery component is evaluated as a recovery-reasoning scaffold rather than an operationally deployable UAV controller. Future work should connect the recovery layer to high-fidelity UAV swarm simulators, hardware-in-the-loop validation, and mission-level safety constraints [R64–R80].""",

"""Finally, future work should extend TRUST-Swarm with privacy-preserving learning, formal safety constraints, online adaptation, and human-in-the-loop mission assurance.""":
"""Finally, future work should extend TRUST-Swarm with privacy-preserving learning, formal safety constraints, online adaptation, and human-in-the-loop mission assurance [R01–R03, R68–R80].""",

"""This paper presented TRUST-Swarm, a high-confidence graph-temporal intelligent computing framework for secure multi-UAV mission assurance under cyber-physical attacks. The framework integrates graph-temporal mission-state recognition, confidence calibration, OOD cyber-physical stress testing, perturbation-based traceability, and recovery-oriented reasoning.""":
"""This paper presented TRUST-Swarm, a high-confidence graph-temporal intelligent computing framework for secure multi-UAV mission assurance under cyber-physical attacks. The framework integrates graph-temporal mission-state recognition, confidence calibration, OOD cyber-physical stress testing, perturbation-based traceability, and recovery-oriented reasoning [R01–R03, R21–R33, R37–R50, R51–R80].""",

"""The study demonstrates that secure UAV swarm mission assurance requires more than accuracy. It requires high-confidence computing mechanisms that can evaluate trustworthiness, uncertainty, robustness, traceability, and recovery support under cyber-physical mission risk.""":
"""The study demonstrates that secure UAV swarm mission assurance requires more than accuracy. It requires high-confidence computing mechanisms that can evaluate trustworthiness, uncertainty, robustness, traceability, and recovery support under cyber-physical mission risk [R01–R03]."""
    }

    for old, new in replacements.items():
        if old not in builder:
            print(f"Warning: builder paragraph not found, skipped: {old[:70]}...")
        builder = builder.replace(old, new)

    builder = builder.replace("operationally operationally deployable", "operationally deployable")
    builder += "\n" + builder_marker + "\n"
    builder_path.write_text(builder)
    print("Updated Limitations/Conclusion citations in builder.")
else:
    print("Limitations/Conclusion citations already inserted.")

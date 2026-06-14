#!/usr/bin/env python3
from pathlib import Path

path = Path("docs/hcc_experimental_setup_v1.md")
if not path.exists():
    raise FileNotFoundError(path)

text = path.read_text()
marker = "<!-- CITATIONS_INSERTED_EXPERIMENTAL_SETUP_V1 -->"

if marker in text:
    print("Experimental Setup citations already inserted. No changes made.")
    raise SystemExit(0)

replacements = {
"""This section describes the experimental setup used to evaluate TRUST-Swarm as a high-confidence graph-temporal intelligent computing framework for secure multi-UAV mission assurance. The evaluation is designed to test mission-state recognition, baseline comparison, confidence calibration, OOD vulnerability, traceable explanation, and recovery-oriented reasoning.""":
"""This section describes the experimental setup used to evaluate TRUST-Swarm as a high-confidence graph-temporal intelligent computing framework for secure multi-UAV mission assurance. The evaluation is designed to test mission-state recognition, baseline comparison, confidence calibration, OOD vulnerability, traceable explanation, and recovery-oriented reasoning [R01–R03, R37–R50, R64–R80].""",

"""A controlled simulation-based telemetry generator was used to evaluate cyber-physical mission assurance under repeatable conditions. Each seed generated:""":
"""A controlled simulation-based telemetry generator was used to evaluate cyber-physical mission assurance under repeatable conditions, motivated by UAV cyber-physical security, communication, spoofing, and tampering risks [R21–R28, R31–R33]. Each seed generated:""",

"""These classes represent communication disruption, navigation manipulation, telemetry integrity attack, and combined cyber-physical mission degradation.""":
"""These classes represent communication disruption, navigation manipulation, telemetry integrity attack, and combined cyber-physical mission degradation [R24–R26, R31–R33].""",

"""These features capture communication reliability, navigation integrity, energy state, mission progress, and coverage quality.""":
"""These features capture communication reliability, navigation integrity, energy state, mission progress, and coverage quality [R21–R28, R31–R33].""",

"""Raw telemetry is transformed into graph-temporal mission windows using a sliding temporal window. Each mission-window sample is represented as:""":
"""Raw telemetry is transformed into graph-temporal mission windows using a sliding temporal window to preserve temporal mission evolution and UAV-node structure [R51–R59]. Each mission-window sample is represented as:""",

"""The evaluation includes the proposed Graph-Temporal Transformer and three temporal baseline models:""":
"""The evaluation includes the proposed Graph-Temporal Transformer and three temporal baseline models based on transformer, graph-learning, recurrent, and convolutional sequence-modeling foundations [R51–R63]:""",

"""Macro-averaged metrics were emphasized because the cyber-physical attack classes are imbalanced.""":
"""Macro-averaged metrics were emphasized because the cyber-physical attack classes are imbalanced and mission-state performance must be interpreted beyond raw accuracy.""",

"""The confidence-aware reliability layer was evaluated using:""":
"""The confidence-aware reliability layer was evaluated using calibration and uncertainty metrics commonly used for probabilistic reliability assessment [R37–R43]:""",

"""OOD stress testing evaluated model behavior under unseen cyber-physical mission shifts. The OOD conditions were:""":
"""OOD stress testing evaluated model behavior under unseen cyber-physical mission shifts, following the broader motivation of OOD and distribution-shift evaluation [R43–R46]. The OOD conditions were:""",

"""The purpose of this evaluation is not to claim perfect OOD detection. Instead, it identifies mission-risk conditions where model performance degrades or confidence becomes unreliable.""":
"""The purpose of this evaluation is not to claim complete OOD reliability. Instead, it identifies mission-risk conditions where model performance degrades or confidence becomes unreliable [R43–R46].""",

"""Traceability was evaluated using perturbation-based feature importance. First, the baseline macro F1 was computed. Then, each telemetry feature was replaced by its mean value, and macro F1 was recomputed.""":
"""Traceability was evaluated using perturbation-based feature importance, motivated by explainability and feature-attribution methods for trustworthy AI [R47–R50]. First, the baseline macro F1 was computed. Then, each telemetry feature was replaced by its mean value, and macro F1 was recomputed.""",

"""The PPO-based recovery module was evaluated as a recovery-reasoning scaffold. The action space included:""":
"""The PPO-based recovery module was evaluated as a recovery-reasoning scaffold, motivated by reinforcement learning, safe RL, multi-agent decision support, and cyber-physical resilience literature [R64–R80]. The action space included:""",

"""This module is included to demonstrate how prediction, confidence, entropy, and mission-risk indicators can support mission-response reasoning. It is not claimed as a deployment-ready UAV controller.""":
"""This module is included to demonstrate how prediction, confidence, entropy, and mission-risk indicators can support mission-response reasoning. It is not claimed as an operationally deployable UAV controller.""",

"""To better match High-Confidence Computing standards, two additional analyses should be added before final submission:

1. ablation study
2. runtime and complexity analysis

These analyses will strengthen the practical high-confidence computing contribution.""":
"""Final HCC-aligned evidence includes ablation analysis and runtime/complexity profiling. The ablation study evaluates the contribution of UAV-node attention, temporal transformer reasoning, and assurance modules. The runtime analysis reports model size, latency, throughput, train-step time, and GPU memory use to support practical feasibility claims."""
}

for old, new in replacements.items():
    if old not in text:
        print(f"Warning: paragraph not found, skipped: {old[:70]}...")
    text = text.replace(old, new)

text = text.rstrip() + "\n\n" + marker + "\n"
path.write_text(text)
print("Updated Experimental Setup citations.")

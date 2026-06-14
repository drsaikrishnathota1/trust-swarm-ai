#!/usr/bin/env python3
from pathlib import Path

path = Path("docs/hcc_introduction_v1.md")
if not path.exists():
    raise FileNotFoundError(path)

text = path.read_text()

marker = "<!-- CITATIONS_INSERTED_INTRO_V1 -->"
if marker in text:
    print("Introduction citations already inserted. No changes made.")
    raise SystemExit(0)

replacements = {
"""Multi-UAV swarm systems are increasingly used in surveillance, reconnaissance, disaster response, infrastructure monitoring, logistics, and cyber-physical mission operations. Compared with single-UAV platforms, UAV swarms provide distributed sensing, wider coverage, redundancy, and adaptive mission execution. However, these advantages depend on the reliability of communication, navigation, telemetry integrity, energy awareness, and mission-progress monitoring. When these information streams are disrupted, autonomous mission decisions may become unreliable.""":
"""Multi-UAV swarm systems are increasingly used in surveillance, reconnaissance, disaster response, infrastructure monitoring, logistics, and cyber-physical mission operations. Compared with single-UAV platforms, UAV swarms provide distributed sensing, wider coverage, redundancy, and adaptive mission execution. However, these advantages depend on the reliability of communication, navigation, telemetry integrity, energy awareness, and mission-progress monitoring. When these information streams are disrupted, autonomous mission decisions may become unreliable [R21, R23, R27, R28].""",

"""Cyber-physical attacks create a major challenge for secure UAV swarm mission assurance. Communication jamming can increase latency and packet loss, reducing coordination among UAV nodes. GPS spoofing can cause route deviation, GPS jumps, and velocity inconsistency. Telemetry tampering can distort battery state, mission progress, energy consumption, or zone coverage. Combined attacks can simultaneously degrade communication, navigation, and mission integrity. These disruptions create a high-confidence computing problem: the system must not only predict mission state, but also evaluate whether the prediction can be trusted.""":
"""Cyber-physical attacks create a major challenge for secure UAV swarm mission assurance. Communication jamming can increase latency and packet loss, reducing coordination among UAV nodes. GPS spoofing can cause route deviation, GPS jumps, and velocity inconsistency. Telemetry tampering can distort battery state, mission progress, energy consumption, or zone coverage. Combined attacks can simultaneously degrade communication, navigation, and mission integrity. These disruptions create a high-confidence computing problem: the system must not only predict mission state, but also evaluate whether the prediction can be trusted [R24, R25, R26, R31, R32, R33].""",

"""Existing UAV security and resilience methods often focus on attack detection, secure communication, intrusion detection, or rule-based recovery. Although these methods are valuable, many of them remain limited in four ways. First, they often treat mission telemetry as ordinary time-series data rather than modeling UAV-node relationships and mission evolution together. Second, they emphasize classification accuracy without calibrated confidence estimation. Third, they rarely evaluate model behavior under unseen out-of-distribution cyber-physical shifts. Fourth, they provide limited traceability and limited connection between prediction outputs and recovery-oriented mission response.""":
"""Existing UAV security and resilience methods often focus on attack detection, secure communication, intrusion detection, or rule-based recovery. Although these methods are valuable, many of them remain limited in four ways. First, they often treat mission telemetry as ordinary time-series data rather than modeling UAV-node relationships and mission evolution together. Second, they emphasize classification accuracy without calibrated confidence estimation. Third, they rarely evaluate model behavior under unseen out-of-distribution cyber-physical shifts. Fourth, they provide limited traceability and limited connection between prediction outputs and recovery-oriented mission response [R37, R41, R43, R44, R47, R48, R64, R66, R76, R80].""",

"""These limitations are critical for high-confidence intelligent systems. In secure autonomous missions, a prediction is not sufficient by itself. A mission-assurance framework should answer five questions: what mission state is predicted, how reliable the prediction is, how the system behaves under unseen cyber-physical shifts, which telemetry factors influenced the decision, and how the output can support recovery reasoning. Therefore, secure UAV swarm mission assurance should be framed as a high-confidence intelligent computing problem rather than only an attack-classification problem.""":
"""These limitations are critical for high-confidence intelligent systems. In secure autonomous missions, a prediction is not sufficient by itself. A mission-assurance framework should answer five questions: what mission state is predicted, how reliable the prediction is, how the system behaves under unseen cyber-physical shifts, which telemetry factors influenced the decision, and how the output can support recovery reasoning. Therefore, secure UAV swarm mission assurance should be framed as a high-confidence intelligent computing problem rather than only an attack-classification problem [R01, R02, R03, R34, R35, R36].""",

"""To address this need, this paper presents TRUST-Swarm, a high-confidence graph-temporal intelligent computing framework for secure multi-UAV mission assurance under cyber-physical attacks. TRUST-Swarm represents distributed UAV telemetry as graph-temporal mission windows and evaluates a Graph-Temporal Transformer for mission-state recognition. The framework further integrates uncertainty calibration, OOD stress testing, perturbation-based explainability, and recovery-oriented reasoning.""":
"""To address this need, this paper presents TRUST-Swarm, a high-confidence graph-temporal intelligent computing framework for secure multi-UAV mission assurance under cyber-physical attacks. TRUST-Swarm represents distributed UAV telemetry as graph-temporal mission windows and evaluates a Graph-Temporal Transformer for mission-state recognition. The framework further integrates uncertainty calibration, OOD stress testing, perturbation-based explainability, and recovery-oriented reasoning [R51, R53, R54, R56, R58, R37, R41, R43, R44, R47, R48, R66]."""
}

changed = False
for old, new in replacements.items():
    if old in text:
        text = text.replace(old, new)
        changed = True
    else:
        print("Warning: paragraph not found, skipped one replacement.")

text = text.rstrip() + "\n\n" + marker + "\n"
path.write_text(text)

print("Updated introduction citations." if changed else "No matching paragraphs changed.")

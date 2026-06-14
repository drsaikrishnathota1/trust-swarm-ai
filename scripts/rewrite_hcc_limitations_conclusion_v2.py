#!/usr/bin/env python3
from pathlib import Path

section_path = Path("docs/hcc_limitations_conclusion_v2.md")
builder_path = Path("scripts/build_hcc_manuscript_v1.py")

section_text = """# High-Confidence Computing Limitations and Conclusion v2

## 6. Limitations and future work

Although TRUST-Swarm provides a high-confidence graph-temporal intelligent computing framework for secure multi-UAV mission assurance, several limitations must be acknowledged. These limitations are important because the paper is positioned as a mission-assurance study rather than as a claim of operational UAV deployment. A high-confidence computing contribution should clearly state the boundary between repeatable experimental evidence and real-world deployment readiness.

First, the current evaluation uses controlled synthetic multi-UAV telemetry rather than field-collected UAV swarm data. This design enables repeatable testing across attack states, random seeds, calibration metrics, OOD conditions, feature perturbations, ablation settings, and runtime profiling. It also allows cyber-physical degradation patterns to be injected in a controlled way. However, synthetic telemetry cannot fully represent real UAV communication channels, weather effects, mobility constraints, sensor imperfections, flight-controller behavior, heterogeneous hardware, and mission-environment complexity. Future work should evaluate TRUST-Swarm using high-fidelity UAV simulators, hardware-in-the-loop testbeds, and real UAV swarm telemetry.

Second, the current attack model includes jamming, spoofing, tampering, and combined cyber-physical attack states, but real adversaries may adapt their strategies over time. For example, an attacker may use low-power jamming, gradual GPS drift, intermittent telemetry corruption, coordinated multi-node compromise, or deception patterns that change according to mission behavior. The OOD stress tests in this study intentionally show that severe unseen shifts can reduce performance. This is not treated as a hidden weakness; it is treated as evidence that deployment-oriented mission assurance requires explicit OOD monitoring. Future work should integrate online OOD detectors, adaptive uncertainty thresholds, continual learning, and adversarial training strategies.

Third, the Graph-Temporal Transformer is evaluated as the prediction layer of an assurance framework, not as a universally superior classifier. The baseline comparison shows that the 1D-CNN achieves stronger raw in-distribution classification performance. This finding limits any claim of classifier superiority. The contribution of TRUST-Swarm is instead the integrated evaluation of prediction, calibration, OOD vulnerability, explanation, ablation evidence, runtime feasibility, and recovery-oriented reasoning. Future work should investigate hybrid models that combine the efficiency of temporal CNNs with graph-temporal attention and calibrated uncertainty estimation.

Fourth, the PPO-based recovery component is evaluated as a recovery-reasoning scaffold rather than an operational UAV controller. The action space of continue, monitor, reroute, reassign, isolate node, and return to base is designed to demonstrate how prediction, confidence, entropy, and mission-risk indicators can support response reasoning. It does not replace flight-control logic, certified autonomy, human authorization, or safety-critical mission planning. Future work should connect the recovery layer to realistic swarm simulators, formal safety constraints, control-theoretic verification, and human-in-the-loop decision workflows.

Fifth, the current graph-temporal representation uses a fixed number of UAV nodes, a fixed telemetry feature set, and a fixed temporal window length. Real missions may involve variable swarm sizes, dynamic communication topology, missing telemetry, heterogeneous UAV roles, and mission-dependent sensor streams. Future work should extend TRUST-Swarm to dynamic graphs, variable-size swarms, missing-data robustness, topology-aware attention, and multi-modal telemetry integration.

Sixth, the current study does not fully address privacy-preserving distributed learning. In real UAV swarm and defense-oriented environments, telemetry may be sensitive and distributed across edge devices, command stations, or organizational boundaries. Future work should investigate federated learning, secure aggregation, differential privacy, and trusted execution environments for UAV mission assurance. These additions would strengthen the secure computing dimension of the framework.

Finally, runtime profiling was conducted in a GPU-based environment and supports computational feasibility at the model-evaluation level. However, practical deployment would require evaluation on embedded edge hardware, onboard compute platforms, bandwidth-limited communication links, and energy-constrained mission settings. Future work should measure end-to-end latency from telemetry capture to prediction, explanation, recovery recommendation, and operator response.

## 7. Conclusion

This paper presented TRUST-Swarm, a high-confidence graph-temporal intelligent computing framework for secure multi-UAV mission assurance under cyber-physical attacks. The framework models distributed UAV telemetry as graph-temporal mission windows and integrates mission-state recognition, confidence calibration, OOD cyber-physical stress testing, perturbation-based explainability, ablation analysis, runtime profiling, and recovery-oriented reasoning.

The experimental results show that the Graph-Temporal Transformer achieves strong mission-state recognition and reliable in-distribution calibration. Across the three-seed evaluation, the model achieves strong accuracy and macro-F1 performance while producing low Expected Calibration Error and Brier score. At the same time, the baseline comparison shows that the 1D-CNN achieves stronger raw in-distribution classification performance. This result clarifies the correct contribution of the paper: TRUST-Swarm is not positioned as the best standalone classifier. It is positioned as a high-confidence secure intelligent computing framework that evaluates the reliability, robustness, traceability, and response usefulness of mission-state prediction.

The OOD stress-test results show that unseen cyber-physical shifts can substantially degrade performance. This finding is central to the high-confidence computing narrative. A trustworthy mission-assurance framework should not hide failure conditions; it should expose them and provide evidence for monitoring, escalation, and recovery-oriented reasoning. The explainability results further strengthen the framework by identifying latency, zone coverage, route deviation, mission progress, and GPS jump as mission-relevant decision drivers. These features connect model behavior to operationally meaningful UAV mission risks.

Overall, the study demonstrates that secure UAV swarm mission assurance requires more than high classification accuracy. It requires integrated evidence about prediction reliability, uncertainty, unseen-shift vulnerability, decision traceability, computational feasibility, and response support. TRUST-Swarm contributes this integrated framework and provides a foundation for future research in high-confidence, secure, and intelligent UAV swarm computing.
"""

section_path.write_text(section_text)

# Update manuscript builder:
# 1. Add limitations/conclusion as a normal part.
# 2. Remove old hardcoded Limitations/Conclusion block.
# 3. Add heading cleanup rule.
b = builder_path.read_text()

part_line = '    ROOT / "docs" / "hcc_limitations_conclusion_v2.md",'
if part_line not in b:
    b = b.replace(
        '    ROOT / "docs" / "hcc_results_discussion_v2.md",\n]',
        '    ROOT / "docs" / "hcc_results_discussion_v2.md",\n'
        '    ROOT / "docs" / "hcc_limitations_conclusion_v2.md",\n]'
    )

start = b.find("# Add missing HCC-ready manuscript sections.")
end = b.find("OUT.parent.mkdir", start)
if start != -1 and end != -1:
    b = b[:start] + b[end:]

cleanup_line = '    text = text.replace("# High-Confidence Computing Limitations and Conclusion v2", "")'
if cleanup_line not in b:
    lines = b.splitlines()
    inserted = False
    for i, line in enumerate(lines):
        if 'text = text.replace("# High-Confidence Computing Results and Discussion v2", "")' in line:
            lines.insert(i + 1, cleanup_line)
            inserted = True
            break
    if inserted:
        b = "\n".join(lines) + "\n"

builder_path.write_text(b)

print(f"Saved: {section_path}")
print("Updated builder: added limitations/conclusion v2 and removed old hardcoded section.")

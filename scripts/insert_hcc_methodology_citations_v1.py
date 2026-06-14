#!/usr/bin/env python3
from pathlib import Path

path = Path("docs/hcc_methodology_v1.md")
if not path.exists():
    raise FileNotFoundError(path)

text = path.read_text()
marker = "<!-- CITATIONS_INSERTED_METHODOLOGY_V1 -->"

if marker in text:
    print("Methodology citations already inserted. No changes made.")
    raise SystemExit(0)

replacements = {
"""This section presents TRUST-Swarm as a high-confidence graph-temporal intelligent computing framework for secure multi-UAV mission assurance under cyber-physical attacks. The framework is designed to support secure prediction, calibrated confidence, OOD vulnerability analysis, traceable explanation, and recovery-oriented reasoning.""":
"""This section presents TRUST-Swarm as a high-confidence graph-temporal intelligent computing framework for secure multi-UAV mission assurance under cyber-physical attacks. The framework is designed to support secure prediction, calibrated confidence, OOD vulnerability analysis, traceable explanation, and recovery-oriented reasoning [R01–R03, R21–R33, R37–R50, R64–R80].""",

"""A controlled simulation-based telemetry generator is used to create multi-UAV cyber-physical mission scenarios. Each mission contains a swarm of UAVs operating across mission time under normal or adversarial conditions.""":
"""A controlled simulation-based telemetry generator is used to create multi-UAV cyber-physical mission scenarios. Each mission contains a swarm of UAVs operating across mission time under normal or adversarial conditions [R21–R28, R31–R33].""",

"""Raw UAV telemetry is converted into graph-temporal mission windows. Each sample is represented as:""":
"""Raw UAV telemetry is converted into graph-temporal mission windows to preserve node-level and temporal mission structure [R51–R59]. Each sample is represented as:""",

"""The Graph-Temporal Transformer is used as the main intelligent prediction model. The model receives an input tensor with shape:""":
"""The Graph-Temporal Transformer is used as the main intelligent prediction model, drawing on attention, transformer, graph neural network, and temporal graph learning foundations [R51, R53, R54, R56, R58]. The model receives an input tensor with shape:""",

"""Three temporal baseline models are evaluated:""":
"""Three temporal baseline models are evaluated to compare TRUST-Swarm against recurrent and convolutional sequence-learning baselines [R60–R63]:""",

"""High-confidence computing requires reliable prediction confidence. TRUST-Swarm evaluates prediction reliability using:""":
"""High-confidence computing requires reliable prediction confidence. TRUST-Swarm evaluates prediction reliability using calibration and uncertainty metrics commonly used to assess probabilistic prediction reliability [R37–R43]:""",

"""Operational UAV swarms may face unseen cyber-physical shifts not represented during training. TRUST-Swarm evaluates OOD behavior under five stress conditions:""":
"""Operational UAV swarms may face unseen cyber-physical shifts not represented during training. TRUST-Swarm evaluates OOD behavior under five stress conditions, motivated by OOD and dataset-shift evaluation literature [R43–R46]:""",

"""TRUST-Swarm uses perturbation-based feature importance to provide traceable mission-risk evidence. First, baseline macro F1 is computed. Then, each telemetry feature is replaced with its mean value, and macro F1 is recomputed.""":
"""TRUST-Swarm uses perturbation-based feature importance to provide traceable mission-risk evidence, following the broader motivation of explainability and feature-attribution methods in trustworthy AI [R47–R50]. First, baseline macro F1 is computed. Then, each telemetry feature is replaced with its mean value, and macro F1 is recomputed.""",

"""TRUST-Swarm includes a PPO-based recovery-reasoning scaffold. The recovery layer receives mission-state predictions, confidence scores, entropy, and mission-risk indicators.""":
"""TRUST-Swarm includes a PPO-based recovery-reasoning scaffold motivated by reinforcement learning, safe RL, multi-agent decision support, and cyber-physical resilience literature [R64–R80]. The recovery layer receives mission-state predictions, confidence scores, entropy, and mission-risk indicators.""",

"""This methodology follows the High-Confidence Computing style of presenting a unified framework rather than an isolated model.""":
"""This methodology follows the High-Confidence Computing style of presenting a unified framework rather than an isolated model [R01–R03]."""
}

for old, new in replacements.items():
    if old not in text:
        print(f"Warning: paragraph not found, skipped: {old[:70]}...")
    text = text.replace(old, new)

text = text.rstrip() + "\n\n" + marker + "\n"
path.write_text(text)
print("Updated Methodology citations.")

#!/usr/bin/env python3
from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

FIG = Path("figures/hcc")
DOCS = Path("docs")
TABLES = Path("docs/tables")
FIG.mkdir(parents=True, exist_ok=True)
TABLES.mkdir(parents=True, exist_ok=True)

plt.rcParams["font.family"] = "DejaVu Sans"
plt.rcParams["figure.dpi"] = 220

def savefig(name):
    path = FIG / name
    plt.tight_layout()
    plt.savefig(path, bbox_inches="tight", dpi=300)
    plt.close()
    print(f"Saved {path}")

def box(ax, xy, w, h, text, fc="#f4f8ff"):
    x, y = xy
    p = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.03",
                       linewidth=1.2, edgecolor="#2d3e50", facecolor=fc)
    ax.add_patch(p)
    ax.text(x + w/2, y + h/2, text, ha="center", va="center", fontsize=9, wrap=True)

def arrow(ax, start, end):
    ax.add_patch(FancyArrowPatch(start, end, arrowstyle="->", mutation_scale=14,
                                 linewidth=1.2, color="#2d3e50"))

# Fig. 1 framework architecture
fig, ax = plt.subplots(figsize=(12, 6))
ax.axis("off")
box(ax, (0.03, 0.62), 0.18, 0.18, "Multi-UAV\nTelemetry\nCommunication\nNavigation\nMission Progress", "#eaf2ff")
box(ax, (0.28, 0.62), 0.18, 0.18, "Graph-Temporal\nMission Windows\nT × N × F", "#eafaf1")
box(ax, (0.53, 0.62), 0.18, 0.18, "Graph-Temporal\nTransformer\nMission-State\nPrediction", "#fff7e6")
box(ax, (0.78, 0.62), 0.18, 0.18, "Confidence +\nCalibration\nECE / Brier /\nEntropy", "#f9eaff")
box(ax, (0.28, 0.22), 0.18, 0.18, "OOD Stress\nTesting\nStealth / Drift /\nTampering", "#fff0f0")
box(ax, (0.53, 0.22), 0.18, 0.18, "Traceability\nFeature\nImportance", "#eef9ff")
box(ax, (0.78, 0.22), 0.18, 0.18, "Recovery\nReasoning\nMonitor / Reroute /\nIsolate / RTB", "#f2f2f2")
arrow(ax, (0.21, 0.71), (0.28, 0.71))
arrow(ax, (0.46, 0.71), (0.53, 0.71))
arrow(ax, (0.71, 0.71), (0.78, 0.71))
arrow(ax, (0.62, 0.62), (0.37, 0.40))
arrow(ax, (0.62, 0.62), (0.62, 0.40))
arrow(ax, (0.87, 0.62), (0.87, 0.40))
ax.text(0.5, 0.95, "Fig. 1. TRUST-Swarm high-confidence mission-assurance framework", ha="center", fontsize=13, fontweight="bold")
savefig("fig1_trust_swarm_framework.png")

# Fig. 2 graph-temporal tensor
fig, ax = plt.subplots(figsize=(9, 5))
ax.axis("off")
for i in range(5):
    ax.add_patch(FancyBboxPatch((0.12 + i*0.06, 0.18 + i*0.04), 0.52, 0.44,
                                boxstyle="round,pad=0.02", linewidth=1,
                                edgecolor="#34495e", facecolor="#eaf2ff", alpha=0.65))
ax.text(0.43, 0.46, "20 UAV nodes × 9 telemetry features", ha="center", fontsize=11, fontweight="bold")
ax.text(0.43, 0.36, "per timestep", ha="center", fontsize=10)
ax.annotate("Temporal window T = 20", xy=(0.72, 0.45), xytext=(0.72, 0.75),
            arrowprops=dict(arrowstyle="->"), ha="center", fontsize=10)
ax.annotate("Node dimension N = 20", xy=(0.20, 0.20), xytext=(0.18, 0.05),
            arrowprops=dict(arrowstyle="->"), ha="center", fontsize=10)
ax.annotate("Feature dimension F = 9", xy=(0.63, 0.19), xytext=(0.78, 0.07),
            arrowprops=dict(arrowstyle="->"), ha="center", fontsize=10)
ax.text(0.5, 0.95, "Fig. 2. Graph-temporal mission-window representation", ha="center", fontsize=13, fontweight="bold")
savefig("fig2_graph_temporal_window.png")

# Fig. 3 main model performance comparison
perf = pd.DataFrame({
    "Model": ["Graph-Temporal Transformer", "1D-CNN"],
    "Macro F1": [0.8750, 0.9971],
    "Accuracy": [0.9647, np.nan],
})
fig, ax = plt.subplots(figsize=(8, 4.5))
ax.bar(perf["Model"], perf["Macro F1"])
ax.set_ylim(0, 1.05)
ax.set_ylabel("Macro F1")
ax.set_title("Fig. 3. In-distribution macro-F1 comparison")
for i, v in enumerate(perf["Macro F1"]):
    ax.text(i, v + 0.02, f"{v:.4f}", ha="center", fontsize=9)
ax.tick_params(axis="x", rotation=10)
savefig("fig3_indistribution_macro_f1.png")

# Fig. 4 OOD stress-test chart
ood = pd.DataFrame({
    "Condition": ["In-distribution", "Intermittent tampering"],
    "Macro F1": [0.8750, 0.5965],
})
fig, ax = plt.subplots(figsize=(8, 4.5))
ax.bar(ood["Condition"], ood["Macro F1"])
ax.set_ylim(0, 1.0)
ax.set_ylabel("Macro F1")
ax.set_title("Fig. 4. OOD stress-test degradation")
for i, v in enumerate(ood["Macro F1"]):
    ax.text(i, v + 0.02, f"{v:.4f}", ha="center", fontsize=9)
savefig("fig4_ood_stress_degradation.png")

# Fig. 5 calibration summary
cal = pd.DataFrame({
    "Metric": ["ECE", "Brier score"],
    "Value": [0.0088, 0.0531],
})
fig, ax = plt.subplots(figsize=(7, 4))
ax.bar(cal["Metric"], cal["Value"])
ax.set_ylabel("Value")
ax.set_title("Fig. 5. In-distribution calibration evidence")
for i, v in enumerate(cal["Value"]):
    ax.text(i, v + 0.003, f"{v:.4f}", ha="center", fontsize=9)
savefig("fig5_calibration_evidence.png")

# Fig. 6 ablation study
abl = pd.DataFrame({
    "Variant": ["Full GTT", "No UAV-node attention", "No temporal transformer"],
    "Macro F1": [0.8734, 0.7903, 0.8237],
})
fig, ax = plt.subplots(figsize=(9, 4.8))
ax.bar(abl["Variant"], abl["Macro F1"])
ax.set_ylim(0, 1.0)
ax.set_ylabel("Macro F1")
ax.set_title("Fig. 6. Ablation evidence for graph-temporal components")
for i, v in enumerate(abl["Macro F1"]):
    ax.text(i, v + 0.02, f"{v:.4f}", ha="center", fontsize=9)
ax.tick_params(axis="x", rotation=12)
savefig("fig6_ablation_evidence.png")

# Fig. 7 feature importance as ordinal evidence
features = pd.DataFrame({
    "Feature": ["latency_ms", "zone_coverage", "route_deviation_m", "mission_progress", "gps_jump_m"],
    "Ordinal rank score": [5, 4, 3, 2, 1],
})
fig, ax = plt.subplots(figsize=(8.5, 4.8))
ax.barh(features["Feature"][::-1], features["Ordinal rank score"][::-1])
ax.set_xlabel("Ordinal importance rank")
ax.set_title("Fig. 7. Top mission-risk telemetry drivers")
savefig("fig7_feature_importance_rank.png")

# Fig. 8 runtime profile
runtime = pd.DataFrame({
    "Metric": ["Params (M)", "Model size (MB)", "Batch latency (ms)", "Sample latency (ms)"],
    "Value": [0.68084, 2.618, 2.267, 0.0177],
})
fig, ax = plt.subplots(figsize=(8.5, 4.8))
ax.bar(runtime["Metric"], runtime["Value"])
ax.set_title("Fig. 8. Runtime and complexity profile")
ax.set_ylabel("Value")
ax.tick_params(axis="x", rotation=15)
for i, v in enumerate(runtime["Value"]):
    ax.text(i, v + max(runtime["Value"])*0.02, f"{v:g}", ha="center", fontsize=8)
savefig("fig8_runtime_profile.png")

# Polished evidence tables in markdown
tables_md = """# HCC Publication-Quality Evidence Tables v1

## Table 1. Positioning of TRUST-Swarm against related research directions

| Research direction | Main focus | Common limitation | TRUST-Swarm positioning |
| --- | --- | --- | --- |
| UAV cybersecurity | Jamming, spoofing, tampering, secure communication, attack detection | Often focused on isolated attack families or link protection | Models multiple cyber-physical mission states and combined attacks |
| Temporal deep learning | LSTM, GRU, CNN, transformer variants | Often emphasizes raw accuracy only | Uses baselines but frames contribution as mission assurance |
| Graph-temporal learning | Node-time relational modeling | Often not connected to calibration, OOD, and recovery | Uses graph-temporal windows inside a full assurance pipeline |
| Calibration and uncertainty | Probability reliability | Often evaluated separately from response support | Integrates ECE, Brier score, confidence, and entropy |
| OOD robustness | Distribution-shift testing | Often not linked to mission response | Uses cyber-physical OOD stress tests to expose risk |
| Explainable AI | Feature attribution | May not connect to operational telemetry meaning | Identifies mission-risk telemetry drivers |
| Reinforcement learning | Adaptive response | Often separated from prediction confidence | Adds PPO-based recovery-reasoning scaffold |

## Table 2. Simulation and dataset configuration

| Parameter | Value |
| --- | ---: |
| Random seeds | 42, 123, 2026 |
| Mission runs per seed | 300 |
| Timesteps per mission | 240 |
| UAV nodes per mission | 20 |
| Raw telemetry rows per seed | 1,440,000 |
| Graph-temporal windows per seed | 66,300 |
| Window tensor shape | 20 × 20 × 9 |
| Mission-state classes | 8 |

## Table 3. Main in-distribution performance evidence

| Model | Accuracy | Macro F1 | Interpretation |
| --- | ---: | ---: | --- |
| Graph-Temporal Transformer | 0.9647 | 0.8750 | Strong prediction layer with calibration and assurance evidence |
| 1D-CNN | Not reported here | 0.9971 | Strongest raw in-distribution classifier in current evaluation |

## Table 4. Calibration evidence

| Metric | Value | Interpretation |
| --- | ---: | --- |
| Expected Calibration Error | 0.0088 | Strong alignment between confidence and empirical correctness |
| Brier score | 0.0531 | Strong probabilistic prediction quality |

## Table 5. OOD stress-test evidence

| Condition | Macro F1 | Interpretation |
| --- | ---: | --- |
| In-distribution test | 0.8750 | Strong normal test performance |
| Intermittent tampering | 0.5965 | Visible degradation under unseen shift |
| Severe unseen shifts | Degraded | Requires monitoring, escalation, or recovery reasoning |

## Table 6. Ablation evidence

| Variant | Macro F1 | Interpretation |
| --- | ---: | --- |
| Full Graph-Temporal Transformer | 0.8734 | Full graph-temporal reasoning |
| Without UAV-node attention | 0.7903 | Node interaction modeling is important |
| Without temporal transformer | 0.8237 | Temporal reasoning contributes to performance |

## Table 7. Runtime and complexity evidence

| Metric | Value |
| --- | ---: |
| Trainable parameters | 680,840 |
| Model size | 2.618 MB |
| Batch inference latency | 2.267 ms |
| Sample inference latency | 0.0177 ms |
| Throughput | 56,458 windows/sec |
| Training-step time | 9.938 ms |
"""

Path("docs/tables/hcc_publication_evidence_tables_v1.md").write_text(tables_md)
print("Saved docs/tables/hcc_publication_evidence_tables_v1.md")

# Insert a figure/evidence block into methodology/results docs if missing
method = Path("docs/hcc_methodology_v2.md")
m = method.read_text()
if "![Fig. 1. TRUST-Swarm high-confidence mission-assurance framework]" not in m:
    m = m.replace(
        "Fig. 1 illustrates the TRUST-Swarm framework architecture.",
        "Fig. 1 illustrates the TRUST-Swarm framework architecture.\n\n![Fig. 1. TRUST-Swarm high-confidence mission-assurance framework](../figures/hcc/fig1_trust_swarm_framework.png)\n\n![Fig. 2. Graph-temporal mission-window representation](../figures/hcc/fig2_graph_temporal_window.png)\n\n"
    )
method.write_text(m)

results = Path("docs/hcc_results_discussion_v2.md")
r = results.read_text()
insert = """
![Fig. 3. In-distribution macro-F1 comparison](../figures/hcc/fig3_indistribution_macro_f1.png)

![Fig. 4. OOD stress-test degradation](../figures/hcc/fig4_ood_stress_degradation.png)

![Fig. 5. In-distribution calibration evidence](../figures/hcc/fig5_calibration_evidence.png)

![Fig. 6. Ablation evidence for graph-temporal components](../figures/hcc/fig6_ablation_evidence.png)

![Fig. 7. Top mission-risk telemetry drivers](../figures/hcc/fig7_feature_importance_rank.png)

![Fig. 8. Runtime and complexity profile](../figures/hcc/fig8_runtime_profile.png)

"""
if "fig3_indistribution_macro_f1.png" not in r:
    r = r.replace("### 5.1. In-distribution mission-state recognition", insert + "\n### 5.1. In-distribution mission-state recognition")
results.write_text(r)

print("Inserted figure references into methodology/results docs.")

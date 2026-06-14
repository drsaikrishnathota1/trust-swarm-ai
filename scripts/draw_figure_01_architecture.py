from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

OUT_DIR = Path("figures/architecture")
OUT_DIR.mkdir(parents=True, exist_ok=True)

def box(ax, x, y, w, h, title, body, fc="#EEF5FF", ec="#2B5C8A"):
    patch = FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0.02,rounding_size=0.03",
        linewidth=1.4,
        edgecolor=ec,
        facecolor=fc
    )
    ax.add_patch(patch)
    ax.text(x + w/2, y + h - 0.08, title, ha="center", va="top",
            fontsize=10, fontweight="bold", color="#12344D")
    ax.text(x + 0.04, y + h - 0.18, body, ha="left", va="top",
            fontsize=8.2, color="#1F2933", linespacing=1.25)
    return patch

def arrow(ax, x1, y1, x2, y2):
    ax.add_patch(FancyArrowPatch(
        (x1, y1), (x2, y2),
        arrowstyle="->",
        mutation_scale=14,
        linewidth=1.4,
        color="#334E68"
    ))

fig, ax = plt.subplots(figsize=(18, 8))
ax.set_xlim(0, 18)
ax.set_ylim(0, 8)
ax.axis("off")

ax.text(
    9, 7.65,
    "TRUST-Swarm: Graph-Temporal Multi-Source Information Fusion for UAV Swarm Mission Assurance",
    ha="center", va="center",
    fontsize=15, fontweight="bold", color="#102A43"
)

box(ax, 0.4, 4.3, 2.4, 2.4,
    "Multi-UAV Mission\nEnvironment",
    "• UAV swarm\n• Mission area\n• Cyber-physical threats\n\nThreats:\n• Jamming\n• GPS spoofing\n• Telemetry tampering\n• Combined attacks",
    fc="#F0F4F8")

box(ax, 3.3, 4.3, 2.5, 2.4,
    "Multi-Source\nTelemetry",
    "Communication:\n• packet loss\n• latency\n\nNavigation:\n• route deviation\n• GPS jump\n\nEnergy / Mission:\n• battery\n• progress\n• coverage",
    fc="#E6F6FF")

box(ax, 6.3, 4.3, 2.5, 2.4,
    "Graph-Temporal\nFusion Window",
    "Tensor representation:\n\nX ∈ R^(T × N × F)\n\nFinal setting:\nT = 20 timesteps\nN = 20 UAVs\nF = 9 features",
    fc="#EAFBE7")

box(ax, 9.3, 4.3, 2.6, 2.4,
    "Graph-Temporal\nTransformer",
    "• Feature projection\n• UAV-node attention\n• Temporal transformer\n• Fused embedding\n• Mission-state classifier\n\nClasses:\nnormal, jamming,\nspoofing, tampering,\ncombined attacks",
    fc="#FFF7E6")

box(ax, 12.4, 4.3, 2.6, 2.4,
    "Trustworthy AI\nLayer",
    "Confidence-aware:\n• ECE\n• Brier score\n• confidence\n• entropy\n\nOOD-aware:\n• stealth jammer\n• GPS drift\n• delayed attacks\n\nExplainability:\n• fusion drivers",
    fc="#F3E8FF")

box(ax, 15.5, 4.3, 2.2, 2.4,
    "Recovery-Oriented\nMission Assurance",
    "PPO recovery actions:\n• continue\n• monitor\n• reroute\n• reassign\n• isolate node\n• return to base\n\nOutput:\nHigh-confidence\nmission decision",
    fc="#FFECEC")

# bottom explanatory layer
box(ax, 3.3, 1.0, 4.2, 1.7,
    "Fusion Sources",
    "TRUST-Swarm fuses communication, navigation, energy, mission-progress, and coverage telemetry across UAV nodes and mission time.",
    fc="#F8FAFC")

box(ax, 8.0, 1.0, 4.2, 1.7,
    "Trust Evaluation",
    "The framework evaluates not only what mission state is predicted, but also how reliable the prediction is under calibration and OOD stress.",
    fc="#F8FAFC")

box(ax, 12.7, 1.0, 4.2, 1.7,
    "Mission Response",
    "Trusted fusion outputs support recovery-oriented reasoning for resilient UAV swarm mission assurance.",
    fc="#F8FAFC")

# arrows top
arrow(ax, 2.8, 5.5, 3.3, 5.5)
arrow(ax, 5.8, 5.5, 6.3, 5.5)
arrow(ax, 8.8, 5.5, 9.3, 5.5)
arrow(ax, 11.9, 5.5, 12.4, 5.5)
arrow(ax, 15.0, 5.5, 15.5, 5.5)

# arrows bottom
arrow(ax, 5.4, 4.3, 5.4, 2.7)
arrow(ax, 10.6, 4.3, 10.6, 2.7)
arrow(ax, 14.5, 4.3, 14.5, 2.7)

# footer
ax.text(
    9, 0.35,
    "Figure 1. TRUST-Swarm overall multi-source information fusion architecture.",
    ha="center", va="center",
    fontsize=10, color="#334E68"
)

png_path = OUT_DIR / "fig_01_trust_swarm_architecture.png"
pdf_path = OUT_DIR / "fig_01_trust_swarm_architecture.pdf"

plt.savefig(png_path, dpi=300, bbox_inches="tight")
plt.savefig(pdf_path, bbox_inches="tight")
plt.close()

print(f"Saved: {png_path}")
print(f"Saved: {pdf_path}")

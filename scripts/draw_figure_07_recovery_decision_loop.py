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
    ax.text(x + 0.06, y + h - 0.22, body, ha="left", va="top",
            fontsize=8.2, color="#1F2933", linespacing=1.23)
    return patch

def arrow(ax, x1, y1, x2, y2, curve=0.0):
    ax.add_patch(FancyArrowPatch(
        (x1, y1), (x2, y2),
        arrowstyle="->",
        mutation_scale=14,
        linewidth=1.4,
        color="#334E68",
        connectionstyle=f"arc3,rad={curve}"
    ))

fig, ax = plt.subplots(figsize=(18, 8))
ax.set_xlim(0, 18)
ax.set_ylim(0, 8)
ax.axis("off")

ax.text(
    9, 7.65,
    "Recovery-Oriented Fusion Decision Loop",
    ha="center", va="center",
    fontsize=16, fontweight="bold", color="#102A43"
)

box(ax, 0.5, 4.35, 2.8, 2.4,
    "Graph-Temporal\nFusion Output",
    "Outputs:\n• predicted mission state\n• class probability\n• confidence score\n• predictive entropy\n\nStates:\nnormal, jamming,\nspoofing, tampering,\ncombined attacks",
    fc="#F0F4F8")

box(ax, 3.8, 4.35, 2.8, 2.4,
    "Mission-Risk\nAssessment",
    "Risk indicators:\n• communication degradation\n• navigation disruption\n• coverage loss\n• mission-progress loss\n• energy stress\n• OOD warning",
    fc="#FFF7E6")

box(ax, 7.1, 4.35, 2.8, 2.4,
    "PPO-Based\nRecovery Policy",
    "Inputs:\n• mission-state prediction\n• confidence\n• entropy\n• risk indicators\n\nPurpose:\nrecovery reasoning scaffold",
    fc="#E6F6FF")

box(ax, 10.4, 4.35, 2.8, 2.4,
    "Recovery\nAction Space",
    "Possible actions:\n• continue\n• monitor\n• reroute\n• reassign\n• isolate node\n• return to base",
    fc="#EAFBE7")

box(ax, 13.7, 4.35, 3.0, 2.4,
    "Mission-Assurance\nDecision",
    "Output:\nhigh-confidence\nmission-assurance action\n\nDecision supports:\nmonitoring, escalation,\nrerouting, isolation,\nor return-to-base logic",
    fc="#F3E8FF")

box(ax, 2.0, 1.05, 3.5, 2.0,
    "Updated UAV\nSwarm Telemetry",
    "Recovery action changes the mission state and produces new communication, navigation, energy, progress, and coverage telemetry.",
    fc="#F8FAFC")

box(ax, 6.3, 1.05, 4.0, 2.0,
    "Closed-Loop\nMission Assurance",
    "TRUST-Swarm connects trustworthy fusion outputs to recovery-oriented reasoning, creating a feedback loop for resilient missions.",
    fc="#F8FAFC")

box(ax, 11.2, 1.05, 4.3, 2.0,
    "Safe Interpretation",
    "The PPO module is a recovery-reasoning scaffold, not a deployment-ready UAV controller.",
    fc="#FFECEC")

arrow(ax, 3.3, 5.55, 3.8, 5.55)
arrow(ax, 6.6, 5.55, 7.1, 5.55)
arrow(ax, 9.9, 5.55, 10.4, 5.55)
arrow(ax, 13.2, 5.55, 13.7, 5.55)

arrow(ax, 15.2, 4.35, 13.4, 3.05, curve=0.05)
arrow(ax, 13.4, 3.05, 4.0, 3.05, curve=0.0)
arrow(ax, 4.0, 3.05, 3.5, 4.35, curve=0.05)

arrow(ax, 3.7, 4.35, 3.7, 3.05)
arrow(ax, 8.3, 4.35, 8.3, 3.05)
arrow(ax, 12.6, 4.35, 13.4, 3.05)

ax.text(
    9, 0.35,
    "Figure 7. Recovery-oriented fusion connects mission-state predictions, uncertainty, and risk indicators to recovery reasoning.",
    ha="center", va="center",
    fontsize=10, color="#334E68"
)

png_path = OUT_DIR / "fig_07_recovery_decision_loop.png"
pdf_path = OUT_DIR / "fig_07_recovery_decision_loop.pdf"

plt.savefig(png_path, dpi=300, bbox_inches="tight")
plt.savefig(pdf_path, bbox_inches="tight")
plt.close()

print(f"Saved: {png_path}")
print(f"Saved: {pdf_path}")

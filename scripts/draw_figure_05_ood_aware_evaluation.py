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
    "OOD-Aware Mission Risk Evaluation Pipeline",
    ha="center", va="center",
    fontsize=16, fontweight="bold", color="#102A43"
)

box(ax, 0.4, 4.35, 2.5, 2.4,
    "In-Distribution\nTest Windows",
    "Standard graph-temporal\nfusion windows from\nthe held-out test set.\n\nReference condition:\nmacro F1 = 0.8750",
    fc="#F0F4F8")

box(ax, 3.4, 4.35, 2.7, 2.4,
    "OOD Cyber-Physical\nStress Generator",
    "Creates unseen mission\nrisk conditions by\nperturbing telemetry\nstreams beyond the\ntraining distribution.",
    fc="#FFF7E6")

box(ax, 6.6, 4.35, 2.8, 2.4,
    "OOD Stress\nScenarios",
    "• stealth jammer\n• slow GPS drift\n• intermittent tampering\n• delayed combined attack\n• unseen swarm noise",
    fc="#FFECEC")

box(ax, 9.9, 4.35, 2.5, 2.4,
    "Trained Fusion\nModel",
    "Graph-Temporal\nTransformer evaluated\non shifted OOD windows.\n\nNo retraining during\nOOD testing.",
    fc="#E6F6FF")

box(ax, 12.9, 4.35, 2.4, 2.4,
    "OOD Evaluation\nMetrics",
    "• accuracy\n• macro F1\n• confidence\n• entropy\n• low-confidence rate",
    fc="#EAFBE7")

box(ax, 15.8, 4.35, 1.9, 2.4,
    "Mission-Risk\nInterpretation",
    "Stable:\nin-distribution\n\nHigh risk:\ndelayed combined\nstealth jammer\nslow GPS drift\n\nModerate risk:\nintermittent tampering",
    fc="#F3E8FF")

box(ax, 1.0, 1.0, 3.5, 2.0,
    "Macro F1 Reference",
    "In-distribution: 0.8750\nIntermittent tampering: 0.5965\nSlow GPS drift: 0.1701\nStealth jammer: 0.0779\nDelayed combined: 0.0521",
    fc="#F8FAFC")

box(ax, 5.0, 1.0, 3.5, 2.0,
    "Why OOD Matters",
    "High in-distribution accuracy does not guarantee reliable mission assurance under unseen cyber-physical shifts.",
    fc="#F8FAFC")

box(ax, 9.0, 1.0, 3.5, 2.0,
    "Trustworthy Fusion View",
    "OOD stress testing exposes where fused predictions degrade and where monitoring or recovery may be needed.",
    fc="#F8FAFC")

box(ax, 13.0, 1.0, 3.8, 2.0,
    "Safe Interpretation",
    "The framework evaluates OOD vulnerability. It does not claim perfect OOD detection under all attack conditions.",
    fc="#F8FAFC")

arrow(ax, 2.9, 5.55, 3.4, 5.55)
arrow(ax, 6.1, 5.55, 6.6, 5.55)
arrow(ax, 9.4, 5.55, 9.9, 5.55)
arrow(ax, 12.4, 5.55, 12.9, 5.55)
arrow(ax, 15.3, 5.55, 15.8, 5.55)

arrow(ax, 2.3, 4.35, 2.3, 3.0)
arrow(ax, 7.5, 4.35, 6.8, 3.0)
arrow(ax, 11.2, 4.35, 10.8, 3.0)
arrow(ax, 14.6, 4.35, 14.9, 3.0)

ax.text(
    9, 0.35,
    "Figure 5. OOD-aware evaluation reveals mission-risk conditions under unseen cyber-physical shifts.",
    ha="center", va="center",
    fontsize=10, color="#334E68"
)

png_path = OUT_DIR / "fig_05_ood_aware_mission_risk_evaluation.png"
pdf_path = OUT_DIR / "fig_05_ood_aware_mission_risk_evaluation.pdf"

plt.savefig(png_path, dpi=300, bbox_inches="tight")
plt.savefig(pdf_path, bbox_inches="tight")
plt.close()

print(f"Saved: {png_path}")
print(f"Saved: {pdf_path}")

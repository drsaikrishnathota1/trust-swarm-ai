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
            fontsize=8.3, color="#1F2933", linespacing=1.25)
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
    "Confidence-Aware Fusion Pipeline",
    ha="center", va="center",
    fontsize=16, fontweight="bold", color="#102A43"
)

box(ax, 0.4, 4.35, 2.4, 2.4,
    "Graph-Temporal\nFusion Window",
    "Input tensor:\n\nX ∈ R^(20 × 20 × 9)\n\n20 timesteps\n20 UAV nodes\n9 telemetry features",
    fc="#F0F4F8")

box(ax, 3.3, 4.35, 2.5, 2.4,
    "Graph-Temporal\nTransformer",
    "Produces mission-state\nclass probabilities.\n\nOutput:\nprobability distribution\nover mission states",
    fc="#E6F6FF")

box(ax, 6.3, 4.35, 2.5, 2.4,
    "MC Dropout\nInference",
    "20 stochastic samples\n\nProbability averaging\n\nUncertainty estimation",
    fc="#EAFBE7")

box(ax, 9.3, 4.35, 2.6, 2.4,
    "Prediction\nOutputs",
    "• predicted mission state\n• class probability\n• confidence score\n• predictive entropy",
    fc="#FFF7E6")

box(ax, 12.4, 4.35, 2.6, 2.4,
    "Calibration\nMetrics",
    "Final reported values:\n\nECE = 0.0088\nBrier = 0.0531\nConfidence = 0.9601\nEntropy = 0.0986",
    fc="#F3E8FF")

box(ax, 15.5, 4.35, 2.2, 2.4,
    "Mission-Assurance\nTrust Decision",
    "Decision options:\n\n• trust prediction\n• monitor closely\n• escalate review\n• trigger recovery",
    fc="#FFECEC")

box(ax, 2.0, 1.1, 3.7, 1.8,
    "Why Confidence Matters",
    "Mission assurance requires knowing whether a fused prediction is reliable, not only which class is predicted.",
    fc="#F8FAFC")

box(ax, 6.2, 1.1, 3.7, 1.8,
    "Uncertainty Estimation",
    "MC dropout provides repeated stochastic predictions for estimating confidence and entropy.",
    fc="#F8FAFC")

box(ax, 10.4, 1.1, 3.7, 1.8,
    "Calibration Check",
    "ECE and Brier score evaluate whether predicted probabilities match observed correctness.",
    fc="#F8FAFC")

box(ax, 14.6, 1.1, 2.7, 1.8,
    "Mission Use",
    "Trust decisions support monitoring, escalation, and recovery reasoning.",
    fc="#F8FAFC")

arrow(ax, 2.8, 5.55, 3.3, 5.55)
arrow(ax, 5.8, 5.55, 6.3, 5.55)
arrow(ax, 8.8, 5.55, 9.3, 5.55)
arrow(ax, 11.9, 5.55, 12.4, 5.55)
arrow(ax, 15.0, 5.55, 15.5, 5.55)

arrow(ax, 4.0, 4.35, 4.0, 2.9)
arrow(ax, 7.9, 4.35, 7.9, 2.9)
arrow(ax, 13.1, 4.35, 12.3, 2.9)
arrow(ax, 16.3, 4.35, 16.0, 2.9)

ax.text(
    9, 0.35,
    "Figure 4. Confidence-aware fusion evaluates whether graph-temporal mission-state predictions are reliable.",
    ha="center", va="center",
    fontsize=10, color="#334E68"
)

png_path = OUT_DIR / "fig_04_confidence_aware_fusion_pipeline.png"
pdf_path = OUT_DIR / "fig_04_confidence_aware_fusion_pipeline.pdf"

plt.savefig(png_path, dpi=300, bbox_inches="tight")
plt.savefig(pdf_path, bbox_inches="tight")
plt.close()

print(f"Saved: {png_path}")
print(f"Saved: {pdf_path}")

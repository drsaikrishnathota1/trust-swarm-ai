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
    "Fusion-Driver Explainability Workflow",
    ha="center", va="center",
    fontsize=16, fontweight="bold", color="#102A43"
)

box(ax, 0.4, 4.35, 2.4, 2.4,
    "Baseline\nTest Set",
    "Graph-temporal fusion\nwindows from the test set.\n\nUsed to compute baseline\nmission-state performance.",
    fc="#F0F4F8")

box(ax, 3.3, 4.35, 2.4, 2.4,
    "Baseline\nPerformance",
    "Compute baseline\nmacro F1 before any\nfeature perturbation.\n\nReference score for\nimportance calculation.",
    fc="#E6F6FF")

box(ax, 6.2, 4.35, 2.8, 2.4,
    "Feature\nPerturbation",
    "Replace one telemetry\nfeature at a time with\nits mean value.\n\nGroups:\n• communication\n• navigation\n• energy\n• progress\n• coverage",
    fc="#FFF7E6")

box(ax, 9.5, 4.35, 2.5, 2.4,
    "Re-Evaluate\nFusion Model",
    "Run the trained\nGraph-Temporal\nTransformer after each\nfeature perturbation.\n\nRecompute macro F1.",
    fc="#EAFBE7")

box(ax, 12.5, 4.35, 2.4, 2.4,
    "Macro-F1\nDrop",
    "Feature importance:\n\nbaseline macro F1\n− perturbed macro F1\n\nLarger drop =\nmore important feature",
    fc="#F3E8FF")

box(ax, 15.4, 4.35, 2.3, 2.4,
    "Ranked Fusion\nDrivers",
    "Top drivers:\n\n1. latency_ms\n2. zone_coverage\n3. route_deviation_m\n4. mission_progress\n5. gps_jump_m",
    fc="#FFECEC")

box(ax, 1.0, 1.0, 3.4, 2.0,
    "Communication Driver",
    "latency_ms indicates communication degradation and possible jamming effects.",
    fc="#F8FAFC")

box(ax, 4.8, 1.0, 3.4, 2.0,
    "Mission Driver",
    "zone_coverage and mission_progress indicate mission coverage loss and task-completion disruption.",
    fc="#F8FAFC")

box(ax, 8.6, 1.0, 3.4, 2.0,
    "Navigation Driver",
    "route_deviation_m and gps_jump_m indicate navigation disruption and spoofing-related displacement.",
    fc="#F8FAFC")

box(ax, 12.4, 1.0, 4.1, 2.0,
    "Trustworthy Fusion View",
    "Explainability links fused predictions back to operationally meaningful telemetry sources.",
    fc="#F8FAFC")

arrow(ax, 2.8, 5.55, 3.3, 5.55)
arrow(ax, 5.7, 5.55, 6.2, 5.55)
arrow(ax, 9.0, 5.55, 9.5, 5.55)
arrow(ax, 12.0, 5.55, 12.5, 5.55)
arrow(ax, 14.9, 5.55, 15.4, 5.55)

arrow(ax, 2.4, 4.35, 2.7, 3.0)
arrow(ax, 6.7, 4.35, 6.5, 3.0)
arrow(ax, 10.8, 4.35, 10.3, 3.0)
arrow(ax, 14.0, 4.35, 14.4, 3.0)

ax.text(
    9, 0.35,
    "Figure 6. Perturbation-based explainability identifies telemetry sources that drive fused mission-state predictions.",
    ha="center", va="center",
    fontsize=10, color="#334E68"
)

png_path = OUT_DIR / "fig_06_fusion_driver_explainability.png"
pdf_path = OUT_DIR / "fig_06_fusion_driver_explainability.pdf"

plt.savefig(png_path, dpi=300, bbox_inches="tight")
plt.savefig(pdf_path, bbox_inches="tight")
plt.close()

print(f"Saved: {png_path}")
print(f"Saved: {pdf_path}")

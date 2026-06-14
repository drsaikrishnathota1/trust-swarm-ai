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
    "Graph-Temporal Fusion Model Architecture",
    ha="center", va="center",
    fontsize=16, fontweight="bold", color="#102A43"
)

box(ax, 0.4, 4.4, 2.3, 2.3,
    "Input Fusion\nWindow",
    "Graph-temporal tensor:\n\nX ∈ R^(T × N × F)\n\nFinal setting:\nX ∈ R^(20 × 20 × 9)",
    fc="#F0F4F8")

box(ax, 3.1, 4.4, 2.3, 2.3,
    "Telemetry Feature\nProjection",
    "Projects 9 raw telemetry\nfeatures into hidden\nembeddings.\n\nInput: telemetry features\nOutput: hidden vectors",
    fc="#E6F6FF")

box(ax, 5.8, 4.4, 2.3, 2.3,
    "UAV-Node\nAttention",
    "Learns relationships\namong UAV nodes inside\neach mission window.\n\nCaptures swarm-level\nnode interactions.",
    fc="#EAFBE7")

box(ax, 8.5, 4.4, 2.5, 2.3,
    "Temporal Transformer\nEncoder",
    "Learns mission evolution\nacross time.\n\nCaptures attack progression\nand temporal degradation.",
    fc="#FFF7E6")

box(ax, 11.4, 4.4, 2.3, 2.3,
    "Graph-Temporal\nMission Embedding",
    "Fused representation\ncombining:\n\n• UAV-node structure\n• temporal mission context\n• telemetry sources",
    fc="#F3E8FF")

box(ax, 14.1, 4.4, 1.8, 2.3,
    "Mission-State\nClassifier",
    "Classifier layer\n\nOutputs class scores\nfor mission state.",
    fc="#FFECEC")

box(ax, 16.3, 4.4, 1.4, 2.3,
    "Output\nProbabilities",
    "normal\njamming\nspoofing\ntampering\ncombined\nattacks",
    fc="#FFF1F2")

box(ax, 2.0, 1.1, 3.7, 1.8,
    "Feature-Level Fusion",
    "Communication, navigation, energy, progress, and coverage features are projected into a shared hidden space.",
    fc="#F8FAFC")

box(ax, 6.2, 1.1, 3.7, 1.8,
    "Node-Level Fusion",
    "Attention models relationships among UAVs, supporting swarm-aware mission-state reasoning.",
    fc="#F8FAFC")

box(ax, 10.4, 1.1, 3.7, 1.8,
    "Temporal Fusion",
    "Transformer encoding captures mission-time evolution and attack progression across the fusion window.",
    fc="#F8FAFC")

box(ax, 14.6, 1.1, 2.7, 1.8,
    "Mission Output",
    "Softmax probabilities support classification, calibration, OOD analysis, and recovery reasoning.",
    fc="#F8FAFC")

arrow(ax, 2.7, 5.55, 3.1, 5.55)
arrow(ax, 5.4, 5.55, 5.8, 5.55)
arrow(ax, 8.1, 5.55, 8.5, 5.55)
arrow(ax, 11.0, 5.55, 11.4, 5.55)
arrow(ax, 13.7, 5.55, 14.1, 5.55)
arrow(ax, 15.9, 5.55, 16.3, 5.55)

arrow(ax, 4.0, 4.4, 4.0, 2.9)
arrow(ax, 7.7, 4.4, 7.7, 2.9)
arrow(ax, 10.0, 4.4, 12.2, 2.9)
arrow(ax, 15.2, 4.4, 15.9, 2.9)

ax.text(
    9, 0.35,
    "Figure 3. The Graph-Temporal Transformer fuses telemetry features, UAV-node relationships, and mission-time evolution.",
    ha="center", va="center",
    fontsize=10, color="#334E68"
)

png_path = OUT_DIR / "fig_03_graph_temporal_model_architecture.png"
pdf_path = OUT_DIR / "fig_03_graph_temporal_model_architecture.pdf"

plt.savefig(png_path, dpi=300, bbox_inches="tight")
plt.savefig(pdf_path, bbox_inches="tight")
plt.close()

print(f"Saved: {png_path}")
print(f"Saved: {pdf_path}")

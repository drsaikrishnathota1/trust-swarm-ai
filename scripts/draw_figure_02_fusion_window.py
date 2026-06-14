from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle

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
            fontsize=8.4, color="#1F2933", linespacing=1.25)
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
    "Graph-Temporal Fusion-Window Construction",
    ha="center", va="center",
    fontsize=16, fontweight="bold", color="#102A43"
)

box(ax, 0.4, 4.35, 3.0, 2.4,
    "Raw Multi-UAV\nTelemetry",
    "Table-like mission stream:\n• mission_id\n• timestep\n• uav_id\n• packet_loss_rate\n• latency_ms\n• route_deviation_m\n• gps_jump_m\n• attack_label",
    fc="#F0F4F8")

box(ax, 3.9, 4.35, 2.5, 2.4,
    "Temporal Sliding\nWindow",
    "Window moves across\nmission time.\n\nT = 20 timesteps\n\nCaptures attack onset,\nprogression, and mission\ndegradation.",
    fc="#E6F6FF")

box(ax, 6.9, 4.35, 2.4, 2.4,
    "UAV Node\nStructure",
    "Each window contains\nall UAV nodes.\n\nN = 20 UAVs\n\nPreserves swarm-level\nnode structure.",
    fc="#EAFBE7")

box(ax, 9.8, 4.35, 3.0, 2.4,
    "Multi-Source\nTelemetry Features",
    "F = 9 features\n\nCommunication:\npacket loss, latency\n\nNavigation:\nroute deviation, GPS jump\n\nEnergy, progress,\nand coverage signals",
    fc="#FFF7E6")

box(ax, 13.3, 4.35, 2.4, 2.4,
    "Fusion Tensor",
    "Graph-temporal sample:\n\nX ∈ R^(T × N × F)\n\nFinal setting:\nX ∈ R^(20 × 20 × 9)",
    fc="#F3E8FF")

box(ax, 16.1, 4.35, 1.6, 2.4,
    "Mission-State\nLabel",
    "normal\njamming\nspoofing\ntampering\ncombined\nattacks",
    fc="#FFECEC")

# illustrative tensor stack
for i in range(5):
    ax.add_patch(Rectangle((13.75 + i*0.08, 1.35 + i*0.08), 1.7, 1.0,
                           linewidth=1.1, edgecolor="#2B5C8A",
                           facecolor="#DCEBFF", alpha=0.85))
ax.text(14.7, 0.95, "Tensor stack: time × UAV nodes × features",
        ha="center", fontsize=9, color="#334E68")

box(ax, 1.1, 1.15, 3.6, 1.8,
    "Telemetry Sources",
    "Communication + navigation + energy + mission progress + coverage are fused into one structured mission window.",
    fc="#F8FAFC")

box(ax, 5.4, 1.15, 3.6, 1.8,
    "Temporal Context",
    "A 20-step window preserves short-term mission evolution and cyber-physical attack progression.",
    fc="#F8FAFC")

box(ax, 9.7, 1.15, 3.3, 1.8,
    "Swarm Context",
    "20 UAV nodes are preserved so the model can learn swarm-level mission patterns.",
    fc="#F8FAFC")

# arrows
arrow(ax, 3.4, 5.55, 3.9, 5.55)
arrow(ax, 6.4, 5.55, 6.9, 5.55)
arrow(ax, 9.3, 5.55, 9.8, 5.55)
arrow(ax, 12.8, 5.55, 13.3, 5.55)
arrow(ax, 15.7, 5.55, 16.1, 5.55)

arrow(ax, 2.9, 4.35, 2.9, 2.95)
arrow(ax, 7.2, 4.35, 7.2, 2.95)
arrow(ax, 11.4, 4.35, 11.4, 2.95)

ax.text(
    9, 0.35,
    "Figure 2. Raw UAV telemetry is converted into graph-temporal fusion windows for mission-state prediction.",
    ha="center", va="center",
    fontsize=10, color="#334E68"
)

png_path = OUT_DIR / "fig_02_fusion_window_construction.png"
pdf_path = OUT_DIR / "fig_02_fusion_window_construction.pdf"

plt.savefig(png_path, dpi=300, bbox_inches="tight")
plt.savefig(pdf_path, bbox_inches="tight")
plt.close()

print(f"Saved: {png_path}")
print(f"Saved: {pdf_path}")

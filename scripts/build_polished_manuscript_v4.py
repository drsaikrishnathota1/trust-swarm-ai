from pathlib import Path
import re

out = Path("manuscript/TRUST-Swarm-information-fusion-polished-v4.md")

def read(path):
    return Path(path).read_text()

def clean(text):
    remove_lines = [
        "# Information Fusion Abstract v2",
        "## Reframed Title",
        "# Information Fusion Introduction v2",
        "# Information Fusion Related Work v3",
        "# Information Fusion Methodology v2",
        "# Information Fusion Results and Discussion v2",
        "# Information Fusion Conclusion and Limitations v2",
        "# TRUST-Swarm Final Numbered Manuscript Tables",
        "# TRUST-Swarm Final Figure Captions",
        "# TRUST-Swarm Cleaned Candidate Reference List v2",
    ]
    for line in remove_lines:
        text = text.replace(line + "\n", "")

    # Remove working duplicate title line inside abstract file if present
    text = re.sub(
        r"TRUST-Swarm: Trustworthy Graph-Temporal Multi-Source Information Fusion for High-Confidence UAV Swarm Mission Assurance Under Cyber-Physical Attacks\n\n## Abstract",
        "## Abstract",
        text
    )

    # Remove candidate/reference warning blocks from final manuscript body
    text = text.replace(
        "This version removes obvious duplicates and keeps only the strongest Information Fusion candidate references.\n"
        "This is still not the final journal bibliography. DOI, venue, page numbers, author order, and peer-reviewed status must still be audited.\n",
        ""
    )

    return text.strip()

def fig(num, title, path):
    return f"""
**Figure {num}. {title}.**

![Figure {num}. {title}](../{path})
"""

parts = []

parts.append("# TRUST-Swarm: Trustworthy Graph-Temporal Multi-Source Information Fusion for High-Confidence UAV Swarm Mission Assurance Under Cyber-Physical Attacks\n")

parts.append(clean(read("docs/information_fusion_abstract_v2.md")))
parts.append(clean(read("docs/information_fusion_introduction_v2.md")))
parts.append(fig(1, "TRUST-Swarm multi-source information fusion architecture", "figures/architecture/fig_01_trust_swarm_architecture.png"))

parts.append(clean(read("docs/information_fusion_related_work_v3.md")))

parts.append(clean(read("docs/information_fusion_methodology_v2.md")))
parts.append(fig(2, "Graph-temporal fusion-window construction", "figures/architecture/fig_02_fusion_window_construction.png"))
parts.append(fig(3, "Graph-temporal fusion model architecture", "figures/architecture/fig_03_graph_temporal_model_architecture.png"))
parts.append(fig(4, "Confidence-aware fusion pipeline", "figures/architecture/fig_04_confidence_aware_fusion_pipeline.png"))
parts.append(fig(5, "OOD-aware mission-risk evaluation pipeline", "figures/architecture/fig_05_ood_aware_mission_risk_evaluation.png"))
parts.append(fig(6, "Fusion-driver explainability workflow", "figures/architecture/fig_06_fusion_driver_explainability.png"))
parts.append(fig(7, "Recovery-oriented fusion decision loop", "figures/architecture/fig_07_recovery_decision_loop.png"))

parts.append(clean(read("docs/experimental_setup_draft.md")))
parts.append(clean(read("docs/final_numbered_manuscript_tables.md")))

parts.append(clean(read("docs/information_fusion_results_discussion_v2.md")))
parts.append(fig(8, "Model comparison by mean macro F1", "figures/manuscript/fig_01_model_comparison_macro_f1.png"))
parts.append(fig(9, "OOD stress-test performance by mean macro F1", "figures/manuscript/fig_05_ood_macro_f1.png"))
parts.append(fig(10, "Perturbation-based feature importance", "figures/manuscript/fig_07_feature_importance.png"))

parts.append(clean(read("docs/information_fusion_conclusion_limitations_v2.md")))

parts.append("## References\n")
refs = clean(read("docs/cleaned_candidate_reference_list_v2.md"))
# Keep only actual references and removed-duplicate note out of final body
refs_lines = []
for line in refs.splitlines():
    if line.startswith("[") or line.startswith("- Numeric references") or line.startswith("- Strong Information") or line.startswith("- Total"):
        refs_lines.append(line)
parts.append("\n".join(refs_lines))

out.write_text("\n\n".join(parts).strip() + "\n")
print(f"Saved: {out}")

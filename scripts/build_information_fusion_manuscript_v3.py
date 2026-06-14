from pathlib import Path

out = Path("manuscript/TRUST-Swarm-information-fusion-manuscript-v3-with-figures.md")

def read(path):
    return Path(path).read_text()

def fig(num, title, path):
    return f"""
**Figure {num}. {title}.**

![Figure {num}. {title}](../{path})

"""

content = []

content.append("# TRUST-Swarm Information Fusion Manuscript v3\n")
content.append("**Working title:** TRUST-Swarm: Trustworthy Graph-Temporal Multi-Source Information Fusion for High-Confidence UAV Swarm Mission Assurance Under Cyber-Physical Attacks\n")
content.append("---\n")

content.append(read("docs/information_fusion_abstract_v2.md"))
content.append("\n---\n")

content.append(read("docs/information_fusion_introduction_v2.md"))
content.append(fig(
    1,
    "TRUST-Swarm multi-source information fusion architecture",
    "figures/architecture/fig_01_trust_swarm_architecture.png"
))
content.append("\n---\n")

content.append(read("docs/information_fusion_related_work_v3.md"))
content.append("\n---\n")

content.append(read("docs/information_fusion_methodology_v2.md"))
content.append(fig(
    2,
    "Graph-temporal fusion-window construction",
    "figures/architecture/fig_02_fusion_window_construction.png"
))
content.append(fig(
    3,
    "Graph-temporal fusion model architecture",
    "figures/architecture/fig_03_graph_temporal_model_architecture.png"
))
content.append(fig(
    4,
    "Confidence-aware fusion pipeline",
    "figures/architecture/fig_04_confidence_aware_fusion_pipeline.png"
))
content.append(fig(
    5,
    "OOD-aware mission-risk evaluation pipeline",
    "figures/architecture/fig_05_ood_aware_mission_risk_evaluation.png"
))
content.append(fig(
    6,
    "Fusion-driver explainability workflow",
    "figures/architecture/fig_06_fusion_driver_explainability.png"
))
content.append(fig(
    7,
    "Recovery-oriented fusion decision loop",
    "figures/architecture/fig_07_recovery_decision_loop.png"
))
content.append("\n---\n")

content.append(read("docs/experimental_setup_draft.md"))
content.append("\n---\n")

content.append(read("docs/final_numbered_manuscript_tables.md"))
content.append("\n---\n")

content.append(read("docs/information_fusion_results_discussion_v2.md"))
content.append(fig(
    8,
    "Model comparison by mean macro F1",
    "figures/manuscript/fig_01_model_comparison_macro_f1.png"
))
content.append(fig(
    9,
    "OOD stress-test performance by mean macro F1",
    "figures/manuscript/fig_05_ood_macro_f1.png"
))
content.append(fig(
    10,
    "Perturbation-based feature importance",
    "figures/manuscript/fig_07_feature_importance.png"
))
content.append("\n---\n")

content.append(read("docs/information_fusion_conclusion_limitations_v2.md"))
content.append("\n---\n")

content.append(read("docs/final_figure_captions.md"))
content.append("\n---\n")

content.append(read("docs/combined_reference_list.md"))
content.append("\n---\n")

content.append(read("docs/information_fusion_candidate_references.md"))

out.write_text("\n".join(content))
print(f"Saved: {out}")

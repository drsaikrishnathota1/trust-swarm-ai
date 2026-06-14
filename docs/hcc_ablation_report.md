# HCC Ablation Study Report

This report evaluates architecture-level and framework-level ablations for TRUST-Swarm.

## Dataset and Training Configuration

- Data: `data/processed/seed_42/graph_windows.pt`
- Samples: 66300
- Window size: 20
- UAV nodes: 20
- Features: 9
- Classes: 8
- Epochs: 30
- Batch size: 128
- Device: cuda

## Ablation Summary

| Configuration | Type | Accuracy | Macro F1 | Calibration | OOD | Explanation | Recovery | Interpretation |
|---|---|---:|---:|---|---|---|---|---|
| A0_full_graph_temporal_transformer | model_architecture | 0.9579 | 0.8734 | yes | yes | yes | yes | Architecture-level ablation trained and evaluated on the same graph-temporal dataset. |
| A1_without_uav_node_attention | model_architecture | 0.9572 | 0.7903 | yes | yes | yes | yes | Architecture-level ablation trained and evaluated on the same graph-temporal dataset. |
| A2_without_temporal_transformer | model_architecture | 0.9507 | 0.8237 | yes | yes | yes | yes | Architecture-level ablation trained and evaluated on the same graph-temporal dataset. |
| A3_without_uncertainty_calibration | framework_module | 0.9579 | 0.8734 | no | yes | yes | yes | Removes confidence reliability evidence; prediction remains available but ECE/Brier/confidence evidence is absent. |
| A4_without_ood_stress_testing | framework_module | 0.9579 | 0.8734 | yes | no | yes | yes | Removes unseen-shift vulnerability evidence; prediction remains available but OOD risk evidence is absent. |
| A5_without_explainability | framework_module | 0.9579 | 0.8734 | yes | yes | no | yes | Removes traceable mission-risk driver evidence; prediction remains available but feature-level explanation is absent. |
| A6_without_recovery_reasoning | framework_module | 0.9579 | 0.8734 | yes | yes | yes | no | Removes mission-response support; prediction, calibration, OOD, and explanation remain available. |

## Manuscript Use

Use this table to show that TRUST-Swarm is a high-confidence computing framework. Architecture ablations test node and temporal reasoning. Framework ablations show what assurance evidence is lost when calibration, OOD testing, explainability, or recovery reasoning is removed.
# TRUST-Swarm Final Figure Captions

## Figure 1. TRUST-Swarm multi-source information fusion architecture

This figure presents the overall TRUST-Swarm pipeline for high-confidence UAV swarm mission assurance. Distributed UAV telemetry streams are fused across communication, navigation, energy, mission-progress, and coverage sources. The graph-temporal fusion window is processed by a Graph-Temporal Transformer, followed by confidence-aware calibration, OOD-aware stress testing, fusion-driver explainability, and recovery-oriented mission reasoning.

File: `figures/architecture/fig_01_trust_swarm_architecture.png`

## Figure 2. Graph-temporal fusion-window construction

This figure shows how raw multi-UAV telemetry is converted into graph-temporal fusion windows. Each sample preserves temporal structure, UAV-node structure, and multi-source telemetry feature structure. In the final experiment, each fusion window is represented as X ∈ R^(20 × 20 × 9), corresponding to 20 timesteps, 20 UAV nodes, and 9 telemetry features.

File: `figures/architecture/fig_02_fusion_window_construction.png`

## Figure 3. Graph-temporal fusion model architecture

This figure illustrates the Graph-Temporal Transformer used in TRUST-Swarm. The model projects telemetry features into hidden embeddings, applies UAV-node attention, encodes temporal mission evolution using a transformer encoder, and outputs mission-state probabilities for normal, jamming, spoofing, tampering, and combined attack states.

File: `figures/architecture/fig_03_graph_temporal_model_architecture.png`

## Figure 4. Confidence-aware fusion pipeline

This figure shows how TRUST-Swarm evaluates the reliability of fused mission-state predictions. Monte Carlo dropout inference is used to estimate confidence and entropy, while Expected Calibration Error and Brier score evaluate probabilistic calibration. The calibrated output supports trust, monitoring, escalation, or recovery reasoning.

File: `figures/architecture/fig_04_confidence_aware_fusion_pipeline.png`

## Figure 5. OOD-aware mission-risk evaluation pipeline

This figure presents the OOD stress-testing workflow. In-distribution graph-temporal windows are perturbed into unseen cyber-physical stress scenarios, including stealth jamming, slow GPS drift, intermittent tampering, delayed combined attacks, and unseen swarm noise. The resulting performance degradation supports OOD-aware mission-risk interpretation.

File: `figures/architecture/fig_05_ood_aware_mission_risk_evaluation.png`

## Figure 6. Fusion-driver explainability workflow

This figure shows the perturbation-based feature-importance method used to identify telemetry sources that drive fused mission-state predictions. Each feature is perturbed one at a time, macro-F1 drop is measured, and the most influential fusion drivers are ranked. The strongest drivers include latency, zone coverage, route deviation, mission progress, and GPS jump.

File: `figures/architecture/fig_06_fusion_driver_explainability.png`

## Figure 7. Recovery-oriented fusion decision loop

This figure shows how TRUST-Swarm connects graph-temporal fusion outputs, uncertainty signals, and mission-risk indicators to recovery-oriented decision support. The PPO module is interpreted as a recovery-reasoning scaffold, not as a deployment-ready UAV controller.

File: `figures/architecture/fig_07_recovery_decision_loop.png`

## Figure 8. Model comparison by mean macro F1

This figure compares the mean macro F1 scores of the evaluated models across three random seeds. The 1D-CNN baseline achieved the strongest in-distribution macro F1, while the Graph-Temporal Transformer supports the broader trustworthy information-fusion framework.

File: `figures/manuscript/fig_01_model_comparison_macro_f1.png`

## Figure 9. OOD stress-test performance by mean macro F1

This figure shows macro F1 performance under in-distribution and OOD cyber-physical stress conditions. Severe unseen shifts such as stealth jamming, slow GPS drift, and delayed combined attacks substantially reduce model performance.

File: `figures/manuscript/fig_05_ood_macro_f1.png`

## Figure 10. Perturbation-based feature importance

This figure shows the most influential telemetry features based on macro-F1 drop after feature perturbation. Latency, zone coverage, route deviation, mission progress, and GPS jump are important mission-relevant fusion drivers.

File: `figures/manuscript/fig_07_feature_importance.png`

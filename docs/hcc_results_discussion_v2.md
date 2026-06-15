# High-Confidence Computing Results and Discussion v2

## 5. Results and discussion

This section presents the experimental findings of TRUST-Swarm and interprets them from a high-confidence computing perspective. The purpose of the evaluation is not limited to identifying the model with the highest in-distribution classification score. Instead, the results are analyzed across five assurance dimensions: mission-state recognition, calibrated reliability, OOD cyber-physical stress behavior, traceable feature-level explanation, and recovery-oriented reasoning. This organization is important because secure multi-UAV mission assurance requires more than a predicted label. A useful framework must also identify when predictions are reliable, when unseen mission shifts create risk, which telemetry signals influence the decision, and how the output can support response planning.


![Fig. 3. In-distribution macro-F1 comparison](../figures/hcc/fig3_indistribution_macro_f1.png)

![Fig. 4. OOD stress-test degradation](../figures/hcc/fig4_ood_stress_degradation.png)

![Fig. 5. In-distribution calibration evidence](../figures/hcc/fig5_calibration_evidence.png)

![Fig. 6. Ablation evidence for graph-temporal components](../figures/hcc/fig6_ablation_evidence.png)

![Fig. 7. Top mission-risk telemetry drivers](../figures/hcc/fig7_feature_importance_rank.png)

![Fig. 8. Runtime and complexity profile](../figures/hcc/fig8_runtime_profile.png)



### 5.0. RunPod-generated experimental evidence

The following figures are copied from the RunPod experimental artifact archive and provide direct evidence from the executed pipeline.

![RunPod Fig. R1. Other](figures/runpod_evidence/runpod_fig_01_other_fig_01_trust_swarm_architecture.png)

![RunPod Fig. R2. Other](figures/runpod_evidence/runpod_fig_02_other_fig_02_fusion_window_construction.png)

![RunPod Fig. R3. Other](figures/runpod_evidence/runpod_fig_03_other_fig_03_graph_temporal_model_architecture.png)

![RunPod Fig. R4. Other](figures/runpod_evidence/runpod_fig_04_other_fig_04_confidence_aware_fusion_pipeline.png)

![RunPod Fig. R5. Ood Stress](figures/runpod_evidence/runpod_fig_05_ood_stress_fig_05_ood_aware_mission_risk_evaluation.png)

![RunPod Fig. R6. Explainability](figures/runpod_evidence/runpod_fig_06_explainability_fig_06_fusion_driver_explainability.png)

![RunPod Fig. R7. Other](figures/runpod_evidence/runpod_fig_07_other_fig_07_recovery_decision_loop.png)

![RunPod Fig. R8. Other](figures/runpod_evidence/runpod_fig_08_other_ra_mars_architecture.png)

![RunPod Fig. R9. Other](figures/runpod_evidence/runpod_fig_09_other_fig1_trust_swarm_framework.png)

![RunPod Fig. R10. Other](figures/runpod_evidence/runpod_fig_10_other_fig2_graph_temporal_window.png)

![RunPod Fig. R11. Other](figures/runpod_evidence/runpod_fig_11_other_fig3_indistribution_macro_f1.png)

![RunPod Fig. R12. Ood Stress](figures/runpod_evidence/runpod_fig_12_ood_stress_fig4_ood_stress_degradation.png)

![RunPod Fig. R13. Calibration](figures/runpod_evidence/runpod_fig_13_calibration_fig5_calibration_evidence.png)

![RunPod Fig. R14. Ablation](figures/runpod_evidence/runpod_fig_14_ablation_fig6_ablation_evidence.png)

![RunPod Fig. R15. Explainability](figures/runpod_evidence/runpod_fig_15_explainability_fig7_feature_importance_rank.png)

![RunPod Fig. R16. Runtime](figures/runpod_evidence/runpod_fig_16_runtime_fig8_runtime_profile.png)

![RunPod Fig. R17. Other](figures/runpod_evidence/runpod_fig_17_other_fig_01_model_comparison_macro_f1.png)

![RunPod Fig. R18. Other](figures/runpod_evidence/runpod_fig_18_other_fig_02_model_comparison_accuracy.png)

![RunPod Fig. R19. Calibration](figures/runpod_evidence/runpod_fig_19_calibration_fig_03_uncertainty_ece.png)

![RunPod Fig. R20. Calibration](figures/runpod_evidence/runpod_fig_20_calibration_fig_04_uncertainty_brier.png)

![RunPod Fig. R21. Ood Stress](figures/runpod_evidence/runpod_fig_21_ood_stress_fig_05_ood_macro_f1.png)

![RunPod Fig. R22. Ood Stress](figures/runpod_evidence/runpod_fig_22_ood_stress_fig_06_ood_entropy.png)

![RunPod Fig. R23. Explainability](figures/runpod_evidence/runpod_fig_23_explainability_fig_07_feature_importance.png)

![RunPod Fig. R24. Other](figures/runpod_evidence/runpod_fig_24_other_ra_mars_threat_model.png)

![RunPod Fig. R25. Explainability](figures/runpod_evidence/runpod_fig_25_explainability_feature_importance.png)

![RunPod Fig. R26. Explainability](figures/runpod_evidence/runpod_fig_26_explainability_feature_importance.png)

![RunPod Fig. R27. Explainability](figures/runpod_evidence/runpod_fig_27_explainability_feature_importance.png)

![RunPod Fig. R28. Explainability](figures/runpod_evidence/runpod_fig_28_explainability_feature_importance.png)

### 5.0. Real RunPod experimental evidence package

This subsection consolidates the actual RunPod-generated experimental evidence used in the manuscript, including model-comparison summaries, OOD stress-test outputs, uncertainty/calibration summaries, feature-importance results, ablation evidence, and runtime-complexity profiling. Unlike conceptual architecture figures, these figures are generated directly from the extracted RunPod CSV result artifacts.

![Fig. 3. RunPod model-comparison macro-F1 evidence](figures/hcc_real_evidence/fig3_runpod_model_macro_f1.png)

![Fig. 4. RunPod model-comparison accuracy evidence](figures/hcc_real_evidence/fig4_runpod_model_accuracy.png)

![Fig. 5. RunPod OOD macro-F1 degradation evidence](figures/hcc_real_evidence/fig5_runpod_ood_macro_f1.png)

![Fig. 6. RunPod OOD uncertainty/entropy evidence](figures/hcc_real_evidence/fig6_runpod_ood_entropy.png)

![Fig. 8. RunPod feature-importance evidence](figures/hcc_real_evidence/fig8_runpod_feature_importance.png)

![Fig. 9. RunPod ablation evidence](figures/hcc_real_evidence/fig9_runpod_ablation.png)

The corresponding publication-quality evidence tables are generated in `docs/tables/hcc_real_runpod_evidence_tables_v1.md` and should be used as the source for final manuscript tables.


### 5.0.1. Compact real RunPod evidence tables

The following compact tables are generated from the real extracted RunPod CSV outputs. They provide the numerical evidence behind the model-comparison, OOD, calibration, feature-importance, ablation, and runtime claims.

### Table R1. RunPod model-comparison summary
| model                    |   accuracy_mean |   macro_f1_mean |
|:-------------------------|----------------:|----------------:|
| GraphTemporalTransformer |          0.9647 |          0.875  |
| cnn1d                    |          0.9987 |          0.9971 |
| gru                      |          0.9796 |          0.9288 |
| lstm                     |          0.9871 |          0.9608 |

### Table R2. RunPod OOD stress-test summary
| condition              |   macro_f1_mean |   mean_entropy_mean |
|:-----------------------|----------------:|--------------------:|
| delayed_combined       |          0.0521 |              0.231  |
| in_distribution_test   |          0.875  |              0.0928 |
| intermittent_tampering |          0.5965 |              0.2486 |
| slow_gps_drift         |          0.1701 |              0.2721 |
| stealth_jammer         |          0.0779 |              0.3449 |
| unseen_swarm_noise     |          0.8744 |              0.0928 |

### Table R3. RunPod calibration and uncertainty summary
| model                    |   mc_samples_mean |   mc_samples_std |   accuracy_mean |   accuracy_std |   macro_f1_mean |   macro_f1_std |   expected_calibration_error_mean |   expected_calibration_error_std |   brier_score_mean |   brier_score_std |   mean_confidence_mean |   mean_confidence_std |   mean_predictive_entropy_mean |   mean_predictive_entropy_std |
|:-------------------------|------------------:|-----------------:|----------------:|---------------:|----------------:|---------------:|----------------------------------:|---------------------------------:|-------------------:|------------------:|-----------------------:|----------------------:|-------------------------------:|------------------------------:|
| GraphTemporalTransformer |                20 |                0 |          0.9655 |         0.0076 |          0.8808 |         0.0122 |                            0.0088 |                           0.0024 |             0.0531 |            0.0129 |                 0.9601 |                0.0056 |                         0.0986 |                        0.0117 |

### Table R4. RunPod top telemetry feature-importance summary
| feature                |   baseline_macro_f1_mean |
|:-----------------------|-------------------------:|
| latency_ms             |                    0.875 |
| zone_coverage          |                    0.875 |
| route_deviation_m      |                    0.875 |
| mission_progress       |                    0.875 |
| gps_jump_m             |                    0.875 |
| velocity_inconsistency |                    0.875 |
| energy_consumption     |                    0.875 |
| packet_loss_rate       |                    0.875 |
| battery_level          |                    0.875 |

### Table R5. RunPod ablation summary
| configuration                      | ablation_type      |   train_loss |   test_loss |   accuracy |   macro_precision |   macro_recall |   macro_f1 |   parameters | calibration_evidence   | ood_evidence   | explanation_evidence   | recovery_support   | interpretation                                                                                                        |
|:-----------------------------------|:-------------------|-------------:|------------:|-----------:|------------------:|---------------:|-----------:|-------------:|:-----------------------|:---------------|:-----------------------|:-------------------|:----------------------------------------------------------------------------------------------------------------------|
| A0_full_graph_temporal_transformer | model_architecture |       0.0955 |      0.1182 |     0.9579 |            0.9276 |         0.8433 |     0.8734 |       680840 | yes                    | yes            | yes                    | yes                | Architecture-level ablation trained and evaluated on the same graph-temporal dataset.                                 |
| A1_without_uav_node_attention      | model_architecture |       0.1224 |      0.102  |     0.9572 |            0.793  |         0.7993 |     0.7903 |       415880 | yes                    | yes            | yes                    | yes                | Architecture-level ablation trained and evaluated on the same graph-temporal dataset.                                 |
| A2_without_temporal_transformer    | model_architecture |       0.0973 |      0.1341 |     0.9507 |            0.9263 |         0.7982 |     0.8237 |       284296 | yes                    | yes            | yes                    | yes                | Architecture-level ablation trained and evaluated on the same graph-temporal dataset.                                 |
| A3_without_uncertainty_calibration | framework_module   |     nan      |      0.1182 |     0.9579 |            0.9276 |         0.8433 |     0.8734 |       680840 | no                     | yes            | yes                    | yes                | Removes confidence reliability evidence; prediction remains available but ECE/Brier/confidence evidence is absent.    |
| A4_without_ood_stress_testing      | framework_module   |     nan      |      0.1182 |     0.9579 |            0.9276 |         0.8433 |     0.8734 |       680840 | yes                    | no             | yes                    | yes                | Removes unseen-shift vulnerability evidence; prediction remains available but OOD risk evidence is absent.            |
| A5_without_explainability          | framework_module   |     nan      |      0.1182 |     0.9579 |            0.9276 |         0.8433 |     0.8734 |       680840 | yes                    | yes            | no                     | yes                | Removes traceable mission-risk driver evidence; prediction remains available but feature-level explanation is absent. |
| A6_without_recovery_reasoning      | framework_module   |     nan      |      0.1182 |     0.9579 |            0.9276 |         0.8433 |     0.8734 |       680840 | yes                    | yes            | yes                    | no                 | Removes mission-response support; prediction, calibration, OOD, and explanation remain available.                     |

### Table R6. RunPod runtime-complexity summary
| model                    |   parameters |   model_size_mb |   batch_size |   window_size |   num_uavs |   num_features |   inference_batch_latency_ms |   inference_sample_latency_ms |   throughput_windows_per_second |   single_train_step_ms | device   |   gpu_memory_mb |
|:-------------------------|-------------:|----------------:|-------------:|--------------:|-----------:|---------------:|-----------------------------:|------------------------------:|--------------------------------:|-----------------------:|:---------|----------------:|
| LSTM                     |       308616 |           1.181 |          128 |            20 |         20 |              9 |                        0.214 |                        0.0017 |                        599007   |                  1.674 | cuda     |         147.314 |
| GRU                      |       235912 |           0.904 |          128 |            20 |         20 |              9 |                        0.177 |                        0.0014 |                        724111   |                  1.48  | cuda     |         147.595 |
| CNN1D                    |       136840 |           0.531 |          128 |            20 |         20 |              9 |                        0.211 |                        0.0016 |                        606987   |                  1.465 | cuda     |         147.595 |
| GraphTemporalTransformer |       680840 |           2.618 |          128 |            20 |         20 |              9 |                        2.267 |                        0.0177 |                         56458.4 |                  9.938 | cuda     |         932.105 |


### 5.1. In-distribution mission-state recognition

Table 2 reports the main in-distribution classification findings. The in-distribution evaluation shows that mission-state recognition is feasible using graph-temporal UAV telemetry. The Graph-Temporal Transformer achieves a mean accuracy of 0.9647 and a mean macro F1 score of 0.8750 across the three-seed evaluation. These values indicate that the model can learn mission-state patterns from communication, navigation, energy, coverage, and mission-progress telemetry. The result is meaningful because the evaluation includes not only normal and single-attack conditions, but also combined cyber-physical attack states.

At the same time, the baseline comparison shows that the 1D-CNN achieves stronger raw in-distribution classification performance, with a mean macro F1 score of 0.9971. This is an important result and should be interpreted carefully. It means TRUST-Swarm should not be presented as a claim that the Graph-Temporal Transformer is the strongest standalone classifier. A journal-level interpretation should avoid that overclaim. The stronger and more accurate conclusion is that TRUST-Swarm contributes an integrated high-confidence mission-assurance framework. In this framework, raw classification is only one component; calibration, OOD vulnerability exposure, explainability, ablation evidence, runtime feasibility, and recovery reasoning are also part of the contribution.

This interpretation imshows the scientific positioning of the paper. A classification-only paper would be weakened by a baseline that performs better. A high-confidence computing paper can still make a strong contribution if it shows that the proposed framework evaluates reliability, robustness, traceability, and response support beyond raw accuracy.

### 5.2. Calibration and confidence reliability

The calibration results show that the Graph-Temporal Transformer produces strong in-distribution probabilistic reliability. The model achieves an Expected Calibration Error of 0.0088 and a Brier score of 0.0531. A low ECE means that the predicted confidence is closely aligned with empirical correctness. A low Brier score indicates that the probability distribution is not only accurate in its top prediction but also reasonably reliable across the class-probability vector.

This result is important for secure UAV swarm mission assurance. In an autonomous mission, a high-confidence wrong prediction can be more dangerous than a low-confidence prediction, because the system may proceed without escalation. Calibration therefore acts as an assurance signal. A prediction with high confidence and low entropy can support normal continuation or targeted response. A prediction with low confidence or high entropy can trigger monitoring, escalation, or recovery reasoning.

The calibration evidence also helps distinguish TRUST-Swarm from ordinary classification systems. A model that reports only accuracy cannot tell whether its probabilities should be trusted. TRUST-Swarm explicitly evaluates this reliability dimension, making the output more useful for high-confidence computing.

### 5.3. OOD cyber-physical stress-test behavior

Fig. 2 summarizes the OOD stress-test trend. The OOD stress-test results reveal a key finding: in-distribution performance does not guarantee reliability under unseen cyber-physical shifts. Under intermittent tampering, macro F1 decreases to 0.5965. More severe unseen conditions such as stealth jamming, slow GPS drift, and delayed combined attacks show substantial degradation. This behavior demonstrates why OOD testing is necessary for high-confidence mission assurance.

This result should not be hidden or softened. In a strong journal paper, the OOD degradation should be presented as evidence that the framework exposes mission-risk conditions that standard testing would miss. If the manuscript only reported in-distribution accuracy, it would give an incomplete and potentially misleading picture of mission reliability. OOD testing shows where the model’s learned decision boundary is vulnerable and where additional monitoring, retraining, adaptation, or recovery logic may be required.

The most important interpretation is that TRUST-Swarm does not solve all unseen attack conditions. Instead, it provides a structured way to identify them. This is scientifically stronger and more honest. For high-confidence computing, exposing failure modes is a contribution because it helps define the reliability boundary of the intelligent system.

### 5.4. Explainability and mission-risk drivers

The perturbation-based explainability analysis identifies latency, zone coverage, route deviation, mission progress, and GPS jump as the strongest mission-risk drivers. These features are operationally meaningful. Latency reflects communication degradation and is strongly associated with jamming-like mission disruption. Zone coverage reflects mission effectiveness and swarm coverage quality. Route deviation and GPS jump reflect navigation manipulation and spoofing-like effects. Mission progress reflects whether the swarm is advancing toward mission completion or being disrupted.

This result supports traceable mission reasoning. Instead of producing only a mission-state label, TRUST-Swarm identifies which telemetry factors most influenced the decision. This helps convert model output into evidence that can be inspected by a human analyst or used by a recovery-reasoning layer. For example, a spoofing prediction becomes more credible when route deviation and GPS jump are highly influential. A jamming prediction becomes more credible when latency and packet loss are influential. A tampering or combined-attack prediction becomes more credible when mission progress, energy state, and coverage variables degrade.

The explainability results therefore strengthen the high-confidence framing of the paper. The framework is not simply a black-box classifier; it provides traceable evidence connected to mission semantics.

### 5.5. Ablation evidence

The ablation study evaluates whether major framework components contribute to the final mission-assurance behavior. Architectural ablations examine the effect of removing UAV-node attention and temporal transformer reasoning. Framework-level ablations examine the contribution of calibration evidence, OOD stress evidence, explainability evidence, and recovery-oriented support.

The full Graph-Temporal Transformer reaches a macro F1 score of 0.8734 in the ablation setting. Removing UAV-node attention reduces macro F1 to 0.7903, and removing the temporal transformer reduces macro F1 to 0.8237. These results indicate that both node-level interaction modeling and temporal reasoning contribute to classification performance. Node attention appears especially important because UAV swarm mission degradation is distributed across multiple nodes rather than isolated to a single flat time-series signal.

From the framework perspective, ablation also clarifies that classification is not the only value of TRUST-Swarm. Calibration, OOD analysis, explanation, and recovery reasoning do not necessarily imshow raw accuracy directly, but they imshow assurance evidence. This distinction is essential for the journal narrative. The paper should clearly separate classification performance from high-confidence mission-assurance value.

### 5.6. Runtime and complexity analysis

Runtime profiling shows that the Graph-Temporal Transformer has 680,840 trainable parameters and a model size of approximately 2.618 MB. The measured inference latency is 2.267 ms per batch and 0.0177 ms per sample, with throughput of approximately 56,458 windows per second. The training-step time is approximately 9.938 ms.

These results support the practical computing feasibility of the framework. A high-confidence intelligent system must not only provide assurance evidence; it must also be computationally reasonable. The measured model size and inference speed suggest that the prediction layer is lightweight enough for rapid mission-window processing in a GPU-enabled environment. However, the current runtime results should be interpreted as computational profiling rather than deployment validation. Real UAV deployment would require additional testing under edge-hardware constraints, communication delays, onboard compute limits, and hardware-in-the-loop conditions.

### 5.7. Recovery-oriented reasoning

The recovery-reasoning layer demonstrates how prediction, confidence, entropy, and mission-risk indicators can be mapped to response-oriented actions. The action space includes continue, monitor, reroute, reassign, isolate node, and return to base. This module should not be described as an validated in field settings UAV controller. Instead, it should be described as a recovery-reasoning scaffold that shows how high-confidence prediction outputs can support mission-response planning.

This distinction is important. A detection system that stops at classification does not complete the mission-assurance loop. TRUST-Swarm connects recognition evidence to possible response actions. When confidence is high and the predicted state is normal, continue may be appropriate. When uncertainty is high, monitor or escalate may be appropriate. When spoofing indicators are strong, rerouting may be considered. When node-level evidence suggests local compromise, isolate-node reasoning may be relevant. When combined attacks and uncertainty are high, return-to-base reasoning may be safer.

### 5.8. Discussion

The results support four main observations. First, graph-temporal mission-state recognition is feasible for simulated UAV swarm cyber-physical telemetry. Second, raw in-distribution classification performance alone is not enough to support high-confidence mission assurance. Third, OOD stress testing is necessary because performance can degrade sharply under unseen cyber-physical shifts. Fourth, explainability and recovery reasoning help connect model predictions to mission-level evidence and response support.

The most important scientific point is that TRUST-Swarm should be framed as an assurance framework rather than a classifier superiority claim. The 1D-CNN baseline shows stronger raw in-distribution classification performance. However, the proposed framework contributes additional high-confidence computing capabilities that are not captured by raw macro F1 alone. These include calibrated confidence, OOD vulnerability exposure, traceable mission-risk drivers, ablation evidence, runtime feasibility, and recovery-oriented reasoning.

This balanced interpretation makes the manuscript stronger. It avoids exaggerated claims and aligns the contribution with the scope of High-Confidence Computing. The paper demonstrates that secure UAV swarm mission assurance requires integrated evidence about prediction, reliability, robustness, traceability, and response support.

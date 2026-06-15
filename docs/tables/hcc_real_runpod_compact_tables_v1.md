# Compact Real RunPod Evidence Tables v1

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

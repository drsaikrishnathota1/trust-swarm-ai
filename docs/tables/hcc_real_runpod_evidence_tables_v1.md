# Real RunPod Evidence Tables v1

## Table R1. Model comparison summary from RunPod

| model                    |   test_loss_mean |   test_loss_std |   accuracy_mean |   accuracy_std |   macro_f1_mean |   macro_f1_std |   macro_precision_mean |   macro_precision_std |   macro_recall_mean |   macro_recall_std |
|:-------------------------|-----------------:|----------------:|----------------:|---------------:|----------------:|---------------:|-----------------------:|----------------------:|--------------------:|-------------------:|
| GraphTemporalTransformer |       0.0932861  |     0.0214069   |        0.964672 |    0.00654239  |        0.874981 |    0.0143455   |               0.89347  |            0.0283992  |            0.870002 |         0.0159637  |
| cnn1d                    |       0.00418065 |     0.000928773 |        0.998726 |    0.000253053 |        0.997101 |    0.000817994 |               0.997089 |            0.00172217 |            0.997135 |         0.00173353 |
| gru                      |       0.054006   |     0.0211247   |        0.979621 |    0.0107419   |        0.928846 |    0.0470609   |               0.946894 |            0.0348889  |            0.917033 |         0.053443   |
| lstm                     |       0.0373852  |     0.00404867  |        0.987062 |    0.00224918  |        0.960757 |    0.0072283   |               0.962745 |            0.0109803  |            0.959749 |         0.00503377 |

## Table R2. Model comparison across all seeds

| model                    |   test_loss |   accuracy |   macro_f1 |   macro_precision |   macro_recall | model_path                                         |   seed |
|:-------------------------|------------:|-----------:|-----------:|------------------:|---------------:|:---------------------------------------------------|-------:|
| lstm                     |  0.0328194  |   0.98904  |   0.965858 |          0.973522 |       0.958864 | results/journal/seed_123/models/lstm_baseline.pt   |    123 |
| gru                      |  0.0371473  |   0.988034 |   0.96336  |          0.971013 |       0.957528 | results/journal/seed_123/models/gru_baseline.pt    |    123 |
| cnn1d                    |  0.00514116 |   0.998492 |   0.996705 |          0.995103 |       0.998335 | results/journal/seed_123/models/cnn1d_baseline.pt  |    123 |
| lstm                     |  0.0405381  |   0.984615 |   0.952486 |          0.951572 |       0.955217 | results/journal/seed_2026/models/lstm_baseline.pt  |   2026 |
| gru                      |  0.0777026  |   0.967521 |   0.875239 |          0.906889 |       0.856458 | results/journal/seed_2026/models/gru_baseline.pt   |   2026 |
| cnn1d                    |  0.00411354 |   0.998693 |   0.996557 |          0.997995 |       0.995147 | results/journal/seed_2026/models/cnn1d_baseline.pt |   2026 |
| lstm                     |  0.038798   |   0.987531 |   0.963928 |          0.963142 |       0.965167 | results/journal/seed_42/models/lstm_baseline.pt    |     42 |
| gru                      |  0.0471681  |   0.983308 |   0.947939 |          0.962781 |       0.937112 | results/journal/seed_42/models/gru_baseline.pt     |     42 |
| cnn1d                    |  0.00328726 |   0.998994 |   0.998042 |          0.998169 |       0.997923 | results/journal/seed_42/models/cnn1d_baseline.pt   |     42 |
| GraphTemporalTransformer |  0.0954526  |   0.965008 |   0.873931 |          0.873847 |       0.879307 | nan                                                |    123 |
| GraphTemporalTransformer |  0.0708784  |   0.971041 |   0.889822 |          0.926034 |       0.87913  | nan                                                |   2026 |
| GraphTemporalTransformer |  0.113527   |   0.957969 |   0.861189 |          0.880528 |       0.851569 | nan                                                |     42 |

## Table R3. OOD summary from RunPod

| condition              |   accuracy_mean |   accuracy_std |   macro_f1_mean |   macro_f1_std |   mean_confidence_mean |   mean_confidence_std |   mean_entropy_mean |   mean_entropy_std |   low_confidence_rate_lt_0_70_mean |   low_confidence_rate_lt_0_70_std |
|:-----------------------|----------------:|---------------:|----------------:|---------------:|-----------------------:|----------------------:|--------------------:|-------------------:|-----------------------------------:|----------------------------------:|
| delayed_combined       |       0.0305346 |     0.0045885  |       0.0521043 |      0.024193  |               0.919412 |            0.0289046  |           0.230969  |         0.0861848  |                          0.0651249 |                        0.00858969 |
| in_distribution_test   |       0.964672  |     0.00654239 |       0.874981  |      0.0143455 |               0.963123 |            0.00760544 |           0.0927598 |         0.0188087  |                          0.0421652 |                        0.0147581  |
| intermittent_tampering |       0.690967  |     0.0309018  |       0.596465  |      0.0517906 |               0.891626 |            0.0141439  |           0.248618  |         0.0206712  |                          0.143355  |                        0.0318368  |
| slow_gps_drift         |       0.125256  |     0.0138451  |       0.170055  |      0.0509539 |               0.887549 |            0.0328046  |           0.272128  |         0.0766101  |                          0.143389  |                        0.0509236  |
| stealth_jammer         |       0.0651249 |     0.01969    |       0.0779012 |      0.0236129 |               0.865214 |            0.0263052  |           0.344934  |         0.00910675 |                          0.120798  |                        0.127478   |
| unseen_swarm_noise     |       0.964538  |     0.00664893 |       0.874441  |      0.0147106 |               0.963103 |            0.00762395 |           0.0928117 |         0.0188697  |                          0.0421652 |                        0.0147372  |

## Table R4. OOD across all seeds

| condition              |   accuracy |   macro_f1 |   mean_confidence |   mean_entropy |   low_confidence_rate_lt_0_70 |   seed |
|:-----------------------|-----------:|-----------:|------------------:|---------------:|------------------------------:|-------:|
| in_distribution_test   |  0.965008  |  0.873931  |          0.957566 |      0.111923  |                     0.0404223 |    123 |
| stealth_jammer         |  0.0433384 |  0.0695055 |          0.871367 |      0.350191  |                     0.0582202 |    123 |
| slow_gps_drift         |  0.116038  |  0.162032  |          0.849701 |      0.359593  |                     0.202011  |    123 |
| intermittent_tampering |  0.657014  |  0.53679   |          0.878165 |      0.27132   |                     0.164907  |    123 |
| delayed_combined       |  0.0293615 |  0.0757544 |          0.886245 |      0.329987  |                     0.0556058 |    123 |
| unseen_swarm_noise     |  0.965008  |  0.873931  |          0.957515 |      0.112051  |                     0.0401207 |    123 |
| in_distribution_test   |  0.971041  |  0.889822  |          0.971791 |      0.0743271 |                     0.028356  |   2026 |
| stealth_jammer         |  0.0703871 |  0.0596334 |          0.836377 |      0.350192  |                     0.267471  |   2026 |
| slow_gps_drift         |  0.118552  |  0.123588  |          0.907805 |      0.216927  |                     0.118049  |   2026 |
| intermittent_tampering |  0.698441  |  0.629688  |          0.906366 |      0.230882  |                     0.106787  |   2026 |
| delayed_combined       |  0.0355958 |  0.0531559 |          0.939222 |      0.172833  |                     0.0722976 |   2026 |
| unseen_swarm_noise     |  0.97094   |  0.8894    |          0.971788 |      0.0743353 |                     0.0285571 |   2026 |
| in_distribution_test   |  0.957969  |  0.861189  |          0.960012 |      0.0920291 |                     0.0577174 |     42 |
| stealth_jammer         |  0.0816491 |  0.104565  |          0.887896 |      0.334418  |                     0.0367019 |     42 |
| slow_gps_drift         |  0.141176  |  0.224544  |          0.905142 |      0.239865  |                     0.110106  |     42 |
| intermittent_tampering |  0.717446  |  0.622917  |          0.890346 |      0.243652  |                     0.158371  |     42 |
| delayed_combined       |  0.0266466 |  0.0274026 |          0.932769 |      0.190086  |                     0.0674711 |     42 |
| unseen_swarm_noise     |  0.957667  |  0.859992  |          0.960006 |      0.0920485 |                     0.057818  |     42 |

## Table R5. Calibration/uncertainty summary

| model                    |   mc_samples_mean |   mc_samples_std |   accuracy_mean |   accuracy_std |   macro_f1_mean |   macro_f1_std |   expected_calibration_error_mean |   expected_calibration_error_std |   brier_score_mean |   brier_score_std |   mean_confidence_mean |   mean_confidence_std |   mean_predictive_entropy_mean |   mean_predictive_entropy_std |
|:-------------------------|------------------:|-----------------:|----------------:|---------------:|----------------:|---------------:|----------------------------------:|---------------------------------:|-------------------:|------------------:|-----------------------:|----------------------:|-------------------------------:|------------------------------:|
| GraphTemporalTransformer |                20 |                0 |        0.965477 |     0.00759447 |         0.88082 |      0.0122383 |                        0.00881825 |                       0.00239235 |          0.0531188 |         0.0129488 |               0.960118 |            0.00560125 |                      0.0986478 |                     0.0117294 |

## Table R6. Calibration/uncertainty across all seeds

|   mc_samples |   accuracy |   macro_f1 |   expected_calibration_error |   brier_score |   mean_confidence |   mean_predictive_entropy |   seed | model                    |
|-------------:|-----------:|-----------:|-----------------------------:|--------------:|------------------:|--------------------------:|-------:|:-------------------------|
|           20 |   0.966918 |   0.878399 |                   0.00963938 |     0.0516318 |          0.957279 |                 0.110788  |    123 | GraphTemporalTransformer |
|           20 |   0.972247 |   0.894087 |                   0.00612348 |     0.0409777 |          0.966571 |                 0.0873777 |   2026 | GraphTemporalTransformer |
|           20 |   0.957265 |   0.869973 |                   0.0106919  |     0.066747  |          0.956505 |                 0.0977775 |     42 | GraphTemporalTransformer |

## Table R7. Feature-importance summary

| feature                |   baseline_macro_f1_mean |   baseline_macro_f1_std |   perturbed_macro_f1_mean |   perturbed_macro_f1_std |   macro_f1_drop_mean |   macro_f1_drop_std |
|:-----------------------|-------------------------:|------------------------:|--------------------------:|-------------------------:|---------------------:|--------------------:|
| latency_ms             |                 0.874981 |               0.0143455 |                  0.185565 |                0.0218403 |          0.689416    |         0.0311225   |
| zone_coverage          |                 0.874981 |               0.0143455 |                  0.47488  |                0.0331432 |          0.4001      |         0.0440301   |
| route_deviation_m      |                 0.874981 |               0.0143455 |                  0.569384 |                0.10205   |          0.305597    |         0.0897453   |
| mission_progress       |                 0.874981 |               0.0143455 |                  0.575979 |                0.053349  |          0.299002    |         0.0415504   |
| gps_jump_m             |                 0.874981 |               0.0143455 |                  0.581613 |                0.0329428 |          0.293368    |         0.0215196   |
| velocity_inconsistency |                 0.874981 |               0.0143455 |                  0.865369 |                0.0275112 |          0.00961181  |         0.0142183   |
| energy_consumption     |                 0.874981 |               0.0143455 |                  0.872556 |                0.014377  |          0.00242423  |         0.00139375  |
| packet_loss_rate       |                 0.874981 |               0.0143455 |                  0.87472  |                0.0145077 |          0.000260533 |         0.000243868 |
| battery_level          |                 0.874981 |               0.0143455 |                  0.875623 |                0.0147503 |         -0.000642676 |         0.00086137  |

## Table R8. Ablation summary

| configuration                      | ablation_type      |   train_loss |   test_loss |   accuracy |   macro_precision |   macro_recall |   macro_f1 |   parameters | calibration_evidence   | ood_evidence   | explanation_evidence   | recovery_support   | interpretation                                                                                                        |
|:-----------------------------------|:-------------------|-------------:|------------:|-----------:|------------------:|---------------:|-----------:|-------------:|:-----------------------|:---------------|:-----------------------|:-------------------|:----------------------------------------------------------------------------------------------------------------------|
| A0_full_graph_temporal_transformer | model_architecture |    0.0954618 |    0.118205 |   0.957919 |          0.927624 |       0.843321 |   0.873416 |       680840 | yes                    | yes            | yes                    | yes                | Architecture-level ablation trained and evaluated on the same graph-temporal dataset.                                 |
| A1_without_uav_node_attention      | model_architecture |    0.122424  |    0.102027 |   0.957164 |          0.792967 |       0.799302 |   0.790346 |       415880 | yes                    | yes            | yes                    | yes                | Architecture-level ablation trained and evaluated on the same graph-temporal dataset.                                 |
| A2_without_temporal_transformer    | model_architecture |    0.0972568 |    0.134144 |   0.950679 |          0.926307 |       0.79822  |   0.82372  |       284296 | yes                    | yes            | yes                    | yes                | Architecture-level ablation trained and evaluated on the same graph-temporal dataset.                                 |
| A3_without_uncertainty_calibration | framework_module   |  nan         |    0.118205 |   0.957919 |          0.927624 |       0.843321 |   0.873416 |       680840 | no                     | yes            | yes                    | yes                | Removes confidence reliability evidence; prediction remains available but ECE/Brier/confidence evidence is absent.    |
| A4_without_ood_stress_testing      | framework_module   |  nan         |    0.118205 |   0.957919 |          0.927624 |       0.843321 |   0.873416 |       680840 | yes                    | no             | yes                    | yes                | Removes unseen-shift vulnerability evidence; prediction remains available but OOD risk evidence is absent.            |
| A5_without_explainability          | framework_module   |  nan         |    0.118205 |   0.957919 |          0.927624 |       0.843321 |   0.873416 |       680840 | yes                    | yes            | no                     | yes                | Removes traceable mission-risk driver evidence; prediction remains available but feature-level explanation is absent. |
| A6_without_recovery_reasoning      | framework_module   |  nan         |    0.118205 |   0.957919 |          0.927624 |       0.843321 |   0.873416 |       680840 | yes                    | yes            | yes                    | no                 | Removes mission-response support; prediction, calibration, OOD, and explanation remain available.                     |

## Table R9. Runtime-complexity summary

| model                    |   parameters |   model_size_mb |   batch_size |   window_size |   num_uavs |   num_features |   inference_batch_latency_ms |   inference_sample_latency_ms |   throughput_windows_per_second |   single_train_step_ms | device   |   gpu_memory_mb |
|:-------------------------|-------------:|----------------:|-------------:|--------------:|-----------:|---------------:|-----------------------------:|------------------------------:|--------------------------------:|-----------------------:|:---------|----------------:|
| LSTM                     |       308616 |           1.181 |          128 |            20 |         20 |              9 |                        0.214 |                      0.001669 |                        599007   |                  1.674 | cuda     |         147.314 |
| GRU                      |       235912 |           0.904 |          128 |            20 |         20 |              9 |                        0.177 |                      0.001381 |                        724111   |                  1.48  | cuda     |         147.595 |
| CNN1D                    |       136840 |           0.531 |          128 |            20 |         20 |              9 |                        0.211 |                      0.001647 |                        606987   |                  1.465 | cuda     |         147.595 |
| GraphTemporalTransformer |       680840 |           2.618 |          128 |            20 |         20 |              9 |                        2.267 |                      0.017712 |                         56458.4 |                  9.938 | cuda     |         932.105 |

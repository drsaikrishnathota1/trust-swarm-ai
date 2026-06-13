# TRUST-Swarm Manuscript Results Tables

These tables summarize the final three-seed RunPod journal experiment.

Configuration: 300 runs, 240 timesteps, 20 UAVs, 30 epochs, seeds 42, 123, and 2026.

## Table 1. Model Comparison Summary

| model                    |   test_loss_mean |   test_loss_std |   accuracy_mean |   accuracy_std |   macro_f1_mean |   macro_f1_std |   macro_precision_mean |   macro_precision_std |   macro_recall_mean |   macro_recall_std |
|:-------------------------|-----------------:|----------------:|----------------:|---------------:|----------------:|---------------:|-----------------------:|----------------------:|--------------------:|-------------------:|
| GraphTemporalTransformer |           0.0933 |          0.0214 |          0.9647 |         0.0065 |          0.875  |         0.0143 |                 0.8935 |                0.0284 |              0.87   |             0.016  |
| cnn1d                    |           0.0042 |          0.0009 |          0.9987 |         0.0003 |          0.9971 |         0.0008 |                 0.9971 |                0.0017 |              0.9971 |             0.0017 |
| gru                      |           0.054  |          0.0211 |          0.9796 |         0.0107 |          0.9288 |         0.0471 |                 0.9469 |                0.0349 |              0.917  |             0.0534 |
| lstm                     |           0.0374 |          0.004  |          0.9871 |         0.0022 |          0.9608 |         0.0072 |                 0.9627 |                0.011  |              0.9597 |             0.005  |



## Table 2. Uncertainty Calibration Summary

| model                    |   mc_samples_mean |   mc_samples_std |   accuracy_mean |   accuracy_std |   macro_f1_mean |   macro_f1_std |   expected_calibration_error_mean |   expected_calibration_error_std |   brier_score_mean |   brier_score_std |   mean_confidence_mean |   mean_confidence_std |   mean_predictive_entropy_mean |   mean_predictive_entropy_std |
|:-------------------------|------------------:|-----------------:|----------------:|---------------:|----------------:|---------------:|----------------------------------:|---------------------------------:|-------------------:|------------------:|-----------------------:|----------------------:|-------------------------------:|------------------------------:|
| GraphTemporalTransformer |                20 |                0 |          0.9655 |         0.0076 |          0.8808 |         0.0122 |                            0.0088 |                           0.0024 |             0.0531 |            0.0129 |                 0.9601 |                0.0056 |                         0.0986 |                        0.0117 |



## Table 3. OOD / Unseen Attack Summary

| condition              |   accuracy_mean |   accuracy_std |   macro_f1_mean |   macro_f1_std |   mean_confidence_mean |   mean_confidence_std |   mean_entropy_mean |   mean_entropy_std |   low_confidence_rate_lt_0_70_mean |   low_confidence_rate_lt_0_70_std |
|:-----------------------|----------------:|---------------:|----------------:|---------------:|-----------------------:|----------------------:|--------------------:|-------------------:|-----------------------------------:|----------------------------------:|
| delayed_combined       |          0.0305 |         0.0046 |          0.0521 |         0.0242 |                 0.9194 |                0.0289 |              0.231  |             0.0862 |                             0.0651 |                            0.0086 |
| in_distribution_test   |          0.9647 |         0.0065 |          0.875  |         0.0143 |                 0.9631 |                0.0076 |              0.0928 |             0.0188 |                             0.0422 |                            0.0148 |
| intermittent_tampering |          0.691  |         0.0309 |          0.5965 |         0.0518 |                 0.8916 |                0.0141 |              0.2486 |             0.0207 |                             0.1434 |                            0.0318 |
| slow_gps_drift         |          0.1253 |         0.0138 |          0.1701 |         0.051  |                 0.8875 |                0.0328 |              0.2721 |             0.0766 |                             0.1434 |                            0.0509 |
| stealth_jammer         |          0.0651 |         0.0197 |          0.0779 |         0.0236 |                 0.8652 |                0.0263 |              0.3449 |             0.0091 |                             0.1208 |                            0.1275 |
| unseen_swarm_noise     |          0.9645 |         0.0066 |          0.8744 |         0.0147 |                 0.9631 |                0.0076 |              0.0928 |             0.0189 |                             0.0422 |                            0.0147 |



## Table 4. Feature Importance Summary

| feature                |   baseline_macro_f1_mean |   baseline_macro_f1_std |   perturbed_macro_f1_mean |   perturbed_macro_f1_std |   macro_f1_drop_mean |   macro_f1_drop_std |
|:-----------------------|-------------------------:|------------------------:|--------------------------:|-------------------------:|---------------------:|--------------------:|
| latency_ms             |                    0.875 |                  0.0143 |                    0.1856 |                   0.0218 |               0.6894 |              0.0311 |
| zone_coverage          |                    0.875 |                  0.0143 |                    0.4749 |                   0.0331 |               0.4001 |              0.044  |
| route_deviation_m      |                    0.875 |                  0.0143 |                    0.5694 |                   0.1021 |               0.3056 |              0.0897 |
| mission_progress       |                    0.875 |                  0.0143 |                    0.576  |                   0.0533 |               0.299  |              0.0416 |
| gps_jump_m             |                    0.875 |                  0.0143 |                    0.5816 |                   0.0329 |               0.2934 |              0.0215 |
| velocity_inconsistency |                    0.875 |                  0.0143 |                    0.8654 |                   0.0275 |               0.0096 |              0.0142 |
| energy_consumption     |                    0.875 |                  0.0143 |                    0.8726 |                   0.0144 |               0.0024 |              0.0014 |
| packet_loss_rate       |                    0.875 |                  0.0143 |                    0.8747 |                   0.0145 |               0.0003 |              0.0002 |
| battery_level          |                    0.875 |                  0.0143 |                    0.8756 |                   0.0148 |              -0.0006 |              0.0009 |



## Key Interpretation

- CNN1D achieved the strongest in-distribution classification performance.

- Graph-Temporal Transformer achieved strong calibrated performance and supports the trustworthy mission-assurance framing.

- OOD stress tests show severe degradation under stealth jamming, slow GPS drift, and delayed combined attacks.

- Feature importance highlights latency, zone coverage, route deviation, mission progress, and GPS jump as major decision drivers.

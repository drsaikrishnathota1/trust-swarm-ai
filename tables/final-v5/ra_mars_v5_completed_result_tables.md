# RA-MARS v5 Completed Validation Result Tables

These tables were generated from completed v5 validation outputs copied into `simulations/final-results`.


## Table 1. Binary LSTM/GRU Attack-vs-Normal Classification Performance

| model | accuracy | precision_macro | recall_macro | f1_macro | precision_weighted | recall_weighted | f1_weighted |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Binary LSTM | 0.9985 | 0.9975 | 0.9988 | 0.9981 | 0.9985 | 0.9985 | 0.9985 |
| Binary GRU | 0.9980 | 0.9973 | 0.9978 | 0.9976 | 0.9980 | 0.9980 | 0.9980 |



## Table 2. Fine-Grained LSTM/GRU 8-Class Classification Performance

| model | accuracy | precision_macro | recall_macro | f1_macro | precision_weighted | recall_weighted | f1_weighted |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Weighted LSTM v4 | 0.9953 | 0.9848 | 0.9989 | 0.9918 | 0.9955 | 0.9953 | 0.9954 |
| Weighted GRU v4 | 0.9924 | 0.9754 | 0.9985 | 0.9866 | 0.9928 | 0.9924 | 0.9925 |



## Table 3. 1D-CNN Temporal Baseline Performance

| accuracy | precision_macro | recall_macro | f1_macro | precision_weighted | recall_weighted | f1_weighted | model |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 0.9997 | 0.9996 | 0.9996 | 0.9996 | 0.9997 | 0.9997 | 0.9997 | 1D-CNN Binary |
| 0.9882 | 0.9669 | 0.9978 | 0.9818 | 0.9888 | 0.9882 | 0.9883 | 1D-CNN Fine-Grained |



## Table 4. Mission Assurance Index by Scenario

| scenario | attack_intensity | mission_assurance_index_mean | mission_assurance_index_ci95 | mission_success_rate_mean | mission_success_rate_ci95 | packet_delivery_ratio_mean | latency_mean | route_deviation_mean | coverage_mean | recovery_time_proxy_sec_mean |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| combined | high | 0.6271 | 0.0088 | 62.5000 | 1.7188 | 0.7340 | 156.9192 | 108.0646 | 43.6574 | 5.7122 |
| combined | low | 0.7615 | 0.0045 | 83.6944 | 1.1944 | 0.9581 | 56.6473 | 26.5746 | 48.4879 | 5.6519 |
| combined | medium | 0.7000 | 0.0068 | 72.3214 | 1.5033 | 0.8557 | 93.1238 | 61.1294 | 46.3276 | 5.6259 |
| jamming | high | 0.7521 | 0.0032 | 88.2237 | 0.9433 | 0.7360 | 152.7713 | 6.0633 | 49.7759 | 5.7888 |
| jamming | low | 0.8008 | 0.0019 | 98.8949 | 0.2808 | 0.9520 | 58.1555 | 6.0064 | 49.8095 | 6.0210 |
| jamming | medium | 0.7810 | 0.0023 | 95.7372 | 0.4810 | 0.8617 | 93.2653 | 5.9274 | 49.7741 | 5.7404 |
| jamming_spoofing | high | 0.6883 | 0.0049 | 66.5942 | 1.2683 | 0.7408 | 153.2559 | 105.8942 | 43.3349 | 5.8371 |
| jamming_spoofing | low | 0.7861 | 0.0025 | 96.0326 | 0.5254 | 0.9563 | 58.9233 | 27.9262 | 48.4196 | 5.6306 |
| jamming_spoofing | medium | 0.7446 | 0.0045 | 81.9643 | 1.3248 | 0.8658 | 93.4373 | 61.3493 | 46.3211 | 5.8711 |
| jamming_tampering | high | 0.6914 | 0.0054 | 66.6422 | 1.4225 | 0.7475 | 154.5729 | 5.9849 | 49.8489 | 5.8828 |
| jamming_tampering | low | 0.7735 | 0.0033 | 90.0000 | 0.9439 | 0.9625 | 56.9024 | 6.1206 | 49.7787 | 5.6900 |
| jamming_tampering | medium | 0.7376 | 0.0041 | 79.1250 | 1.1159 | 0.8619 | 93.5588 | 6.0205 | 49.7723 | 5.6762 |
| normal | none | 0.8152 | 0.0025 | 100.0000 | 0.0000 | 1.0000 | 45.0827 | 6.1129 | 49.8330 | 0.0000 |
| spoofing | high | 0.7461 | 0.0034 | 88.0324 | 0.9957 | 1.0000 | 44.9214 | 105.6849 | 43.2993 | 5.7185 |
| spoofing | low | 0.7954 | 0.0028 | 99.9359 | 0.0801 | 1.0000 | 45.0611 | 28.3303 | 48.4168 | 5.9516 |
| spoofing | medium | 0.7747 | 0.0033 | 97.0513 | 0.6250 | 1.0000 | 45.1515 | 60.5794 | 46.4622 | 5.8862 |
| spoofing_tampering | high | 0.6879 | 0.0059 | 62.7500 | 1.5278 | 1.0000 | 44.8442 | 105.0761 | 43.7494 | 5.8167 |
| spoofing_tampering | low | 0.7689 | 0.0037 | 84.8026 | 0.9978 | 1.0000 | 44.9842 | 27.4847 | 48.3647 | 5.4129 |
| spoofing_tampering | medium | 0.7275 | 0.0054 | 71.8750 | 1.6497 | 1.0000 | 44.9702 | 62.9360 | 46.2661 | 6.0021 |
| tampering | high | 0.7499 | 0.0031 | 95.8772 | 0.5592 | 1.0000 | 45.1302 | 6.0296 | 49.7872 | 5.8388 |
| tampering | low | 0.7821 | 0.0035 | 96.0069 | 0.7118 | 1.0000 | 44.9282 | 6.0899 | 49.8353 | 5.7118 |
| tampering | medium | 0.7661 | 0.0026 | 95.7341 | 0.5655 | 1.0000 | 45.1238 | 6.0393 | 49.7843 | 5.7732 |



## Table 5. RA-MARS Ablation Results

| method | mission_assurance_index_mean | mission_assurance_index_ci95 | mission_success_rate_mean | mission_success_rate_ci95 | packet_delivery_ratio_mean | route_deviation_mean | recovery_time_proxy_sec_mean | energy_consumption_mean |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Full RA-MARS | 0.7012 | 0.0042 | 73.6077 | 0.8690 | 0.8575 | 62.2245 | 5.6607 | 0.0165 |
| Without AI Detection | 0.6559 | 0.0037 | 73.4553 | 0.8592 | 0.8575 | 62.2245 | 60.0000 | 0.0165 |
| Without Mission Assurance Index | 0.6859 | 0.0040 | 73.4756 | 0.9046 | 0.8575 | 62.2245 | 5.6607 | 0.0165 |
| Without Adaptive Continuation | 0.6899 | 0.0045 | 73.5163 | 0.8692 | 0.8575 | 93.3368 | 5.6607 | 0.0165 |
| Without Digital Twin Action Selection | 0.6875 | 0.0040 | 73.4858 | 0.8539 | 0.8575 | 62.2245 | 7.3589 | 0.0165 |
| Without Tamper-Resistant Logging | 0.5837 | 0.0027 | 49.6646 | 1.0014 | 0.8575 | 62.2245 | 5.6607 | 0.0165 |
| Without Navigation Trust Module | 0.6873 | 0.0044 | 73.4553 | 0.8285 | 0.8575 | 124.4490 | 5.6607 | 0.0165 |



## Table 6. Latency Budget Summary

| parameter | value | notes |
| --- | --- | --- |
| Simulation step (telemetry interval) | 1000 ms (1 Hz MAVLink logging) | Limited by MAVLink logging rate, not FC loop |
| UAV cruise speed | 15 m/s | DJI Matrice 300 class, surveillance mode |
| Flight controller loop rate | 400 Hz (2.5 ms/cycle) | Pixhawk 6C / PX4 default attitude control loop |
| MAVLink telemetry rate | 10 Hz (100 ms/message) | Standard MAVLink HEARTBEAT + telemetry stream |
| LSTM inference time (Jetson Nano, 20 steps) | 8.0 ms | PyTorch LSTM, batch=1, CPU inference |
| MAI scoring time | 2.0 ms | Weighted sum of 5 component scores |
| Digital twin action selection | 1.5 ms | argmax over 6 candidate actions |
| Total RA-MARS framework overhead per cycle | 11.5 ms | 1.15% of telemetry interval — negligible |
| Framework overhead as % of 1s telemetry interval | 1.15% | FC operates independently of RA-MARS |
| Mean detection delay (low intensity, jamming) | ~32653 ms | Detection occurs within 33 telemetry cycles |
| Mean detection delay (high intensity, jamming) | ~15310 ms | Detection occurs within 16 telemetry cycles |
| Distance travelled during low-intensity detection | ~490 m | UAV travels ~495m before detection at low intensity |
| Distance travelled during high-intensity detection | ~230 m | UAV travels ~240m before detection at high intensity |
| FC cycles during low-intensity detection | ~13061 cycles | FC completes ~13,200 cycles before detection |
| FC cycles during high-intensity detection | ~6124 cycles | FC completes ~6,400 cycles before detection |



## Table 7. RF/SINR Physics Validation Summary

| scenario | attack_intensity | sinr_mean_db | sinr_min_db | sinr_std_db | pdr_mean | latency_mean_ms | packet_loss_mean |
| --- | --- | --- | --- | --- | --- | --- | --- |
| combined | high | 27.0126 | -17.5044 | 17.2977 | 0.7340 | 156.9192 | 0.2624 |
| combined | low | 35.9473 | -8.9152 | 9.3958 | 0.9581 | 56.6473 | 0.0400 |
| combined | medium | 31.6657 | -13.6531 | 13.8539 | 0.8557 | 93.1238 | 0.1390 |
| jamming | high | 26.9006 | -21.0896 | 17.0649 | 0.7360 | 152.7713 | 0.2614 |
| jamming | low | 35.5345 | -8.2660 | 9.7899 | 0.9520 | 58.1555 | 0.0451 |
| jamming | medium | 31.8482 | -14.9593 | 13.8311 | 0.8617 | 93.2653 | 0.1357 |
| jamming_spoofing | high | 27.0850 | -19.1014 | 17.1406 | 0.7408 | 153.2559 | 0.2590 |
| jamming_spoofing | low | 35.6609 | -8.2733 | 9.7675 | 0.9563 | 58.9233 | 0.0463 |
| jamming_spoofing | medium | 31.7267 | -15.7041 | 13.8487 | 0.8658 | 93.4373 | 0.1360 |
| jamming_tampering | high | 26.9415 | -21.4493 | 17.1451 | 0.7475 | 154.5729 | 0.2581 |
| jamming_tampering | low | 35.7922 | -6.4200 | 9.4688 | 0.9625 | 56.9024 | 0.0410 |
| jamming_tampering | medium | 31.8365 | -15.0830 | 13.8146 | 0.8619 | 93.5588 | 0.1347 |
| normal | none | 39.9068 | 34.8802 | 0.4488 | 1.0000 | 45.0827 | 0.0000 |
| spoofing | high | 39.9125 | 35.1831 | 0.4287 | 1.0000 | 44.9214 | 0.0000 |
| spoofing | low | 39.9232 | 34.5452 | 0.3818 | 1.0000 | 45.0611 | 0.0000 |
| spoofing | medium | 39.9231 | 34.6341 | 0.3890 | 1.0000 | 45.1515 | 0.0000 |
| spoofing_tampering | high | 39.9283 | 35.7216 | 0.3597 | 1.0000 | 44.8442 | 0.0000 |
| spoofing_tampering | low | 39.9163 | 34.6979 | 0.3975 | 1.0000 | 44.9842 | 0.0000 |
| spoofing_tampering | medium | 39.9188 | 34.7144 | 0.3837 | 1.0000 | 44.9702 | 0.0000 |
| tampering | high | 39.9191 | 34.0730 | 0.4187 | 1.0000 | 45.1302 | 0.0000 |
| tampering | low | 39.9257 | 35.0211 | 0.3829 | 1.0000 | 44.9282 | 0.0000 |
| tampering | medium | 39.9183 | 33.7041 | 0.3944 | 1.0000 | 45.1238 | 0.0000 |



## Table 8. Detection Delay Results

| actual_attack_type | attack_intensity | detection_delay_mean | detection_delay_std | detection_delay_ci95 | records |
| --- | --- | --- | --- | --- | --- |
| combined | high | 15.2324 | 7.9339 | 0.4658 | 1080.0000 |
| combined | low | 33.7430 | 16.0680 | 1.2208 | 603.0000 |
| combined | medium | 20.3040 | 10.8170 | 0.6746 | 931.0000 |
| jamming | high | 14.9898 | 7.8705 | 0.3597 | 1761.0000 |
| jamming | low | 32.8744 | 16.6006 | 1.0136 | 1011.0000 |
| jamming | medium | 21.2708 | 10.8588 | 0.4864 | 1684.0000 |
| jamming_spoofing | high | 15.4686 | 7.9325 | 0.3256 | 2083.0000 |
| jamming_spoofing | low | 32.1085 | 16.2793 | 1.0137 | 968.0000 |
| jamming_spoofing | medium | 21.1890 | 10.5831 | 0.7225 | 931.0000 |
| jamming_tampering | high | 15.3465 | 7.9700 | 0.4006 | 1564.0000 |
| jamming_tampering | low | 32.2431 | 16.3940 | 1.1405 | 720.0000 |
| jamming_tampering | medium | 20.8462 | 10.7292 | 0.5464 | 1307.0000 |
| spoofing | high | 15.0634 | 7.8495 | 0.3791 | 1640.0000 |
| spoofing | low | 33.5787 | 16.5914 | 1.3129 | 553.0000 |
| spoofing | medium | 21.4795 | 10.5243 | 0.6921 | 855.0000 |
| spoofing_tampering | high | 15.5920 | 8.0121 | 0.4141 | 1343.0000 |
| spoofing_tampering | low | 31.7671 | 16.9253 | 1.1970 | 777.0000 |
| spoofing_tampering | medium | 21.0805 | 10.7469 | 0.7300 | 820.0000 |
| tampering | high | 15.4797 | 7.9692 | 0.3713 | 1720.0000 |
| tampering | low | 32.2549 | 16.7170 | 1.4366 | 510.0000 |
| tampering | medium | 20.8730 | 10.3699 | 0.5556 | 1394.0000 |



## Table 9. Adversarial Training Robustness Results

| attack | epsilon | clean_f1 | adv_f1 | f1_drop_pct |
| --- | --- | --- | --- | --- |
| FGSM | 0.0100 | 0.9986 | 0.9975 | 0.1173 |
| FGSM | 0.0500 | 0.9986 | 0.9840 | 1.4630 |
| FGSM | 0.1000 | 0.9986 | 0.9453 | 5.3310 |
| FGSM | 0.2000 | 0.9986 | 0.9066 | 9.2070 |
| FGSM | 0.3000 | 0.9986 | 0.8772 | 12.1453 |
| PGD | 0.0500 | 0.9986 | 0.9831 | 1.5496 |
| PGD | 0.1000 | 0.9986 | 0.9498 | 4.8805 |
| PGD | 0.2000 | 0.9986 | 0.9387 | 5.9928 |


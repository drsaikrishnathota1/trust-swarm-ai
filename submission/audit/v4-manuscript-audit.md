# RA-MARS v4 Manuscript Audit Report


## old_v3_or_v2_terms

Matches: 0


## weak_or_internal_terms

Matches: 1

- Line 970: [1] P. Stodola, J. Nohel, and L. Horák, “Dynamic reconnaissance operations with UAV swarms: adapting to environmental changes,” Scientific Reports, vol. 15, article 15092, 2025, doi: 10.1038/s41598-025-00201-4.

## synthetic_data_limitations

Matches: 26

- Line 17: - Achieves 85.70% mission success under stressed attack scenarios using synthetic simulation data.
- Line 25: A simulation-based v4 evaluation is conducted using synthetic multi-UAV telemetry data. The physics-based v4 dataset contains 90,000 sampled telemetry rows and 82,875 time-series windows, with 20 telemetry steps per window and 9 raw non-leakage features per step. The classifier excludes derived Mission Assurance Index and component scores from attack-detection inputs to avoid leakage. Across eight mission-state classes, the best macro-F1 model, Binary GRU achieved 95.77% accuracy and 95.77% macro F1-score for attack-versus-normal mission assurance classification, while the fine-grained Weighted GRU achieved 75.36% accuracy and 60.07% macro F1-score across eight mission-state classes. The best classical baseline, Gradient Boosting achieved 76.99% accuracy and 60.40% macro F1-score among the classical baselines.
- Line 29: The results indicate that RA-MARS improves multi-UAV resilience by linking temporal attack detection, mission assurance scoring, adaptive action selection, operational recovery, and tamper-resistant mission provenance. The study provides simulation-based evidence for a defence-oriented mission assurance digital twin, while acknowledging that real UAV flight tests and hardware-in-the-loop validation are required before deployment claims can be made.
- Line 57: 5. A simulation-based evaluation is conducted to compare the proposed framework with conventional UAV surveillance, AI-only detection, blockchain-only logging, and non-adaptive security baselines using mission success rate, detection accuracy, packet delivery ratio, latency, energy consumption, and tamper-detection performance.
- Line 493: RA-MARS should be presented as a simulation-based defence mission-assurance framework. The paper should not claim real-world deployment or military-grade validation unless supported by field testing. The contribution should focus on integrated mission assurance, comparative simulation, and operational resilience under contested conditions.
- Line 501: This section describes the simulation-based evaluation setup for RA-MARS. The purpose of the experiment is to evaluate whether the proposed framework improves mission assurance for multi-UAV defence surveillance under normal and adversarial conditions.
- Line 517: The simulation generates synthetic UAV telemetry data and attack events. The generated dataset is used to train and evaluate AI-based attack detection models and to compare RA-MARS with baseline systems.
- Line 665: 1. Generate synthetic UAV mission data for each scenario.
- Line 682: | synthetic_uav_mission_data.csv | Full generated telemetry dataset |
- Line 694: All numerical values used in the final manuscript must be generated from the simulation code. The synthetic dataset should be clearly described as simulation-generated UAV telemetry data and should not be presented as real military flight data.
- Line 696: The results should be interpreted as simulation-based evidence of mission-assurance improvement under controlled attack scenarios. Real-world flight testing and hardware-in-the-loop validation are left for future work.
- Line 760: All v4 results are based on synthetic simulation data and should be interpreted as simulation-based evidence. The results do not represent real military UAV flight validation, classified operational data, or deployed battlefield testing.
- Line 790: The physics-based v4 evaluation uses synthetic multi-UAV telemetry data generated under normal, jamming, spoofing, tampering, and combined attack scenarios. The final v4 sample contains 90,000 sampled telemetry rows and 82,875 time-series windows. Each window contains 20 telemetry steps and 9 raw non-leakage features per step.
- Line 820: The v4 results should be interpreted as simulation-based evidence. They do not represent real military UAV flight validation or battlefield deployment.
- Line 856: | Synthetic v4 simulation | 90,000 sampled multi-UAV telemetry rows and 82,875 temporal windows | Jamming, spoofing, tampering, combined attacks | Attack detection, Mission Assurance Index, ablation, scalability, attack-intensity results | Statistical mission-assurance evaluation under controlled synthetic conditions |
- Line 861: The comparison shows that the present study provides simulation-based and PX4-style telemetry-emulation evidence. It does not claim real PX4/Gazebo SITL execution, hardware-in-the-loop validation, real UAV flight testing, or battlefield deployment.
- Line 866: To complement the synthetic v4 evaluation, a lightweight PX4-style MAVLink telemetry validation case study was conducted. This case study does not claim real PX4/Gazebo execution, real UAV flight testing, hardware-in-the-loop validation, or military-grade field validation. Instead, it emulates MAVLink/PX4-style telemetry fields to evaluate whether RA-MARS can process UAV simulator-style telemetry streams under safe software-emulated attack conditions.
- Line 885: First, the evaluation is simulation-based. The UAV telemetry data, attack events, mission-zone coverage, and adversarial conditions are generated through controlled simulation. Therefore, the results should be interpreted as simulation-based evidence rather than real-world flight validation.
- Line 893: Fifth, the proposed AI-based detection module depends on the quality and representativeness of the generated telemetry and attack data. Real-world attack patterns may differ from the synthetic scenarios used in this study.
- Line 921: The physics-based v4 evaluation used synthetic multi-UAV telemetry data with 90,000 sampled telemetry rows and 82,875 time-series windows. Each window contained 20 telemetry steps and 9 raw non-leakage features per step. Derived Mission Assurance Index and component scores were excluded from classifier inputs to avoid feature leakage. Across eight mission-state classes, the best macro-F1 model, Binary GRU achieved 95.77% accuracy and 95.77% macro F1-score for attack-versus-normal mission assurance classification, while the fine-grained Weighted GRU achieved 75.36% accuracy and 60.07% macro F1-score across eight mission-state classes. The Gradient Boosting classical baseline achieved 76.99% accuracy and 60.40% macro F1-score.
- Line 927: This study has limitations. The evaluation is based on synthetic simulation data and does not represent real military UAV flight data, classified operational systems, or deployed battlefield validation. The attack models are controlled abstractions of jamming, spoofing, tampering, and combined attacks. Future work should include hardware-in-the-loop validation, real UAV flight experiments, more detailed RF and GNSS channel modeling, human-machine teaming interfaces, adversarial learning, and operational field testing.
- Line 935: The generated dataset consists of synthetic UAV telemetry records, mission-status information, communication indicators, navigation-deviation features, attack labels, mission-risk scores, and log-integrity indicators.
- Line 939: Simulation scripts, synthetic dataset generation scripts, evaluation scripts, result files, and figures are available in the project repository: https://github.com/drsaikrishnathota1/ra-mars-defence-technology.
- Line 943: The simulation code was developed in Python and used to generate synthetic UAV telemetry data, attack scenarios, AI detection results, mission-risk scores, and performance metrics.
- Line 947: # Synthetic Data Statement
- Line 949: This study uses simulation-generated synthetic data for controlled experimental evaluation. The data should not be interpreted as real-world UAV flight data or operational military mission data.

## key_v4_results

Matches: 7

- Line 17: - Achieves 85.70% mission success under stressed attack scenarios using synthetic simulation data.
- Line 25: A simulation-based v4 evaluation is conducted using synthetic multi-UAV telemetry data. The physics-based v4 dataset contains 90,000 sampled telemetry rows and 82,875 time-series windows, with 20 telemetry steps per window and 9 raw non-leakage features per step. The classifier excludes derived Mission Assurance Index and component scores from attack-detection inputs to avoid leakage. Across eight mission-state classes, the best macro-F1 model, Binary GRU achieved 95.77% accuracy and 95.77% macro F1-score for attack-versus-normal mission assurance classification, while the fine-grained Weighted GRU achieved 75.36% accuracy and 60.07% macro F1-score across eight mission-state classes. The best classical baseline, Gradient Boosting achieved 76.99% accuracy and 60.40% macro F1-score among the classical baselines.
- Line 27: Mission-level evaluation shows that full RA-MARS achieved a Mission Assurance Index of 0.7497 and a mission success rate of 85.70% under stressed attack scenarios. Adversarial training further improved binary robustness, achieving 99.86% clean macro-F1, 99.75% macro-F1 under FGSM at ε=0.01, and 98.31% macro-F1 under PGD at ε=0.05. Ablation analysis shows that ablation analysis confirmed that removing core mission-assurance components reduced mission performance, while latency-budget analysis showed that RA-MARS added only 11.5 ms of framework overhead per telemetry cycle. Scalability analysis showed stable mission success across 10, 20, and 30 UAV swarms, while attack-intensity testing showed mission success decreasing from 81.34% under low-intensity attacks to 76.98% under high-intensity attacks.
- Line 796: The v4 model evaluation compares classical baselines, binary LSTM/GRU models, and fine-grained weighted sequence models. For binary attack-versus-normal mission assurance classification, the Binary GRU achieved 95.77% accuracy and 95.77% macro F1-score. For fine-grained eight-class mission-state classification, the Weighted GRU achieved 75.36% accuracy and 60.07% macro F1-score.
- Line 804: Full RA-MARS achieved a Mission Assurance Index of 0.7497 and a mission success rate of 85.70% under stressed attack scenarios. The physics-based RF/SINR evaluation showed normal mean SINR of 39.9 dB, jammed mean SINR of 9.9 dB, and jammed mean packet delivery ratio of 0.477.
- Line 921: The physics-based v4 evaluation used synthetic multi-UAV telemetry data with 90,000 sampled telemetry rows and 82,875 time-series windows. Each window contained 20 telemetry steps and 9 raw non-leakage features per step. Derived Mission Assurance Index and component scores were excluded from classifier inputs to avoid feature leakage. Across eight mission-state classes, the best macro-F1 model, Binary GRU achieved 95.77% accuracy and 95.77% macro F1-score for attack-versus-normal mission assurance classification, while the fine-grained Weighted GRU achieved 75.36% accuracy and 60.07% macro F1-score across eight mission-state classes. The Gradient Boosting classical baseline achieved 76.99% accuracy and 60.40% macro F1-score.
- Line 923: At the mission level, full RA-MARS achieved a Mission Assurance Index of 0.7497 and a mission success rate of 85.70% under stressed attack scenarios. The ablation study showed that ablation analysis confirmed that removing core mission-assurance components reduced mission performance, while latency-budget analysis showed that RA-MARS added only 11.5 ms of framework overhead per telemetry cycle. Scalability results showed that mission success remained stable across 10, 20, and 30 UAV swarms, while attack-intensity analysis showed an expected reduction in mission success from low-intensity to high-intensity attacks.

## figure_links

Matches: 6

- Line 1059: ![Figure 1. RA-MARS v4 model macro-F1 comparison.](../figures/graphs/v4/figure_v4_model_f1_comparison.svg)
- Line 1061: ![Figure 2. RA-MARS v4 mission success by scenario.](../figures/graphs/v4/figure_v4_mission_success_by_scenario.svg)
- Line 1063: ![Figure 3. RA-MARS v4 ablation study for mission success.](../figures/graphs/v4/figure_v4_ablation_mission_success.svg)
- Line 1065: ![Figure 4. RA-MARS v4 RF/SINR validation summary.](../figures/graphs/v4/figure_v4_rf_sinr_validation.svg)
- Line 1067: ![Figure 5. RA-MARS v4 detection-delay analysis.](../figures/graphs/v4/figure_v4_detection_delay.svg)
- Line 1069: ![Figure 6. RA-MARS v4 adversarial training robustness.](../figures/graphs/v4/figure_v4_adversarial_training_robustness.svg)

## Basic Manuscript Stats

- Word count: 10178
- Characters: 73425
- Figure links: 6
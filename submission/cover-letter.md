# Cover Letter

Dear Editor-in-Chief,

Please consider our manuscript entitled **“RA-MARS: A Cross-Layer Mission Assurance Digital Twin for Secure Multi-UAV Defence Surveillance Under Cyber-Electromagnetic and Navigation Attacks”** for publication in *Defence Technology*.

This manuscript presents RA-MARS, a defence-oriented mission-assurance framework for secure multi-UAV surveillance under RF jamming, GPS/GNSS spoofing, mission-data tampering, and combined attack scenarios. The work positions UAV security as a mission-level assurance problem rather than an isolated attack-detection or communication-security problem.

The proposed framework integrates temporal AI-based attack detection, Mission Assurance Index scoring, digital twin-based action selection, adaptive mission continuation, and tamper-resistant mission provenance. A physics-based v4 simulation workflow was used to evaluate the framework using RF/SINR-aware telemetry, sequence-window modeling, classical baselines, LSTM/GRU models, ablation analysis, latency-budget analysis, and adversarial robustness testing.

The completed v5 validation results show that RA-MARS achieved a Mission Assurance Index of 0.7012 and a mission success rate of 73.61% under stressed attack scenarios. For attack-versus-normal mission assurance classification, the Binary GRU achieved 99.85% accuracy and 99.81% macro-F1. For fine-grained eight-class mission-state classification, the Weighted LSTM achieved 99.53% accuracy and 99.18% macro-F1. A 1D-CNN temporal baseline achieved 99.97% accuracy and 99.96% macro-F1 for binary classification, and 98.82% accuracy and 98.18% macro-F1 for fine-grained classification. PGD-augmented adversarial training further achieved 99.86% clean macro-F1, 99.75% macro-F1 under FGSM at ε=0.01, and 98.31% macro-F1 under PGD at ε=0.05. Latency-budget analysis showed that the RA-MARS framework added only 11.5 ms of framework overhead per telemetry cycle.

The high classification scores are interpreted within a controlled synthetic-telemetry setting. The study uses simulation-generated synthetic UAV telemetry data and does not claim real military flight testing, classified operational validation, or deployed battlefield performance. The manuscript clearly states these limitations and positions the contribution as a reproducible simulation-based mission-assurance framework.

We believe the manuscript is suitable for *Defence Technology* because it addresses resilient autonomous systems, UAV mission assurance, cyber-electromagnetic threats, AI-enabled defence surveillance, and operational reliability under contested environments.

Thank you for considering this manuscript.

Sincerely,  
Dr. Sai Krishna Thota

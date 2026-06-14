#!/usr/bin/env python3
from pathlib import Path

setup_path = Path("docs/hcc_experimental_setup_v2.md")
builder_path = Path("scripts/build_hcc_manuscript_v1.py")

setup_text = """# High-Confidence Computing Experimental Setup v2

## 4. Experimental setup

This section describes the experimental setup used to evaluate TRUST-Swarm as a high-confidence graph-temporal intelligent computing framework for secure multi-UAV mission assurance. The evaluation is designed to be broader than ordinary classification testing. It measures mission-state recognition, temporal baseline comparison, confidence calibration, OOD cyber-physical stress behavior, feature-level traceability, recovery-oriented reasoning, ablation evidence, and runtime feasibility. This structure follows the high-confidence computing requirement that security-critical intelligent systems should be evaluated not only for predictive accuracy, but also for reliability, robustness, interpretability, and practical computational behavior.

### 4.1. Computing environment and implementation

The final experiments were executed in a GPU-based RunPod environment using Python and PyTorch. The implementation also used pandas and NumPy for data processing, scikit-learn for evaluation metrics and baseline utilities, matplotlib for result visualization, Gymnasium for the recovery-reasoning environment, and Stable-Baselines3 for PPO-based reinforcement learning. Neural-network training and runtime profiling were conducted with GPU acceleration.

The runtime and complexity profiling was conducted on an NVIDIA H200 GPU. This environment was used to measure inference latency, model size, throughput, training-step time, and GPU memory behavior. Reporting these details is important because TRUST-Swarm is positioned as a high-confidence computing framework, and practical feasibility must be supported by evidence rather than only by accuracy metrics.

### 4.2. Random seeds and repeatability

The evaluation used three random seeds: 42, 123, and 2026. Each seed generated an independent simulation run and train-test split. Using multiple seeds reduces dependence on a single data-generation instance and supports more reliable performance reporting. Results are reported using mean and standard deviation where applicable.

For each seed, the telemetry generator produced 300 mission runs, 240 timesteps per mission, 20 UAV nodes per mission, 1,440,000 raw telemetry rows, and 66,300 graph-temporal mission windows. This setup provides enough repeated mission structure to evaluate normal operation, individual cyber-physical attacks, and combined attack states while preserving repeatability.

### 4.3. Synthetic multi-UAV cyber-physical telemetry

The dataset is generated using a controlled simulation-based telemetry environment. The purpose of using controlled synthetic telemetry is not to replace real UAV flight validation. Instead, it provides a repeatable benchmark for stress-testing cyber-physical mission-assurance behavior under known attack conditions, multiple random seeds, and controlled OOD shifts.

The simulated mission environment includes normal operation and seven attack-related mission states: jamming, spoofing, tampering, jamming-spoofing, jamming-tampering, spoofing-tampering, and combined attack. These labels represent communication disruption, navigation manipulation, telemetry integrity attack, and multi-vector mission degradation. Jamming affects packet loss and latency. Spoofing affects route deviation, GPS jumps, and velocity inconsistency. Tampering affects battery level, mission progress, zone coverage, and energy consumption. Combined attack states affect several telemetry groups at the same time.

### 4.4. Telemetry features

Each UAV node is represented using nine telemetry features:

1. packet_loss_rate
2. latency_ms
3. route_deviation_m
4. gps_jump_m
5. velocity_inconsistency
6. battery_level
7. mission_progress
8. zone_coverage
9. energy_consumption

These features were selected to represent the major information streams required for cyber-physical mission assurance. Packet loss and latency capture communication reliability. Route deviation, GPS jump, and velocity inconsistency capture navigation integrity. Battery level and energy consumption capture energy state. Mission progress and zone coverage capture mission effectiveness and coverage quality. Together, these features allow the framework to evaluate how attacks degrade mission-state prediction across communication, navigation, energy, and mission-progress dimensions.

### 4.5. Graph-temporal mission-window construction

Raw telemetry is transformed into graph-temporal mission windows using a sliding temporal window. Each mission-window sample is represented as:

X ∈ R^(T × N × F),

where T is the temporal window length, N is the number of UAV nodes, and F is the number of telemetry features. In the final experiment, T = 20 timesteps, N = 20 UAV nodes, and F = 9 telemetry features. Therefore, each mission-window tensor has the shape:

X ∈ R^(20 × 20 × 9).

This representation preserves mission-time evolution, UAV-node structure, and telemetry-feature heterogeneity. It allows the Graph-Temporal Transformer to learn mission degradation patterns across nodes and time. It also allows baseline models to be evaluated on the same mission-window evidence after reshaping into temporal input formats.

### 4.6. Evaluated models

The experimental comparison includes four models:

1. LSTM
2. GRU
3. 1D-CNN
4. Graph-Temporal Transformer

The LSTM and GRU baselines evaluate recurrent temporal modeling. The 1D-CNN baseline evaluates local temporal pattern extraction. The Graph-Temporal Transformer evaluates graph-temporal mission reasoning across UAV nodes, temporal windows, and telemetry features.

This comparison is included to prevent overclaiming. The goal is not to force the proposed model to be the strongest raw classifier in every condition. Instead, the goal is to evaluate whether TRUST-Swarm provides high-confidence mission-assurance value beyond ordinary classification, including calibration, OOD exposure, traceability, recovery reasoning, ablation evidence, and runtime feasibility.

### 4.7. Training configuration

Each model was trained for 30 epochs using a batch size of 128. The same three random seeds were used across the evaluation pipeline. For each seed, the dataset was split into training and testing partitions after graph-window construction. Performance was then aggregated across seeds.

The training configuration was kept consistent across baseline models and the Graph-Temporal Transformer to support fair comparison. The evaluation emphasizes macro-averaged metrics because the cyber-physical attack classes are imbalanced. Macro-level reporting prevents the normal or frequent classes from dominating the interpretation.

### 4.8. In-distribution classification metrics

The in-distribution mission-state recognition task was evaluated using test loss, accuracy, macro precision, macro recall, and macro F1. Accuracy measures overall correctness, while macro precision, macro recall, and macro F1 evaluate class-balanced performance across normal, single-attack, and combined-attack states.

Macro F1 is emphasized because mission assurance must correctly recognize minority attack states, not only frequent states. A high accuracy score alone may hide poor recognition of rare or combined attacks. Therefore, macro F1 provides a more meaningful measure of cyber-physical mission-state recognition.

### 4.9. Confidence calibration metrics

The confidence-aware reliability layer was evaluated using Expected Calibration Error, Brier score, mean predictive confidence, predictive entropy, and low-confidence rate. Monte Carlo dropout with 20 stochastic samples was used during uncertainty evaluation.

These metrics support the high-confidence computing objective. Expected Calibration Error measures the gap between predicted confidence and empirical correctness. Brier score measures probabilistic prediction quality. Predictive entropy captures uncertainty in the output distribution. Low-confidence rate identifies cases where the model may require monitoring, escalation, or recovery-oriented reasoning.

### 4.10. OOD cyber-physical stress testing

OOD stress testing was used to evaluate model behavior under unseen cyber-physical mission shifts. The OOD conditions were:

1. in-distribution test
2. stealth jammer
3. slow GPS drift
4. intermittent tampering
5. delayed combined attack
6. unseen swarm noise

Each OOD condition was evaluated using accuracy, macro F1, mean confidence, predictive entropy, and low-confidence rate. The goal is not to claim complete OOD reliability. Instead, the goal is to expose mission-risk conditions where performance degrades or confidence becomes unreliable. This is important because high-confidence systems should reveal failure modes rather than only report favorable in-distribution results.

### 4.11. Traceable explanation evaluation

Traceability was evaluated using perturbation-based feature importance. First, baseline macro F1 was computed. Then, each telemetry feature was replaced with its mean value, and macro F1 was recomputed. Feature importance was calculated as:

Feature importance = baseline macro F1 − perturbed macro F1.

A larger macro-F1 drop indicates that the feature has greater influence on mission-state prediction. The final explanation analysis identifies latency, zone coverage, route deviation, mission progress, and GPS jump as the most influential mission-risk drivers. These features are operationally meaningful because they correspond to communication degradation, mission coverage loss, navigation disruption, mission-progress interruption, and spoofing-related displacement.

### 4.12. Recovery-oriented reasoning evaluation

The PPO-based recovery module was evaluated as a recovery-reasoning scaffold. The action space includes continue, monitor, reroute, reassign, isolate node, and return to base. The recovery state includes mission-state prediction, confidence, entropy, and mission-risk indicators.

This module is not claimed as an operationally deployable UAV controller. Instead, it demonstrates how high-confidence prediction outputs can support mission-response reasoning. This is important because mission assurance should not stop at detection. It should connect risk recognition to possible response actions.

### 4.13. Ablation and runtime evaluation

The final evaluation includes both architectural and framework-level ablation analysis. Architectural ablations remove UAV-node attention and temporal transformer reasoning. Framework-level ablations remove calibration evidence, OOD evidence, explanation evidence, or recovery support. This design shows which components contribute to classification performance and which components contribute to high-confidence assurance evidence.

Runtime and complexity analysis was conducted to evaluate practical feasibility. The profiling reports trainable parameters, model size, inference batch latency, inference sample latency, throughput, and training-step time. These measurements support the practical computing dimension of the HCC contribution.

### 4.14. Experimental limitation

The current evaluation uses controlled synthetic telemetry rather than field-collected UAV telemetry. This design enables repeatable testing across attack states, OOD conditions, and random seeds, but real-world validation remains future work. Future evaluation should include high-fidelity UAV simulators, hardware-in-the-loop experiments, real swarm telemetry, adaptive attackers, communication-topology changes, and operational mission constraints.

Despite this limitation, the controlled setup is useful for the present study because it allows the framework to evaluate prediction, calibration, OOD behavior, explanation, recovery reasoning, ablation, and runtime feasibility in a repeatable environment.
"""

setup_path.write_text(setup_text)

if builder_path.exists():
    b = builder_path.read_text()
    b = b.replace('ROOT / "docs" / "hcc_experimental_setup_v1.md"', 'ROOT / "docs" / "hcc_experimental_setup_v2.md"')
    lines = b.splitlines()
    marker = '    text = text.replace("# High-Confidence Computing Experimental Setup v2", "")'
    if marker not in lines:
        for idx, line in enumerate(lines):
            if 'text = text.replace("# High-Confidence Computing Experimental Setup v1", "")' in line:
                lines.insert(idx + 1, marker)
                break
    builder_path.write_text("\n".join(lines) + "\n")

print(f"Saved: {setup_path}")
print("Updated manuscript builder to use Experimental Setup v2.")

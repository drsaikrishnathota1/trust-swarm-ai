# HCC Publication-Quality Evidence Tables v1

## Table 1. Positioning of TRUST-Swarm against related research directions

| Research direction | Main focus | Common limitation | TRUST-Swarm positioning |
| --- | --- | --- | --- |
| UAV cybersecurity | Jamming, spoofing, tampering, secure communication, attack detection | Often focused on isolated attack families or link protection | Models multiple cyber-physical mission states and combined attacks |
| Temporal deep learning | LSTM, GRU, CNN, transformer variants | Often emphasizes raw accuracy only | Uses baselines but frames contribution as mission assurance |
| Graph-temporal learning | Node-time relational modeling | Often not connected to calibration, OOD, and recovery | Uses graph-temporal windows inside a full assurance pipeline |
| Calibration and uncertainty | Probability reliability | Often evaluated separately from response support | Integrates ECE, Brier score, confidence, and entropy |
| OOD robustness | Distribution-shift testing | Often not linked to mission response | Uses cyber-physical OOD stress tests to expose risk |
| Explainable AI | Feature attribution | May not connect to operational telemetry meaning | Identifies mission-risk telemetry drivers |
| Reinforcement learning | Adaptive response | Often separated from prediction confidence | Adds PPO-based recovery-reasoning scaffold |

## Table 2. Simulation and dataset configuration

| Parameter | Value |
| --- | ---: |
| Random seeds | 42, 123, 2026 |
| Mission runs per seed | 300 |
| Timesteps per mission | 240 |
| UAV nodes per mission | 20 |
| Raw telemetry rows per seed | 1,440,000 |
| Graph-temporal windows per seed | 66,300 |
| Window tensor shape | 20 × 20 × 9 |
| Mission-state classes | 8 |

## Table 3. Main in-distribution performance evidence

| Model | Accuracy | Macro F1 | Interpretation |
| --- | ---: | ---: | --- |
| Graph-Temporal Transformer | 0.9647 | 0.8750 | Strong prediction layer with calibration and assurance evidence |
| 1D-CNN | Not reported here | 0.9971 | Strongest raw in-distribution classifier in current evaluation |

## Table 4. Calibration evidence

| Metric | Value | Interpretation |
| --- | ---: | --- |
| Expected Calibration Error | 0.0088 | Strong alignment between confidence and empirical correctness |
| Brier score | 0.0531 | Strong probabilistic prediction quality |

## Table 5. OOD stress-test evidence

| Condition | Macro F1 | Interpretation |
| --- | ---: | --- |
| In-distribution test | 0.8750 | Strong normal test performance |
| Intermittent tampering | 0.5965 | Visible degradation under unseen shift |
| Severe unseen shifts | Degraded | Requires monitoring, escalation, or recovery reasoning |

## Table 6. Ablation evidence

| Variant | Macro F1 | Interpretation |
| --- | ---: | --- |
| Full Graph-Temporal Transformer | 0.8734 | Full graph-temporal reasoning |
| Without UAV-node attention | 0.7903 | Node interaction modeling is important |
| Without temporal transformer | 0.8237 | Temporal reasoning contributes to performance |

## Table 7. Runtime and complexity evidence

| Metric | Value |
| --- | ---: |
| Trainable parameters | 680,840 |
| Model size | 2.618 MB |
| Batch inference latency | 2.267 ms |
| Sample inference latency | 0.0177 ms |
| Throughput | 56,458 windows/sec |
| Training-step time | 9.938 ms |

# TRUST-Swarm Results Interpretation Report

## Experiment Status

The final TRUST-Swarm journal experiment was completed using three seeds: 42, 123, and 2026.

Each seed used:

* 300 mission runs
* 240 timesteps
* 20 UAVs
* 30 training epochs
* 66,300 graph-temporal windows per seed

The experiment included:

* LSTM baseline
* GRU baseline
* 1D-CNN baseline
* Graph-Temporal Transformer
* uncertainty calibration
* OOD / unseen attack evaluation
* feature-importance explainability
* multi-seed aggregation

## Main Classification Results

The Graph-Temporal Transformer achieved:

* Mean accuracy: 0.9647
* Mean macro F1: 0.8750
* Mean macro precision: 0.8935
* Mean macro recall: 0.8700

This confirms that the graph-temporal model can learn meaningful multi-UAV mission-state patterns under cyber-physical attacks.

However, the 1D-CNN baseline achieved stronger in-distribution classification performance:

* CNN1D mean accuracy: 0.9987
* CNN1D mean macro F1: 0.9971

Therefore, the manuscript should not claim that the Graph-Temporal Transformer outperforms every baseline in standard classification accuracy.

## Correct Manuscript Claim

The correct claim is:

TRUST-Swarm provides an integrated trustworthy mission-assurance framework combining graph-temporal learning, calibrated uncertainty, OOD stress testing, explainability, and recovery reasoning for multi-UAV cyber-physical missions.

The paper should emphasize high-confidence AI reasoning rather than only raw classification accuracy.

## Uncertainty Results

The Graph-Temporal Transformer produced strong calibration results:

* Expected Calibration Error mean: 0.0088
* Brier score mean: 0.0531
* Mean confidence: 0.9601
* Mean predictive entropy: 0.0986

These results support the high-confidence computing direction because the model is well calibrated on the in-distribution test set.

## OOD / Unseen Attack Results

In-distribution performance was strong:

* In-distribution macro F1: 0.8750

Performance dropped significantly under severe OOD conditions:

* Intermittent tampering macro F1: 0.5965
* Slow GPS drift macro F1: 0.1701
* Stealth jammer macro F1: 0.0779
* Delayed combined attack macro F1: 0.0521

This shows that unseen cyber-physical shifts are challenging and should be treated as mission-risk conditions.

The manuscript should not claim that uncertainty perfectly detects all OOD attacks. Instead, it should state that OOD stress tests reveal vulnerability under unseen attack shifts and motivate uncertainty-aware monitoring and recovery.

## Explainability Results

Feature importance consistently identified mission-relevant telemetry signals.

Top features:

1. latency_ms
2. zone_coverage
3. route_deviation_m
4. mission_progress
5. gps_jump_m

This supports the interpretation that TRUST-Swarm learns from communication degradation, mission coverage loss, route deviation, mission progress disruption, and GPS anomalies.

## Recommended Paper Framing

Recommended title:

TRUST-Swarm: Trustworthy Graph-Temporal AI for High-Confidence Multi-UAV Mission Assurance Under Cyber-Physical Attacks

Recommended framing:

* This is not only a classifier paper.
* This is a trustworthy mission-assurance framework.
* The novelty is the integration of graph-temporal AI, calibration, OOD testing, explainability, and recovery reasoning.
* CNN baselines may perform better in-distribution, but they do not provide the same high-confidence mission-assurance analysis.

## Required Manuscript Tables

1. Dataset configuration table
2. Baseline model comparison table
3. Uncertainty calibration table
4. OOD unseen attack table
5. Feature-importance table
6. Recovery / DRL table
7. Claim-positioning table comparing RA-MARS and TRUST-Swarm

## Required Manuscript Figures

1. TRUST-Swarm architecture
2. Graph-temporal model structure
3. Training curves
4. Calibration / reliability figure
5. OOD entropy or confidence shift figure
6. Feature-importance figure
7. Mission recovery workflow

## Final Verdict

The final RunPod experiment provides a strong experimental foundation, but the manuscript must be written carefully.

Do not claim:

Graph-Temporal Transformer is the best classifier across all baselines.

Do claim:

TRUST-Swarm provides a high-confidence mission-assurance framework that integrates graph-temporal modeling, uncertainty calibration, OOD stress testing, explainability, and recovery reasoning for resilient multi-UAV operations under cyber-physical attacks.


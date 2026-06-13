# TRUST-Swarm Manuscript Table Captions Draft

## Table 1. Experimental dataset configuration

This table summarizes the final TRUST-Swarm experimental configuration used for the three-seed journal run. The setup includes 300 mission runs per seed, 240 timesteps per mission, 20 UAVs per mission, 9 telemetry features, 8 mission-state classes, and 66,300 graph-temporal windows per seed.

Recommended placement: Experimental Setup section.

## Table 2. Telemetry feature description

This table defines the nine telemetry features used in the TRUST-Swarm graph-temporal windows. The features represent communication reliability, navigation consistency, energy state, mission progress, and mission coverage. These telemetry variables provide the basis for detecting and reasoning about jamming, spoofing, tampering, and combined cyber-physical attacks.

Recommended placement: Methodology or Experimental Setup section.

## Table 3. Model comparison across three seeds

This table compares the Graph-Temporal Transformer against LSTM, GRU, and 1D-CNN baselines using mean and standard deviation across three random seeds. The reported metrics include test loss, accuracy, macro F1, macro precision, and macro recall.

Key interpretation: the 1D-CNN baseline achieved the strongest in-distribution classification performance, while the Graph-Temporal Transformer supports the broader TRUST-Swarm framework with graph-temporal reasoning, calibration, OOD testing, explainability, and recovery-oriented analysis.

Recommended placement: Results section, model comparison subsection.

Source file: `docs/manuscript_results_tables.md`

## Table 4. Uncertainty calibration results

This table reports uncertainty calibration metrics for the Graph-Temporal Transformer. Metrics include Expected Calibration Error, Brier score, mean confidence, and predictive entropy. The low Expected Calibration Error supports the high-confidence computing direction of TRUST-Swarm under in-distribution test conditions.

Recommended placement: Results section, uncertainty calibration subsection.

Source file: `docs/manuscript_results_tables.md`

## Table 5. OOD and unseen attack stress-test results

This table reports model behavior under in-distribution and OOD cyber-physical stress conditions. The evaluated conditions include stealth jamming, slow GPS drift, intermittent tampering, delayed combined attacks, and unseen swarm noise. The results show that severe unseen shifts can substantially degrade macro F1 performance, demonstrating the need for OOD-aware mission-assurance evaluation.

Recommended placement: Results section, OOD stress testing subsection.

Source file: `docs/manuscript_results_tables.md`

## Table 6. Perturbation-based feature-importance results

This table reports feature importance using macro-F1 drop after perturbing each telemetry feature. Features with larger macro-F1 drops have greater influence on model predictions. Latency, zone coverage, route deviation, mission progress, and GPS jump were among the most important telemetry drivers, aligning with operational indicators of communication degradation, navigation disruption, and mission progress loss.

Recommended placement: Results section, explainability subsection.

Source file: `docs/manuscript_results_tables.md`

## Table 7. OOD-safe interpretation and claim-positioning table

This table should summarize what the manuscript can safely claim and what it should avoid claiming.

Safe claims:

* TRUST-Swarm provides a high-confidence mission-assurance framework.
* The Graph-Temporal Transformer achieved strong calibrated in-distribution performance.
* OOD stress testing revealed major vulnerability under unseen cyber-physical shifts.
* Feature importance identified operationally meaningful telemetry drivers.
* PPO recovery is included as a recovery-reasoning scaffold.

Claims to avoid:

* Graph-Temporal Transformer outperforms all baselines.
* OOD detection is perfect.
* PPO recovery is deployment-ready.
* Synthetic telemetry fully represents real UAV missions.
* TRUST-Swarm is a complete operational UAV control system.

Recommended placement: Discussion or Limitations section.

## Table 8. Limitations and future-work summary

This table should summarize the main limitations and corresponding future-work directions.

Recommended rows:

1. Synthetic telemetry limitation → field telemetry and simulator-in-the-loop validation
2. Simplified graph construction → physics-aware dynamic UAV communication graphs
3. OOD degradation → stronger OOD detection, conformal prediction, and ensembles
4. CNN baseline superiority → improved graph-temporal architecture and harder benchmark design
5. PPO recovery scaffold → safety-constrained recovery policy learning
6. Controlled simulation setting → real UAV swarm testbed or hardware-in-the-loop validation

Recommended placement: Limitations and Future Work section.


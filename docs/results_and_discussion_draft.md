# Results and Discussion Draft

## Experimental Configuration

The TRUST-Swarm experiment was evaluated using a three-seed journal-grade configuration with seeds 42, 123, and 2026. For each seed, the telemetry generator produced 300 mission runs with 240 timesteps and 20 UAVs per mission. The graph-window builder generated 66,300 graph-temporal windows per seed using a 20-step temporal window, 20 UAV nodes, and 9 telemetry features.

The evaluation included temporal baselines, a graph-temporal model, uncertainty calibration, out-of-distribution attack evaluation, and perturbation-based feature-importance analysis. The baseline models included LSTM, GRU, and 1D-CNN. The proposed TRUST-Swarm model used a Graph-Temporal Transformer to jointly reason over UAV-node interactions and temporal mission evolution.

## In-Distribution Classification Performance

The Graph-Temporal Transformer achieved a mean accuracy of 0.9647 and a mean macro F1 score of 0.8750 across the three seeds. This confirms that the proposed graph-temporal architecture can learn meaningful mission-state patterns from multi-UAV telemetry under cyber-physical attack conditions.

The 1D-CNN baseline achieved the strongest in-distribution classification performance, with a mean accuracy of 0.9987 and a mean macro F1 score of 0.9971. The LSTM and GRU baselines achieved mean macro F1 scores of 0.9608 and 0.9288, respectively.

These results indicate that the current synthetic telemetry setting contains strong local temporal signatures that can be captured effectively by convolutional temporal models. Therefore, the contribution of TRUST-Swarm should not be framed as outperforming every baseline in standard classification accuracy. Instead, the correct contribution is the integration of graph-temporal learning with uncertainty calibration, OOD stress testing, explainability, and mission-recovery reasoning.

## Uncertainty Calibration

The Graph-Temporal Transformer demonstrated strong in-distribution calibration. Across the three seeds, the model achieved a mean Expected Calibration Error of 0.0088 and a mean Brier score of 0.0531. The mean predictive confidence was 0.9601, while the mean predictive entropy was 0.0986.

These results support the high-confidence computing framing of TRUST-Swarm. The model is not only capable of producing accurate predictions under in-distribution conditions, but it also provides calibrated confidence estimates that can be used by a mission-assurance layer.

## OOD and Unseen Attack Stress Testing

OOD evaluation revealed that unseen cyber-physical shifts cause substantial degradation in model performance. The in-distribution macro F1 score was 0.8750, while intermittent tampering reduced macro F1 to 0.5965. More severe shifts produced larger degradation: slow GPS drift achieved a macro F1 of 0.1701, stealth jamming achieved 0.0779, and delayed combined attacks achieved 0.0521.

These results show that unseen attack conditions can significantly alter mission telemetry distributions. The findings support the need for OOD-aware monitoring in safety-critical multi-UAV systems. However, the model should not be described as perfectly detecting all OOD conditions. Some severe OOD cases retained high confidence, indicating that confidence alone is not sufficient for reliable OOD rejection. Instead, the results motivate the combined use of uncertainty monitoring, OOD stress testing, explainability, and recovery policies.

## Explainability Analysis

Perturbation-based feature importance showed that the most influential telemetry features were latency, zone coverage, route deviation, mission progress, and GPS jump. These features align with the operational meaning of the attack scenarios. Latency reflects communication degradation, zone coverage reflects mission-level impact, route deviation and GPS jump reflect navigation disruption, and mission progress reflects task completion under cyber-physical interference.

This explainability result improves the interpretability of TRUST-Swarm because the model’s most important features correspond to mission-relevant risk factors rather than arbitrary telemetry artifacts.

## Discussion

The final results show that TRUST-Swarm should be positioned as a high-confidence mission-assurance framework rather than only a classifier. Although the 1D-CNN baseline achieved stronger in-distribution classification accuracy, it does not provide the same integrated framework for graph-temporal mission modeling, calibration, OOD evaluation, explainability, and recovery reasoning.

The Graph-Temporal Transformer provides a structured representation of multi-UAV mission state by incorporating both UAV-node interactions and temporal evolution. Its calibrated uncertainty metrics support high-confidence decision-making under normal conditions, while the OOD stress tests expose vulnerability under unseen attack shifts. These findings are important because real-world UAV operations rarely remain fully in-distribution. Mission-assurance systems must identify not only what class is predicted, but also how trustworthy the prediction is and which telemetry factors contributed to the decision.

The feature-importance results further support the operational relevance of the model. The strongest decision drivers were latency, zone coverage, route deviation, mission progress, and GPS jump, all of which are meaningful indicators of cyber-physical mission degradation. This improves the credibility of the model for defense and autonomous-systems applications.

## Manuscript Claim to Use

The final manuscript should claim that TRUST-Swarm provides an integrated trustworthy AI framework for multi-UAV mission assurance under cyber-physical attacks. The framework combines graph-temporal learning, calibration, OOD stress testing, explainability, and recovery reasoning.

The manuscript should not claim that the Graph-Temporal Transformer is the best in-distribution classifier across all baselines. Instead, it should state that the proposed framework adds trust, interpretability, OOD awareness, and recovery support beyond raw classification performance.

## Limitations

The current dataset is synthetically generated and should be described as a controlled simulation-based evaluation. Although it includes multiple attack types, multiple seeds, and large-scale telemetry generation, it does not replace field-tested UAV data. The OOD results also show that severe unseen shifts can produce major performance degradation, and in some cases the model remains highly confident under OOD conditions. This limitation should be acknowledged clearly.

Future work should include more realistic communication-channel simulation, physics-based UAV mobility, larger swarm-size variation, field telemetry, and stronger OOD detection mechanisms.

## Final Interpretation

The results provide a strong foundation for a journal manuscript if the contribution is framed correctly. TRUST-Swarm should be presented as a high-confidence mission-assurance framework rather than a pure classifier. The strongest contribution is the combined evaluation of graph-temporal learning, uncertainty calibration, OOD stress testing, explainability, and recovery reasoning for resilient multi-UAV operations under cyber-physical attacks.


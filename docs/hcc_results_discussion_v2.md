# High-Confidence Computing Results and Discussion v2

## 5. Results and discussion

This section presents the experimental findings of TRUST-Swarm and interprets them from a high-confidence computing perspective. The purpose of the evaluation is not limited to identifying the model with the highest in-distribution classification score. Instead, the results are analyzed across five assurance dimensions: mission-state recognition, calibrated reliability, OOD cyber-physical stress behavior, traceable feature-level explanation, and recovery-oriented reasoning. This organization is important because secure multi-UAV mission assurance requires more than a predicted label. A useful framework must also identify when predictions are reliable, when unseen mission shifts create risk, which telemetry signals influence the decision, and how the output can support response planning.

### 5.1. In-distribution mission-state recognition

Table 2 reports the main in-distribution classification findings. The in-distribution evaluation shows that mission-state recognition is feasible using graph-temporal UAV telemetry. The Graph-Temporal Transformer achieves a mean accuracy of 0.9647 and a mean macro F1 score of 0.8750 across the three-seed evaluation. These values indicate that the model can learn mission-state patterns from communication, navigation, energy, coverage, and mission-progress telemetry. The result is meaningful because the evaluation includes not only normal and single-attack conditions, but also combined cyber-physical attack states.

At the same time, the baseline comparison shows that the 1D-CNN achieves stronger raw in-distribution classification performance, with a mean macro F1 score of 0.9971. This is an important result and should be interpreted carefully. It means TRUST-Swarm should not be presented as a claim that the Graph-Temporal Transformer is the strongest standalone classifier. A journal-level interpretation should avoid that overclaim. The stronger and more accurate conclusion is that TRUST-Swarm contributes an integrated high-confidence mission-assurance framework. In this framework, raw classification is only one component; calibration, OOD vulnerability exposure, explainability, ablation evidence, runtime feasibility, and recovery reasoning are also part of the contribution.

This interpretation imshows the scientific positioning of the paper. A classification-only paper would be weakened by a baseline that performs better. A high-confidence computing paper can still make a strong contribution if it shows that the proposed framework evaluates reliability, robustness, traceability, and response support beyond raw accuracy.

### 5.2. Calibration and confidence reliability

The calibration results show that the Graph-Temporal Transformer produces strong in-distribution probabilistic reliability. The model achieves an Expected Calibration Error of 0.0088 and a Brier score of 0.0531. A low ECE means that the predicted confidence is closely aligned with empirical correctness. A low Brier score indicates that the probability distribution is not only accurate in its top prediction but also reasonably reliable across the class-probability vector.

This result is important for secure UAV swarm mission assurance. In an autonomous mission, a high-confidence wrong prediction can be more dangerous than a low-confidence prediction, because the system may proceed without escalation. Calibration therefore acts as an assurance signal. A prediction with high confidence and low entropy can support normal continuation or targeted response. A prediction with low confidence or high entropy can trigger monitoring, escalation, or recovery reasoning.

The calibration evidence also helps distinguish TRUST-Swarm from ordinary classification systems. A model that reports only accuracy cannot tell whether its probabilities should be trusted. TRUST-Swarm explicitly evaluates this reliability dimension, making the output more useful for high-confidence computing.

### 5.3. OOD cyber-physical stress-test behavior

Fig. 2 summarizes the OOD stress-test trend. The OOD stress-test results reveal a key finding: in-distribution performance does not guarantee reliability under unseen cyber-physical shifts. Under intermittent tampering, macro F1 decreases to 0.5965. More severe unseen conditions such as stealth jamming, slow GPS drift, and delayed combined attacks show substantial degradation. This behavior demonstrates why OOD testing is necessary for high-confidence mission assurance.

This result should not be hidden or softened. In a strong journal paper, the OOD degradation should be presented as evidence that the framework exposes mission-risk conditions that standard testing would miss. If the manuscript only reported in-distribution accuracy, it would give an incomplete and potentially misleading picture of mission reliability. OOD testing shows where the model’s learned decision boundary is vulnerable and where additional monitoring, retraining, adaptation, or recovery logic may be required.

The most important interpretation is that TRUST-Swarm does not solve all unseen attack conditions. Instead, it provides a structured way to identify them. This is scientifically stronger and more honest. For high-confidence computing, exposing failure modes is a contribution because it helps define the reliability boundary of the intelligent system.

### 5.4. Explainability and mission-risk drivers

The perturbation-based explainability analysis identifies latency, zone coverage, route deviation, mission progress, and GPS jump as the strongest mission-risk drivers. These features are operationally meaningful. Latency reflects communication degradation and is strongly associated with jamming-like mission disruption. Zone coverage reflects mission effectiveness and swarm coverage quality. Route deviation and GPS jump reflect navigation manipulation and spoofing-like effects. Mission progress reflects whether the swarm is advancing toward mission completion or being disrupted.

This result supports traceable mission reasoning. Instead of producing only a mission-state label, TRUST-Swarm identifies which telemetry factors most influenced the decision. This helps convert model output into evidence that can be inspected by a human analyst or used by a recovery-reasoning layer. For example, a spoofing prediction becomes more credible when route deviation and GPS jump are highly influential. A jamming prediction becomes more credible when latency and packet loss are influential. A tampering or combined-attack prediction becomes more credible when mission progress, energy state, and coverage variables degrade.

The explainability results therefore strengthen the high-confidence framing of the paper. The framework is not simply a black-box classifier; it provides traceable evidence connected to mission semantics.

### 5.5. Ablation evidence

The ablation study evaluates whether major framework components contribute to the final mission-assurance behavior. Architectural ablations examine the effect of removing UAV-node attention and temporal transformer reasoning. Framework-level ablations examine the contribution of calibration evidence, OOD stress evidence, explainability evidence, and recovery-oriented support.

The full Graph-Temporal Transformer reaches a macro F1 score of 0.8734 in the ablation setting. Removing UAV-node attention reduces macro F1 to 0.7903, and removing the temporal transformer reduces macro F1 to 0.8237. These results indicate that both node-level interaction modeling and temporal reasoning contribute to classification performance. Node attention appears especially important because UAV swarm mission degradation is distributed across multiple nodes rather than isolated to a single flat time-series signal.

From the framework perspective, ablation also clarifies that classification is not the only value of TRUST-Swarm. Calibration, OOD analysis, explanation, and recovery reasoning do not necessarily imshow raw accuracy directly, but they imshow assurance evidence. This distinction is essential for the journal narrative. The paper should clearly separate classification performance from high-confidence mission-assurance value.

### 5.6. Runtime and complexity analysis

Runtime profiling shows that the Graph-Temporal Transformer has 680,840 trainable parameters and a model size of approximately 2.618 MB. The measured inference latency is 2.267 ms per batch and 0.0177 ms per sample, with throughput of approximately 56,458 windows per second. The training-step time is approximately 9.938 ms.

These results support the practical computing feasibility of the framework. A high-confidence intelligent system must not only provide assurance evidence; it must also be computationally reasonable. The measured model size and inference speed suggest that the prediction layer is lightweight enough for rapid mission-window processing in a GPU-enabled environment. However, the current runtime results should be interpreted as computational profiling rather than deployment validation. Real UAV deployment would require additional testing under edge-hardware constraints, communication delays, onboard compute limits, and hardware-in-the-loop conditions.

### 5.7. Recovery-oriented reasoning

The recovery-reasoning layer demonstrates how prediction, confidence, entropy, and mission-risk indicators can be mapped to response-oriented actions. The action space includes continue, monitor, reroute, reassign, isolate node, and return to base. This module should not be described as an validated in field settings UAV controller. Instead, it should be described as a recovery-reasoning scaffold that shows how high-confidence prediction outputs can support mission-response planning.

This distinction is important. A detection system that stops at classification does not complete the mission-assurance loop. TRUST-Swarm connects recognition evidence to possible response actions. When confidence is high and the predicted state is normal, continue may be appropriate. When uncertainty is high, monitor or escalate may be appropriate. When spoofing indicators are strong, rerouting may be considered. When node-level evidence suggests local compromise, isolate-node reasoning may be relevant. When combined attacks and uncertainty are high, return-to-base reasoning may be safer.

### 5.8. Discussion

The results support four main observations. First, graph-temporal mission-state recognition is feasible for simulated UAV swarm cyber-physical telemetry. Second, raw in-distribution classification performance alone is not enough to support high-confidence mission assurance. Third, OOD stress testing is necessary because performance can degrade sharply under unseen cyber-physical shifts. Fourth, explainability and recovery reasoning help connect model predictions to mission-level evidence and response support.

The most important scientific point is that TRUST-Swarm should be framed as an assurance framework rather than a classifier superiority claim. The 1D-CNN baseline shows stronger raw in-distribution classification performance. However, the proposed framework contributes additional high-confidence computing capabilities that are not captured by raw macro F1 alone. These include calibrated confidence, OOD vulnerability exposure, traceable mission-risk drivers, ablation evidence, runtime feasibility, and recovery-oriented reasoning.

This balanced interpretation makes the manuscript stronger. It avoids exaggerated claims and aligns the contribution with the scope of High-Confidence Computing. The paper demonstrates that secure UAV swarm mission assurance requires integrated evidence about prediction, reliability, robustness, traceability, and response support.

### 5.9. Automatically inserted result-table previews

The following tables are automatically extracted from available CSV files under the local `results/` directory. They are included to preserve numeric reproducibility and prevent manual copying errors.

**Source file:** `results/hcc/ablation_summary.csv`

| configuration | ablation_type | train_loss | test_loss | accuracy | macro_precision | macro_recall | macro_f1 | parameters | calibration_evidence | ood_evidence | explanation_evidence | recovery_support | interpretation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A0_full_graph_temporal_transformer | model_architecture | 0.09546179582465844 | 0.11820491030812263 | 0.9579185520361991 | 0.927624114385649 | 0.8433213650876751 | 0.8734159371910365 | 680840 | yes | yes | yes | yes | Architecture-level ablation trained and evaluated on the same graph-temporal dataset. |
| A1_without_uav_node_attention | model_architecture | 0.12242422580988292 | 0.10202680718010435 | 0.9571644042232278 | 0.792966784801138 | 0.7993020771300401 | 0.7903457708140788 | 415880 | yes | yes | yes | yes | Architecture-level ablation trained and evaluated on the same graph-temporal dataset. |
| A2_without_temporal_transformer | model_architecture | 0.09725682711206286 | 0.13414442351159567 | 0.9506787330316742 | 0.9263067869267713 | 0.7982204460529145 | 0.8237202081472406 | 284296 | yes | yes | yes | yes | Architecture-level ablation trained and evaluated on the same graph-temporal dataset. |
| A3_without_uncertainty_calibration | framework_module |  | 0.11820491030812263 | 0.9579185520361991 | 0.927624114385649 | 0.8433213650876751 | 0.8734159371910365 | 680840 | no | yes | yes | yes | Removes confidence reliability evidence; prediction remains available but ECE/Brier/confidence evidence is absent. |
| A4_without_ood_stress_testing | framework_module |  | 0.11820491030812263 | 0.9579185520361991 | 0.927624114385649 | 0.8433213650876751 | 0.8734159371910365 | 680840 | yes | no | yes | yes | Removes unseen-shift vulnerability evidence; prediction remains available but OOD risk evidence is absent. |
| A5_without_explainability | framework_module |  | 0.11820491030812263 | 0.9579185520361991 | 0.927624114385649 | 0.8433213650876751 | 0.8734159371910365 | 680840 | yes | yes | no | yes | Removes traceable mission-risk driver evidence; prediction remains available but feature-level explanation is absent. |
| A6_without_recovery_reasoning | framework_module |  | 0.11820491030812263 | 0.9579185520361991 | 0.927624114385649 | 0.8433213650876751 | 0.8734159371910365 | 680840 | yes | yes | yes | no | Removes mission-response support; prediction, calibration, OOD, and explanation remain available. |


**Source file:** `results/hcc/runtime_complexity_summary.csv`

| model | parameters | model_size_mb | batch_size | window_size | num_uavs | num_features | inference_batch_latency_ms | inference_sample_latency_ms | throughput_windows_per_second | single_train_step_ms | device | gpu_memory_mb |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LSTM | 308616 | 1.181 | 128 | 20 | 20 | 9 | 0.214 | 0.001669 | 599006.617 | 1.674 | cuda | 147.314 |
| GRU | 235912 | 0.904 | 128 | 20 | 20 | 9 | 0.177 | 0.001381 | 724111.11 | 1.48 | cuda | 147.595 |
| CNN1D | 136840 | 0.531 | 128 | 20 | 20 | 9 | 0.211 | 0.001647 | 606987.446 | 1.465 | cuda | 147.595 |
| GraphTemporalTransformer | 680840 | 2.618 | 128 | 20 | 20 | 9 | 2.267 | 0.017712 | 56458.364 | 9.938 | cuda | 932.105 |


**Source file:** `results/tables/realistic_dataset_summary.csv`

| attack_label | attack_name | rows |
| --- | --- | --- |
| 0 | normal | 1076680 |
| 1 | jamming | 87480 |
| 2 | spoofing | 83100 |
| 3 | tampering | 60620 |
| 4 | jamming_spoofing | 44660 |
| 5 | jamming_tampering | 29840 |
| 6 | spoofing_tampering | 26920 |
| 7 | combined | 30700 |


# TRUST-Swarm Figure Captions Draft

## Figure 1. Model comparison by mean macro F1

This figure compares the mean macro F1 scores of the evaluated models across three random seeds. The 1D-CNN baseline achieved the highest in-distribution macro F1, while the Graph-Temporal Transformer achieved strong classification performance with additional support for graph-temporal reasoning, uncertainty calibration, OOD stress testing, explainability, and recovery-oriented analysis.

File: `figures/manuscript/fig_01_model_comparison_macro_f1.png`

## Figure 2. Model comparison by mean accuracy

This figure compares the mean in-distribution accuracy of the evaluated models. The 1D-CNN baseline achieved the strongest raw classification accuracy, indicating that the synthetic telemetry contains strong local temporal signatures. The result supports positioning TRUST-Swarm as a high-confidence mission-assurance framework rather than only a raw classifier.

File: `figures/manuscript/fig_02_model_comparison_accuracy.png`

## Figure 3. Uncertainty calibration using Expected Calibration Error

This figure shows the Expected Calibration Error of the Graph-Temporal Transformer. The low ECE value indicates strong in-distribution calibration, supporting the use of calibrated confidence estimates for high-confidence mission assurance.

File: `figures/manuscript/fig_03_uncertainty_ece.png`

## Figure 4. Uncertainty calibration using Brier score

This figure reports the Brier score for the Graph-Temporal Transformer uncertainty evaluation. A lower Brier score indicates better probabilistic prediction quality, supporting the reliability of the model’s in-distribution confidence estimates.

File: `figures/manuscript/fig_04_uncertainty_brier.png`

## Figure 5. OOD stress-test performance by mean macro F1

This figure shows macro F1 performance under in-distribution and OOD cyber-physical stress conditions. Severe unseen shifts such as stealth jamming, slow GPS drift, and delayed combined attacks substantially reduce performance, demonstrating the importance of OOD-aware mission-assurance evaluation.

File: `figures/manuscript/fig_05_ood_macro_f1.png`

## Figure 6. OOD stress-test predictive entropy

This figure shows predictive entropy across in-distribution and OOD conditions. Entropy helps characterize model uncertainty under shifted mission conditions, although the results should not be interpreted as perfect OOD detection. The figure supports the need for combined uncertainty monitoring, OOD stress testing, and recovery reasoning.

File: `figures/manuscript/fig_06_ood_entropy.png`

## Figure 7. Perturbation-based feature importance

This figure shows the most influential telemetry features based on macro-F1 drop after feature perturbation. Latency, zone coverage, route deviation, mission progress, and GPS jump were among the most important drivers, aligning with operationally meaningful indicators of communication degradation, navigation disruption, and mission-progress loss.

File: `figures/manuscript/fig_07_feature_importance.png`

## Manuscript Placement Guide

Recommended placement:

* Figure 1: Results section, model comparison subsection
* Figure 2: Results section, model comparison subsection
* Figure 3: Results section, uncertainty calibration subsection
* Figure 4: Results section, uncertainty calibration subsection
* Figure 5: Results section, OOD stress testing subsection
* Figure 6: Results section, OOD stress testing subsection
* Figure 7: Results section, explainability subsection


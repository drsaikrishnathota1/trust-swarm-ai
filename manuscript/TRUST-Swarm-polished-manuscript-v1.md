# TRUST-Swarm: Trustworthy Graph-Temporal AI for High-Confidence Multi-UAV Mission Assurance Under Cyber-Physical Attacks

## Abstract

Multi-UAV swarm missions are increasingly exposed to cyber-physical disruptions, including communication jamming, GPS spoofing, telemetry tampering, and combined attack conditions. Existing UAV security and resilience studies commonly emphasize attack detection or communication protection, but many provide limited support for calibrated confidence estimation, out-of-distribution stress testing, explainability, and recovery-oriented mission assurance [1–4, 34–38]. This paper presents TRUST-Swarm, a trustworthy graph-temporal AI framework for high-confidence multi-UAV mission assurance under cyber-physical attacks.

TRUST-Swarm models UAV swarms as dynamic graph-temporal telemetry windows, where UAV nodes evolve across mission time under normal and adversarial conditions. The framework integrates graph-temporal learning, uncertainty calibration, OOD stress testing, perturbation-based explainability, and PPO-based recovery reasoning [8–13, 18–25, 29–33]. A three-seed simulation study was conducted using 300 mission runs per seed, 240 timesteps per mission, 20 UAVs per mission, and 66,300 graph-temporal windows per seed. The Graph-Temporal Transformer achieved a mean accuracy of 0.9647 and mean macro F1 of 0.8750, while producing strong calibration with an Expected Calibration Error of 0.0088 and Brier score of 0.0531.

The results show that severe unseen cyber-physical shifts substantially degrade model performance, especially delayed combined attacks, stealth jamming, and slow GPS drift. Explainability analysis identified latency, zone coverage, route deviation, mission progress, and GPS jump as influential telemetry drivers. Although a 1D-CNN baseline achieved stronger in-distribution classification performance, TRUST-Swarm provides a broader high-confidence mission-assurance framework by integrating graph-temporal modeling, calibration, OOD evaluation, explainability, and recovery reasoning.

## Keywords

Multi-UAV swarms; mission assurance; graph-temporal AI; cyber-physical attacks; jamming; GPS spoofing; telemetry tampering; uncertainty calibration; out-of-distribution testing; explainable AI; reinforcement learning.

## 1. Introduction

Multi-UAV swarm systems are increasingly used for surveillance, reconnaissance, disaster response, border monitoring, logistics, and defense-oriented autonomous missions. Compared with single-UAV systems, coordinated UAV swarms provide distributed coverage, redundancy, adaptive coordination, and improved mission scalability. However, these advantages also introduce cyber-physical vulnerabilities because a swarm mission can be degraded through communication jamming, GPS spoofing, telemetry tampering, compromised nodes, route disruption, and coordinated combined attacks [1–4, 34–38].

In contested environments, cyber-physical attacks can affect mission assurance at multiple levels. Jamming can increase packet loss and latency, reducing inter-UAV coordination. GPS spoofing can induce route deviation, localization jumps, and velocity inconsistency. Telemetry tampering can distort mission-progress reporting, battery state, energy consumption, or coverage information. Combined attacks can simultaneously degrade communication, navigation, and mission-integrity signals [3, 4, 38–47].

Existing UAV security and resilience methods often focus on attack detection, secure communication, intrusion detection, anomaly monitoring, or rule-based recovery. Although these approaches are valuable, many remain limited in four ways. First, they may treat UAV telemetry as independent time-series data rather than modeling the relational structure among UAV nodes. Second, they often emphasize classification accuracy without calibrated confidence estimation. Third, they rarely evaluate behavior under unseen OOD cyber-physical shifts. Fourth, they provide limited explainability and limited connection between risk prediction and recovery-oriented mission reasoning [18–25, 29–33].

To address this gap, this paper presents TRUST-Swarm, a trustworthy graph-temporal AI framework for high-confidence multi-UAV mission assurance under cyber-physical attacks. TRUST-Swarm models swarm telemetry as graph-temporal mission windows, evaluates a Graph-Temporal Transformer for mission-state recognition, and integrates uncertainty calibration, OOD stress testing, perturbation-based explainability, and PPO-based recovery reasoning.

The main contributions are:

1. A trustworthy graph-temporal AI framework for multi-UAV mission assurance under cyber-physical attacks.
2. A graph-temporal telemetry representation for modeling UAV-node interactions and mission evolution.
3. A Graph-Temporal Transformer evaluation under jamming, spoofing, tampering, and combined attacks.
4. A three-seed simulation study with 300 mission runs per seed, 240 timesteps, 20 UAVs, and 66,300 graph-temporal windows per seed.
5. Baseline comparison against LSTM, GRU, and 1D-CNN models.
6. Uncertainty calibration using Expected Calibration Error, Brier score, confidence, and entropy.
7. OOD stress testing under stealth jamming, slow GPS drift, intermittent tampering, delayed combined attacks, and unseen swarm noise.
8. Perturbation-based explainability identifying mission-relevant telemetry drivers.
9. A recovery-reasoning scaffold using PPO for mission-assurance decision support.

## 2. Related Work

UAV swarm mission assurance requires continuous evaluation of communication reliability, navigation integrity, mission progress, and swarm coordination. Prior studies have examined UAV security risks, UAS traffic-management security, sensor-channel threats, and cyber-physical vulnerabilities [1, 2, 34–37]. These studies motivate the need for mission-assurance frameworks that can reason about both cyber disruption and physical mission degradation.

Cyber-physical attacks on UAV swarms include jamming, GPS/GNSS spoofing, telemetry tampering, and combined disruptions. Recent work has studied UAV swarm spoofing, cooperative formation spoofing mitigation, anti-jamming communication, and adaptive UAV planning under adversarial communication conditions [3, 4, 38–47]. TRUST-Swarm builds on this motivation by evaluating normal, jamming, spoofing, tampering, and combined attack states, together with unseen OOD attack variants.

Temporal deep learning models such as LSTM, GRU, and 1D-CNN are widely used for sequence modeling and telemetry classification [14–17]. In TRUST-Swarm, these models serve as baselines for in-distribution mission-state recognition. The strong 1D-CNN result confirms that local temporal signatures are highly informative in the current synthetic telemetry setting.

Graph-temporal AI is relevant because UAV swarms naturally form dynamic multi-agent systems. Graph neural networks, graph attention, transformers, and time-series transformer architectures provide foundations for learning relational and temporal dependencies [8–13]. TRUST-Swarm uses this direction by representing each mission window as a temporal sequence of UAV-node telemetry states.

Uncertainty calibration and OOD evaluation are central to high-confidence AI. Prior work has shown that neural networks may be poorly calibrated, and that predictive uncertainty can degrade under dataset shift [18–28]. TRUST-Swarm therefore evaluates Expected Calibration Error, Brier score, predictive confidence, entropy, and OOD stress-test performance.

Explainable AI methods such as LIME, SHAP, saliency evaluation, and XAI frameworks support interpretation of model decisions [29–32]. TRUST-Swarm uses perturbation-based feature importance to identify telemetry features most responsible for model predictions. Finally, PPO and multi-agent reinforcement learning provide foundations for recovery-oriented mission reasoning [33, 48–53].

## 3. Methodology

TRUST-Swarm consists of synthetic telemetry generation, graph-temporal window construction, temporal baseline modeling, Graph-Temporal Transformer learning, uncertainty calibration, OOD stress testing, explainability, and PPO-based recovery reasoning.

The telemetry generator simulates multi-UAV missions under normal and adversarial conditions. Each UAV is represented using nine telemetry features: packet loss rate, latency, route deviation, GPS jump, velocity inconsistency, battery level, mission progress, zone coverage, and energy consumption. The attack classes include normal, jamming, spoofing, tampering, jamming-spoofing, jamming-tampering, spoofing-tampering, and combined attack.

Raw telemetry is converted into graph-temporal windows represented as `T × N × F`, where `T` is the temporal window length, `N` is the number of UAV nodes, and `F` is the number of telemetry features. In the final experiment, `T = 20`, `N = 20`, and `F = 9`.

The Graph-Temporal Transformer first projects telemetry features into a hidden representation, applies UAV-node attention, encodes temporal evolution using a transformer encoder, and predicts the mission-state class. Temporal baselines include LSTM, GRU, and 1D-CNN. Uncertainty is evaluated using Monte Carlo dropout, Expected Calibration Error, Brier score, confidence, and entropy. OOD stress testing evaluates stealth jamming, slow GPS drift, intermittent tampering, delayed combined attack, and unseen swarm noise. Explainability is computed using macro-F1 drop after feature perturbation. PPO recovery is included as a recovery-reasoning scaffold, not as a deployment-ready UAV controller.

## 4. Experimental Setup

The final experiment was executed using three random seeds: 42, 123, and 2026. For each seed, the telemetry generator produced 300 mission runs, 240 timesteps per mission, 20 UAVs per mission, 1,440,000 raw telemetry rows, and 66,300 graph-temporal windows. Each model was trained for 30 epochs with a batch size of 128.

Evaluation metrics included accuracy, macro F1, macro precision, macro recall, and test loss. Macro-averaged metrics were emphasized because cyber-physical attack classes were imbalanced. Calibration was evaluated using Expected Calibration Error, Brier score, confidence, and entropy. OOD stress testing reported accuracy, macro F1, confidence, entropy, and low-confidence rate. Explainability was evaluated using perturbation-based feature importance.

## 5. Results and Discussion

The Graph-Temporal Transformer achieved mean accuracy of 0.9647 and mean macro F1 of 0.8750 across three seeds. These results show that graph-temporal learning can capture meaningful multi-UAV mission-state patterns under cyber-physical attack conditions.

The 1D-CNN baseline achieved the strongest in-distribution classification performance, with mean accuracy of 0.9987 and mean macro F1 of 0.9971. LSTM and GRU achieved mean macro F1 scores of 0.9608 and 0.9288, respectively. This result indicates that the synthetic telemetry contains strong local temporal signatures. Therefore, the manuscript should not claim that the Graph-Temporal Transformer is the best raw classifier. Instead, TRUST-Swarm should be positioned as a high-confidence mission-assurance framework that adds graph-temporal modeling, calibration, OOD evaluation, explainability, and recovery reasoning.

The Graph-Temporal Transformer produced strong in-distribution calibration, with mean Expected Calibration Error of 0.0088 and mean Brier score of 0.0531. This supports the high-confidence computing framing because calibrated confidence can help a mission-assurance layer decide when predictions should be trusted, monitored, or escalated [18–24].

OOD stress testing revealed substantial degradation under severe unseen cyber-physical shifts. In-distribution macro F1 was 0.8750, while intermittent tampering reduced macro F1 to 0.5965. Slow GPS drift, stealth jamming, and delayed combined attacks reduced macro F1 to 0.1701, 0.0779, and 0.0521, respectively. These findings show that unseen attack conditions can significantly alter mission telemetry distributions and should be evaluated explicitly in UAV mission-assurance systems [22, 25–28, 54, 55].

Perturbation-based explainability identified latency, zone coverage, route deviation, mission progress, and GPS jump as major telemetry drivers. These features are operationally meaningful because they reflect communication degradation, coverage loss, navigation disruption, and mission-progress interruption. This improves the credibility of TRUST-Swarm because the model relies on mission-relevant signals rather than arbitrary telemetry artifacts.

## 6. Limitations and Future Work

This study has several limitations. First, the evaluation uses synthetic telemetry. Although this enables controlled multi-seed testing across cyber-physical attack conditions, it does not replace field-collected UAV telemetry. Second, graph construction is based on graph-temporal telemetry windows rather than full physics-aware communication graphs. Third, OOD stress tests show severe degradation under unseen shifts, and some OOD cases may retain high confidence. Fourth, the 1D-CNN baseline outperforms the Graph-Temporal Transformer in raw in-distribution classification. Fifth, the PPO recovery module is an initial recovery-reasoning scaffold rather than a complete operational controller.

Future work should include field-realistic UAV telemetry, physics-aware communication modeling, stronger OOD detection, conformal prediction, ensembles, safety-constrained recovery policies, and simulator-in-the-loop or hardware-in-the-loop validation.

## 7. Conclusion

This paper presented TRUST-Swarm, a trustworthy graph-temporal AI framework for high-confidence multi-UAV mission assurance under cyber-physical attacks. The framework combines graph-temporal learning, uncertainty calibration, OOD stress testing, explainability, and recovery-oriented reasoning.

The final three-seed experiment showed strong Graph-Temporal Transformer performance and calibration, while also revealing that 1D-CNN achieved the best in-distribution classification performance. This finding supports a careful interpretation: TRUST-Swarm should not be framed as simply the best classifier, but as an integrated trustworthy mission-assurance framework. OOD stress tests revealed major vulnerability under unseen cyber-physical shifts, and explainability identified operationally meaningful telemetry drivers. Overall, TRUST-Swarm provides a strong foundation for trustworthy AI-enabled UAV swarm mission assurance under cyber-physical uncertainty.


# TRUST-Swarm Journal Submission Package Drafts

## 1. Cover Letter Draft

Dear Editor,

We are pleased to submit our manuscript entitled **“TRUST-Swarm: Trustworthy Graph-Temporal AI for High-Confidence Multi-UAV Mission Assurance Under Cyber-Physical Attacks”** for consideration for publication in your journal.

This manuscript presents TRUST-Swarm, a trustworthy AI framework for high-confidence multi-UAV mission assurance under cyber-physical attacks. The framework integrates graph-temporal learning, uncertainty calibration, out-of-distribution stress testing, perturbation-based explainability, and recovery-oriented reasoning. The study focuses on cyber-physical attack conditions relevant to UAV swarm operations, including jamming, spoofing, telemetry tampering, and combined attack scenarios.

The experimental evaluation was conducted using a three-seed simulation study with 300 mission runs per seed, 240 timesteps per mission, 20 UAVs per mission, and 66,300 graph-temporal windows per seed. The results show that the Graph-Temporal Transformer achieved strong in-distribution performance and calibration, while OOD stress testing revealed substantial degradation under severe unseen cyber-physical shifts. The manuscript carefully positions TRUST-Swarm as a high-confidence mission-assurance framework rather than only a raw attack-classification model.

The main contributions of this work are:

1. A trustworthy graph-temporal AI framework for multi-UAV mission assurance under cyber-physical attacks.
2. A graph-temporal telemetry representation for modeling UAV-node behavior and mission evolution over time.
3. A Graph-Temporal Transformer evaluation under jamming, spoofing, tampering, and combined attack scenarios.
4. A multi-seed experimental study comparing Graph-Temporal Transformer performance with LSTM, GRU, and 1D-CNN baselines.
5. An uncertainty calibration and OOD stress-testing analysis for high-confidence mission assurance.
6. A perturbation-based explainability analysis identifying mission-relevant telemetry drivers.
7. A recovery-reasoning scaffold connecting prediction outputs to mission-assurance decision support.

We believe this manuscript will be of interest to readers working in autonomous systems, UAV swarm resilience, cyber-physical security, trustworthy AI, high-confidence computing, and mission assurance.

This manuscript is original, has not been published previously, and is not under consideration elsewhere. All authors have approved the manuscript and agree with its submission. The authors declare no competing interests.

Thank you for considering our manuscript. We look forward to your response.

Sincerely,

[Author Name]
[Affiliation]
[Email Address]

---

## 2. Highlights Draft

* TRUST-Swarm integrates graph-temporal AI for multi-UAV mission assurance.
* The framework evaluates jamming, spoofing, tampering, and combined attacks.
* Calibration and OOD stress testing support high-confidence AI analysis.
* Explainability identifies latency, coverage, route deviation, and GPS jump.
* Recovery reasoning links cyber-physical risk to mission-assurance actions.

---

## 3. Data Availability Statement Draft

The data used in this study were generated using a synthetic multi-UAV telemetry generator developed for controlled cyber-physical mission-assurance experiments. The generated telemetry includes normal, jamming, spoofing, tampering, and combined attack scenarios across multiple seeds. Due to file-size constraints, large generated datasets and result archives are not included directly in the repository. However, the data-generation scripts and experiment configuration are available in the associated code repository, allowing the synthetic datasets and results to be regenerated.

---

## 4. Code Availability Statement Draft

The source code, experiment scripts, model implementations, telemetry-generation pipeline, baseline models, uncertainty evaluation, OOD evaluation, explainability analysis, and manuscript-support files are available at:

https://github.com/drsaikrishnathota1/trust-swarm-ai

---

## 5. Declaration of Competing Interest Draft

The author declares that there are no known competing financial interests or personal relationships that could have appeared to influence the work reported in this manuscript.

---

## 6. Funding Statement Draft

This research did not receive any specific grant from funding agencies in the public, commercial, or not-for-profit sectors.

---

## 7. Ethical Approval Statement Draft

This study does not involve human participants, human data, animal subjects, or clinical data. The evaluation is based on synthetic simulation-generated UAV telemetry for cyber-physical mission-assurance research.

---

## 8. Author Contribution Statement Draft

The author contributed to the conceptualization, methodology, software implementation, simulation design, experimental evaluation, analysis, manuscript preparation, and final review of the work.

---

## 9. Suggested Reviewer Areas

Potential reviewer expertise areas:

1. UAV swarm autonomy
2. Cyber-physical systems security
3. Jamming and spoofing detection
4. Graph neural networks
5. Temporal transformers
6. Trustworthy AI
7. Uncertainty calibration
8. OOD detection
9. Explainable AI
10. Reinforcement learning for autonomous systems


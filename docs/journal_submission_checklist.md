# TRUST-Swarm Journal Submission Checklist

## Current Status

The first full TRUST-Swarm manuscript draft is assembled.

Completed items:

* Abstract draft
* Contributions draft
* Introduction draft
* Related Work draft
* Methodology draft
* Experimental Setup draft
* Manuscript-ready results tables
* Results and Discussion draft
* Conclusion and Limitations draft
* Full manuscript draft assembled
* Three-seed RunPod experiment completed
* Summary results generated and downloaded

## Strong Parts Already Completed

1. Clear paper title and trustworthy AI framing
2. Strong experimental scale: 3 seeds, 300 runs per seed, 240 timesteps, 20 UAVs
3. Baseline comparison with LSTM, GRU, and 1D-CNN
4. Graph-Temporal Transformer evaluation
5. Uncertainty calibration metrics
6. OOD / unseen attack stress testing
7. Feature-importance explainability
8. PPO recovery scaffold
9. Careful claim positioning without overclaiming

## Missing Items Before Journal Submission

### 1. Figures Needed

Required figures:

1. TRUST-Swarm overall architecture
2. Synthetic telemetry generation workflow
3. Graph-temporal window construction
4. Graph-Temporal Transformer model architecture
5. Training curves
6. Model comparison bar chart
7. Calibration / uncertainty figure
8. OOD attack performance figure
9. Feature-importance figure
10. PPO mission recovery workflow

### 2. References Needed

The manuscript needs 45–70 high-quality references.

Recommended reference categories:

1. UAV swarm mission assurance
2. UAV cyber-physical attacks
3. Jamming detection and anti-jamming
4. GPS spoofing detection
5. Telemetry tampering and UAV cybersecurity
6. Graph neural networks
7. Temporal transformers
8. Uncertainty calibration
9. OOD detection
10. Explainable AI
11. Reinforcement learning for autonomous recovery
12. High-confidence computing / trustworthy AI

### 3. Literature Gap Strengthening

The related work must clearly show that existing studies usually handle attack detection, graph learning, calibration, OOD, explainability, or recovery separately.

TRUST-Swarm should be positioned as an integrated framework combining:

* graph-temporal mission modeling
* uncertainty calibration
* OOD stress testing
* explainability
* recovery reasoning

### 4. Manuscript Polishing Needed

The full manuscript still needs:

* journal-style formatting
* citation insertion
* figure references
* table numbering
* equation formatting
* stronger transition sentences
* removal of repeated claims
* tighter academic tone
* final abstract polishing
* final conclusion polishing

### 5. Results Section Improvements

The results section should clearly state:

* CNN1D achieved the best in-distribution classification
* Graph-Temporal Transformer achieved strong calibrated performance
* TRUST-Swarm is not claimed as the best classifier
* TRUST-Swarm is claimed as a high-confidence mission-assurance framework
* OOD results reveal vulnerabilities under unseen attacks
* explainability results align with operational telemetry meaning

### 6. Risk Points to Avoid

Do not claim:

* Graph-Temporal Transformer beats all baselines
* OOD detection is perfect
* PPO recovery is fully operational
* synthetic telemetry equals field UAV data
* the framework is deployment-ready

Safe claims:

* TRUST-Swarm provides a controlled simulation-based trustworthy AI framework
* the model is strongly calibrated in-distribution
* OOD stress tests reveal mission-risk vulnerability
* feature importance identifies meaningful telemetry drivers
* recovery reasoning is demonstrated as a scaffold

### 7. Final Submission Package Needed

Before submission, prepare:

1. Final manuscript document
2. Figures folder
3. Tables folder
4. Reference list
5. Cover letter
6. Highlights
7. Declaration of competing interest
8. Data availability statement
9. Code availability statement
10. Ethical statement if required
11. Reviewer suggestion list if required

## Recommended Next Steps

1. Generate manuscript figures from result CSVs
2. Create final numbered tables
3. Add 45–70 references
4. Convert draft into journal-style Word document
5. Create cover letter and highlights
6. Run plagiarism/self-similarity check
7. Submit to the selected journal

## Final Positioning

TRUST-Swarm should be submitted as a trustworthy AI and high-confidence mission-assurance paper, not as a pure attack-classification paper.

The strongest contribution is the integrated evaluation pipeline combining graph-temporal AI, uncertainty calibration, OOD stress testing, explainability, and recovery reasoning for multi-UAV cyber-physical missions.


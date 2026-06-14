# TRUST-Swarm Citation Insertion Map — Information Fusion Update

## Purpose

This document updates the citation insertion strategy after adding Information Fusion candidate references [IF1]–[IF15].

The goal is to strengthen the manuscript’s Information Fusion framing and avoid presenting TRUST-Swarm as only a machine-learning classifier.

---

## 1. Introduction Citation Updates

### Multi-source mission telemetry fusion motivation

Use:

* [IF1], [IF2], [IF3], [IF4], [IF5]

Placement:

After the paragraph explaining that UAV swarm mission assurance depends on fusing communication, navigation, energy, mission-progress, and coverage telemetry.

Suggested citation sentence:

Multi-source mission-state estimation has long been studied in information-fusion research, where heterogeneous sensor and data streams are combined to improve situational awareness and decision reliability [IF1–IF5].

### High-level mission awareness and fusion architecture

Use:

* [IF6], [IF7], [IF8], [IF15]

Placement:

After the paragraph explaining that TRUST-Swarm is a mission-assurance framework rather than only a classifier.

Suggested citation sentence:

High-level information fusion frameworks emphasize the transformation of low-level measurements into decision-relevant mission awareness, which aligns with the TRUST-Swarm objective of converting distributed UAV telemetry into mission-assurance decisions [IF6–IF8, IF15].

---

## 2. Related Work Citation Updates

### New subsection needed

Add a stronger subsection titled:

**Multi-Source Information Fusion for Mission Awareness**

Use:

* [IF1] Hall and Llinas
* [IF2] Khaleghi et al.
* [IF3] Castanedo
* [IF4] Dasarathy
* [IF5] Handbook of Multisensor Data Fusion
* [IF6] High-Level Information Fusion
* [IF7] JDL model revisions
* [IF8] Multi-Sensor Data Fusion book
* [IF15] Context-enhanced information fusion

Purpose:

Support the claim that TRUST-Swarm belongs to the information-fusion literature, not only UAV cybersecurity or deep learning.

### Uncertainty-aware fusion subsection

Use:

* [IF9], [IF10], [IF11], [IF12]
* plus calibration references [18]–[24]

Purpose:

Support confidence-aware fusion, uncertainty-aware fusion, and conflict-aware fusion under degraded or adversarial information.

### Multi-source and multi-temporal fusion subsection

Use:

* [IF13], [IF14]

Purpose:

Support the use of multi-source and multi-temporal data fusion ideas.

---

## 3. Methodology Citation Updates

### Graph-temporal fusion-window construction

Use:

* [IF1], [IF2], [IF5], [IF13]
* plus graph-learning references [8]–[13]

Placement:

After explaining the tensor representation:

X ∈ R^(T × N × F)

Suggested citation sentence:

This graph-temporal fusion-window representation follows the broader information-fusion principle of combining heterogeneous data sources into a unified representation for downstream decision-making [IF1, IF2, IF5, IF13].

### Confidence-aware fusion calibration

Use:

* [IF9], [IF10], [IF11], [IF12]
* plus [18], [19], [20], [22], [24]

Placement:

After explaining ECE, Brier score, confidence, and entropy.

Suggested citation sentence:

The calibration layer extends the fusion pipeline with uncertainty-aware reliability assessment, consistent with uncertainty-aware and conflict-aware fusion principles [IF9–IF12, 18–24].

### Fusion-driver explainability

Use:

* [IF15]
* plus [29]–[32]

Placement:

After explaining perturbation-based feature importance.

Suggested citation sentence:

Fusion-driver explainability supports context-enhanced mission awareness by linking model decisions to operationally meaningful telemetry sources [IF15, 29–32].

---

## 4. Results and Discussion Citation Updates

### Model comparison discussion

Use mostly ML references:

* [14]–[17]

Do not overload this part with Information Fusion citations.

### Calibration discussion

Use:

* [IF9]–[IF12]
* [18]–[24]

Purpose:

Support the statement that confidence-aware fusion is necessary for high-confidence mission assurance.

### OOD discussion

Use:

* [22], [25]–[28], [54], [55]
* optionally [IF11], [IF12] for conflict-aware fusion under uncertainty

Purpose:

Support distribution-shift and adversarial uncertainty discussion.

### Explainability discussion

Use:

* [IF15]
* [29]–[32]

Purpose:

Support operational interpretation of fusion drivers.

---

## 5. Limitations and Future Work Citation Updates

### Synthetic telemetry limitation

Use:

* [IF1], [IF2], [IF5]
* UAV mission/security references [1], [2], [34]

Purpose:

Support the need for realistic multi-source fusion validation.

### Physics-aware graph construction future work

Use:

* graph references [8]–[13]
* fusion references [IF1], [IF2], [IF13]

Purpose:

Support future integration of dynamic communication graphs and multi-source telemetry fusion.

### Stronger OOD and uncertainty future work

Use:

* [IF9]–[IF12]
* [18]–[28]

Purpose:

Support uncertainty-aware and distribution-shift-aware fusion improvements.

---

## 6. Final Manuscript Citation Balance

Recommended final citation mix:

* UAV security / mission assurance: [1]–[7], [34]–[47]
* Information fusion: [IF1]–[IF15]
* Graph-temporal AI: [8]–[13]
* Temporal baselines: [14]–[17]
* Uncertainty / OOD: [18]–[28]
* Explainability: [29]–[32]
* Recovery / RL: [33], [48]–[53]
* Adversarial robustness: [54], [55]

## 7. Important Rule

Do not cite all Information Fusion references everywhere.

Use them mainly in:

1. Introduction framing
2. Related Work fusion subsection
3. Methodology fusion-window construction
4. Discussion framing

The final paper should look balanced, not citation-stuffed.

## 8. Final Audit Reminder

The `[IF1]–[IF15]` references are candidate references. Before final submission, verify:

* author order
* exact title
* publication venue
* year
* DOI
* publisher page
* relevance to cited claim


# TRUST-Swarm Journal Target Decision

## Purpose

This document compares possible journal targets for the TRUST-Swarm manuscript and recommends the safest submission strategy.

## Manuscript Title

TRUST-Swarm: Trustworthy Graph-Temporal AI for High-Confidence Multi-UAV Mission Assurance Under Cyber-Physical Attacks

## Manuscript Positioning

TRUST-Swarm should be positioned as a trustworthy AI and high-confidence mission-assurance framework for multi-UAV cyber-physical systems.

The paper should not be positioned as only a classifier paper.

Core strengths:

- graph-temporal AI framework
- uncertainty calibration
- OOD stress testing
- explainability
- recovery reasoning scaffold
- multi-UAV cyber-physical mission assurance
- three-seed simulation evaluation

Core risk:

- 1D-CNN outperforms Graph-Temporal Transformer on in-distribution classification
- dataset is synthetic
- references still need final audit
- PPO recovery is a scaffold, not a complete controller

---

## Option 1. Defence Technology

### Fit

Potentially strong if the paper is framed around defence mission assurance, contested UAV swarm operations, cyber-physical attack resilience, and simulation-based evaluation.

### Strengths

- Direct defence relevance
- UAV swarm resilience topic fits defence technology applications
- Cyber-physical attack framing is relevant
- Simulation-based applied investigation may fit

### Risks

- The journal may expect stronger defence novelty and deeper engineering realism
- Prior Defence Technology rejection risk exists if novelty is not made very clear
- Synthetic-only dataset may be challenged
- Need stronger defence-specific references and field-realistic simulation discussion

### Required improvements before submission

- Strengthen defence novelty
- Add more defence/UAV mission assurance references
- Improve architecture figures
- Emphasize contested environments
- Reduce generic AI language
- Make the contribution clearly different from RA-MARS

### Recommendation

Good but high-risk.

Submit here only after the manuscript is polished heavily and the novelty is sharpened.

---

## Option 2. Information Fusion

### Fit

Strong fit if TRUST-Swarm is reframed as a multi-source / multi-level information fusion framework for UAV mission assurance.

### Strengths

- Graph-temporal telemetry can be framed as multi-source UAV information fusion
- Calibration and uncertainty fit imperfect/incomplete information fusion
- OOD stress testing fits robust fusion under distribution shift
- Distributed UAV telemetry and cyber-physical mission awareness align well
- The paper can emphasize fusion of communication, navigation, energy, coverage, and mission-progress telemetry

### Risks

- Need stronger fusion language throughout manuscript
- Current paper says graph-temporal AI more than information fusion
- Need to add information-fusion references
- Need to present TRUST-Swarm as architecture + algorithm + application

### Required improvements before submission

- Add “multi-source telemetry fusion” wording
- Add information fusion references
- Rename parts of methodology to “graph-temporal mission information fusion”
- Add a figure showing fusion levels: UAV telemetry → graph-temporal fusion → confidence/OOD/explainability → recovery
- Emphasize imperfect, incomplete, adversarial, and distributed information

### Recommendation

Best high-impact target if we revise framing strongly.

---

## Option 3. Expert Systems with Applications

### Fit

Risky.

### Strengths

- AI application paper
- Expert/intelligent systems framing could fit generally
- Baselines, uncertainty, and explainability are application-oriented

### Major risk

ESWA currently states that it no longer considers papers containing applications to military/defense systems.

### Recommendation

Avoid for this manuscript unless all military/defense wording is removed and the paper is reframed as civilian UAV infrastructure assurance. Even then, it may still be risky because the manuscript currently uses defence-oriented mission-assurance framing.

---

## Option 4. IEEE Access

### Fit

Safe broad-scope option.

### Strengths

- Broad IEEE fields of interest
- Good fit for applied AI, UAVs, cyber-physical systems, communications, and trustworthy AI
- Faster and more practical submission path
- Public code repository helps reproducibility
- Less narrow than Defence Technology or Information Fusion

### Risks

- APC cost
- Need strong formatting and references
- Reviewers may still challenge synthetic-only evaluation
- Need to be honest about CNN baseline outperforming GTT

### Recommendation

Safest practical target.

---

## Recommended Submission Strategy

### Best prestige/high-impact route

1. Information Fusion  
2. Defence Technology  
3. IEEE Access  

### Best acceptance-probability route

1. IEEE Access  
2. Defence Technology  
3. Information Fusion  

### Journals to avoid for current version

1. Expert Systems with Applications  
2. Any journal that rejects military/defense applications  
3. Any journal requiring field UAV data only

---

## Final Recommendation

The strongest strategic path is:

### Primary target: Information Fusion

But only if the manuscript is revised as a graph-temporal multi-source information fusion framework for high-confidence UAV mission assurance.

### Backup target: IEEE Access

Use IEEE Access if we want a safer, faster, broader submission path.

### Defence Technology

Use Defence Technology only after strengthening defence novelty and making the paper much more engineering/mission-assurance focused.

---

## Action Plan Before Choosing Final Journal

1. Decide whether the paper should be defence-focused or information-fusion-focused.
2. If targeting Information Fusion, revise title and abstract to include multi-source mission telemetry fusion.
3. If targeting Defence Technology, revise title and abstract to emphasize contested defence UAV mission assurance.
4. If targeting IEEE Access, keep the broader trustworthy AI + UAV cyber-physical systems framing.
5. Do not target ESWA unless the paper is completely reframed away from military/defense applications.

## Current Best Choice

Information Fusion is the best high-impact target after reframing.

IEEE Access is the safest practical backup.

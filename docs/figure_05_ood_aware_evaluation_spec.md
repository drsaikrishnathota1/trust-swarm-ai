# Figure 5 OOD-Aware Mission Risk Evaluation Specification

## Figure Title

OOD-Aware Mission Risk Evaluation Pipeline

## Purpose

This figure should show how TRUST-Swarm evaluates model behavior under unseen cyber-physical attack shifts.

The goal is to show that TRUST-Swarm does not rely only on in-distribution accuracy. It also stress-tests fused mission-state predictions under OOD mission-risk conditions.

## Main Message

OOD-aware evaluation exposes mission-risk conditions where unseen cyber-physical shifts degrade prediction reliability.

## Figure Layout

Use a left-to-right academic pipeline.

### Block 1. In-Distribution Test Windows

Show standard graph-temporal fusion windows from the test set.

Label:

In-distribution graph-temporal fusion windows

### Block 2. OOD Perturbation Engine

Show a central perturbation module.

Label:

OOD cyber-physical stress generator

### Block 3. OOD Stress Scenarios

Show five OOD scenarios:

1. stealth jammer
2. slow GPS drift
3. intermittent tampering
4. delayed combined attack
5. unseen swarm noise

### Block 4. Graph-Temporal Fusion Model

Show the trained Graph-Temporal Transformer receiving OOD windows.

Label:

Trained graph-temporal fusion model

### Block 5. OOD Evaluation Metrics

Show metrics:

1. accuracy
2. macro F1
3. confidence
4. entropy
5. low-confidence rate

### Block 6. Mission-Risk Interpretation

Show risk interpretation:

* stable under in-distribution condition
* degraded under severe OOD shifts
* delayed combined attack: high-risk
* stealth jammer: high-risk
* slow GPS drift: high-risk
* intermittent tampering: moderate-risk

### Key Result Values

Include:

* in-distribution macro F1 = 0.8750
* intermittent tampering macro F1 = 0.5965
* slow GPS drift macro F1 = 0.1701
* stealth jammer macro F1 = 0.0779
* delayed combined attack macro F1 = 0.0521

## Visual Style

Use:

* clean white background
* blue/gray technical colors
* red/orange only for OOD risk indicators
* simple arrows
* OOD stress icons
* small bar chart icon for performance degradation
* academic labels

Avoid:

* dramatic attack imagery
* too much red
* crowded numbers
* cinematic effects

## Diagram Prompt

Create a clean academic research diagram titled “OOD-Aware Mission Risk Evaluation Pipeline.”

Use a left-to-right pipeline. Start with in-distribution graph-temporal fusion windows from the test set. Then show an OOD cyber-physical stress generator that creates unseen stress scenarios: stealth jammer, slow GPS drift, intermittent tampering, delayed combined attack, and unseen swarm noise.

Next, show the trained Graph-Temporal Transformer receiving the OOD windows. Then show evaluation metrics: accuracy, macro F1, confidence, entropy, and low-confidence rate. On the right, show a mission-risk interpretation block that compares in-distribution performance with degraded OOD performance.

Include key macro F1 values: in-distribution = 0.8750, intermittent tampering = 0.5965, slow GPS drift = 0.1701, stealth jammer = 0.0779, delayed combined attack = 0.0521. Use a clean white-background academic style, blue and gray palette, limited red/orange for risk indicators, readable labels, and clear arrows.


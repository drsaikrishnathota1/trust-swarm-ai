# TRUST-Swarm Information Fusion Reframing Plan

## Purpose

This document explains how to reframe TRUST-Swarm for a stronger Information Fusion-style submission.

The current manuscript is framed mainly as graph-temporal trustworthy AI for UAV mission assurance. For Information Fusion, the manuscript should be reframed as a multi-source, graph-temporal mission telemetry fusion framework for high-confidence UAV swarm assurance under cyber-physical attacks.

## Recommended Reframed Title

TRUST-Swarm: Trustworthy Graph-Temporal Multi-Source Information Fusion for High-Confidence UAV Swarm Mission Assurance Under Cyber-Physical Attacks

## Core Reframing Idea

Instead of presenting TRUST-Swarm only as an AI classifier, present it as a mission information-fusion framework.

The framework fuses multiple telemetry streams:

* communication telemetry
* navigation telemetry
* energy telemetry
* mission-progress telemetry
* coverage telemetry
* cyber-physical attack indicators
* uncertainty signals
* explainability signals
* recovery-state indicators

## New Central Claim

TRUST-Swarm provides a trustworthy graph-temporal information-fusion framework that integrates distributed UAV telemetry, calibrated confidence, OOD stress testing, explainability, and recovery reasoning for high-confidence mission assurance.

## Language Changes Needed

Replace or reduce:

* “attack classifier”
* “classification model”
* “Graph-Temporal Transformer outperforms”
* “AI model for UAV attacks”

Use more:

* “multi-source mission telemetry fusion”
* “graph-temporal fusion”
* “distributed UAV information”
* “mission-state fusion”
* “confidence-aware fusion”
* “OOD-aware fusion”
* “trustworthy information fusion”
* “cyber-physical mission awareness”
* “fusion of communication, navigation, coverage, energy, and mission-progress signals”

## Abstract Changes Needed

The abstract should emphasize:

1. UAV swarms generate distributed, heterogeneous telemetry.
2. Mission assurance requires fusing communication, navigation, energy, coverage, and mission-progress signals.
3. Cyber-physical attacks corrupt or distort these information streams.
4. TRUST-Swarm performs graph-temporal multi-source telemetry fusion.
5. Calibration, OOD testing, explainability, and recovery reasoning support high-confidence fusion.
6. The framework is not only a classifier.

## Introduction Changes Needed

Add a stronger information-fusion motivation:

Multi-UAV mission assurance depends on fusing heterogeneous and distributed information streams. A single telemetry variable rarely provides enough evidence to determine mission risk. Communication latency, packet loss, GPS displacement, route deviation, energy depletion, coverage reduction, and mission-progress disruption must be interpreted jointly over time and across UAV nodes.

Then state the gap:

Existing UAV security studies often detect individual attack types but do not fully integrate graph-temporal multi-source telemetry fusion with uncertainty calibration, OOD stress testing, explainability, and recovery reasoning.

## Methodology Changes Needed

Rename methodology components:

* Synthetic telemetry generation → Multi-source mission telemetry generation
* Graph-window construction → Graph-temporal fusion-window construction
* Graph-Temporal Transformer → Graph-temporal fusion model
* Uncertainty calibration → Confidence-aware fusion calibration
* OOD stress testing → Distribution-shift-aware fusion evaluation
* Explainability → Fusion-driver explainability
* PPO recovery → Recovery-oriented mission fusion reasoning

## Results Changes Needed

Do not focus only on model ranking.

Instead, organize results around fusion questions:

1. Can graph-temporal fusion classify mission state?
2. How does it compare with temporal baselines?
3. Is the fused prediction calibrated?
4. How does fusion behave under unseen cyber-physical shifts?
5. Which telemetry sources drive the fused decision?
6. How can fused mission state support recovery reasoning?

## Figures Needed for Information Fusion Framing

Required new figures:

1. Multi-source UAV telemetry fusion architecture
2. Graph-temporal fusion-window construction
3. Confidence-aware fusion pipeline
4. OOD-aware mission-risk evaluation pipeline
5. Fusion-driver explainability figure
6. Recovery-oriented fusion decision loop

## Tables Needed for Information Fusion Framing

Required tables:

1. Multi-source telemetry categories
2. Fusion input features and mission meaning
3. Model comparison
4. Calibration metrics
5. OOD fusion stress-test results
6. Feature/fusion-driver importance
7. Safe claim-positioning table

## References Needed

Add references in these categories:

1. Information fusion theory
2. Multi-sensor data fusion
3. Distributed sensor fusion
4. Uncertainty-aware fusion
5. Information fusion under adversarial conditions
6. UAV sensor fusion
7. Cyber-physical information fusion
8. Trustworthy AI for fusion systems

## Risk to Avoid

Do not oversell the current model as a complete fusion system if the implementation is still mainly graph-temporal telemetry modeling.

Safe wording:

“TRUST-Swarm operationalizes mission telemetry fusion through graph-temporal windows that combine communication, navigation, energy, coverage, and mission-progress signals.”

Avoid wording:

“TRUST-Swarm fully solves UAV information fusion under all cyber-physical attack conditions.”

## Best Final Positioning

TRUST-Swarm should be positioned as:

A simulation-based trustworthy graph-temporal information-fusion framework for UAV swarm mission assurance that combines multi-source telemetry fusion, calibrated confidence, OOD stress testing, explainability, and recovery reasoning.

## Action Items

1. Rewrite abstract with information-fusion framing.
2. Rewrite introduction with multi-source telemetry fusion motivation.
3. Update methodology terminology.
4. Add an Information Fusion-specific architecture figure.
5. Add 8–12 information-fusion references.
6. Keep the CNN baseline result honest.
7. Emphasize TRUST-Swarm as a framework, not only a model.
8. Prepare IEEE Access backup version if Information Fusion scope becomes too demanding.


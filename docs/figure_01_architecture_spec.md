# Figure 1 Architecture Specification

## Figure Title

TRUST-Swarm Overall Multi-Source Information Fusion Architecture

## Purpose

This figure should show TRUST-Swarm as a trustworthy graph-temporal multi-source information fusion framework for UAV swarm mission assurance under cyber-physical attacks.

The figure should make clear that TRUST-Swarm is not only a classifier. It is a full mission-assurance pipeline that fuses distributed telemetry, predicts mission state, evaluates confidence, tests OOD behavior, explains fusion drivers, and supports recovery reasoning.

## Figure Layout

Use a left-to-right pipeline.

### Block 1. Multi-UAV Swarm Mission Environment

Show:

* UAV swarm
* mission area
* cyber-physical threats

Threat labels:

* Jamming
* GPS spoofing
* Telemetry tampering
* Combined attacks

### Block 2. Multi-Source Mission Telemetry

Show five telemetry streams:

1. Communication telemetry

   * packet loss
   * latency

2. Navigation telemetry

   * route deviation
   * GPS jump
   * velocity inconsistency

3. Energy telemetry

   * battery level
   * energy consumption

4. Mission-progress telemetry

   * mission progress

5. Coverage telemetry

   * zone coverage

### Block 3. Graph-Temporal Fusion Window

Show telemetry converted into:

X ∈ R^(T × N × F)

Include final experiment values:

* T = 20 timesteps
* N = 20 UAVs
* F = 9 features

### Block 4. Graph-Temporal Transformer

Show internal modules:

1. feature projection
2. UAV-node attention
3. temporal transformer encoder
4. fused mission embedding
5. mission-state classifier

Output classes:

* normal
* jamming
* spoofing
* tampering
* combined attacks

### Block 5. Trustworthy AI Layer

Show three submodules:

1. Confidence-aware calibration

   * ECE
   * Brier score
   * confidence
   * entropy

2. OOD-aware stress testing

   * stealth jammer
   * slow GPS drift
   * intermittent tampering
   * delayed combined attack
   * unseen swarm noise

3. Fusion-driver explainability

   * latency
   * zone coverage
   * route deviation
   * mission progress
   * GPS jump

### Block 6. Recovery-Oriented Mission Assurance

Show PPO recovery reasoning with actions:

* continue
* monitor
* reroute
* reassign
* isolate node
* return to base

Final output:

High-confidence UAV swarm mission assurance decision

## Visual Style

Use a clean academic style.

Recommended style:

* white background
* blue/gray technical color palette
* simple icons
* arrows between blocks
* readable text
* no cinematic effects
* no crowded labels
* no exaggerated 3D graphics

## Diagram Prompt for Image/Diagram Tool

Create a clean academic research architecture diagram titled “TRUST-Swarm: Graph-Temporal Multi-Source Information Fusion for UAV Swarm Mission Assurance.”

Use a left-to-right pipeline layout. On the far left, show a multi-UAV swarm mission environment with cyber-physical threats labeled jamming, GPS spoofing, telemetry tampering, and combined attacks. Next, show multi-source mission telemetry streams: communication telemetry, navigation telemetry, energy telemetry, mission-progress telemetry, and coverage telemetry. Then show graph-temporal fusion-window construction with notation X ∈ R^(T × N × F), where T = 20 timesteps, N = 20 UAVs, and F = 9 features.

Next, show a Graph-Temporal Transformer block with feature projection, UAV-node attention, temporal transformer encoder, fused mission embedding, and mission-state classifier. Then show a trustworthy AI layer with confidence-aware calibration, OOD-aware stress testing, and fusion-driver explainability. Finally, show a recovery-oriented mission-assurance block using PPO recovery reasoning with possible actions: continue, monitor, reroute, reassign, isolate node, and return to base.

Use a clean white-background academic style, blue and gray color palette, simple vector icons, readable labels, and clear arrows. The figure should look suitable for a journal paper on information fusion and trustworthy AI.


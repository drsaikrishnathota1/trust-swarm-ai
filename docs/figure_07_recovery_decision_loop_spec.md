# Figure 7 Recovery-Oriented Fusion Decision Loop Specification

## Figure Title

Recovery-Oriented Fusion Decision Loop

## Purpose

This figure should show how TRUST-Swarm connects fused mission-state predictions, uncertainty signals, and mission-risk indicators to recovery-oriented decision support.

The goal is to explain that TRUST-Swarm is not only a prediction model. It also provides a pathway from trustworthy information fusion to mission-assurance actions.

## Main Message

TRUST-Swarm links graph-temporal fusion outputs to recovery reasoning so that UAV swarm missions can respond to cyber-physical risk conditions.

## Figure Layout

Use a circular or left-to-right feedback-loop diagram.

### Block 1. Graph-Temporal Fusion Output

Show outputs from the Graph-Temporal Transformer:

1. predicted mission state
2. class probability
3. confidence score
4. predictive entropy

Mission states:

* normal
* jamming
* spoofing
* tampering
* combined attacks

### Block 2. Mission-Risk Assessment

Show risk indicators:

1. communication degradation
2. navigation disruption
3. coverage loss
4. mission-progress disruption
5. energy stress
6. OOD warning

### Block 3. PPO Recovery Policy

Show PPO recovery reasoning.

Label:

PPO-based recovery policy

Inputs:

* mission-state prediction
* confidence
* entropy
* mission-risk indicators

### Block 4. Recovery Action Space

Show possible actions:

1. continue
2. monitor
3. reroute
4. reassign
5. isolate node
6. return to base

### Block 5. Mission-Assurance Decision

Show final decision:

High-confidence mission-assurance action

### Block 6. Updated Mission State

Show feedback arrow back to telemetry stream.

Label:

Updated UAV swarm telemetry

This closes the decision loop.

## Visual Style

Use:

* clean white background
* blue/gray technical colors
* limited orange for risk
* simple UAV icon
* policy/decision icon
* circular feedback arrow
* readable labels

Avoid:

* dramatic combat visuals
* cinematic effects
* too much red
* claiming deployment-ready control
* crowded reinforcement-learning details

## Important Caption Note

The figure caption should clearly state that the PPO module is a recovery-reasoning scaffold, not a deployment-ready UAV controller.

## Diagram Prompt

Create a clean academic research diagram titled “Recovery-Oriented Fusion Decision Loop.”

Show a mission-assurance feedback loop. Start with graph-temporal fusion outputs from the Graph-Temporal Transformer: predicted mission state, class probability, confidence score, and predictive entropy. Then show a mission-risk assessment block with communication degradation, navigation disruption, coverage loss, mission-progress disruption, energy stress, and OOD warning.

Next, show a PPO-based recovery policy block that receives mission-state prediction, confidence, entropy, and mission-risk indicators. Then show the recovery action space with six actions: continue, monitor, reroute, reassign, isolate node, and return to base. Then show a high-confidence mission-assurance decision block. Finally, show an updated UAV swarm telemetry block with a feedback arrow returning to the graph-temporal fusion pipeline.

Use a clean white-background academic style, blue and gray technical palette, limited orange for risk indicators, simple vector icons, readable labels, and clear arrows. Make the figure suitable for a journal paper on trustworthy information fusion and UAV swarm mission assurance. Do not make it look like a cinematic or military poster.


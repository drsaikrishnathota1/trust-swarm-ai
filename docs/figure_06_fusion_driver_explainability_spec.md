# Figure 6 Fusion-Driver Explainability Specification

## Figure Title

Fusion-Driver Explainability Workflow

## Purpose

This figure should show how TRUST-Swarm identifies which telemetry sources most influence the fused mission-state prediction.

The goal is to explain the perturbation-based feature-importance method used in the manuscript.

## Main Message

TRUST-Swarm explains graph-temporal fusion decisions by measuring how much model performance drops when each telemetry feature is perturbed.

## Figure Layout

Use a left-to-right academic workflow.

### Block 1. Baseline Test Set

Show graph-temporal fusion test windows.

Label:

Baseline graph-temporal test set

### Block 2. Baseline Performance

Show baseline macro F1 before perturbation.

Label:

Baseline macro F1

### Block 3. Feature Perturbation

Show one telemetry feature being replaced by its mean value.

Label:

Perturb one telemetry feature at a time

Feature groups:

1. Communication

   * packet_loss_rate
   * latency_ms

2. Navigation

   * route_deviation_m
   * gps_jump_m
   * velocity_inconsistency

3. Energy

   * battery_level
   * energy_consumption

4. Mission progress

   * mission_progress

5. Coverage

   * zone_coverage

### Block 4. Re-Evaluate Model

Show the trained Graph-Temporal Transformer being evaluated after perturbation.

Label:

Recompute macro F1 after perturbation

### Block 5. Macro-F1 Drop

Show formula:

Feature importance = baseline macro F1 − perturbed macro F1

### Block 6. Ranked Fusion Drivers

Show top drivers:

1. latency_ms
2. zone_coverage
3. route_deviation_m
4. mission_progress
5. gps_jump_m

### Block 7. Mission Interpretation

Show operational meanings:

* latency_ms → communication degradation
* zone_coverage → mission coverage loss
* route_deviation_m → navigation disruption
* mission_progress → mission completion disruption
* gps_jump_m → spoofing-related displacement

## Visual Style

Use:

* clean white background
* blue/gray academic colors
* simple feature icons
* perturbation arrow
* ranked bar-list icon
* clear arrows
* readable labels

Avoid:

* too much math
* too many feature names inside one block
* cinematic effects
* crowded layout

## Diagram Prompt

Create a clean academic research diagram titled “Fusion-Driver Explainability Workflow.”

Use a left-to-right workflow. Start with baseline graph-temporal fusion test windows. Then show baseline macro F1 measurement. Next, show feature perturbation where one telemetry feature at a time is replaced by its mean value. Group the telemetry features into communication, navigation, energy, mission progress, and coverage.

Then show the trained Graph-Temporal Transformer being re-evaluated after perturbation. Next, show the feature-importance formula: feature importance = baseline macro F1 − perturbed macro F1. On the right, show ranked fusion drivers: latency_ms, zone_coverage, route_deviation_m, mission_progress, and gps_jump_m. Add mission interpretations: latency means communication degradation, zone coverage means mission coverage loss, route deviation means navigation disruption, mission progress means mission completion disruption, and GPS jump means spoofing-related displacement.

Use a clean white-background academic style, blue and gray technical palette, simple vector icons, readable labels, and clear arrows. The figure should look suitable for a journal paper on trustworthy information fusion and UAV swarm mission assurance.


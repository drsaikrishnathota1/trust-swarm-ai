# Figure 2 Fusion-Window Construction Specification

## Figure Title

Graph-Temporal Fusion-Window Construction

## Purpose

This figure should show how raw multi-UAV telemetry is transformed into graph-temporal fusion windows for TRUST-Swarm.

The goal is to make clear that TRUST-Swarm fuses telemetry across:

1. Mission time
2. UAV nodes
3. Multiple telemetry features

## Main Message

Raw UAV telemetry is converted into a structured graph-temporal tensor:

X ∈ R^(T × N × F)

where:

* T = temporal window length
* N = number of UAV nodes
* F = number of telemetry features

Final experiment values:

* T = 20 timesteps
* N = 20 UAVs
* F = 9 features

## Figure Layout

Use a left-to-right academic diagram.

### Block 1. Raw Multi-UAV Telemetry

Show a table-like telemetry stream with columns:

* mission_id
* timestep
* uav_id
* packet_loss_rate
* latency_ms
* route_deviation_m
* gps_jump_m
* velocity_inconsistency
* battery_level
* mission_progress
* zone_coverage
* energy_consumption
* attack_label

### Block 2. Temporal Sliding Window

Show a sliding window moving across mission time.

Label:

Window length T = 20 timesteps

### Block 3. UAV Node Structure

Show 20 UAV nodes inside each window.

Label:

N = 20 UAV nodes

### Block 4. Multi-Source Telemetry Features

Show feature channels grouped into:

1. Communication

   * packet loss
   * latency

2. Navigation

   * route deviation
   * GPS jump
   * velocity inconsistency

3. Energy

   * battery level
   * energy consumption

4. Mission progress

   * mission progress

5. Coverage

   * zone coverage

Label:

F = 9 telemetry features

### Block 5. Graph-Temporal Fusion Tensor

Show final tensor:

X ∈ R^(20 × 20 × 9)

Label:

Graph-temporal fusion window used for mission-state prediction

### Block 6. Mission-State Label

Show output label:

* normal
* jamming
* spoofing
* tampering
* combined attack states

## Visual Style

Use:

* clean white background
* blue/gray technical colors
* table icon for raw telemetry
* sliding window icon
* UAV-node graph icon
* tensor/cube icon
* clear arrows
* readable academic labels

Avoid:

* cinematic style
* crowded text
* 3D dramatic graphics
* too many colors

## Diagram Prompt

Create a clean academic research diagram titled “Graph-Temporal Fusion-Window Construction.”

Use a left-to-right pipeline. On the left, show raw multi-UAV telemetry as a table with mission time, UAV ID, communication features, navigation features, energy features, mission-progress features, coverage features, and attack label. Next, show a temporal sliding window with length T = 20 timesteps. Then show UAV node structure with N = 20 UAV nodes. Then show grouped multi-source telemetry features: communication, navigation, energy, mission progress, and coverage.

On the right, show the final graph-temporal fusion tensor with notation X ∈ R^(T × N × F), and include final experiment values X ∈ R^(20 × 20 × 9). Add a final mission-state label output showing normal, jamming, spoofing, tampering, and combined attack states.

Use a clean white-background academic style, blue and gray color palette, simple vector icons, readable labels, and clear arrows. The figure should look suitable for a journal paper on information fusion and trustworthy UAV swarm mission assurance.


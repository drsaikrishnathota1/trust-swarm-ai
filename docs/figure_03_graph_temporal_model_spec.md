# Figure 3 Graph-Temporal Fusion Model Architecture Specification

## Figure Title

Graph-Temporal Fusion Model Architecture

## Purpose

This figure should show the internal TRUST-Swarm Graph-Temporal Transformer pipeline.

The goal is to explain how a graph-temporal fusion window is processed into a mission-state prediction.

## Main Message

The model learns both:

1. UAV-node relationships
2. Mission-time evolution

from fused multi-source UAV telemetry.

## Figure Layout

Use a left-to-right academic model architecture diagram.

### Block 1. Input Graph-Temporal Fusion Window

Show input tensor:

X ∈ R^(T × N × F)

Final experiment values:

X ∈ R^(20 × 20 × 9)

Meaning:

* T = 20 timesteps
* N = 20 UAV nodes
* F = 9 telemetry features

### Block 2. Feature Projection

Show a neural layer converting raw telemetry features into hidden embeddings.

Label:

Telemetry Feature Projection

Input:

9 telemetry features

Output:

hidden feature embedding

### Block 3. UAV-Node Attention

Show attention across UAV nodes.

Label:

UAV-Node Attention

Purpose:

Learns relationships among UAV nodes within each temporal window.

### Block 4. Temporal Transformer Encoder

Show transformer layers across mission time.

Label:

Temporal Transformer Encoder

Purpose:

Learns mission evolution, attack progression, and temporal degradation patterns.

### Block 5. Fused Mission Embedding

Show a compact representation vector.

Label:

Graph-Temporal Mission Embedding

Purpose:

Combines node-level and temporal mission-state information.

### Block 6. Mission-State Classifier

Show classifier layer.

Output classes:

* normal
* jamming
* spoofing
* tampering
* jamming-spoofing
* jamming-tampering
* spoofing-tampering
* combined attack

### Block 7. Output Probabilities

Show softmax probability output.

Label:

Mission-State Probabilities

## Visual Style

Use:

* clean academic style
* white background
* blue/gray color palette
* neural network blocks
* attention icon
* transformer encoder icon
* simple arrows
* readable labels

Avoid:

* too much text
* cinematic effects
* dark background
* overloaded neural network details

## Diagram Prompt

Create a clean academic model architecture diagram titled “Graph-Temporal Fusion Model Architecture.”

Use a left-to-right pipeline. Start with an input graph-temporal fusion tensor labeled X ∈ R^(T × N × F), with final experiment values X ∈ R^(20 × 20 × 9), where T = 20 timesteps, N = 20 UAV nodes, and F = 9 telemetry features.

Next show a telemetry feature projection block that converts raw telemetry features into hidden embeddings. Then show a UAV-node attention block that learns relationships among UAV nodes. Then show a temporal transformer encoder block that learns mission evolution and attack progression across time. Then show a fused graph-temporal mission embedding. Finally, show a mission-state classifier outputting probabilities for normal, jamming, spoofing, tampering, jamming-spoofing, jamming-tampering, spoofing-tampering, and combined attack.

Use a clean white-background academic style, blue and gray technical palette, simple vector blocks, readable labels, and clear arrows. The figure should look suitable for a journal paper on graph-temporal information fusion and trustworthy UAV swarm mission assurance.


# Figure 4 Confidence-Aware Fusion Pipeline Specification

## Figure Title

Confidence-Aware Fusion Pipeline

## Purpose

This figure should show how TRUST-Swarm evaluates whether a fused mission-state prediction is reliable.

The goal is to explain that TRUST-Swarm does not only output a class label. It also estimates confidence, entropy, calibration error, and probabilistic reliability.

## Main Message

TRUST-Swarm supports high-confidence UAV swarm mission assurance by evaluating the trustworthiness of graph-temporal fusion predictions.

## Figure Layout

Use a left-to-right academic pipeline.

### Block 1. Graph-Temporal Fusion Window

Show input:

X ∈ R^(20 × 20 × 9)

Meaning:

* 20 timesteps
* 20 UAV nodes
* 9 telemetry features

### Block 2. Graph-Temporal Fusion Model

Show the Graph-Temporal Transformer producing mission-state probabilities.

Label:

Graph-Temporal Transformer

Output:

class probability distribution

### Block 3. Monte Carlo Dropout Inference

Show repeated stochastic inference.

Label:

MC Dropout Inference

Include:

* 20 stochastic samples
* probability averaging
* uncertainty estimation

### Block 4. Prediction Outputs

Show:

1. predicted mission state
2. class probability
3. confidence score
4. predictive entropy

### Block 5. Calibration Metrics

Show calibration evaluation:

1. Expected Calibration Error
2. Brier score
3. mean confidence
4. mean entropy

Final reported values:

* ECE = 0.0088
* Brier score = 0.0531
* mean confidence = 0.9601
* mean entropy = 0.0986

### Block 6. Mission-Assurance Trust Decision

Show decision options:

1. trust prediction
2. monitor closely
3. escalate for review
4. trigger recovery reasoning

## Visual Style

Use:

* clean white background
* blue/gray palette
* simple model block
* probability bars
* uncertainty gauge icon
* calibration meter icon
* clear arrows
* academic diagram style

Avoid:

* crowded equations
* cinematic graphics
* too many colors
* large paragraphs inside the figure

## Diagram Prompt

Create a clean academic research diagram titled “Confidence-Aware Fusion Pipeline.”

Use a left-to-right pipeline. Start with a graph-temporal fusion window labeled X ∈ R^(20 × 20 × 9), representing 20 timesteps, 20 UAV nodes, and 9 telemetry features. Then show a Graph-Temporal Transformer block producing mission-state class probabilities. Next, show Monte Carlo dropout inference with 20 stochastic samples and probability averaging.

Then show prediction outputs: predicted mission state, class probability, confidence score, and predictive entropy. Next, show calibration metrics: Expected Calibration Error, Brier score, mean confidence, and mean entropy. Include final reported values: ECE = 0.0088, Brier score = 0.0531, mean confidence = 0.9601, and mean entropy = 0.0986.

On the right, show a mission-assurance trust decision block with options: trust prediction, monitor closely, escalate for review, or trigger recovery reasoning. Use a clean white-background academic style, blue and gray technical palette, simple vector icons, readable labels, and clear arrows.


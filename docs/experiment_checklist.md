# TRUST-Swarm Experiment Checklist

## Baseline Import

- [ ] RA-MARS baseline CSVs copied or referenced.
- [ ] LSTM baseline recorded.
- [ ] GRU baseline recorded.
- [ ] 1D-CNN baseline recorded.
- [ ] MAI, mission success, recovery time, and detection delay recorded.

## Graph Dataset

- [ ] Graph nodes are UAVs.
- [ ] Node features are 9 raw telemetry fields.
- [ ] Time window is 20 steps.
- [ ] Edges include distance, SINR similarity, zone overlap, or shared attack exposure.
- [ ] Train/validation/test split is run-level safe.
- [ ] OOD set is separated from training.

## Models

- [ ] GAT-LSTM trained.
- [ ] Graph Transformer trained.
- [ ] Graph-Temporal Transformer trained.
- [ ] Baseline comparison table generated.

## Uncertainty

- [ ] MC dropout enabled.
- [ ] Expected Calibration Error computed.
- [ ] Brier score computed.
- [ ] Reliability diagram generated.
- [ ] OOD confidence shift measured.

## OOD Testing

- [ ] Stealth jammer tested.
- [ ] Slow GPS drift tested.
- [ ] Intermittent tampering tested.
- [ ] Unseen jammer location tested.
- [ ] Delayed combined attack tested.
- [ ] Unseen swarm size tested.

## Explainability

- [ ] Feature-importance heatmap generated.
- [ ] UAV-node attention heatmap generated.
- [ ] Attack-specific explanation examples generated.

## DRL Recovery

- [ ] PPO environment defined.
- [ ] PPO policy trained.
- [ ] Compared against deterministic action selector.
- [ ] Mission success and recovery time reported.

## Manuscript Readiness

- [ ] New title finalized.
- [ ] New abstract drafted.
- [ ] Contribution matrix completed.
- [ ] New figures created.
- [ ] New results tables created.
- [ ] Duplicate-overlap risk checked against RA-MARS.

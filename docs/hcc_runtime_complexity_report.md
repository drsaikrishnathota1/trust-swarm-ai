# HCC Runtime and Complexity Report

This report summarizes runtime and complexity profiling for TRUST-Swarm models.

## Environment

- Python: 3.14.4
- Platform: macOS-26.5.1-arm64-arm-64bit-Mach-O
- PyTorch: 2.12.0
- Device: mps
- CUDA available: False

## Profiling Configuration

- Batch size: 32
- Window size: 20
- UAV nodes: 20
- Telemetry features: 9
- Classes: 8
- Warmup iterations: 3
- Timed inference iterations: 5

## Runtime and Complexity Table

| Model | Params | Size MB | Batch latency ms | Sample latency ms | Throughput windows/s | Train step ms | Device |
|---|---:|---:|---:|---:|---:|---:|---|
| LSTM | 308616 | 1.182 | 0.578 | 0.018059 | 55375.297 | 3.904 | mps |
| GRU | 235912 | 0.905 | 2.565 | 0.080146 | 12477.214 | 11.548 | mps |
| CNN1D | 136840 | 0.531 | 0.269 | 0.008418 | 118797.208 | 2.691 | mps |
| GraphTemporalTransformer | 680840 | 2.617 | 1.515 | 0.047355 | 21117.002 | 19.14 | mps |

## Manuscript Use

Use this table in the HCC manuscript to support practical feasibility. For final submission, rerun this profiler on the same RunPod GPU used for the final experiment.
# HCC Runtime and Complexity Report

This report summarizes runtime and complexity profiling for TRUST-Swarm models.

## Environment

- Python: 3.11.10
- Platform: Linux-6.8.0-53-generic-x86_64-with-glibc2.35
- PyTorch: 2.11.0+cu128
- Device: cuda
- CUDA available: True
- GPU: NVIDIA H200

## Profiling Configuration

- Batch size: 128
- Window size: 20
- UAV nodes: 20
- Telemetry features: 9
- Classes: 8
- Warmup iterations: 10
- Timed inference iterations: 50

## Runtime and Complexity Table

| Model | Params | Size MB | Batch latency ms | Sample latency ms | Throughput windows/s | Train step ms | Device |
|---|---:|---:|---:|---:|---:|---:|---|
| LSTM | 308616 | 1.181 | 0.214 | 0.001669 | 599006.617 | 1.674 | cuda |
| GRU | 235912 | 0.904 | 0.177 | 0.001381 | 724111.11 | 1.48 | cuda |
| CNN1D | 136840 | 0.531 | 0.211 | 0.001647 | 606987.446 | 1.465 | cuda |
| GraphTemporalTransformer | 680840 | 2.618 | 2.267 | 0.017712 | 56458.364 | 9.938 | cuda |

## Manuscript Use

Use this table in the HCC manuscript to support practical feasibility. For final submission, rerun this profiler on the same RunPod GPU used for the final experiment.
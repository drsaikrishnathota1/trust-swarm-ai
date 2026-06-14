#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import platform
import tempfile
import time
from pathlib import Path

import torch
import torch.nn as nn

from trust_swarm.models.baseline_temporal import LSTMBaseline, GRUBaseline, CNN1DBaseline
from trust_swarm.models.graph_temporal_transformer import GraphTemporalTransformer


def pick_device(device_arg: str) -> torch.device:
    if device_arg != "auto":
        return torch.device(device_arg)
    if torch.cuda.is_available():
        return torch.device("cuda")
    if hasattr(torch.backends, "mps") and torch.backends.mps.is_available():
        return torch.device("mps")
    return torch.device("cpu")


def count_parameters(model: nn.Module) -> int:
    return sum(p.numel() for p in model.parameters() if p.requires_grad)


def model_size_mb(model: nn.Module) -> float:
    with tempfile.NamedTemporaryFile(suffix=".pt", delete=True) as tmp:
        torch.save(model.state_dict(), tmp.name)
        return Path(tmp.name).stat().st_size / (1024 * 1024)


def sync(device: torch.device) -> None:
    if device.type == "cuda":
        torch.cuda.synchronize()


def profile_model(
    name: str,
    model: nn.Module,
    device: torch.device,
    batch_size: int,
    window_size: int,
    num_uavs: int,
    num_features: int,
    num_classes: int,
    warmup: int,
    iters: int,
) -> dict:
    model = model.to(device)
    model.eval()

    x = torch.randn(batch_size, window_size, num_uavs, num_features, device=device)
    y = torch.randint(0, num_classes, (batch_size,), device=device)
    criterion = nn.CrossEntropyLoss()

    # Inference warmup
    with torch.inference_mode():
        for _ in range(warmup):
            _ = model(x)
    sync(device)

    # Inference timing
    start = time.perf_counter()
    with torch.inference_mode():
        for _ in range(iters):
            _ = model(x)
    sync(device)
    elapsed = time.perf_counter() - start

    batch_latency_ms = (elapsed / iters) * 1000
    sample_latency_ms = batch_latency_ms / batch_size
    throughput = batch_size / (batch_latency_ms / 1000)

    # One training step timing
    model.train()
    optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)

    for _ in range(max(1, warmup // 2)):
        optimizer.zero_grad(set_to_none=True)
        loss = criterion(model(x), y)
        loss.backward()
        optimizer.step()
    sync(device)

    start = time.perf_counter()
    optimizer.zero_grad(set_to_none=True)
    loss = criterion(model(x), y)
    loss.backward()
    optimizer.step()
    sync(device)
    train_step_ms = (time.perf_counter() - start) * 1000

    gpu_memory_mb = ""
    if device.type == "cuda":
        gpu_memory_mb = round(torch.cuda.max_memory_allocated(device) / (1024 * 1024), 3)

    return {
        "model": name,
        "parameters": count_parameters(model),
        "model_size_mb": round(model_size_mb(model), 3),
        "batch_size": batch_size,
        "window_size": window_size,
        "num_uavs": num_uavs,
        "num_features": num_features,
        "inference_batch_latency_ms": round(batch_latency_ms, 3),
        "inference_sample_latency_ms": round(sample_latency_ms, 6),
        "throughput_windows_per_second": round(throughput, 3),
        "single_train_step_ms": round(train_step_ms, 3),
        "device": str(device),
        "gpu_memory_mb": gpu_memory_mb,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--batch-size", type=int, default=128)
    parser.add_argument("--window-size", type=int, default=20)
    parser.add_argument("--num-uavs", type=int, default=20)
    parser.add_argument("--num-features", type=int, default=9)
    parser.add_argument("--num-classes", type=int, default=8)
    parser.add_argument("--hidden-dim", type=int, default=128)
    parser.add_argument("--warmup", type=int, default=10)
    parser.add_argument("--iters", type=int, default=50)
    parser.add_argument("--device", default="auto")
    parser.add_argument("--out-csv", default="results/hcc/runtime_complexity_summary.csv")
    parser.add_argument("--out-md", default="docs/hcc_runtime_complexity_report.md")
    args = parser.parse_args()

    device = pick_device(args.device)

    models = {
        "LSTM": LSTMBaseline(
            num_uavs=args.num_uavs,
            num_features=args.num_features,
            hidden_dim=args.hidden_dim,
            num_classes=args.num_classes,
        ),
        "GRU": GRUBaseline(
            num_uavs=args.num_uavs,
            num_features=args.num_features,
            hidden_dim=args.hidden_dim,
            num_classes=args.num_classes,
        ),
        "CNN1D": CNN1DBaseline(
            num_uavs=args.num_uavs,
            num_features=args.num_features,
            hidden_dim=args.hidden_dim,
            num_classes=args.num_classes,
        ),
        "GraphTemporalTransformer": GraphTemporalTransformer(
            num_features=args.num_features,
            hidden_dim=args.hidden_dim,
            num_classes=args.num_classes,
        ),
    }

    rows = []
    print(f"Profiling on device: {device}")
    for name, model in models.items():
        print(f"Profiling {name}...")
        rows.append(
            profile_model(
                name=name,
                model=model,
                device=device,
                batch_size=args.batch_size,
                window_size=args.window_size,
                num_uavs=args.num_uavs,
                num_features=args.num_features,
                num_classes=args.num_classes,
                warmup=args.warmup,
                iters=args.iters,
            )
        )

    out_csv = Path(args.out_csv)
    out_csv.parent.mkdir(parents=True, exist_ok=True)

    with out_csv.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)

    out_md = Path(args.out_md)
    out_md.parent.mkdir(parents=True, exist_ok=True)

    lines = []
    lines.append("# HCC Runtime and Complexity Report\n")
    lines.append("This report summarizes runtime and complexity profiling for TRUST-Swarm models.\n")
    lines.append("## Environment\n")
    lines.append(f"- Python: {platform.python_version()}")
    lines.append(f"- Platform: {platform.platform()}")
    lines.append(f"- PyTorch: {torch.__version__}")
    lines.append(f"- Device: {device}")
    lines.append(f"- CUDA available: {torch.cuda.is_available()}")
    if torch.cuda.is_available():
        lines.append(f"- GPU: {torch.cuda.get_device_name(0)}")
    lines.append("\n## Profiling Configuration\n")
    lines.append(f"- Batch size: {args.batch_size}")
    lines.append(f"- Window size: {args.window_size}")
    lines.append(f"- UAV nodes: {args.num_uavs}")
    lines.append(f"- Telemetry features: {args.num_features}")
    lines.append(f"- Classes: {args.num_classes}")
    lines.append(f"- Warmup iterations: {args.warmup}")
    lines.append(f"- Timed inference iterations: {args.iters}\n")

    lines.append("## Runtime and Complexity Table\n")
    header = "| Model | Params | Size MB | Batch latency ms | Sample latency ms | Throughput windows/s | Train step ms | Device |"
    sep = "|---|---:|---:|---:|---:|---:|---:|---|"
    lines.append(header)
    lines.append(sep)
    for r in rows:
        lines.append(
            f"| {r['model']} | {r['parameters']} | {r['model_size_mb']} | "
            f"{r['inference_batch_latency_ms']} | {r['inference_sample_latency_ms']} | "
            f"{r['throughput_windows_per_second']} | {r['single_train_step_ms']} | {r['device']} |"
        )

    lines.append("\n## Manuscript Use\n")
    lines.append(
        "Use this table in the HCC manuscript to support practical feasibility. "
        "For final submission, rerun this profiler on the same RunPod GPU used for the final experiment."
    )

    out_md.write_text("\n".join(lines))

    print(f"Saved CSV: {out_csv}")
    print(f"Saved report: {out_md}")


if __name__ == "__main__":
    main()

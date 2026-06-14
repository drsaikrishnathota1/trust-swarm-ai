#!/usr/bin/env python3
from pathlib import Path
import pandas as pd

RESULTS_DOC = Path("docs/hcc_results_discussion_v1.md")
ABLATION = Path("results/hcc/ablation_summary.csv")
RUNTIME = Path("results/hcc/runtime_complexity_summary.csv")

if not RESULTS_DOC.exists():
    raise FileNotFoundError(RESULTS_DOC)
if not ABLATION.exists():
    raise FileNotFoundError(ABLATION)
if not RUNTIME.exists():
    raise FileNotFoundError(RUNTIME)

text = RESULTS_DOC.read_text()

ab = pd.read_csv(ABLATION)
rt = pd.read_csv(RUNTIME)

ab_cols = [
    "configuration",
    "accuracy",
    "macro_f1",
    "calibration_evidence",
    "ood_evidence",
    "explanation_evidence",
    "recovery_support",
]
ab_table = ab[ab_cols].copy()
ab_table["accuracy"] = ab_table["accuracy"].map(lambda x: f"{x:.4f}")
ab_table["macro_f1"] = ab_table["macro_f1"].map(lambda x: f"{x:.4f}")

rt_cols = [
    "model",
    "parameters",
    "model_size_mb",
    "inference_batch_latency_ms",
    "inference_sample_latency_ms",
    "throughput_windows_per_second",
    "single_train_step_ms",
]
rt_table = rt[rt_cols].copy()

for col in [
    "model_size_mb",
    "inference_batch_latency_ms",
    "inference_sample_latency_ms",
    "throughput_windows_per_second",
    "single_train_step_ms",
]:
    rt_table[col] = rt_table[col].map(lambda x: f"{x:.4f}")

new_section = f"""
## 5.7 Final Ablation Study

A final HCC ablation study was conducted on the seed-42 graph-temporal dataset using 66,300 mission windows, 20 UAV nodes, 20 timesteps, 9 telemetry features, and 8 mission-state classes. The full Graph-Temporal Transformer achieved an accuracy of 0.9579 and a macro F1 score of 0.8734.

Removing UAV-node attention reduced macro F1 from 0.8734 to 0.7903, showing that swarm-node relational reasoning contributes meaningfully to mission-state recognition. Removing the temporal transformer reduced macro F1 to 0.8237, showing that temporal mission-evolution modeling is also important.

Framework-level ablations do not change classifier accuracy because they remove assurance modules rather than the classifier itself. However, they show what high-confidence evidence is lost when calibration, OOD stress testing, explainability, or recovery reasoning is removed.

{ab_table.to_markdown(index=False)}

## 5.8 Runtime and Complexity Analysis

Runtime and complexity profiling was conducted on an NVIDIA H200 GPU using batch size 128, 20 UAV nodes, 20 timesteps, and 9 telemetry features. The Graph-Temporal Transformer has 680,840 trainable parameters and a model size of 2.618 MB. Its inference latency was 2.267 ms per batch and 0.0177 ms per graph-temporal mission window, corresponding to approximately 56,458 windows per second.

Although the Graph-Temporal Transformer is heavier than LSTM, GRU, and 1D-CNN baselines, the profiling results show that it remains computationally practical for high-throughput mission-window inference on modern GPU hardware.

{rt_table.to_markdown(index=False)}
"""

start_marker = "## 5.7 Final Ablation Study"
end_marker = "## 5.7 Discussion Against High-Confidence Computing Standards"

if start_marker in text:
    start = text.index(start_marker)
    end = text.index(end_marker)
    text = text[:start] + new_section.strip() + "\n\n" + text[end:]
else:
    text = text.replace(end_marker, new_section.strip() + "\n\n" + end_marker)

# Renumber later headings if needed
text = text.replace("## 5.7 Discussion Against High-Confidence Computing Standards", "## 5.9 Discussion Against High-Confidence Computing Standards")
text = text.replace("## 5.8 Safe Final Interpretation", "## 5.10 Safe Final Interpretation")

RESULTS_DOC.write_text(text)
print(f"Updated {RESULTS_DOC}")

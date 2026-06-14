# HCC Missing Experiment Plan: Ablation and Runtime/Complexity

## Purpose

This document identifies the additional experiments needed before submitting TRUST-Swarm to High-Confidence Computing.

The current manuscript already contains:

* graph-temporal mission-state prediction
* LSTM, GRU, and 1D-CNN baseline comparison
* uncertainty calibration
* OOD stress testing
* perturbation-based explainability
* PPO recovery scaffold
* multi-seed evaluation

However, accepted High-Confidence Computing papers typically include stronger system-level validation, ablation analysis, runtime analysis, and practical feasibility evaluation. Therefore, TRUST-Swarm needs two additional experiment groups before final submission:

1. Ablation study
2. Runtime and complexity analysis

## 1. Ablation Study

### Goal

The ablation study should show why each TRUST-Swarm component matters.

The purpose is not to prove that every module improves classification accuracy. The purpose is to show that TRUST-Swarm is a high-confidence computing framework where each module contributes to security, confidence, traceability, OOD awareness, or recovery reasoning.

### Required Ablation Rows

| Ablation ID | Configuration                   | Purpose                                                   |
| ----------- | ------------------------------- | --------------------------------------------------------- |
| A0          | Full TRUST-Swarm                | Complete framework                                        |
| A1          | Without UAV-node attention      | Tests contribution of node-level swarm reasoning          |
| A2          | Without temporal transformer    | Tests contribution of temporal mission evolution modeling |
| A3          | Without uncertainty calibration | Tests loss of confidence-aware reliability evidence       |
| A4          | Without OOD stress testing      | Tests loss of unseen-shift vulnerability evaluation       |
| A5          | Without explainability          | Tests loss of traceable mission-risk evidence             |
| A6          | Without recovery reasoning      | Tests loss of mission-response decision support           |

### Metrics to Report

For model ablations A0–A2:

* accuracy
* macro F1
* macro precision
* macro recall
* test loss

For framework ablations A3–A6:

* availability of confidence evidence
* availability of OOD risk evidence
* availability of traceable explanation
* availability of recovery action support
* qualitative mission-assurance impact

### Recommended Ablation Table

| Configuration                   |        Accuracy |        Macro F1 | Calibration evidence | OOD evidence | Explanation evidence | Recovery support | Interpretation                           |
| ------------------------------- | --------------: | --------------: | -------------------- | ------------ | -------------------- | ---------------- | ---------------------------------------- |
| Full TRUST-Swarm                |    report value |    report value | Yes                  | Yes          | Yes                  | Yes              | Complete high-confidence framework       |
| Without UAV-node attention      |    report value |    report value | Yes                  | Yes          | Yes                  | Yes              | Reduced swarm relational reasoning       |
| Without temporal transformer    |    report value |    report value | Yes                  | Yes          | Yes                  | Yes              | Reduced temporal mission reasoning       |
| Without uncertainty calibration | same classifier | same classifier | No                   | Yes          | Yes                  | Yes              | Cannot assess confidence reliability     |
| Without OOD stress testing      | same classifier | same classifier | Yes                  | No           | Yes                  | Yes              | Cannot expose unseen-shift vulnerability |
| Without explainability          | same classifier | same classifier | Yes                  | Yes          | No                   | Yes              | Cannot trace mission-risk drivers        |
| Without recovery reasoning      | same classifier | same classifier | Yes                  | Yes          | Yes                  | No               | Cannot connect prediction to response    |

## 2. Runtime and Complexity Analysis

### Goal

High-Confidence Computing reviewers may ask whether TRUST-Swarm is practical for secure intelligent systems. A runtime and complexity table will strengthen practical feasibility.

### Required Metrics

| Metric                     | Description                          |
| -------------------------- | ------------------------------------ |
| Model parameters           | Number of trainable parameters       |
| Model file size            | Size of saved model checkpoint       |
| Training time per seed     | Total training time for one seed     |
| Average inference latency  | Time per graph-temporal window       |
| Batch inference throughput | Windows processed per second         |
| Memory usage               | Approximate CPU/GPU memory footprint |
| Hardware environment       | GPU/CPU used                         |
| Software environment       | Python, PyTorch, CUDA versions       |

### Recommended Runtime Table

| Model                      | Parameters | Model size | Training time | Inference latency | Throughput | Hardware   |
| -------------------------- | ---------: | ---------: | ------------: | ----------------: | ---------: | ---------- |
| LSTM                       |     report |     report |        report |            report |     report | RunPod GPU |
| GRU                        |     report |     report |        report |            report |     report | RunPod GPU |
| 1D-CNN                     |     report |     report |        report |            report |     report | RunPod GPU |
| Graph-Temporal Transformer |     report |     report |        report |            report |     report | RunPod GPU |

## 3. Minimal New Coding Needed

Add these scripts:

1. `scripts/run_ablation_study.py`
2. `scripts/profile_runtime_complexity.py`
3. `scripts/aggregate_hcc_experiments.py`

Expected outputs:

1. `results/hcc/ablation_summary.csv`
2. `results/hcc/runtime_complexity_summary.csv`
3. `results/hcc/hcc_final_summary.csv`

## 4. Practical Plan

### Phase 1 — Local sanity test

Run small data to verify scripts:

* 10 mission runs
* 80 timesteps
* 10 UAVs
* 1 epoch
* 1 seed

Goal: script correctness only.

### Phase 2 — RunPod final HCC run

Run final configuration:

* 300 mission runs
* 240 timesteps
* 20 UAVs
* 30 epochs
* seeds 42, 123, 2026

Goal: final HCC-ready ablation and runtime evidence.

## 5. Manuscript Sections to Update After Experiments

After generating ablation and runtime results, update:

1. Experimental Setup
2. Results and Discussion
3. Tables
4. Figures
5. Abstract, if necessary
6. Limitations

## 6. Why This Matters for High-Confidence Computing

Accepted High-Confidence Computing papers usually present unified frameworks and validate them with practical evidence such as ablation studies, benchmark comparisons, runtime feasibility, case studies, or robustness analysis.

TRUST-Swarm already has baseline comparison, uncertainty calibration, OOD stress testing, and explainability. Adding ablation and runtime/complexity analysis will make the manuscript much closer to High-Confidence Computing standards.

## Final Priority

Before final submission, do not spend more time on planning documents.

The next real technical task should be:

1. implement ablation script,
2. implement runtime/complexity profiler,
3. run local sanity test,
4. run final RunPod experiment,
5. update HCC manuscript with new results.


# High-Confidence Computing Final TODO Checklist

## Target Journal

High-Confidence Computing

## Current Manuscript Status

TRUST-Swarm has been reframed for High-Confidence Computing as a secure, high-confidence, graph-temporal intelligent computing framework for UAV swarm mission assurance.

Completed items:

* HCC title and abstract
* HCC contribution table
* HCC introduction
* HCC related work
* HCC methodology
* HCC experimental setup
* HCC results and discussion
* HCC limitation and conclusion sections
* HCC submission package drafts
* runtime/complexity profiler script
* ablation study script
* HCC manuscript v1 builder
* HCC manuscript quality checker

## Remaining Critical Tasks Before Submission

### 1. Run Final Ablation Study on RunPod GPU

Status: Not final yet.

Run final ablation on GPU, not Mac.

Command:

```bash
python scripts/run_hcc_ablation_study.py \
  --data data/processed/seed_42/graph_windows.pt \
  --epochs 30 \
  --batch-size 128
```

Required output:

* results/hcc/ablation_summary.csv
* docs/hcc_ablation_report.md

Manuscript update needed:

* Add ablation table to Results and Discussion.
* Explain what is lost when node attention, temporal modeling, calibration, OOD testing, explanation, or recovery reasoning is removed.

### 2. Run Final Runtime and Complexity Profiling on RunPod GPU

Status: Not final yet.

Command:

```bash
python scripts/profile_runtime_complexity.py \
  --batch-size 128 \
  --warmup 10 \
  --iters 50
```

Required output:

* results/hcc/runtime_complexity_summary.csv
* docs/hcc_runtime_complexity_report.md

Manuscript update needed:

* Add runtime and complexity table.
* Report model parameters, model size, inference latency, throughput, and training-step time.

### 3. Update HCC Manuscript With Final Ablation and Runtime Results

Status: Pending final RunPod outputs.

Files to update:

* docs/hcc_results_discussion_v1.md
* docs/hcc_experimental_setup_v1.md
* manuscript/TRUST-Swarm-HCC-manuscript-v1.md

Required additions:

* Ablation subsection
* Runtime and complexity subsection
* Practical feasibility discussion

### 4. Clean References

Status: Pending.

Required actions:

* Remove weak or irrelevant references.
* Add stronger High-Confidence Computing, trustworthy AI, cyber-physical security, UAV security, calibration, OOD, explainability, and recovery references.
* Verify DOI, journal name, year, and citation format.
* Avoid unsupported or fake citations.

### 5. Remove Working Notes From Final Manuscript

Status: Pending.

Before submission, remove:

* “Target journal”
* “HCC Final Submission Items Still Needed”
* planning notes
* placeholder author brackets
* any internal checklist language

### 6. Convert Manuscript to Word/PDF

Status: Pending.

Required final files:

* Word manuscript
* PDF manuscript
* figures folder
* cover letter
* highlights
* declaration of interest
* data availability statement
* code availability statement

### 7. Final Quality Check

Status: Pending.

Run:

```bash
python scripts/check_hcc_manuscript_quality.py
cat docs/hcc_manuscript_quality_check.md
```

Fix anything marked:

* MISSING
* CHECK
* overclaim warning
* missing limitation
* missing HCC framing

## Claims Allowed

Safe claim:

TRUST-Swarm provides a high-confidence graph-temporal intelligent computing framework for secure multi-UAV mission assurance by integrating mission-state recognition, calibrated confidence, OOD cyber-physical stress testing, traceable explanation, and recovery-oriented reasoning.

## Claims to Avoid

Do not claim:

* Graph-Temporal Transformer is the best classifier.
* TRUST-Swarm outperforms all baselines.
* TRUST-Swarm solves OOD detection.
* PPO recovery is deployment-ready.
* Synthetic telemetry replaces real UAV field validation.
* The system is field-tested or hardware validated.

## Final Submission Priority Order

1. Final RunPod ablation study
2. Final RunPod runtime/complexity profiling
3. Update manuscript results section
4. Clean references
5. Remove internal notes
6. Convert to Word/PDF
7. Submit package preparation

## Current Risk Level

Topic fit for High-Confidence Computing: strong.

Main remaining risk:

* synthetic-only validation
* missing final ablation table
* missing final runtime/complexity table
* references need verification

Once ablation and runtime results are added, the manuscript will be much closer to High-Confidence Computing standards.


# RA-MARS Defence Technology Submission Repository

## Project Title

**RA-MARS: A Resilient AI-Driven Mission Assurance Framework for Secure Multi-UAV Defence Surveillance Under Jamming, GPS Spoofing, and Data-Tampering Attacks**

This repository supports a journal manuscript prepared for submission to **Defence Technology**.

RA-MARS is a simulation-based defence mission-assurance framework for secure multi-UAV surveillance under cyber-electromagnetic, navigation, and data-integrity attacks.

---

## Paper Summary

RA-MARS treats UAV security as a **mission-assurance problem**, not only as an attack-classification problem.

The framework integrates:

- Temporal AI-based attack detection using LSTM/GRU sequence models.
- 1D-CNN temporal baseline validation.
- Mission Assurance Index scoring.
- Mission-risk evaluation.
- Digital-twin-inspired action selection.
- Adaptive mission-continuation logic.
- Hash-chain-based tamper-evident mission provenance.
- RF/SINR-aware mission evaluation.
- Latency-budget analysis.
- Ablation analysis.
- Adversarial robustness testing.
- Controlled simulation-based validation.

---

## Threat Scenarios Covered

The final validation workflow evaluates:

- Normal mission operation.
- RF jamming.
- GPS/GNSS spoofing.
- Mission-data tampering.
- Jamming + spoofing.
- Spoofing + tampering.
- Jamming + tampering.
- Combined jamming + spoofing + tampering.

---

## Completed v5 Validation Results

Final headline results:

- Binary LSTM: **99.85% accuracy**, **99.81% macro-F1**.
- Binary GRU: **99.80% accuracy**, **99.76% macro-F1**.
- Weighted LSTM fine-grained: **99.53% accuracy**, **99.18% macro-F1**.
- Weighted GRU fine-grained: **99.24% accuracy**, **98.66% macro-F1**.
- 1D-CNN binary baseline: **99.97% accuracy**, **99.96% macro-F1**.
- 1D-CNN fine-grained baseline: **98.82% accuracy**, **98.18% macro-F1**.
- Full RA-MARS Mission Assurance Index: **0.7012**.
- Full RA-MARS mission success rate: **73.61%**.
- Framework overhead: **11.5 ms per telemetry cycle**.
- PGD-augmented adversarial training:
  - Clean macro-F1: **99.86%**.
  - FGSM ε=0.01 macro-F1: **99.75%**.
  - PGD ε=0.05 macro-F1: **98.31%**.

---

## Important Research Interpretation

The high classification scores are interpreted within a **controlled synthetic-telemetry setting**.

The data are simulation-generated and physics-informed. They are **not** real military flight-test data, classified operational data, hardware-in-the-loop results, or deployed battlefield validation.

The main contribution of RA-MARS is not classifier accuracy alone. The core contribution is the integration of:

- attack detection,
- mission-risk scoring,
- adaptive mission continuation,
- mission-assurance evaluation,
- RF/SINR-aware analysis,
- and tamper-evident provenance.

The reported results should be interpreted as controlled simulation evidence of framework behavior, not proof of deployed battlefield effectiveness.

---

## Research Limitations Explicitly Addressed

The manuscript now clearly addresses the following limitations:

- Synthetic-data-only validation.
- No real UAV flight-test dataset.
- No hardware-in-the-loop validation.
- No classified military operational validation.
- No deployed battlefield validation.
- Possible domain shift in real UAV operations.
- Very high classification scores due to controlled synthetic telemetry.
- Adversarial robustness limited mainly to binary attack-vs-normal detection.
- Need for future RF testbed validation.
- Need for future cross-dataset and real-flight-log validation.

---

## Research-Framing Fixes Completed

The manuscript was strengthened to avoid reviewer overclaiming concerns:

- High model scores are framed as controlled synthetic-telemetry results.
- Blockchain wording was de-emphasized.
- The provenance module is framed as **hash-chain-based tamper-evident mission provenance**.
- Classical baseline wording was softened.
- A qualitative prior-work comparison table was added.
- Domain-shift limitation was added.
- A no-overclaiming conclusion sentence was added.
- Fine-grained adversarial robustness limitation was stated.
- Figure-generation transparency was added.

---

## Standards and Submission-Compliance Fixes Completed

The package was aligned with journal submission standards as much as possible:

- Double-anonymized manuscript created.
- Author-identifying information removed from anonymous manuscript.
- Repository URL removed from anonymous manuscript.
- Anonymous DOCX exported.
- Anonymous HTML exported.
- Title page prepared separately.
- Cover letter prepared.
- Highlights shortened for journal-style submission.
- Declaration of interest prepared.
- Generative AI declaration prepared.
- Data and code availability statement prepared.
- PNG figure exports prepared.
- SVG figure versions retained.
- Final ZIP package rebuilt.
- Duplicate-folder audit passed.
- Old-number audit passed.
- Anonymous identity audit passed.

---

## What We Completed Since Yesterday

Major work completed:

1. Reverified the repository and pipeline status.
2. Fixed active v3 references in v4 training scripts.
3. Confirmed train-only scaling for LSTM/GRU sequence models.
4. Confirmed train-only scaling for classical baselines.
5. Added and ran the 1D-CNN temporal baseline.
6. Completed missing CNN baseline validation.
7. Archived and restored RunPod validation results.
8. Copied completed result CSVs into `simulations/final-results/`.
9. Generated completed v5 result tables.
10. Updated manuscript with final v5 numbers.
11. Updated cover letter and highlights with final v5 values.
12. Generated v5 SVG figures.
13. Converted v5 SVG figures to PNG.
14. Updated manuscript figure links to v5.
15. Refreshed final submission folder.
16. Exported updated DOCX and HTML files.
17. Created anonymous manuscript for double-anonymized review.
18. Exported anonymous DOCX and HTML.
19. Added AI-use declaration.
20. Added figure-generation transparency statement.
21. Added data/code availability statement.
22. Added separate title page.
23. Rebuilt final v5 submission ZIP.
24. Ran final identity, old-number, and duplicate-folder audits.

---

## Key Repository Files

### Manuscript

- `manuscript/RA-MARS-journal-draft-final-v4.md`

### Final Submission Folder

- `final-submission-v4/`

### Anonymous Manuscript

- `final-submission-v4/RA-MARS-journal-draft-final-v5-anonymous.md`
- `final-submission-v4/export/RA-MARS-journal-draft-final-v5-anonymous.docx`
- `final-submission-v4/export/RA-MARS-journal-draft-final-v5-anonymous.html`

### Non-Anonymous Manuscript for Author Records

- `final-submission-v4/export/RA-MARS-journal-draft-final-v5.docx`
- `final-submission-v4/export/RA-MARS-journal-draft-final-v5.html`

### Figures

SVG figures:

- `final-submission-v4/figures-v5/`

PNG figures:

- `final-submission-v4/figures-v5-png/`

### Result Tables

- `tables/final-v5/ra_mars_v5_completed_result_tables.md`
- `final-submission-v4/ra_mars_v5_completed_result_tables.md`

### Final Result CSVs

- `simulations/final-results/`
- `final-submission-v4/final-results/`

### Submission Declarations

- `final-submission-v4/title-page.md`
- `final-submission-v4/cover-letter.md`
- `final-submission-v4/highlights.md`
- `final-submission-v4/declaration-of-interest.md`
- `final-submission-v4/declaration-of-generative-ai.md`
- `final-submission-v4/data-availability.md`

### Final ZIP Package

- `RA-MARS-final-submission-v5.zip`

---

## Final Submission Upload Guide

For **Defence Technology double-anonymized review**, upload:

### Main Manuscript

Use:

`final-submission-v4/export/RA-MARS-journal-draft-final-v5-anonymous.docx`

Do **not** upload the non-anonymous manuscript as the review manuscript.

### Title Page

Use:

`final-submission-v4/title-page.md`

or the exported title page file if available.

### Figures

Use PNGs if the system asks for separate figures:

`final-submission-v4/figures-v5-png/*.png`

SVG versions are also retained in:

`final-submission-v4/figures-v5/`

### Cover Letter

Use:

`final-submission-v4/cover-letter.md`

### Highlights

Use:

`final-submission-v4/highlights.md`

### Declaration of Interest

Use:

`final-submission-v4/declaration-of-interest.md`

### Generative AI Declaration

Use:

`final-submission-v4/declaration-of-generative-ai.md`

### Data and Code Availability Statement

Use:

`final-submission-v4/data-availability.md`

### Backup Package

Keep:

`RA-MARS-final-submission-v5.zip`

---

## Final Package Audit Status

The final package passed:

- Anonymous manuscript identity check.
- Old-number audit.
- v4 figure-link audit.
- Duplicate nested-folder audit.
- PNG figure inclusion check.
- AI declaration inclusion check.
- Git clean check.

---

## Remaining Research Risks

No blocking research gaps remain for first submission.

Remaining reviewer-level risks:

- Synthetic-only validation.
- No real UAV flight-test dataset.
- No RF hardware-in-the-loop testbed.
- No same-dataset numerical SOTA comparison.
- High classification scores under controlled synthetic telemetry.
- Fine-grained adversarial robustness left for future work.

These risks are now disclosed and framed as limitations/future work.

---

## Final Recommendation

The repository and submission package are ready for journal submission.

Submit RA-MARS as a:

**reproducible simulation-based mission-assurance framework for secure multi-UAV defence surveillance**

not as a deployed battlefield-validated UAV defence system.


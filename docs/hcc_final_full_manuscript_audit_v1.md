# HCC Final Full Manuscript Audit v1

**Manuscript:** `manuscript/TRUST-Swarm-HCC-manuscript-v1.md`
**Approx total word count:** 9704
**Section word-count CSV:** `docs/hcc_section_word_counts_v1.csv`

## Overall status

**Status: PASS WITH WARNINGS — review warnings before final DOCX/PDF.**

## Section word counts

| Section | Word count |
| --- | ---: |
| HCC-Framed Abstract | 347 |
| Keywords | 18 |
| HCC Contribution Table | 120 |
| 1. Introduction | 1361 |
| 2. Related work | 1742 |
| 3. Methodology | 1804 |
| 4. Experimental setup | 1487 |
| 5. Results and discussion | 1921 |
| 6. Limitations and future work | 586 |
| 7. Conclusion | 272 |

## Critical issues

- None.

## Warnings

- Overclaim trigger `best standalone classifier` found 2 time(s). Review context manually.
- Overclaim trigger `operationally deployable` found 1 time(s). Review context manually.
- Overclaim trigger `operationally validated` found 1 time(s). Review context manually.
- Overclaim trigger `proves` found 2 time(s). Review context manually.
- No numbered reference entries detected in this manuscript file.
- Abstract heading still says `HCC-Framed Abstract`; final clean manuscript should rename it to `Abstract`.
- Contribution table heading still says `HCC Contribution Table`; final clean manuscript may rename it to `Contributions`.
- No figure mentions detected. HCC-style paper should include architecture/results figures.
- No table mentions detected. HCC-style paper should include comparison/result tables.
- Git status has uncommitted/untracked files:

```text
?? docs/hcc_section_word_counts_v1.csv
?? scripts/audit_hcc_full_manuscript_v1.py
?? scripts/build_hcc_elsevier_template_docx_v1.py
?? scripts/build_hcc_submission_docx_pdf_v1.py
?? submission/TRUST-Swarm-HCC-Elsevier-template-submission-v1.docx
?? submission/TRUST-Swarm-HCC-submission-draft-v4.docx
?? submission/TRUST-Swarm-HCC-submission-draft-v4.pdf
```

## Passed checks

- All required v2 section files exist.
- Required manuscript sections are present.
- Total word count is journal-level: 9704 words.
- No duplicate top-level section headings found.
- No R-label citations found.
- Results section includes CSV table previews or did not report missing CSV previews.
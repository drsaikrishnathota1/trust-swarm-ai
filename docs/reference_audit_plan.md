# TRUST-Swarm Reference Audit Plan

## Purpose

This document audits the current TRUST-Swarm reference list before journal submission.

The current reference list is useful as a draft foundation, but not every reference should be treated as final. Some references are strong foundational papers, while others are recent arXiv/preprint items that must be verified or replaced with peer-reviewed IEEE, Elsevier, Springer, ACM, or journal versions.

## Audit Categories

### Category A — Safe Foundational References

These references are standard and should likely remain in the final manuscript:

* Transformer / attention foundation
* GCN
* GAT
* LSTM
* GRU
* Adam optimizer
* Batch normalization
* Calibration of neural networks
* MC dropout uncertainty
* Deep ensembles
* OOD baseline detection
* ODIN / generalized ODIN
* Outlier exposure
* LIME
* SHAP
* PPO
* Adversarial machine learning robustness

These are standard machine-learning references and are acceptable for methodology support.

## Category B — Keep but Verify Details

These references may be good, but exact author order, venue, DOI, publication year, and page details must be checked before final submission:

* Time-series transformer references
* Time-series anomaly detection survey
* uncertainty survey papers
* XAI survey papers
* UAV swarm graph-learning papers
* multi-agent reinforcement-learning papers
* UAV path-planning reinforcement-learning papers

Action required:

* Verify DOI or publisher page
* Confirm final venue
* Replace arXiv version with journal/conference version if available
* Format according to target journal style

## Category C — Use Carefully

Recent arXiv UAV security and UAV communication papers can support “latest work,” but they should not dominate the final reference list.

Use carefully:

* 2025–2026 arXiv UAV security surveys
* 2025–2026 anti-jamming preprints
* 2025–2026 GNSS spoofing preprints
* recent RL/UAV preprints

Action required:

* Keep only if directly relevant
* Replace with peer-reviewed papers where possible
* Avoid relying on too many preprints in the final version

## Category D — Replace Before Submission

The final manuscript should not cite:

* Wikipedia pages
* blogs
* random web pages
* unverified author-profile pages
* papers where venue/year cannot be confirmed
* future-dated references that are not clearly available and real
* duplicate references already listed in another batch

Action required:

* Remove Wikipedia-based lookup references
* Replace with original papers or publisher pages
* Re-check all 2025–2026 references before final use

## Immediate Fix Needed

The files named “verified reference list” should be treated as draft reference batches, not final verified reference files.

Recommended rename in final manuscript language:

* “Candidate Reference List — Batch 1”
* “Candidate Reference List — Batch 2”

Avoid saying “verified” until DOI, venue, and publisher pages are confirmed.

## Final Reference Quality Target

For journal submission, the final bibliography should contain:

* 35–45 peer-reviewed journal/conference references
* 10–15 foundational AI methodology references
* 5–10 recent arXiv references only if they are highly relevant
* 0 Wikipedia/blog citations

## Final Reference Mix

Recommended final mix:

| Reference type                             | Target count |
| ------------------------------------------ | -----------: |
| UAV cybersecurity / mission assurance      |        15–20 |
| Jamming, spoofing, telemetry attacks       |        10–12 |
| Graph neural networks / graph-temporal AI  |         8–10 |
| Temporal deep learning / transformers      |          5–7 |
| Uncertainty calibration / OOD              |         8–10 |
| Explainable AI                             |          4–6 |
| Reinforcement learning / PPO recovery      |          4–6 |
| Trustworthy AI / high-confidence computing |          5–8 |

## Manual Audit Checklist

For every reference, verify:

1. Is the paper real?
2. Is the author order correct?
3. Is the title exact?
4. Is the publication year correct?
5. Is it peer-reviewed or arXiv only?
6. Does it have DOI?
7. Is the paper directly relevant to TRUST-Swarm?
8. Should it be cited in Introduction, Related Work, Methodology, or Discussion?
9. Is there a newer journal version?
10. Should it be replaced by a stronger source?

## Safe Manuscript Rule

Do not insert a citation into the final manuscript unless it passes at least one of these:

* peer-reviewed journal paper
* peer-reviewed conference paper
* foundational AI method paper
* official arXiv paper from a known method or highly relevant recent work
* publisher page or DOI verified

## Final Verdict

The current 55-reference list is a good starting point, but it is not final submission-ready.

Before journal submission, the list must be audited and improved by replacing weak or unverified references with stronger peer-reviewed sources.


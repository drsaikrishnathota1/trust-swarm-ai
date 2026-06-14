# TRUST-Swarm Final Remaining Tasks Checklist

## Current Status

TRUST-Swarm now has:

* journal-style manuscript v3
* Information Fusion framing
* results tables
* figure captions
* 10 figure references
* 7 architecture diagrams
* result figures
* candidate references
* reference audit checklist
* submission package drafts

The project should now move from drafting/planning into final polishing.

## Remaining High-Priority Tasks

### 1. Reference Audit

Status: Required before submission.

Tasks:

* remove duplicate references
* verify author order
* verify paper titles
* verify year and venue
* verify DOI or arXiv ID
* replace weak arXiv-only references where possible
* add stronger peer-reviewed Information Fusion references
* reduce final arXiv-only count
* make final bibliography journal-style

Target:

* 50–60 strong references
* fewer than 10 arXiv-only references
* no Wikipedia/blog citations
* no duplicates

## 2. Manuscript Polishing

Status: Required.

Tasks:

* remove repeated paragraphs
* make tone more journal-style
* tighten abstract
* strengthen novelty statement
* insert citations properly
* ensure all tables are numbered
* ensure all figures are cited in text
* ensure all limitations are honest
* avoid overclaiming Graph-Temporal Transformer superiority

Safe main claim:

TRUST-Swarm provides a trustworthy graph-temporal multi-source information-fusion framework for UAV swarm mission assurance by integrating mission-state recognition, calibrated confidence, OOD stress testing, fusion-driver explainability, and recovery-oriented reasoning.

## 3. Figure Quality Check

Status: Required.

Tasks:

* check readability of all 7 architecture diagrams
* confirm labels are not too small
* confirm PNG and PDF versions exist
* use PDF versions for journal submission if allowed
* use PNG versions for Word draft preview

Required figure folders:

* figures/architecture
* figures/manuscript

## 4. Results Verification

Status: Required.

Tasks:

* verify tables match final CSV summaries
* verify reported means and standard deviations
* keep CNN1D superiority honest
* avoid saying GTT is best classifier
* emphasize calibration, OOD, explainability, and framework contribution

## 5. Journal Target Decision

Recommended targets:

1. Information Fusion — high-impact but needs strong fusion framing and reference audit
2. IEEE Access — safer practical backup
3. Defence Technology — possible but higher novelty/defence realism risk

Avoid:

* ESWA unless all defense/military framing is removed

## 6. Final Submission Package

Needed:

* final manuscript Word/PDF
* separate figure files
* cover letter
* highlights
* data availability statement
* code availability statement
* competing interest statement
* funding statement
* ethics statement
* reviewer suggestions if required

## 7. GitHub Cleanup

Before submission:

* do not commit large generated datasets
* do not commit tar.gz result archives
* keep scripts, figures, docs, and manuscript files
* verify git status is clean

Command:

git status

Expected:

nothing to commit, working tree clean

## Final Stop Rule

Stop creating more planning documents unless necessary.

Next real work should be:

1. audit references,
2. polish manuscript v3,
3. create final Word/PDF manuscript,
4. prepare submission files.


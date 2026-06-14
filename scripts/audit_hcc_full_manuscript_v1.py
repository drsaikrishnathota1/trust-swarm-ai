#!/usr/bin/env python3
from pathlib import Path
import re
import csv
import subprocess
from collections import Counter

MANUSCRIPT = Path("manuscript/TRUST-Swarm-HCC-manuscript-v1.md")
REPORT = Path("docs/hcc_final_full_manuscript_audit_v1.md")
CSV_OUT = Path("docs/hcc_section_word_counts_v1.csv")

REQUIRED_FILES = [
    "docs/hcc_title_abstract_contributions_v2.md",
    "docs/hcc_introduction_v2.md",
    "docs/hcc_related_work_v2.md",
    "docs/hcc_methodology_v2.md",
    "docs/hcc_experimental_setup_v2.md",
    "docs/hcc_results_discussion_v2.md",
    "docs/hcc_limitations_conclusion_v2.md",
]

REQUIRED_SECTION_PATTERNS = [
    r"##\s+HCC-Framed Abstract|##\s+Abstract",
    r"##\s+Keywords",
    r"##\s+1\.\s+Introduction",
    r"##\s+2\.\s+Related work",
    r"##\s+3\.\s+Methodology",
    r"##\s+4\.\s+Experimental setup",
    r"##\s+5\.\s+Results and discussion",
    r"##\s+6\.\s+Limitations and future work",
    r"##\s+7\.\s+Conclusion",
]

OVERCLAIMS = [
    "best classifier",
    "best standalone classifier",
    "superior to all baselines",
    "fully solved",
    "solves all",
    "guaranteed",
    "guarantees",
    "operationally deployable",
    "operationally validated",
    "real UAV hardware",
    "field validated",
    "proves",
]

PLACEHOLDERS = [
    "TODO",
    "TBD",
    "XXXX",
    "citation needed",
    "insert citation",
    "HCC Final Submission Items Still Needed",
]

def word_count(s: str) -> int:
    return len(re.findall(r"\b[\w\-]+\b", s))

def git_status():
    try:
        out = subprocess.check_output(["git", "status", "--short"], text=True)
        return out.strip()
    except Exception as e:
        return f"Could not run git status: {e}"

def extract_sections(text: str):
    headings = list(re.finditer(r"^##\s+(.+)$", text, flags=re.MULTILINE))
    sections = []
    for i, m in enumerate(headings):
        start = m.end()
        end = headings[i + 1].start() if i + 1 < len(headings) else len(text)
        sections.append((m.group(1).strip(), text[start:end].strip()))
    return sections

if not MANUSCRIPT.exists():
    raise FileNotFoundError(MANUSCRIPT)

text = MANUSCRIPT.read_text()

issues = []
warnings = []
passes = []

# Required files.
missing_files = [p for p in REQUIRED_FILES if not Path(p).exists()]
if missing_files:
    issues.append("Missing required v2 section files: " + ", ".join(missing_files))
else:
    passes.append("All required v2 section files exist.")

# Required sections.
for pat in REQUIRED_SECTION_PATTERNS:
    if not re.search(pat, text, flags=re.IGNORECASE):
        issues.append(f"Missing required section pattern: `{pat}`")
if not issues:
    passes.append("Required manuscript sections are present.")

# Section word counts.
sections = extract_sections(text)
section_rows = []
for heading, body in sections:
    wc = word_count(body)
    section_rows.append([heading, wc])

CSV_OUT.parent.mkdir(parents=True, exist_ok=True)
with CSV_OUT.open("w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["section", "word_count"])
    w.writerows(section_rows)

total_words = word_count(text)

# Target word count.
if total_words < 8500:
    warnings.append(f"Total word count is {total_words}; journal-style target is about 8500–11000 words.")
elif total_words > 12000:
    warnings.append(f"Total word count is {total_words}; may be long for first submission draft.")
else:
    passes.append(f"Total word count is journal-level: {total_words} words.")

# Duplicate headings.
heading_names = [h for h, _ in sections]
dups = [h for h, c in Counter(heading_names).items() if c > 1]
if dups:
    warnings.append("Duplicate section headings found: " + ", ".join(dups))
else:
    passes.append("No duplicate top-level section headings found.")

# Overclaims.
for term in OVERCLAIMS:
    count = len(re.findall(re.escape(term), text, flags=re.IGNORECASE))
    if count:
        warnings.append(f"Overclaim trigger `{term}` found {count} time(s). Review context manually.")

# Placeholders.
for term in PLACEHOLDERS:
    count = len(re.findall(re.escape(term), text, flags=re.IGNORECASE))
    if count:
        issues.append(f"Placeholder/planning trigger `{term}` found {count} time(s).")

# Citation scan.
r_labels = sorted(set(re.findall(r"\bR\d{2,3}\b", text)))
if r_labels:
    warnings.append(f"Leftover R-label citations found: {len(r_labels)} unique labels. Convert to final numbered references before submission.")
else:
    passes.append("No R-label citations found.")

numbered_refs = re.findall(r"^\[(\d+)\]\s+", text, flags=re.MULTILINE)
if numbered_refs:
    ref_nums = sorted({int(x) for x in numbered_refs})
    passes.append(f"Numbered reference entries found: {len(ref_nums)}.")
else:
    warnings.append("No numbered reference entries detected in this manuscript file.")

# Abstract naming.
if "## HCC-Framed Abstract" in text:
    warnings.append("Abstract heading still says `HCC-Framed Abstract`; final clean manuscript should rename it to `Abstract`.")
if "## HCC Contribution Table" in text:
    warnings.append("Contribution table heading still says `HCC Contribution Table`; final clean manuscript may rename it to `Contributions`.")

# Results table preview.
if "_No result CSV preview tables were found automatically" in text:
    warnings.append("Results section says no CSV previews were found. Confirm result CSV files are present locally before final DOCX.")
else:
    passes.append("Results section includes CSV table previews or did not report missing CSV previews.")

# Figure/table mentions.
fig_mentions = len(re.findall(r"\bFig\.\s*\d+|\bFigure\s+\d+", text))
table_mentions = len(re.findall(r"\bTable\s+\d+", text))
if fig_mentions == 0:
    warnings.append("No figure mentions detected. HCC-style paper should include architecture/results figures.")
else:
    passes.append(f"Figure mentions detected: {fig_mentions}.")
if table_mentions == 0:
    warnings.append("No table mentions detected. HCC-style paper should include comparison/result tables.")
else:
    passes.append(f"Table mentions detected: {table_mentions}.")

# Git status.
status = git_status()
if status:
    warnings.append("Git status has uncommitted/untracked files:\n\n```text\n" + status + "\n```")
else:
    passes.append("Git status is clean.")

# Write report.
lines = []
lines.append("# HCC Final Full Manuscript Audit v1\n")
lines.append(f"**Manuscript:** `{MANUSCRIPT}`")
lines.append(f"**Approx total word count:** {total_words}")
lines.append(f"**Section word-count CSV:** `{CSV_OUT}`\n")

lines.append("## Overall status\n")
if issues:
    lines.append("**Status: FAIL — fix required before final DOCX/PDF.**\n")
elif warnings:
    lines.append("**Status: PASS WITH WARNINGS — review warnings before final DOCX/PDF.**\n")
else:
    lines.append("**Status: PASS — ready for final formatting stage.**\n")

lines.append("## Section word counts\n")
lines.append("| Section | Word count |")
lines.append("| --- | ---: |")
for heading, wc in section_rows:
    lines.append(f"| {heading} | {wc} |")

lines.append("\n## Critical issues\n")
if issues:
    for x in issues:
        lines.append(f"- {x}")
else:
    lines.append("- None.")

lines.append("\n## Warnings\n")
if warnings:
    for x in warnings:
        lines.append(f"- {x}")
else:
    lines.append("- None.")

lines.append("\n## Passed checks\n")
for x in passes:
    lines.append(f"- {x}")

REPORT.write_text("\n".join(lines))
print(f"Saved: {REPORT}")
print(f"Saved: {CSV_OUT}")
print(f"Status: {'FAIL' if issues else 'PASS WITH WARNINGS' if warnings else 'PASS'}")

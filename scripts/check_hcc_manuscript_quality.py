#!/usr/bin/env python3
from pathlib import Path
import re

MANUSCRIPT = Path("manuscript/TRUST-Swarm-HCC-manuscript-v1.md")
OUT = Path("docs/hcc_manuscript_quality_check.md")

if not MANUSCRIPT.exists():
    raise FileNotFoundError(f"Missing manuscript: {MANUSCRIPT}")

text = MANUSCRIPT.read_text()
lower = text.lower()
words = re.findall(r"\b\w+\b", text)

required_sections = [
    "## Abstract",
    "## Contributions",
    "## 1. Introduction",
    "## 2. Related Work",
    "## 3. Methodology",
    "## 4. Experimental Setup",
    "## 5. Results and Discussion",
    "## 6. Limitations and Future Work",
    "## 7. Conclusion",
]

hcc_terms = [
    "high-confidence",
    "secure",
    "intelligent computing",
    "calibration",
    "ood",
    "traceable",
    "recovery",
    "mission assurance",
]

danger_phrases = [
    "outperforms all baselines",
    "best classifier",
    "perfect ood",
    "solves ood",
    "deployment-ready",
    "real-world validated",
    "field validated",
    "guarantees safety",
    "fully autonomous controller",
]

required_honest_phrases = [
    "not positioned as the best standalone classifier",
    "synthetic",
    "future work",
    "not claimed as a deployment-ready",
]

lines = []
lines.append("# HCC Manuscript Quality Check\n")
lines.append(f"- Manuscript: `{MANUSCRIPT}`")
lines.append(f"- Approximate word count: {len(words)}\n")

lines.append("## Required Sections\n")
for sec in required_sections:
    status = "PASS" if sec in text else "MISSING"
    lines.append(f"- {status}: {sec}")

lines.append("\n## HCC Framing Terms\n")
for term in hcc_terms:
    count = lower.count(term)
    status = "PASS" if count > 0 else "MISSING"
    lines.append(f"- {status}: `{term}` appears {count} time(s)")

lines.append("\n## Overclaim Scan\n")
found_danger = False
for phrase in danger_phrases:
    count = lower.count(phrase)
    if count:
        found_danger = True
        lines.append(f"- CHECK: `{phrase}` appears {count} time(s)")
if not found_danger:
    lines.append("- PASS: No major overclaim phrases found")

lines.append("\n## Honesty / Limitation Scan\n")
for phrase in required_honest_phrases:
    count = lower.count(phrase.lower())
    status = "PASS" if count > 0 else "CHECK"
    lines.append(f"- {status}: `{phrase}` appears {count} time(s)")

lines.append("\n## Tables / Evidence Scan\n")
checks = {
    "Contribution table": "| High-Confidence Computing Requirement |" in text,
    "Baseline comparison discussion": "1D-CNN" in text or "CNN" in text,
    "Calibration metrics": "Expected Calibration Error" in text and "Brier" in text,
    "OOD stress testing": "stealth" in lower and "slow gps" in lower,
    "Explainability": "feature importance" in lower or "traceable" in lower,
    "Recovery actions": "reroute" in lower and "return to base" in lower,
}
for name, ok in checks.items():
    lines.append(f"- {'PASS' if ok else 'CHECK'}: {name}")

lines.append("\n## Final Submission Gap Scan\n")
gap_markers = [
    "HCC Final Submission Items Still Needed",
    "Add final ablation results",
    "Add final runtime and complexity results",
    "Clean and verify all references",
]
for marker in gap_markers:
    count = text.count(marker)
    status = "EXPECTED IN V1" if count else "NOT FOUND"
    lines.append(f"- {status}: `{marker}`")

lines.append("\n## Recommendation\n")
lines.append(
    "This manuscript is HCC-framed, but it is still a working v1. "
    "Before submission, add final RunPod ablation results, final runtime/complexity results, "
    "clean references, remove the final-submission placeholder section, and convert to journal Word/PDF format."
)

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text("\n".join(lines))
print(f"Saved: {OUT}")

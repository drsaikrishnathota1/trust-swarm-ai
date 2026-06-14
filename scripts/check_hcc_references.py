#!/usr/bin/env python3
from pathlib import Path
import re
import csv

MANUSCRIPT = Path("manuscript/TRUST-Swarm-HCC-submission-draft-v2.md")
OUT_MD = Path("docs/hcc_reference_audit_report.md")
OUT_CSV = Path("docs/hcc_reference_audit.csv")

if not MANUSCRIPT.exists():
    raise FileNotFoundError(f"Missing manuscript: {MANUSCRIPT}")

text = MANUSCRIPT.read_text()

citation_patterns = re.findall(r"\[(?:\d+(?:\s*[-,]\s*\d+)*)\]", text)

numbers = set()
for pat in citation_patterns:
    inner = pat.strip("[]")
    parts = re.split(r"\s*,\s*", inner)
    for part in parts:
        if "-" in part:
            a, b = [int(x.strip()) for x in part.split("-", 1)]
            for n in range(min(a, b), max(a, b) + 1):
                numbers.add(n)
        elif part.strip().isdigit():
            numbers.add(int(part.strip()))

ref_section_present = bool(re.search(r"(?im)^#{1,3}\s*references\s*$", text))
reference_lines = []
if ref_section_present:
    split = re.split(r"(?im)^#{1,3}\s*references\s*$", text, maxsplit=1)
    if len(split) > 1:
        reference_lines = [ln for ln in split[1].splitlines() if ln.strip()]

numbered_refs = []
for ln in reference_lines:
    if re.match(r"^\s*(\[\d+\]|\d+\.)\s+", ln):
        numbered_refs.append(ln.strip())

rows = []
for n in sorted(numbers):
    rows.append({
        "citation_number": n,
        "status": "needs_verified_reference_entry",
        "notes": "Verify title, authors, venue, year, DOI, and relevance."
    })

OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
with OUT_CSV.open("w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["citation_number", "status", "notes"])
    writer.writeheader()
    writer.writerows(rows)

lines = []
lines.append("# HCC Reference Audit Report\n")
lines.append(f"- Manuscript: `{MANUSCRIPT}`")
lines.append(f"- Citation patterns found: {len(citation_patterns)}")
lines.append(f"- Unique citation numbers found: {len(numbers)}")
lines.append(f"- Reference section present: {'YES' if ref_section_present else 'NO'}")
lines.append(f"- Numbered reference entries detected: {len(numbered_refs)}\n")

lines.append("## Citation Numbers Found\n")
if numbers:
    lines.append(", ".join(str(n) for n in sorted(numbers)))
else:
    lines.append("No numeric citations detected.")

lines.append("\n## Issues\n")
if not ref_section_present:
    lines.append("- MISSING: Reference section not detected.")
if numbers and len(numbered_refs) < len(numbers):
    lines.append("- CHECK: Fewer numbered reference entries than citation numbers.")
if not numbers:
    lines.append("- CHECK: No numeric citations found; manuscript may still need citation insertion.")
if ref_section_present and numbered_refs:
    lines.append("- PASS: Reference section and numbered entries detected.")

lines.append("\n## Next Action\n")
lines.append(
    "Build a verified reference list manually using official journal pages, DOI pages, IEEE Xplore, ScienceDirect, Springer, ACM, or Crossref. Do not rely on unverified AI-generated references."
)

OUT_MD.write_text("\n".join(lines))
print(f"Saved: {OUT_MD}")
print(f"Saved: {OUT_CSV}")

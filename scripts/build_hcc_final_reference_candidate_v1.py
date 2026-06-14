#!/usr/bin/env python3
from pathlib import Path
import re
import csv

MASTER = Path("docs/hcc_reference_master_candidate_v1.md")
REPL = Path("docs/hcc_reference_placeholder_replacements_v1.md")
OUT_MD = Path("docs/hcc_final_reference_candidate_v1.md")
OUT_CSV = Path("docs/hcc_final_reference_candidate_v1.csv")

if not MASTER.exists():
    raise FileNotFoundError(MASTER)
if not REPL.exists():
    raise FileNotFoundError(REPL)

master = MASTER.read_text()
repl = REPL.read_text()

refs = {}

# Load master references
for rid, ref in re.findall(r"^- \[(R\d+)\]\s+(.*)$", master, flags=re.MULTILINE):
    if "Candidate needed" in ref:
        continue
    refs[rid] = ref.strip()

# Replace placeholders using Rxx-replacement entries
for rid, ref in re.findall(r"^\[(R\d+)-replacement\]\s+(.*)$", repl, flags=re.MULTILINE):
    refs[rid] = ref.strip()

def ref_num(rid):
    return int(rid.replace("R", ""))

rows = []
seen_text = set()

for rid in sorted(refs, key=ref_num):
    ref = refs[rid]
    norm = re.sub(r"\s+", " ", ref.lower()).strip()
    duplicate = "yes" if norm in seen_text else "no"
    seen_text.add(norm)

    status = "candidate_needs_final_verification"
    if "arxiv" in ref.lower():
        status = "candidate_verify_published_version"
    if "doi:" in ref.lower():
        status = "candidate_likely_usable_after_doi_check"

    rows.append({
        "reference_id": rid,
        "status": status,
        "duplicate_text": duplicate,
        "reference": ref
    })

with OUT_CSV.open("w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["reference_id", "status", "duplicate_text", "reference"])
    writer.writeheader()
    writer.writerows(rows)

lines = []
lines.append("# HCC Final Reference Candidate List v1\n")
lines.append("Status: cleaned candidate list. This is not final verified bibliography yet.\n")
lines.append("Before manuscript submission, verify every source using official publisher, DOI, IEEE, ACM, Springer, ScienceDirect, or Crossref pages.\n")
lines.append("## Cleaned Candidate References\n")

for row in rows:
    lines.append(f"[{row['reference_id']}] {row['reference']}")

lines.append("\n## Verification Notes\n")
lines.append("- Placeholder entries were removed or replaced.")
lines.append("- arXiv entries should be replaced with peer-reviewed versions where available.")
lines.append("- Duplicate entries should be merged before final manuscript insertion.")
lines.append("- Only references actually cited in the manuscript should remain in the final bibliography.")
lines.append("- Final manuscript references should be numbered sequentially, not with R-labels.\n")

OUT_MD.write_text("\n\n".join(lines))

print(f"Saved: {OUT_MD}")
print(f"Saved: {OUT_CSV}")
print(f"Total cleaned candidate references: {len(rows)}")

#!/usr/bin/env python3
from pathlib import Path
import re
import csv

MASTER = Path("docs/hcc_reference_master_candidate_v1.md")
OUT_MD = Path("docs/hcc_reference_verification_tracker.md")
OUT_CSV = Path("docs/hcc_reference_verification_tracker.csv")

if not MASTER.exists():
    raise FileNotFoundError(MASTER)

text = MASTER.read_text()
refs = re.findall(r"^- \[(R\d+)\]\s+(.*)$", text, flags=re.MULTILINE)

rows = []
for rid, ref in refs:
    lower = ref.lower()

    if "candidate needed" in lower:
        status = "REMOVE_OR_REPLACE"
        reason = "Placeholder entry; must be replaced with a verified source."
    elif "arxiv" in lower:
        status = "VERIFY_PUBLISHED_VERSION"
        reason = "arXiv entry; check if a peer-reviewed journal/conference version exists."
    elif "doi:" in lower or "nature" in lower or "neural computation" in lower or "monthly weather review" in lower:
        status = "LIKELY_USABLE_AFTER_FINAL_CHECK"
        reason = "Contains DOI or stable venue details; still verify before final manuscript."
    else:
        status = "NEEDS_FINAL_VERIFICATION"
        reason = "Needs official venue/DOI/page verification before final use."

    rows.append({
        "reference_id": rid,
        "status": status,
        "reason": reason,
        "reference": ref
    })

OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
with OUT_CSV.open("w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["reference_id", "status", "reason", "reference"])
    writer.writeheader()
    writer.writerows(rows)

lines = []
lines.append("# HCC Reference Verification Tracker\n")
lines.append(f"- Source: `{MASTER}`")
lines.append(f"- Total references/entries: {len(rows)}\n")

summary = {}
for row in rows:
    summary[row["status"]] = summary.get(row["status"], 0) + 1

lines.append("## Summary\n")
for k, v in summary.items():
    lines.append(f"- {k}: {v}")

lines.append("\n## Remove or Replace First\n")
for row in rows:
    if row["status"] == "REMOVE_OR_REPLACE":
        lines.append(f"- [{row['reference_id']}] {row['reference']}")

lines.append("\n## Verify Published Version\n")
for row in rows:
    if row["status"] == "VERIFY_PUBLISHED_VERSION":
        lines.append(f"- [{row['reference_id']}] {row['reference']}")

lines.append("\n## Likely Usable After Final Check\n")
for row in rows:
    if row["status"] == "LIKELY_USABLE_AFTER_FINAL_CHECK":
        lines.append(f"- [{row['reference_id']}] {row['reference']}")

lines.append("\n## Needs Final Verification\n")
for row in rows:
    if row["status"] == "NEEDS_FINAL_VERIFICATION":
        lines.append(f"- [{row['reference_id']}] {row['reference']}")

lines.append("\n## Next Action\n")
lines.append("Replace all placeholder entries first. Then verify arXiv entries against official published versions before inserting final citation numbers into the manuscript.")

OUT_MD.write_text("\n".join(lines))
print(f"Saved: {OUT_MD}")
print(f"Saved: {OUT_CSV}")

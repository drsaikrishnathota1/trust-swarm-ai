#!/usr/bin/env python3
from pathlib import Path
import re

docs = [
    Path("docs/hcc_reference_batch_01_core_methods_candidate.md"),
    Path("docs/hcc_reference_batch_02_uav_security_candidate.md"),
    Path("docs/hcc_reference_batch_03_trustworthy_ai_candidate.md"),
    Path("docs/hcc_reference_batch_04_graph_temporal_candidate.md"),
    Path("docs/hcc_reference_batch_05_recovery_resilience_candidate.md"),
]

out = Path("docs/hcc_reference_master_candidate_v1.md")

lines = []
lines.append("# HCC Reference Master Candidate List v1\n")
lines.append("This file merges all current candidate references for TRUST-Swarm.\n")
lines.append("Status: candidate list only. Do not submit until each reference is verified using official publisher, DOI, IEEE, ACM, Springer, ScienceDirect, or Crossref pages.\n")
lines.append("## Candidate References\n")

seen = set()

for doc in docs:
    if not doc.exists():
        print(f"Missing: {doc}")
        continue

    text = doc.read_text()
    refs = re.findall(r"^\[(R\d+)\]\s+(.*)$", text, flags=re.MULTILINE)

    lines.append(f"\n### From `{doc.name}`\n")

    for rid, ref in refs:
        if rid in seen:
            continue
        seen.add(rid)
        lines.append(f"- [{rid}] {ref}")

lines.append("\n## Verification Checklist\n")
lines.append("- Check exact author names.")
lines.append("- Check official paper title.")
lines.append("- Check journal/conference/book/source.")
lines.append("- Check year, volume, issue, pages, or article number.")
lines.append("- Check DOI or stable official URL.")
lines.append("- Replace arXiv-only entries with peer-reviewed versions where available.")
lines.append("- Remove placeholder entries before final submission.")
lines.append("- Insert only verified references into the final manuscript.\n")

lines.append("## Next Action\n")
lines.append("Verify references section by section, then convert selected references into numbered final manuscript citations.\n")

out.write_text("\n".join(lines))
print(f"Saved: {out}")
print(f"Unique references found: {len(seen)}")

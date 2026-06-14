#!/usr/bin/env python3
from pathlib import Path
import re
import csv

MANUSCRIPT = Path("manuscript/TRUST-Swarm-HCC-numbered-citation-draft-v3.md")
OUT_MD = Path("docs/hcc_numbered_draft_final_audit.md")
OUT_CSV = Path("docs/hcc_numbered_draft_reference_audit.csv")

if not MANUSCRIPT.exists():
    raise FileNotFoundError(MANUSCRIPT)

text = MANUSCRIPT.read_text()

# Split manuscript/reference section
parts = re.split(r"(?im)^## References\s*$", text, maxsplit=1)
body = parts[0]
refs = parts[1] if len(parts) > 1 else ""

# Citations in body
citation_blocks = re.findall(r"\[(?:\d+(?:\s*[,\-–]\s*\d+)*)\]", body)

cited_nums = set()
for block in citation_blocks:
    inner = block.strip("[]").replace("–", "-")
    for part in inner.split(","):
        part = part.strip()
        if "-" in part:
            a, b = [int(x.strip()) for x in part.split("-", 1)]
            for n in range(min(a, b), max(a, b) + 1):
                cited_nums.add(n)
        elif part.isdigit():
            cited_nums.add(int(part))

# Reference entries
ref_entries = re.findall(r"^\[(\d+)\]\s+(.*)$", refs, flags=re.MULTILINE)
ref_nums = {int(n) for n, _ in ref_entries}

missing_refs = sorted(cited_nums - ref_nums)
uncited_refs = sorted(ref_nums - cited_nums)
leftover_r_labels = re.findall(r"R\d{2}", body)
placeholder_words = re.findall(r"Candidate needed|placeholder|TODO|Final Submission Items Still Needed", text, flags=re.IGNORECASE)

overclaim_terms = [
    "perfect OOD",
    "deployment-ready",
    "operationally operationally deployable",
    "best raw classifier",
    "superior to all baselines",
    "fully solved",
]

overclaims = []
for term in overclaim_terms:
    count = len(re.findall(re.escape(term), text, flags=re.IGNORECASE))
    if count:
        overclaims.append((term, count))

arxiv_refs = []
duplicate_refs = {}
seen = {}
for n, ref in ref_entries:
    norm = re.sub(r"\s+", " ", ref.lower()).strip()
    if "arxiv" in norm:
        arxiv_refs.append((n, ref))
    if norm in seen:
        duplicate_refs.setdefault(norm, [seen[norm]]).append(n)
    else:
        seen[norm] = n

rows = []
for n, ref in ref_entries:
    status = "OK_NEEDS_FINAL_VERIFICATION"
    if "arxiv" in ref.lower():
        status = "CHECK_PUBLISHED_VERSION"
    if "candidate" in ref.lower() or "placeholder" in ref.lower():
        status = "REMOVE_OR_REPLACE"
    rows.append({"number": n, "status": status, "reference": ref})

with OUT_CSV.open("w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["number", "status", "reference"])
    writer.writeheader()
    writer.writerows(rows)

lines = []
lines.append("# HCC Numbered Draft Final Audit\n")
lines.append(f"- Manuscript: `{MANUSCRIPT}`")
lines.append(f"- Body citation blocks: {len(citation_blocks)}")
lines.append(f"- Unique cited reference numbers: {len(cited_nums)}")
lines.append(f"- Numbered reference entries: {len(ref_entries)}")
lines.append(f"- Missing reference entries: {len(missing_refs)}")
lines.append(f"- Uncited reference entries: {len(uncited_refs)}")
lines.append(f"- Leftover R-labels in body: {len(leftover_r_labels)}")
lines.append(f"- Placeholder/TODO terms found: {len(placeholder_words)}")
lines.append(f"- arXiv references to verify: {len(arxiv_refs)}")
lines.append(f"- Duplicate reference texts: {len(duplicate_refs)}\n")

lines.append("## Problems\n")
if missing_refs:
    lines.append(f"- Missing reference entries for cited numbers: {missing_refs}")
if leftover_r_labels:
    lines.append(f"- Leftover R-labels found: {sorted(set(leftover_r_labels))}")
if placeholder_words:
    lines.append(f"- Placeholder/TODO-like terms found: {sorted(set(placeholder_words))}")
if overclaims:
    for term, count in overclaims:
        lines.append(f"- Overclaim scan: `{term}` appears {count} time(s)")
if duplicate_refs:
    for _, nums in duplicate_refs.items():
        lines.append(f"- Duplicate reference text at numbers: {nums}")

if not missing_refs and not leftover_r_labels and not placeholder_words:
    lines.append("- No critical citation-structure problems found.")

lines.append("\n## arXiv References to Verify\n")
for n, ref in arxiv_refs:
    lines.append(f"- [{n}] {ref}")

lines.append("\n## Next Action\n")
lines.append("Verify arXiv items against published versions where possible, then generate journal-style DOCX/PDF.")

OUT_MD.write_text("\n".join(lines))
print(f"Saved: {OUT_MD}")
print(f"Saved: {OUT_CSV}")

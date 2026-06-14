#!/usr/bin/env python3
from pathlib import Path
import re
import csv

MANUSCRIPT = Path("manuscript/TRUST-Swarm-HCC-submission-draft-v2.md")
REFS = Path("docs/hcc_final_reference_candidate_v1.md")
OUT = Path("manuscript/TRUST-Swarm-HCC-numbered-citation-draft-v3.md")
MAP_CSV = Path("docs/hcc_numbered_reference_map_v1.csv")
REPORT = Path("docs/hcc_numbered_citation_conversion_report.md")

if not MANUSCRIPT.exists():
    raise FileNotFoundError(MANUSCRIPT)
if not REFS.exists():
    raise FileNotFoundError(REFS)

text = MANUSCRIPT.read_text()
refs_text = REFS.read_text()

# Load R-label references.
ref_map = {}
for rid, ref in re.findall(r"^\[(R\d+)\]\s+(.*)$", refs_text, flags=re.MULTILINE):
    ref_map[rid] = ref.strip()

def normalize_dash(s: str) -> str:
    return s.replace("–", "-").replace("—", "-")

def expand_r_items(citation_inner: str):
    citation_inner = normalize_dash(citation_inner)
    parts = [p.strip() for p in citation_inner.split(",")]
    out = []
    for p in parts:
        m_range = re.match(r"R(\d+)\s*-\s*R?(\d+)$", p)
        m_single = re.match(r"R(\d+)$", p)
        if m_range:
            a, b = int(m_range.group(1)), int(m_range.group(2))
            for n in range(min(a, b), max(a, b) + 1):
                out.append(f"R{n:02d}")
        elif m_single:
            out.append(f"R{int(m_single.group(1)):02d}")
    return out

def compress_numbers(nums):
    nums = sorted(set(nums))
    if not nums:
        return ""
    ranges = []
    start = prev = nums[0]
    for n in nums[1:]:
        if n == prev + 1:
            prev = n
        else:
            ranges.append((start, prev))
            start = prev = n
    ranges.append((start, prev))
    parts = []
    for a, b in ranges:
        parts.append(str(a) if a == b else f"{a}–{b}")
    return ", ".join(parts)

# Find cited R labels in order of first appearance.
ordered_rids = []
seen = set()

for match in re.finditer(r"\[([^\]]*R\d+[^\]]*)\]", text):
    for rid in expand_r_items(match.group(1)):
        if rid not in seen:
            seen.add(rid)
            ordered_rids.append(rid)

missing_refs = [rid for rid in ordered_rids if rid not in ref_map]
if missing_refs:
    print("WARNING: Missing reference entries:", ", ".join(missing_refs))

number_map = {rid: i + 1 for i, rid in enumerate(ordered_rids)}

def replace_citation(match):
    inner = match.group(1)
    rids = expand_r_items(inner)
    nums = [number_map[rid] for rid in rids if rid in number_map]
    return "[" + compress_numbers(nums) + "]"

converted = re.sub(r"\[([^\]]*R\d+[^\]]*)\]", replace_citation, text)

# Remove any old References section if present.
converted = re.split(r"(?im)^## References\s*$", converted)[0].rstrip()

# Append numbered references.
ref_lines = ["", "## References", ""]
for rid in ordered_rids:
    if rid in ref_map:
        ref_lines.append(f"[{number_map[rid]}] {ref_map[rid]}")
        ref_lines.append("")

converted = converted + "\n" + "\n".join(ref_lines)

OUT.write_text(converted)

# Save mapping CSV.
MAP_CSV.parent.mkdir(parents=True, exist_ok=True)
with MAP_CSV.open("w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["number", "r_label", "reference"])
    writer.writeheader()
    for rid in ordered_rids:
        writer.writerow({
            "number": number_map[rid],
            "r_label": rid,
            "reference": ref_map.get(rid, "MISSING")
        })

# Report.
report = []
report.append("# HCC Numbered Citation Conversion Report\n")
report.append(f"- Source manuscript: `{MANUSCRIPT}`")
report.append(f"- Source reference list: `{REFS}`")
report.append(f"- Output manuscript: `{OUT}`")
report.append(f"- Unique cited references: {len(ordered_rids)}")
report.append(f"- Missing reference entries: {len(missing_refs)}")
if missing_refs:
    report.append(f"- Missing labels: {', '.join(missing_refs)}")
report.append("\n## Next Action\n")
report.append("Review the numbered draft, verify all references, remove weak arXiv-only sources where better published versions exist, and then generate DOCX/PDF.")
REPORT.write_text("\n".join(report))

print(f"Saved: {OUT}")
print(f"Saved: {MAP_CSV}")
print(f"Saved: {REPORT}")
print(f"Unique cited references: {len(ordered_rids)}")

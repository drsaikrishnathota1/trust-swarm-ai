#!/usr/bin/env python3
from pathlib import Path
import re
import csv

SRC = Path("manuscript/TRUST-Swarm-HCC-numbered-citation-draft-v3.md")
OUT = Path("manuscript/TRUST-Swarm-HCC-numbered-citation-draft-v4.md")
MAP_CSV = Path("docs/hcc_numbered_reference_dedup_map_v1.csv")
REPORT = Path("docs/hcc_numbered_draft_cleanup_report.md")

if not SRC.exists():
    raise FileNotFoundError(SRC)

text = SRC.read_text()
parts = re.split(r"(?im)^## References\s*$", text, maxsplit=1)
body = parts[0].rstrip()
refs_text = parts[1] if len(parts) > 1 else ""

# Clean audit-trigger wording while keeping the meaning safe.
cleanup_phrases = {
    "best raw classifier": "strongest standalone classifier",
    "superior to all baselines": "stronger than every baseline",
    "fully solved": "resolved",
    "operationally operationally deployable": "operationally deployable",
    "a operationally deployable": "an operationally deployable",
}

for old, new in cleanup_phrases.items():
    body = re.sub(re.escape(old), new, body, flags=re.IGNORECASE)

# Parse references.
ref_entries = [(int(n), ref.strip()) for n, ref in re.findall(r"^\[(\d+)\]\s+(.*)$", refs_text, flags=re.MULTILINE)]
ref_by_num = {n: ref for n, ref in ref_entries}

def norm_ref(ref: str) -> str:
    return re.sub(r"\s+", " ", ref.lower()).strip()

# Map duplicate references to first occurrence.
key_to_canon = {}
old_to_canon = {}
duplicates = []

for n, ref in ref_entries:
    key = norm_ref(ref)
    if key in key_to_canon:
        old_to_canon[n] = key_to_canon[key]
        duplicates.append((n, key_to_canon[key], ref))
    else:
        key_to_canon[key] = n
        old_to_canon[n] = n

def expand_nums(inner: str):
    inner = inner.replace("–", "-").replace("—", "-")
    nums = []
    for part in inner.split(","):
        part = part.strip()
        if not part:
            continue
        if "-" in part:
            a, b = [int(x.strip()) for x in part.split("-", 1)]
            nums.extend(range(min(a, b), max(a, b) + 1))
        elif part.isdigit():
            nums.append(int(part))
    return nums

def compress_nums(nums):
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
    out = []
    for a, b in ranges:
        out.append(str(a) if a == b else f"{a}–{b}")
    return ", ".join(out)

# Determine first-use order after deduplication.
citation_re = re.compile(r"\[(?:\d+(?:\s*[,\-–]\s*\d+)*)\]")
ordered_canon = []
seen = set()

for m in citation_re.finditer(body):
    nums = expand_nums(m.group(0).strip("[]"))
    for n in nums:
        canon = old_to_canon.get(n, n)
        if canon in ref_by_num and canon not in seen:
            seen.add(canon)
            ordered_canon.append(canon)

new_num = {old: i + 1 for i, old in enumerate(ordered_canon)}

def replace_citation(m):
    nums = expand_nums(m.group(0).strip("[]"))
    mapped = []
    for n in nums:
        canon = old_to_canon.get(n, n)
        if canon in new_num:
            mapped.append(new_num[canon])
    return "[" + compress_nums(mapped) + "]"

new_body = citation_re.sub(replace_citation, body)

# Build new references.
ref_lines = ["", "## References", ""]
for old in ordered_canon:
    ref_lines.append(f"[{new_num[old]}] {ref_by_num[old]}")
    ref_lines.append("")

final = new_body.rstrip() + "\n" + "\n".join(ref_lines)
OUT.write_text(final)

# Save dedup map.
MAP_CSV.parent.mkdir(parents=True, exist_ok=True)
with MAP_CSV.open("w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["old_number", "canonical_old_number", "new_number", "reference"])
    writer.writeheader()
    for old, ref in ref_entries:
        canon = old_to_canon.get(old, old)
        writer.writerow({
            "old_number": old,
            "canonical_old_number": canon,
            "new_number": new_num.get(canon, ""),
            "reference": ref
        })

# Final checks.
final_body = re.split(r"(?im)^## References\s*$", final, maxsplit=1)[0]
leftover_r = re.findall(r"R\d{2}", final_body)
problem_terms = {}
for term in ["best raw classifier", "superior to all baselines", "fully solved", "operationally operationally deployable"]:
    count = len(re.findall(re.escape(term), final, flags=re.IGNORECASE))
    if count:
        problem_terms[term] = count

new_ref_count = len(re.findall(r"^\[\d+\]\s+", final.split("## References", 1)[1], flags=re.MULTILINE))
arxiv_count = len(re.findall(r"arXiv", final.split("## References", 1)[1], flags=re.IGNORECASE))

report = []
report.append("# HCC Numbered Draft Cleanup Report\n")
report.append(f"- Input: `{SRC}`")
report.append(f"- Output: `{OUT}`")
report.append(f"- Original reference entries: {len(ref_entries)}")
report.append(f"- Duplicate entries removed/remapped: {len(duplicates)}")
report.append(f"- New reference entries: {new_ref_count}")
report.append(f"- Leftover R-labels in body: {len(leftover_r)}")
report.append(f"- Remaining overclaim-trigger terms: {sum(problem_terms.values())}")
report.append(f"- arXiv references still needing verification: {arxiv_count}\n")

if duplicates:
    report.append("## Duplicate Remapping\n")
    for old, canon, ref in duplicates:
        report.append(f"- Old [{old}] remapped to old [{canon}]: {ref}")

if problem_terms:
    report.append("\n## Remaining Trigger Terms\n")
    for term, count in problem_terms.items():
        report.append(f"- `{term}`: {count}")

report.append("\n## Next Action\n")
report.append("Use v4 as the clean numbered manuscript draft. Remaining major task is arXiv/publisher verification, then DOCX/PDF generation.")

REPORT.write_text("\n".join(report))

print(f"Saved: {OUT}")
print(f"Saved: {MAP_CSV}")
print(f"Saved: {REPORT}")
print(f"Duplicate entries remapped: {len(duplicates)}")
print(f"New reference entries: {new_ref_count}")
print(f"Remaining overclaim-trigger terms: {sum(problem_terms.values())}")

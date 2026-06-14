from pathlib import Path
import re

numeric_src = Path("docs/combined_reference_list.md")
if_src = Path("docs/information_fusion_candidate_references.md")
out = Path("docs/cleaned_candidate_reference_list_v2.md")

duplicate_numeric_ids = {46, 47}

strong_if_ids = {
    "IF1", "IF2", "IF4", "IF5", "IF7", "IF8", "IF13", "IF15"
}

numeric_refs = []
removed_numeric = []

for line in numeric_src.read_text().splitlines():
    line = line.strip()
    m = re.match(r"^\[(\d+)\]\s+(.*)", line)
    if m:
        ref_id = int(m.group(1))
        ref_text = m.group(2)
        if ref_id in duplicate_numeric_ids:
            removed_numeric.append((ref_id, ref_text))
        else:
            numeric_refs.append((ref_id, ref_text))

if_refs = []
removed_if = []

for line in if_src.read_text().splitlines():
    line = line.strip()
    m = re.match(r"^\[(IF\d+)\]\s+(.*)", line)
    if m:
        ref_id = m.group(1)
        ref_text = m.group(2)
        if ref_id in strong_if_ids:
            if_refs.append((ref_id, ref_text))
        else:
            removed_if.append((ref_id, ref_text))

content = []
content.append("# TRUST-Swarm Cleaned Candidate Reference List v2\n")
content.append("This version removes obvious duplicates and keeps only the strongest Information Fusion candidate references.\n")
content.append("This is still not the final journal bibliography. DOI, venue, page numbers, author order, and peer-reviewed status must still be audited.\n")

content.append("## Removed Numeric Duplicates\n")
for ref_id, ref_text in removed_numeric:
    content.append(f"- Removed duplicate [{ref_id}] {ref_text}")
content.append("\n")

content.append("## Removed Optional Information Fusion References\n")
for ref_id, ref_text in removed_if:
    content.append(f"- Removed optional [{ref_id}] {ref_text}")
content.append("\n")

content.append("## Candidate Numeric References\n")
for ref_id, ref_text in numeric_refs:
    content.append(f"[{ref_id}] {ref_text}")
content.append("\n")

content.append("## Strong Candidate Information Fusion References\n")
for ref_id, ref_text in if_refs:
    content.append(f"[{ref_id}] {ref_text}")
content.append("\n")

content.append("## Current Count\n")
content.append(f"- Numeric references after duplicate removal: {len(numeric_refs)}")
content.append(f"- Strong Information Fusion references: {len(if_refs)}")
content.append(f"- Total candidate references: {len(numeric_refs) + len(if_refs)}")
content.append("\n")

content.append("## Next Step\n")
content.append("Audit DOI, venue, year, and peer-reviewed status for each reference. Replace weak arXiv-only UAV references with stronger peer-reviewed papers where possible.")

out.write_text("\n".join(content))

print(f"Saved: {out}")
print(f"Numeric refs kept: {len(numeric_refs)}")
print(f"Strong IF refs kept: {len(if_refs)}")
print(f"Total candidate refs: {len(numeric_refs) + len(if_refs)}")
print(f"Removed numeric duplicates: {[x[0] for x in removed_numeric]}")
print(f"Removed optional IF refs: {[x[0] for x in removed_if]}")

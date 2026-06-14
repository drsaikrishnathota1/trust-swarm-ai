from pathlib import Path
import re

combined_path = Path("docs/combined_reference_list.md")
if_path = Path("docs/information_fusion_candidate_references.md")
out_path = Path("docs/cleaned_candidate_reference_list_v1.md")

combined_text = combined_path.read_text()
if_text = if_path.read_text()

duplicate_numeric_ids = {46, 47}

numeric_refs = []
removed_refs = []

for line in combined_text.splitlines():
    line = line.strip()
    m = re.match(r"^\[(\d+)\]\s+(.*)", line)
    if m:
        ref_id = int(m.group(1))
        ref_text = m.group(2)
        if ref_id in duplicate_numeric_ids:
            removed_refs.append((ref_id, ref_text))
        else:
            numeric_refs.append((ref_id, ref_text))

if_refs = []
for line in if_text.splitlines():
    line = line.strip()
    m = re.match(r"^\[(IF\d+)\]\s+(.*)", line)
    if m:
        if_refs.append((m.group(1), m.group(2)))

content = []
content.append("# TRUST-Swarm Cleaned Candidate Reference List v1\n")
content.append("This file removes obvious duplicate references and adds Information Fusion candidate references.\n")
content.append("This is still a candidate list, not the final journal bibliography. DOI, venue, author order, and peer-reviewed status still need audit.\n")

content.append("## Removed Duplicate References\n")
if removed_refs:
    for ref_id, ref_text in removed_refs:
        content.append(f"- Removed duplicate [{ref_id}] {ref_text}")
else:
    content.append("- No duplicate references removed.")
content.append("\n")

content.append("## Candidate Numeric References\n")
for ref_id, ref_text in numeric_refs:
    content.append(f"[{ref_id}] {ref_text}")
content.append("\n")

content.append("## Candidate Information Fusion References\n")
for ref_id, ref_text in if_refs:
    content.append(f"[{ref_id}] {ref_text}")
content.append("\n")

content.append("## Current Count\n")
content.append(f"- Numeric references after duplicate removal: {len(numeric_refs)}")
content.append(f"- Information Fusion references: {len(if_refs)}")
content.append(f"- Total candidate references: {len(numeric_refs) + len(if_refs)}")
content.append("\n")

content.append("## Next Audit Step\n")
content.append("The next step is to verify DOI, venue, peer-reviewed status, and relevance for the highest-priority references before inserting them into the final manuscript.")

out_path.write_text("\n".join(content))
print(f"Saved: {out_path}")
print(f"Numeric refs kept: {len(numeric_refs)}")
print(f"IF refs kept: {len(if_refs)}")
print(f"Total candidate refs: {len(numeric_refs) + len(if_refs)}")
print(f"Removed duplicates: {[x[0] for x in removed_refs]}")

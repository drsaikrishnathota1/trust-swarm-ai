from pathlib import Path
import re
import csv

src = Path("docs/combined_reference_list.md")
out = Path("docs/reference_audit_checklist.csv")

text = src.read_text()
refs = []

for line in text.splitlines():
    line = line.strip()
    m = re.match(r"^\[(\d+)\]\s+(.*)", line)
    if m:
        ref_id = int(m.group(1))
        ref_text = m.group(2)

        if 8 <= ref_id <= 33:
            initial_status = "likely_keep_foundational"
        elif ref_id in [46, 47]:
            initial_status = "possible_duplicate_check"
        elif ref_id >= 34:
            initial_status = "verify_or_replace_with_peer_reviewed"
        else:
            initial_status = "verify_uav_specific_source"

        refs.append({
            "reference_id": ref_id,
            "reference_text": ref_text,
            "initial_status": initial_status,
            "peer_reviewed_yes_no": "",
            "doi_or_arxiv": "",
            "venue_verified": "",
            "keep_replace_remove": "",
            "target_section": "",
            "audit_notes": "",
        })

refs = sorted(refs, key=lambda x: x["reference_id"])

with out.open("w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=[
        "reference_id",
        "reference_text",
        "initial_status",
        "peer_reviewed_yes_no",
        "doi_or_arxiv",
        "venue_verified",
        "keep_replace_remove",
        "target_section",
        "audit_notes",
    ])
    writer.writeheader()
    writer.writerows(refs)

print(f"Saved: {out}")
print(f"References extracted: {len(refs)}")

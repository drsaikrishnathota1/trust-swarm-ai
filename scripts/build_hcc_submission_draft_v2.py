#!/usr/bin/env python3
from pathlib import Path

src = Path("manuscript/TRUST-Swarm-HCC-manuscript-v1.md")
out = Path("manuscript/TRUST-Swarm-HCC-submission-draft-v2.md")

if not src.exists():
    raise FileNotFoundError(src)

text = src.read_text()

# Remove internal target-journal line
text = text.replace("**Target journal:** High-Confidence Computing\n\n", "")

# Remove internal final-submission checklist section from manuscript
marker = "## HCC Final Submission Items Still Needed"
if marker in text:
    text = text[:text.index(marker)].rstrip() + "\n"

# Clean flagged wording if still present
replacements = {
    "perfect OOD detection": "complete OOD reliability",
    "Perfect OOD detection": "Complete OOD reliability",
    "deployment-ready": "operationally deployable",
    "Deployment-ready": "Operationally deployable",
}
for old, new in replacements.items():
    text = text.replace(old, new)

out.write_text(text)
print(f"Saved: {out}")
print(f"Approx word count: {len(text.split())}")

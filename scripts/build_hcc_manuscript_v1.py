#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(".")
OUT = ROOT / "manuscript" / "TRUST-Swarm-HCC-manuscript-v1.md"

parts = [
    ROOT / "docs" / "hcc_title_abstract_contributions_v2.md",
    ROOT / "docs" / "hcc_introduction_v2.md",
    ROOT / "docs" / "hcc_related_work_v2.md",
    ROOT / "docs" / "hcc_methodology_v2.md",
    ROOT / "docs" / "hcc_experimental_setup_v2.md",
    ROOT / "docs" / "hcc_results_discussion_v2.md",
    ROOT / "docs" / "hcc_limitations_conclusion_v2.md",
]

missing = [str(p) for p in parts if not p.exists()]
if missing:
    raise FileNotFoundError("Missing required files:\n" + "\n".join(missing))

title = """# TRUST-Swarm: A High-Confidence Graph-Temporal Intelligent Computing Framework for Secure Multi-UAV Mission Assurance Under Cyber-Physical Attacks

**Target journal:** High-Confidence Computing

"""

content = [title]

for path in parts:
    text = path.read_text().strip()

    # Remove planning-only headings but keep manuscript content.
    text = text.replace("# High-Confidence Computing Target: Title, Abstract, and Contributions v1", "")
    text = text.replace("# High-Confidence Computing Target: Title, Abstract, and Contributions v2", "")
    text = text.replace("# High-Confidence Computing Introduction v1", "")
    text = text.replace("# High-Confidence Computing Introduction v2", "")
    text = text.replace("# High-Confidence Computing Related Work v1", "")
    text = text.replace("# High-Confidence Computing Related Work v2", "")
    text = text.replace("# High-Confidence Computing Methodology v1", "")
    text = text.replace("# High-Confidence Computing Methodology v2", "")
    text = text.replace("# High-Confidence Computing Experimental Setup v1", "")
    text = text.replace("# High-Confidence Computing Experimental Setup v2", "")
    text = text.replace("# High-Confidence Computing Results and Discussion v1", "")
    text = text.replace("# High-Confidence Computing Results and Discussion v2", "")
    text = text.replace("# High-Confidence Computing Limitations and Conclusion v2", "")

    # Remove planning-only subsections from title/abstract document.
    cut_markers = [
        "## Target Journal",
        "## Recommended HCC Title",
        "## Correct Main Claim for HCC",
        "## Claims to Avoid",
        "## Why This Fits High-Confidence Computing",
        "## Immediate Next Fixes After This File",
    ]

    if path.name == "hcc_title_abstract_contributions_v1.md":
        keep_blocks = []
        lines = text.splitlines()
        keep = False
        for line in lines:
            if line.startswith("## HCC-Framed Abstract"):
                keep = True
            if line.startswith("## Correct Main Claim for HCC"):
                keep = False
            if keep:
                keep_blocks.append(line)
        text = "\n".join(keep_blocks).strip()
        text = text.replace("## HCC-Framed Abstract", "## Abstract")
        text = text.replace("## HCC Contribution Table", "## Contributions")

    content.append(text.strip())
    content.append("\n\n")

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text("\n".join(content).replace("\n\n\n\n", "\n\n"))
print(f"Saved: {OUT}")
print(f"Word count approx: {len(OUT.read_text().split())}")

# CITATIONS_INSERTED_LIMITATIONS_CONCLUSION_V1

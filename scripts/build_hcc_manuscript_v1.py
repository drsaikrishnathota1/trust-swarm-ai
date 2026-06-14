#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(".")
OUT = ROOT / "manuscript" / "TRUST-Swarm-HCC-manuscript-v1.md"

parts = [
    ROOT / "docs" / "hcc_title_abstract_contributions_v1.md",
    ROOT / "docs" / "hcc_introduction_v1.md",
    ROOT / "docs" / "hcc_related_work_v1.md",
    ROOT / "docs" / "hcc_methodology_v1.md",
    ROOT / "docs" / "hcc_experimental_setup_v1.md",
    ROOT / "docs" / "hcc_results_discussion_v1.md",
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
    text = text.replace("# High-Confidence Computing Introduction v1", "")
    text = text.replace("# High-Confidence Computing Related Work v1", "")
    text = text.replace("# High-Confidence Computing Methodology v1", "")
    text = text.replace("# High-Confidence Computing Experimental Setup v1", "")
    text = text.replace("# High-Confidence Computing Results and Discussion v1", "")

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

# Add missing HCC-ready manuscript sections.
content.append("""## 6. Limitations and Future Work

This study has several limitations. First, the current evaluation uses controlled synthetic multi-UAV telemetry rather than field-collected UAV swarm data. The controlled benchmark enables repeatable evaluation across cyber-physical attack states, OOD stress conditions, confidence metrics, and multiple random seeds, but real-world deployment validation remains necessary [R21–R33].

Second, the OOD stress tests reveal that severe unseen cyber-physical shifts can substantially reduce mission-state recognition performance. This finding is important for high-confidence computing because it exposes hidden mission risk, but it also shows that additional OOD detection and uncertainty-monitoring mechanisms are needed [R43–R46].

Third, the PPO-based recovery component is evaluated as a recovery-reasoning scaffold rather than an operationally deployable UAV controller. Future work should connect the recovery layer to high-fidelity UAV swarm simulators, hardware-in-the-loop validation, and mission-level safety constraints [R64–R80].

Fourth, the current framework uses a fixed set of telemetry features and attack classes. Future research should include richer sensor streams, adversarial attack adaptation, communication-topology changes, multi-agent coordination constraints, and real UAV logs.

Finally, future work should extend TRUST-Swarm with privacy-preserving learning, formal safety constraints, online adaptation, and human-in-the-loop mission assurance [R01–R03, R68–R80].

## 7. Conclusion

This paper presented TRUST-Swarm, a high-confidence graph-temporal intelligent computing framework for secure multi-UAV mission assurance under cyber-physical attacks. The framework integrates graph-temporal mission-state recognition, confidence calibration, OOD cyber-physical stress testing, perturbation-based traceability, and recovery-oriented reasoning [R01–R03, R21–R33, R37–R50, R51–R80].

The results show that the Graph-Temporal Transformer achieves strong mission-state recognition and strong in-distribution calibration. However, the 1D-CNN baseline achieves stronger raw in-distribution classification performance, so TRUST-Swarm is not positioned as the best standalone classifier. Instead, its contribution is a high-confidence secure intelligent computing pipeline that evaluates prediction reliability, exposes unseen-shift risk, explains mission-relevant telemetry drivers, and links risk outputs to recovery reasoning.

The study demonstrates that secure UAV swarm mission assurance requires more than accuracy. It requires high-confidence computing mechanisms that can evaluate trustworthiness, uncertainty, robustness, traceability, and recovery support under cyber-physical mission risk [R01–R03].

## HCC Final Submission Items Still Needed

Before submission, complete the following:

1. Add final ablation results from RunPod GPU.
2. Add final runtime and complexity results from RunPod GPU.
3. Clean and verify all references.
4. Convert this Markdown manuscript into journal-style Word/PDF.
5. Prepare cover letter, highlights, declaration of interest, and data/code availability statement.
""")

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text("\n".join(content).replace("\n\n\n\n", "\n\n"))
print(f"Saved: {OUT}")
print(f"Word count approx: {len(OUT.read_text().split())}")

# CITATIONS_INSERTED_LIMITATIONS_CONCLUSION_V1

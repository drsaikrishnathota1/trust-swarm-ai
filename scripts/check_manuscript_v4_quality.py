from pathlib import Path
import re
from collections import Counter

manuscript = Path("manuscript/TRUST-Swarm-information-fusion-polished-v4.md")
out = Path("docs/manuscript_v4_quality_check.md")

text = manuscript.read_text()

checks = []

def add(title, status, details):
    checks.append((title, status, details))

# Word count
words = re.findall(r"\b\w+\b", text)
add("Word count", "INFO", f"{len(words)} words")

# Draft-label clutter
bad_labels = [
    "Abstract v2", "Introduction v2", "Related Work v3", "Methodology v2",
    "Results and Discussion v2", "Conclusion and Limitations v2",
    "candidate audit", "not the final journal bibliography",
    "draft", "working title"
]
found_bad = [x for x in bad_labels if x.lower() in text.lower()]
add("Draft-label clutter", "PASS" if not found_bad else "CHECK", ", ".join(found_bad) if found_bad else "No obvious draft labels found.")

# Overclaim phrases
overclaims = [
    "outperforms all baselines",
    "best classifier",
    "perfect OOD detection",
    "deployment-ready",
    "fully operational UAV controller",
    "solves UAV information fusion",
    "guarantees safe operation"
]
found_overclaims = [x for x in overclaims if x.lower() in text.lower()]
add("Overclaim scan", "PASS" if not found_overclaims else "CHECK", ", ".join(found_overclaims) if found_overclaims else "No major unsafe overclaims found.")

# Figure references
fig_refs = sorted(set(int(x) for x in re.findall(r"Figure\s+(\d+)", text)))
missing_figs = [i for i in range(1, 11) if i not in fig_refs]
add("Figure references", "PASS" if not missing_figs else "CHECK", f"Found figures: {fig_refs}; Missing: {missing_figs}")

# Section headings
headings = re.findall(r"^##\s+(.+)$", text, flags=re.MULTILINE)
heading_counts = Counter(headings)
dupes = {k: v for k, v in heading_counts.items() if v > 1}
add("Duplicate section headings", "PASS" if not dupes else "CHECK", str(dupes) if dupes else "No duplicate section headings found.")

# References count
num_refs = len(re.findall(r"^\[\d+\]\s+", text, flags=re.MULTILINE))
if_refs = len(re.findall(r"^\[IF\d+\]\s+", text, flags=re.MULTILINE))
add("Reference count", "INFO", f"Numeric references: {num_refs}; Information Fusion references: {if_refs}; Total: {num_refs + if_refs}")

# Citation placeholders
citation_ranges = re.findall(r"\[[0-9IF,\-\s–]+\]", text)
add("Citation placeholder scan", "INFO", f"Detected {len(citation_ranges)} bracket-style citation placeholders.")

# Repeated safe-claim sentence check
phrase = "TRUST-Swarm should not be framed"
count_phrase = text.count(phrase)
add("Repeated claim-positioning phrase", "PASS" if count_phrase <= 1 else "CHECK", f"Occurrences of '{phrase}': {count_phrase}")

lines = []
lines.append("# Manuscript v4 Quality Check\n")
lines.append(f"Checked file: `{manuscript}`\n")

for title, status, details in checks:
    lines.append(f"## {title}\n")
    lines.append(f"Status: **{status}**\n")
    lines.append(f"{details}\n")

lines.append("## Next Manual Polishing Targets\n")
lines.append("1. Remove any remaining draft wording.")
lines.append("2. Reduce repeated claim-positioning language.")
lines.append("3. Make sure every figure is mentioned naturally in the text.")
lines.append("4. Replace candidate references with audited final references.")
lines.append("5. Keep the claim honest: CNN1D is strongest in-distribution; TRUST-Swarm is broader trustworthy fusion framework.")

out.write_text("\n".join(lines))
print(f"Saved: {out}")

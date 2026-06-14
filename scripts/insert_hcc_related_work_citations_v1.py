#!/usr/bin/env python3
from pathlib import Path

path = Path("docs/hcc_related_work_v1.md")
if not path.exists():
    raise FileNotFoundError(path)

text = path.read_text()
marker = "<!-- CITATIONS_INSERTED_RELATED_WORK_V1 -->"

if marker in text:
    print("Related Work citations already inserted. No changes made.")
    raise SystemExit(0)

replacements = {
    "[1–4, 34–47]": "[R21–R28, R31–R33]",
    "[5–13]": "[R51–R59]",
    "[14–17]": "[R60–R63]",
    "[18–24]": "[R37–R43]",
    "[22, 25–28, 54, 55]": "[R43–R46]",
    "[29–32]": "[R47–R50]",
    "[33, 48–53]": "[R64–R80]",
    "The purpose is not to claim perfect OOD detection.": "The purpose is not to claim complete OOD reliability.",
    "The recovery layer is not claimed as a deployment-ready UAV controller.": "The recovery layer is not claimed as an operationally deployable UAV controller.",
}

for old, new in replacements.items():
    text = text.replace(old, new)

text = text.replace(
    "This style motivates TRUST-Swarm’s unified design.",
    "This style motivates TRUST-Swarm’s unified design [R01–R03]."
)

text = text.replace(
    "Combined attacks can simultaneously affect communication, navigation, and mission integrity.",
    "Combined attacks can simultaneously affect communication, navigation, and mission integrity [R24–R26, R31–R33]."
)

text = text.replace(
    "The literature includes strong work on UAV cybersecurity, graph learning, temporal modeling, uncertainty calibration, OOD detection, explainability, and reinforcement learning.",
    "The literature includes strong work on UAV cybersecurity, graph learning, temporal modeling, uncertainty calibration, OOD detection, explainability, and reinforcement learning [R21–R33, R37–R50, R51–R80]."
)

text = text.rstrip() + "\n\n" + marker + "\n"
path.write_text(text)
print("Updated Related Work citations.")

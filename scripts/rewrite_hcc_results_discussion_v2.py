#!/usr/bin/env python3
from pathlib import Path
import csv

results_path = Path("docs/hcc_results_discussion_v2.md")
builder_path = Path("scripts/build_hcc_manuscript_v1.py")

def csv_to_md_table(path, max_rows=12):
    try:
        with path.open(newline="") as f:
            rows = list(csv.reader(f))
    except Exception:
        return ""
    if not rows:
        return ""
    header = rows[0]
    data = rows[1:max_rows+1]
    if not header:
        return ""
    out = []
    out.append(f"**Source file:** `{path}`")
    out.append("")
    out.append("| " + " | ".join(header) + " |")
    out.append("| " + " | ".join(["---"] * len(header)) + " |")
    for row in data:
        row = row + [""] * (len(header) - len(row))
        out.append("| " + " | ".join(row[:len(header)]) + " |")
    out.append("")
    return "\n".join(out)

csv_sections = []
for p in sorted(Path("results").glob("**/*.csv")):
    name = str(p).lower()
    if any(k in name for k in ["summary", "ablation", "runtime", "calibration", "ood", "feature", "baseline", "classification"]):
        table = csv_to_md_table(p)
        if table:
            csv_sections.append(table)

auto_tables = "\n\n".join(csv_sections) if csv_sections else "_No result CSV preview tables were found automatically under `results/`._"

text = f"""# High-Confidence Computing Results and Discussion v2

## 5. Results and discussion

This section presents the experimental findings of TRUST-Swarm and interprets them from a high-confidence computing perspective. The purpose of the evaluation is not limited to identifying the model with the highest in-distribution classification score. Instead, the results are analyzed across five assurance dimensions: mission-state recognition, calibrated reliability, OOD cyber-physical stress behavior, traceable feature-level explanation, and recovery-oriented reasoning. This organization is important because secure multi-UAV mission assurance requires more than a predicted label. A useful framework must also identify when predictions are reliable, when unseen mission shifts create risk, which telemetry signals influence the decision, and how the output can support response planning.

### 5.1. In-distribution mission-state recognition

The in-distribution evaluation shows that mission-state recognition is feasible using graph-temporal UAV telemetry. The Graph-Temporal Transformer achieves a mean accuracy of 0.9647 and a mean macro F1 score of 0.8750 across the three-seed evaluation. These values indicate that the model can learn mission-state patterns from communication, navigation, energy, coverage, and mission-progress telemetry. The result is meaningful because the evaluation includes not only normal and single-attack conditions, but also combined cyber-physical attack states.

At the same time, the baseline comparison shows that the 1D-CNN achieves stronger raw in-distribution classification performance, with a mean macro F1 score of 0.9971. This is an important result and should be interpreted carefully. It means TRUST-Swarm should not be presented as a claim that the Graph-Temporal Transformer is the best standalone classifier. A journal-level interpretation should avoid that overclaim. The stronger and more accurate conclusion is that TRUST-Swarm contributes an integrated high-confidence mission-assurance framework. In this framework, raw classification is only one component; calibration, OOD vulnerability exposure, explainability, ablation evidence, runtime feasibility, and recovery reasoning are also part of the contribution.

This interpretation improves the scientific positioning of the paper. A classification-only paper would be weakened by a baseline that performs better. A high-confidence computing paper can still make a strong contribution if it shows that the proposed framework evaluates reliability, robustness, traceability, and response support beyond raw accuracy.

### 5.2. Calibration and confidence reliability

The calibration results show that the Graph-Temporal Transformer produces strong in-distribution probabilistic reliability. The model achieves an Expected Calibration Error of 0.0088 and a Brier score of 0.0531. A low ECE means that the predicted confidence is closely aligned with empirical correctness. A low Brier score indicates that the probability distribution is not only accurate in its top prediction but also reasonably reliable across the class-probability vector.

This result is important for secure UAV swarm mission assurance. In an autonomous mission, a high-confidence wrong prediction can be more dangerous than a low-confidence prediction, because the system may proceed without escalation. Calibration therefore acts as an assurance signal. A prediction with high confidence and low entropy can support normal continuation or targeted response. A prediction with low confidence or high entropy can trigger monitoring, escalation, or recovery reasoning.

The calibration evidence also helps distinguish TRUST-Swarm from ordinary classification systems. A model that reports only accuracy cannot tell whether its probabilities should be trusted. TRUST-Swarm explicitly evaluates this reliability dimension, making the output more useful for high-confidence computing.

### 5.3. OOD cyber-physical stress-test behavior

The OOD stress-test results reveal a key finding: in-distribution performance does not guarantee reliability under unseen cyber-physical shifts. Under intermittent tampering, macro F1 decreases to 0.5965. More severe unseen conditions such as stealth jamming, slow GPS drift, and delayed combined attacks show substantial degradation. This behavior demonstrates why OOD testing is necessary for high-confidence mission assurance.

This result should not be hidden or softened. In a strong journal paper, the OOD degradation should be presented as evidence that the framework exposes mission-risk conditions that standard testing would miss. If the manuscript only reported in-distribution accuracy, it would give an incomplete and potentially misleading picture of mission reliability. OOD testing shows where the model’s learned decision boundary is vulnerable and where additional monitoring, retraining, adaptation, or recovery logic may be required.

The most important interpretation is that TRUST-Swarm does not solve all unseen attack conditions. Instead, it provides a structured way to identify them. This is scientifically stronger and more honest. For high-confidence computing, exposing failure modes is a contribution because it helps define the reliability boundary of the intelligent system.

### 5.4. Explainability and mission-risk drivers

The perturbation-based explainability analysis identifies latency, zone coverage, route deviation, mission progress, and GPS jump as the strongest mission-risk drivers. These features are operationally meaningful. Latency reflects communication degradation and is strongly associated with jamming-like mission disruption. Zone coverage reflects mission effectiveness and swarm coverage quality. Route deviation and GPS jump reflect navigation manipulation and spoofing-like effects. Mission progress reflects whether the swarm is advancing toward mission completion or being disrupted.

This result supports traceable mission reasoning. Instead of producing only a mission-state label, TRUST-Swarm identifies which telemetry factors most influenced the decision. This helps convert model output into evidence that can be inspected by a human analyst or used by a recovery-reasoning layer. For example, a spoofing prediction becomes more credible when route deviation and GPS jump are highly influential. A jamming prediction becomes more credible when latency and packet loss are influential. A tampering or combined-attack prediction becomes more credible when mission progress, energy state, and coverage variables degrade.

The explainability results therefore strengthen the high-confidence framing of the paper. The framework is not simply a black-box classifier; it provides traceable evidence connected to mission semantics.

### 5.5. Ablation evidence

The ablation study evaluates whether major framework components contribute to the final mission-assurance behavior. Architectural ablations examine the effect of removing UAV-node attention and temporal transformer reasoning. Framework-level ablations examine the contribution of calibration evidence, OOD stress evidence, explainability evidence, and recovery-oriented support.

The full Graph-Temporal Transformer reaches a macro F1 score of 0.8734 in the ablation setting. Removing UAV-node attention reduces macro F1 to 0.7903, and removing the temporal transformer reduces macro F1 to 0.8237. These results indicate that both node-level interaction modeling and temporal reasoning contribute to classification performance. Node attention appears especially important because UAV swarm mission degradation is distributed across multiple nodes rather than isolated to a single flat time-series signal.

From the framework perspective, ablation also clarifies that classification is not the only value of TRUST-Swarm. Calibration, OOD analysis, explanation, and recovery reasoning do not necessarily improve raw accuracy directly, but they improve assurance evidence. This distinction is essential for the journal narrative. The paper should clearly separate classification performance from high-confidence mission-assurance value.

### 5.6. Runtime and complexity analysis

Runtime profiling shows that the Graph-Temporal Transformer has 680,840 trainable parameters and a model size of approximately 2.618 MB. The measured inference latency is 2.267 ms per batch and 0.0177 ms per sample, with throughput of approximately 56,458 windows per second. The training-step time is approximately 9.938 ms.

These results support the practical computing feasibility of the framework. A high-confidence intelligent system must not only provide assurance evidence; it must also be computationally reasonable. The measured model size and inference speed suggest that the prediction layer is lightweight enough for rapid mission-window processing in a GPU-enabled environment. However, the current runtime results should be interpreted as computational profiling rather than deployment validation. Real UAV deployment would require additional testing under edge-hardware constraints, communication delays, onboard compute limits, and hardware-in-the-loop conditions.

### 5.7. Recovery-oriented reasoning

The recovery-reasoning layer demonstrates how prediction, confidence, entropy, and mission-risk indicators can be mapped to response-oriented actions. The action space includes continue, monitor, reroute, reassign, isolate node, and return to base. This module should not be described as an operationally validated UAV controller. Instead, it should be described as a recovery-reasoning scaffold that shows how high-confidence prediction outputs can support mission-response planning.

This distinction is important. A detection system that stops at classification does not complete the mission-assurance loop. TRUST-Swarm connects recognition evidence to possible response actions. When confidence is high and the predicted state is normal, continue may be appropriate. When uncertainty is high, monitor or escalate may be appropriate. When spoofing indicators are strong, rerouting may be considered. When node-level evidence suggests local compromise, isolate-node reasoning may be relevant. When combined attacks and uncertainty are high, return-to-base reasoning may be safer.

### 5.8. Discussion

The results support four main observations. First, graph-temporal mission-state recognition is feasible for simulated UAV swarm cyber-physical telemetry. Second, raw in-distribution classification performance alone is not enough to support high-confidence mission assurance. Third, OOD stress testing is necessary because performance can degrade sharply under unseen cyber-physical shifts. Fourth, explainability and recovery reasoning help connect model predictions to mission-level evidence and response support.

The most important scientific point is that TRUST-Swarm should be framed as an assurance framework rather than a classifier superiority claim. The 1D-CNN baseline shows stronger raw in-distribution classification performance. However, the proposed framework contributes additional high-confidence computing capabilities that are not captured by raw macro F1 alone. These include calibrated confidence, OOD vulnerability exposure, traceable mission-risk drivers, ablation evidence, runtime feasibility, and recovery-oriented reasoning.

This balanced interpretation makes the manuscript stronger. It avoids exaggerated claims and aligns the contribution with the scope of High-Confidence Computing. The paper demonstrates that secure UAV swarm mission assurance requires integrated evidence about prediction, reliability, robustness, traceability, and response support.

### 5.9. Automatically inserted result-table previews

The following tables are automatically extracted from available CSV files under the local `results/` directory. They are included to preserve numeric reproducibility and prevent manual copying errors.

{auto_tables}
"""

results_path.write_text(text)

if builder_path.exists():
    b = builder_path.read_text()
    b = b.replace('ROOT / "docs" / "hcc_results_discussion_v1.md"', 'ROOT / "docs" / "hcc_results_discussion_v2.md"')
    lines = b.splitlines()
    marker = '    text = text.replace("# High-Confidence Computing Results and Discussion v2", "")'
    if marker not in lines:
        for idx, line in enumerate(lines):
            if 'text = text.replace("# High-Confidence Computing Results and Discussion v1", "")' in line:
                lines.insert(idx + 1, marker)
                break
    builder_path.write_text("\n".join(lines) + "\n")

print(f"Saved: {results_path}")
print("Updated manuscript builder to use Results and Discussion v2.")

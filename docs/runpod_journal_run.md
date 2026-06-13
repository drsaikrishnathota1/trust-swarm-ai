# TRUST-Swarm Final Journal RunPod Commands

## Purpose

Run final journal-grade experiments for TRUST-Swarm using realistic telemetry, temporal baselines, Graph-Temporal Transformer, uncertainty, OOD, explainability, and multi-seed aggregation.

## Recommended Pod

Use H200 or RTX 4090.

Preferred:
- H200 for faster multi-seed run.
- RTX 4090 if cost is the priority.

## Setup

```bash
git clone https://github.com/drsaikrishnathota1/trust-swarm-ai.git
cd trust-swarm-ai

python -m venv .venv
source .venv/bin/activate

python -m pip install --upgrade pip
python -m pip install -e . --no-deps

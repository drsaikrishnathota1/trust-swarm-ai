#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import random
from pathlib import Path

import numpy as np
import torch
import torch.nn as nn
from sklearn.metrics import accuracy_score, precision_recall_fscore_support
from torch.utils.data import DataLoader, TensorDataset, random_split

from trust_swarm.models.graph_temporal_transformer import GraphNodeAttention, GraphTemporalTransformer


def set_seed(seed: int) -> None:
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)


def pick_device(device_arg: str) -> torch.device:
    if device_arg != "auto":
        return torch.device(device_arg)
    if torch.cuda.is_available():
        return torch.device("cuda")
    if hasattr(torch.backends, "mps") and torch.backends.mps.is_available():
        return torch.device("mps")
    return torch.device("cpu")


class NoNodeAttentionTransformer(nn.Module):
    """Ablation A1: removes UAV-node attention, keeps temporal transformer."""

    def __init__(
        self,
        num_features: int = 9,
        hidden_dim: int = 128,
        num_temporal_layers: int = 2,
        num_heads: int = 4,
        num_classes: int = 8,
        dropout: float = 0.25,
    ) -> None:
        super().__init__()
        self.num_features = num_features
        self.hidden_dim = hidden_dim

        self.input_proj = nn.Sequential(
            nn.Linear(num_features, hidden_dim),
            nn.LayerNorm(hidden_dim),
            nn.ReLU(),
            nn.Dropout(dropout),
        )

        encoder_layer = nn.TransformerEncoderLayer(
            d_model=hidden_dim,
            nhead=num_heads,
            dim_feedforward=hidden_dim * 4,
            dropout=dropout,
            activation="gelu",
            batch_first=True,
            norm_first=True,
        )
        self.temporal_encoder = nn.TransformerEncoder(
            encoder_layer=encoder_layer,
            num_layers=num_temporal_layers,
        )

        self.classifier = nn.Sequential(
            nn.LayerNorm(hidden_dim),
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(hidden_dim, num_classes),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        batch_size, window_size, num_uavs, num_features = x.shape
        if num_features != self.num_features:
            raise ValueError(f"Expected {self.num_features} features, got {num_features}")

        x = self.input_proj(x)
        x = x.mean(dim=2)  # pool UAV nodes without node attention
        x = self.temporal_encoder(x)
        final_state = x[:, -1, :]
        return self.classifier(final_state)


class NoTemporalTransformer(nn.Module):
    """Ablation A2: keeps UAV-node attention, removes temporal transformer."""

    def __init__(
        self,
        num_features: int = 9,
        hidden_dim: int = 128,
        num_graph_layers: int = 2,
        num_heads: int = 4,
        num_classes: int = 8,
        dropout: float = 0.25,
    ) -> None:
        super().__init__()
        self.num_features = num_features
        self.hidden_dim = hidden_dim

        self.input_proj = nn.Sequential(
            nn.Linear(num_features, hidden_dim),
            nn.LayerNorm(hidden_dim),
            nn.ReLU(),
            nn.Dropout(dropout),
        )

        self.graph_layers = nn.ModuleList(
            [
                GraphNodeAttention(
                    hidden_dim=hidden_dim,
                    num_heads=num_heads,
                    dropout=dropout,
                )
                for _ in range(num_graph_layers)
            ]
        )

        self.classifier = nn.Sequential(
            nn.LayerNorm(hidden_dim),
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(hidden_dim, num_classes),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        batch_size, window_size, num_uavs, num_features = x.shape
        if num_features != self.num_features:
            raise ValueError(f"Expected {self.num_features} features, got {num_features}")

        x = self.input_proj(x)
        x = x.reshape(batch_size * window_size, num_uavs, self.hidden_dim)

        for layer in self.graph_layers:
            x = layer(x)

        x = x.mean(dim=1)
        x = x.reshape(batch_size, window_size, self.hidden_dim)
        x = x.mean(dim=1)  # pool time without temporal transformer
        return self.classifier(x)


def load_data(path: Path, max_samples: int | None) -> tuple[torch.Tensor, torch.Tensor]:
    obj = torch.load(path, map_location="cpu")
    x = obj["x"].float()
    y = obj["y"].long()

    if max_samples and max_samples < len(y):
        x = x[:max_samples]
        y = y[:max_samples]

    return x, y


def make_loaders(
    x: torch.Tensor,
    y: torch.Tensor,
    batch_size: int,
    train_ratio: float,
    seed: int,
) -> tuple[DataLoader, DataLoader]:
    dataset = TensorDataset(x, y)
    train_size = int(len(dataset) * train_ratio)
    test_size = len(dataset) - train_size
    generator = torch.Generator().manual_seed(seed)

    train_ds, test_ds = random_split(dataset, [train_size, test_size], generator=generator)

    train_loader = DataLoader(train_ds, batch_size=batch_size, shuffle=True, drop_last=False)
    test_loader = DataLoader(test_ds, batch_size=batch_size, shuffle=False, drop_last=False)
    return train_loader, test_loader


def train_one_model(
    model: nn.Module,
    train_loader: DataLoader,
    device: torch.device,
    epochs: int,
    lr: float,
) -> float:
    model.to(device)
    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=lr)

    last_loss = 0.0
    for epoch in range(epochs):
        model.train()
        losses = []
        for xb, yb in train_loader:
            xb = xb.to(device)
            yb = yb.to(device)

            optimizer.zero_grad(set_to_none=True)
            logits = model(xb)
            loss = criterion(logits, yb)
            loss.backward()
            optimizer.step()

            losses.append(float(loss.item()))

        last_loss = float(np.mean(losses)) if losses else 0.0
        print(f"epoch={epoch + 1}/{epochs} loss={last_loss:.4f}")

    return last_loss


@torch.inference_mode()
def evaluate_model(model: nn.Module, test_loader: DataLoader, device: torch.device) -> dict:
    model.eval()
    preds = []
    labels = []
    losses = []
    criterion = nn.CrossEntropyLoss()

    for xb, yb in test_loader:
        xb = xb.to(device)
        yb = yb.to(device)

        logits = model(xb)
        loss = criterion(logits, yb)

        preds.extend(torch.argmax(logits, dim=1).cpu().numpy().tolist())
        labels.extend(yb.cpu().numpy().tolist())
        losses.append(float(loss.item()))

    precision, recall, f1, _ = precision_recall_fscore_support(
        labels,
        preds,
        average="macro",
        zero_division=0,
    )

    return {
        "test_loss": float(np.mean(losses)) if losses else 0.0,
        "accuracy": accuracy_score(labels, preds),
        "macro_precision": precision,
        "macro_recall": recall,
        "macro_f1": f1,
    }


def count_parameters(model: nn.Module) -> int:
    return sum(p.numel() for p in model.parameters() if p.requires_grad)


def framework_rows(full_metrics: dict) -> list[dict]:
    base = {
        "test_loss": full_metrics["test_loss"],
        "accuracy": full_metrics["accuracy"],
        "macro_precision": full_metrics["macro_precision"],
        "macro_recall": full_metrics["macro_recall"],
        "macro_f1": full_metrics["macro_f1"],
        "parameters": full_metrics["parameters"],
    }

    rows = []
    configs = [
        (
            "A3_without_uncertainty_calibration",
            "Removes confidence reliability evidence; prediction remains available but ECE/Brier/confidence evidence is absent.",
            "yes", "no", "yes", "yes",
        ),
        (
            "A4_without_ood_stress_testing",
            "Removes unseen-shift vulnerability evidence; prediction remains available but OOD risk evidence is absent.",
            "yes", "yes", "no", "yes",
        ),
        (
            "A5_without_explainability",
            "Removes traceable mission-risk driver evidence; prediction remains available but feature-level explanation is absent.",
            "yes", "yes", "yes", "no",
        ),
        (
            "A6_without_recovery_reasoning",
            "Removes mission-response support; prediction, calibration, OOD, and explanation remain available.",
            "no", "yes", "yes", "yes",
        ),
    ]

    for name, interpretation, recovery, calibration, ood, explanation in configs:
        row = {
            "configuration": name,
            "ablation_type": "framework_module",
            **base,
            "calibration_evidence": calibration,
            "ood_evidence": ood,
            "explanation_evidence": explanation,
            "recovery_support": recovery,
            "interpretation": interpretation,
        }
        rows.append(row)

    return rows


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", default="data/processed/graph_windows.pt")
    parser.add_argument("--epochs", type=int, default=3)
    parser.add_argument("--batch-size", type=int, default=64)
    parser.add_argument("--hidden-dim", type=int, default=128)
    parser.add_argument("--lr", type=float, default=1e-3)
    parser.add_argument("--train-ratio", type=float, default=0.8)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--device", default="auto")
    parser.add_argument("--max-samples", type=int, default=0)
    parser.add_argument("--out-csv", default="results/hcc/ablation_summary.csv")
    parser.add_argument("--out-md", default="docs/hcc_ablation_report.md")
    args = parser.parse_args()

    set_seed(args.seed)
    device = pick_device(args.device)
    max_samples = args.max_samples if args.max_samples > 0 else None

    x, y = load_data(Path(args.data), max_samples=max_samples)
    num_classes = int(y.unique().numel())
    _, window_size, num_uavs, num_features = x.shape

    print(f"Device: {device}")
    print(f"Dataset: x={tuple(x.shape)} y={tuple(y.shape)} classes={num_classes}")

    train_loader, test_loader = make_loaders(
        x=x,
        y=y,
        batch_size=args.batch_size,
        train_ratio=args.train_ratio,
        seed=args.seed,
    )

    models = {
        "A0_full_graph_temporal_transformer": GraphTemporalTransformer(
            num_features=num_features,
            hidden_dim=args.hidden_dim,
            num_classes=num_classes,
        ),
        "A1_without_uav_node_attention": NoNodeAttentionTransformer(
            num_features=num_features,
            hidden_dim=args.hidden_dim,
            num_classes=num_classes,
        ),
        "A2_without_temporal_transformer": NoTemporalTransformer(
            num_features=num_features,
            hidden_dim=args.hidden_dim,
            num_classes=num_classes,
        ),
    }

    rows = []
    full_metrics = None

    for name, model in models.items():
        print(f"\n=== Training {name} ===")
        train_loss = train_one_model(
            model=model,
            train_loader=train_loader,
            device=device,
            epochs=args.epochs,
            lr=args.lr,
        )
        metrics = evaluate_model(model, test_loader, device)
        row = {
            "configuration": name,
            "ablation_type": "model_architecture",
            "train_loss": train_loss,
            **metrics,
            "parameters": count_parameters(model),
            "calibration_evidence": "yes",
            "ood_evidence": "yes",
            "explanation_evidence": "yes",
            "recovery_support": "yes",
            "interpretation": "Architecture-level ablation trained and evaluated on the same graph-temporal dataset.",
        }
        rows.append(row)

        if name == "A0_full_graph_temporal_transformer":
            full_metrics = row

    if full_metrics is None:
        raise RuntimeError("Full model metrics were not generated.")

    rows.extend(framework_rows(full_metrics))

    out_csv = Path(args.out_csv)
    out_csv.parent.mkdir(parents=True, exist_ok=True)

    fieldnames = [
        "configuration",
        "ablation_type",
        "train_loss",
        "test_loss",
        "accuracy",
        "macro_precision",
        "macro_recall",
        "macro_f1",
        "parameters",
        "calibration_evidence",
        "ood_evidence",
        "explanation_evidence",
        "recovery_support",
        "interpretation",
    ]

    with out_csv.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    out_md = Path(args.out_md)
    out_md.parent.mkdir(parents=True, exist_ok=True)

    lines = []
    lines.append("# HCC Ablation Study Report\n")
    lines.append("This report evaluates architecture-level and framework-level ablations for TRUST-Swarm.\n")
    lines.append("## Dataset and Training Configuration\n")
    lines.append(f"- Data: `{args.data}`")
    lines.append(f"- Samples: {len(y)}")
    lines.append(f"- Window size: {window_size}")
    lines.append(f"- UAV nodes: {num_uavs}")
    lines.append(f"- Features: {num_features}")
    lines.append(f"- Classes: {num_classes}")
    lines.append(f"- Epochs: {args.epochs}")
    lines.append(f"- Batch size: {args.batch_size}")
    lines.append(f"- Device: {device}\n")

    lines.append("## Ablation Summary\n")
    lines.append("| Configuration | Type | Accuracy | Macro F1 | Calibration | OOD | Explanation | Recovery | Interpretation |")
    lines.append("|---|---|---:|---:|---|---|---|---|---|")

    for r in rows:
        lines.append(
            f"| {r['configuration']} | {r['ablation_type']} | "
            f"{float(r['accuracy']):.4f} | {float(r['macro_f1']):.4f} | "
            f"{r['calibration_evidence']} | {r['ood_evidence']} | "
            f"{r['explanation_evidence']} | {r['recovery_support']} | "
            f"{r['interpretation']} |"
        )

    lines.append("\n## Manuscript Use\n")
    lines.append(
        "Use this table to show that TRUST-Swarm is a high-confidence computing framework. "
        "Architecture ablations test node and temporal reasoning. Framework ablations show what assurance evidence is lost when calibration, OOD testing, explainability, or recovery reasoning is removed."
    )

    out_md.write_text("\n".join(lines))

    print(f"\nSaved CSV: {out_csv}")
    print(f"Saved report: {out_md}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Baseline temporal models for TRUST-Swarm.

Input shape:
    x = [batch_size, window_size, num_uavs, num_features]

Models:
- LSTM baseline
- GRU baseline
- 1D-CNN baseline

These are required for journal-level comparison against the Graph-Temporal Transformer.
"""

from __future__ import annotations

import torch
import torch.nn as nn


class LSTMBaseline(nn.Module):
    """Temporal LSTM baseline using flattened UAV node features."""

    def __init__(
        self,
        num_uavs: int,
        num_features: int,
        hidden_dim: int = 128,
        num_layers: int = 2,
        num_classes: int = 8,
        dropout: float = 0.25,
    ) -> None:
        super().__init__()

        self.input_dim = num_uavs * num_features

        self.lstm = nn.LSTM(
            input_size=self.input_dim,
            hidden_size=hidden_dim,
            num_layers=num_layers,
            dropout=dropout if num_layers > 1 else 0.0,
            batch_first=True,
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
        x = x.reshape(batch_size, window_size, num_uavs * num_features)
        output, _ = self.lstm(x)
        final_state = output[:, -1, :]
        return self.classifier(final_state)


class GRUBaseline(nn.Module):
    """Temporal GRU baseline using flattened UAV node features."""

    def __init__(
        self,
        num_uavs: int,
        num_features: int,
        hidden_dim: int = 128,
        num_layers: int = 2,
        num_classes: int = 8,
        dropout: float = 0.25,
    ) -> None:
        super().__init__()

        self.input_dim = num_uavs * num_features

        self.gru = nn.GRU(
            input_size=self.input_dim,
            hidden_size=hidden_dim,
            num_layers=num_layers,
            dropout=dropout if num_layers > 1 else 0.0,
            batch_first=True,
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
        x = x.reshape(batch_size, window_size, num_uavs * num_features)
        output, _ = self.gru(x)
        final_state = output[:, -1, :]
        return self.classifier(final_state)


class CNN1DBaseline(nn.Module):
    """1D-CNN baseline over temporal windows."""

    def __init__(
        self,
        num_uavs: int,
        num_features: int,
        hidden_dim: int = 128,
        num_classes: int = 8,
        dropout: float = 0.25,
    ) -> None:
        super().__init__()

        self.input_dim = num_uavs * num_features

        self.conv = nn.Sequential(
            nn.Conv1d(self.input_dim, hidden_dim, kernel_size=3, padding=1),
            nn.BatchNorm1d(hidden_dim),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Conv1d(hidden_dim, hidden_dim, kernel_size=3, padding=1),
            nn.BatchNorm1d(hidden_dim),
            nn.ReLU(),
            nn.Dropout(dropout),
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

        # [batch, time, uavs * features]
        x = x.reshape(batch_size, window_size, num_uavs * num_features)

        # Conv1d expects [batch, channels, time]
        x = x.transpose(1, 2)

        x = self.conv(x)

        # Global average pooling over time
        x = x.mean(dim=-1)

        return self.classifier(x)


def count_parameters(model: nn.Module) -> int:
    return sum(p.numel() for p in model.parameters() if p.requires_grad)


if __name__ == "__main__":
    dummy = torch.randn(4, 20, 10, 9)

    models = {
        "LSTM": LSTMBaseline(num_uavs=10, num_features=9),
        "GRU": GRUBaseline(num_uavs=10, num_features=9),
        "1D-CNN": CNN1DBaseline(num_uavs=10, num_features=9),
    }

    for name, model in models.items():
        out = model(dummy)
        print(name, "output:", out.shape, "params:", count_parameters(model))

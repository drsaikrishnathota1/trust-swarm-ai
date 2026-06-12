#!/usr/bin/env python3
"""
TRUST-Swarm Graph-Temporal Transformer.

Input shape:
    x = [batch_size, window_size, num_uavs, num_features]

The model:
1. projects UAV node features,
2. applies graph-style node attention at each timestep,
3. pools UAV nodes into swarm embeddings,
4. applies temporal Transformer over the 20-step window,
5. outputs attack-class logits.
"""

from __future__ import annotations

import torch
import torch.nn as nn


class GraphNodeAttention(nn.Module):
    """Lightweight node self-attention over UAVs at each timestep."""

    def __init__(self, hidden_dim: int, num_heads: int, dropout: float) -> None:
        super().__init__()
        self.attn = nn.MultiheadAttention(
            embed_dim=hidden_dim,
            num_heads=num_heads,
            dropout=dropout,
            batch_first=True,
        )
        self.norm = nn.LayerNorm(hidden_dim)
        self.ffn = nn.Sequential(
            nn.Linear(hidden_dim, hidden_dim * 2),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(hidden_dim * 2, hidden_dim),
        )
        self.ffn_norm = nn.LayerNorm(hidden_dim)

    def forward(self, node_emb: torch.Tensor) -> torch.Tensor:
        """
        Args:
            node_emb: [batch*time, num_uavs, hidden_dim]
        Returns:
            node_emb: [batch*time, num_uavs, hidden_dim]
        """
        attn_out, _ = self.attn(node_emb, node_emb, node_emb, need_weights=False)
        node_emb = self.norm(node_emb + attn_out)

        ffn_out = self.ffn(node_emb)
        node_emb = self.ffn_norm(node_emb + ffn_out)
        return node_emb


class GraphTemporalTransformer(nn.Module):
    """Graph-temporal AI classifier for TRUST-Swarm."""

    def __init__(
        self,
        num_features: int = 9,
        hidden_dim: int = 128,
        num_graph_layers: int = 2,
        num_temporal_layers: int = 2,
        num_heads: int = 4,
        num_classes: int = 8,
        dropout: float = 0.25,
    ) -> None:
        super().__init__()

        self.num_features = num_features
        self.hidden_dim = hidden_dim
        self.num_classes = num_classes

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
        """
        Args:
            x: [batch_size, window_size, num_uavs, num_features]
        Returns:
            logits: [batch_size, num_classes]
        """
        if x.ndim != 4:
            raise ValueError(
                f"Expected x with shape [batch, time, num_uavs, features], got {tuple(x.shape)}"
            )

        batch_size, window_size, num_uavs, num_features = x.shape

        if num_features != self.num_features:
            raise ValueError(
                f"Expected {self.num_features} features, got {num_features}"
            )

        x = self.input_proj(x)

        # Combine batch and time so node attention runs across UAV nodes.
        x = x.reshape(batch_size * window_size, num_uavs, self.hidden_dim)

        for layer in self.graph_layers:
            x = layer(x)

        # Pool UAV node embeddings into one swarm embedding per timestep.
        x = x.mean(dim=1)

        # Restore temporal sequence.
        x = x.reshape(batch_size, window_size, self.hidden_dim)

        x = self.temporal_encoder(x)

        # Use final timestep as mission-state representation.
        final_state = x[:, -1, :]

        logits = self.classifier(final_state)
        return logits


def count_parameters(model: nn.Module) -> int:
    return sum(p.numel() for p in model.parameters() if p.requires_grad)


if __name__ == "__main__":
    model = GraphTemporalTransformer()
    dummy = torch.randn(4, 20, 10, 9)
    out = model(dummy)

    print(model)
    print("Output shape:", out.shape)
    print("Trainable parameters:", count_parameters(model))

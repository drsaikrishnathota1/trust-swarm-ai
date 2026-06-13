#!/usr/bin/env python3
"""
TRUST-Swarm mission recovery environment.

This is a lightweight Gymnasium-compatible environment for testing
PPO/DRL mission recovery policies.

State vector:
    [S_comm, S_nav, S_cov, S_int, S_rec, S_energy, attack_class, uncertainty]

Actions:
    0 Continue
    1 Monitor
    2 Reroute
    3 Reassign
    4 Isolate Node
    5 Return to Base
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Tuple

import gymnasium as gym
import numpy as np
from gymnasium import spaces


ACTION_NAMES = {
    0: "Continue",
    1: "Monitor",
    2: "Reroute",
    3: "Reassign",
    4: "Isolate Node",
    5: "Return to Base",
}


@dataclass
class RecoveryConfig:
    max_steps: int = 120
    seed: int = 42
    mai_success_threshold: float = 0.60


class MissionRecoveryEnv(gym.Env):
    """Simple mission-recovery environment for PPO experiments."""

    metadata = {"render_modes": ["human"]}

    def __init__(self, config: RecoveryConfig | None = None):
        super().__init__()

        self.config = config or RecoveryConfig()
        self.rng = np.random.default_rng(self.config.seed)

        # 8 continuous/discrete-like state values normalized to [0, 1]
        self.observation_space = spaces.Box(
            low=0.0,
            high=1.0,
            shape=(8,),
            dtype=np.float32,
        )

        # Six mission recovery actions
        self.action_space = spaces.Discrete(6)

        self.step_count = 0
        self.state = None

    def _compute_mai(self, state: np.ndarray) -> float:
        s_comm, s_nav, s_cov, s_int, s_rec, s_energy, _, _ = state

        mai = (
            0.24 * s_comm
            + 0.22 * s_nav
            + 0.22 * s_cov
            + 0.16 * s_int
            + 0.10 * s_rec
            - 0.06 * s_energy
        )
        return float(np.clip(mai, 0.0, 1.0))

    def _random_initial_state(self) -> np.ndarray:
        s_comm = self.rng.uniform(0.35, 0.95)
        s_nav = self.rng.uniform(0.35, 0.95)
        s_cov = self.rng.uniform(0.40, 0.95)
        s_int = self.rng.choice([0.0, 1.0], p=[0.25, 0.75])
        s_rec = self.rng.uniform(0.20, 0.90)
        s_energy = self.rng.uniform(0.05, 0.65)
        attack_class = self.rng.integers(0, 8) / 7.0
        uncertainty = self.rng.uniform(0.05, 0.65)

        return np.array(
            [s_comm, s_nav, s_cov, s_int, s_rec, s_energy, attack_class, uncertainty],
            dtype=np.float32,
        )

    def reset(self, seed: int | None = None, options: Dict | None = None) -> Tuple[np.ndarray, Dict]:
        super().reset(seed=seed)

        if seed is not None:
            self.rng = np.random.default_rng(seed)

        self.step_count = 0
        self.state = self._random_initial_state()

        return self.state.copy(), {"mai": self._compute_mai(self.state)}

    def step(self, action: int):
        if self.state is None:
            raise RuntimeError("Environment must be reset before calling step().")

        self.step_count += 1

        old_mai = self._compute_mai(self.state)
        next_state = self.state.copy()

        # Action effects are intentionally simple for scaffold testing.
        if action == 0:  # Continue
            next_state[0] -= 0.03
            next_state[1] -= 0.02
            next_state[2] += 0.01
            next_state[5] += 0.01

        elif action == 1:  # Monitor
            next_state[7] -= 0.04
            next_state[4] += 0.02
            next_state[5] += 0.005

        elif action == 2:  # Reroute
            next_state[0] += 0.08
            next_state[1] += 0.05
            next_state[2] -= 0.02
            next_state[5] += 0.04

        elif action == 3:  # Reassign
            next_state[2] += 0.08
            next_state[4] += 0.05
            next_state[5] += 0.03

        elif action == 4:  # Isolate Node
            next_state[3] = 1.0
            next_state[1] += 0.03
            next_state[2] -= 0.04
            next_state[5] += 0.02

        elif action == 5:  # Return to Base
            next_state[0] += 0.04
            next_state[1] += 0.04
            next_state[2] -= 0.10
            next_state[5] -= 0.03

        next_state = np.clip(next_state, 0.0, 1.0)

        new_mai = self._compute_mai(next_state)

        mission_success_reward = 1.0 if new_mai >= self.config.mai_success_threshold else -0.5
        improvement_reward = new_mai - old_mai
        uncertainty_penalty = 0.15 * next_state[7]
        energy_penalty = 0.10 * next_state[5]

        reward = mission_success_reward + improvement_reward - uncertainty_penalty - energy_penalty

        self.state = next_state

        terminated = new_mai >= 0.85
        truncated = self.step_count >= self.config.max_steps

        info = {
            "mai": new_mai,
            "action_name": ACTION_NAMES[int(action)],
            "old_mai": old_mai,
            "mai_delta": new_mai - old_mai,
        }

        return self.state.copy(), float(reward), terminated, truncated, info

    def render(self):
        if self.state is None:
            print("MissionRecoveryEnv not reset.")
            return

        mai = self._compute_mai(self.state)
        print(f"step={self.step_count}, MAI={mai:.3f}, state={self.state}")


if __name__ == "__main__":
    env = MissionRecoveryEnv()
    obs, info = env.reset(seed=42)
    print("Initial:", obs, info)

    for _ in range(5):
        action = env.action_space.sample()
        obs, reward, terminated, truncated, info = env.step(action)
        print("Action:", ACTION_NAMES[action], "Reward:", reward, "Info:", info)

        if terminated or truncated:
            break


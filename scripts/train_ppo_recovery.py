#!/usr/bin/env python3
"""
Train PPO mission recovery policy for TRUST-Swarm.

This is a scaffold training script for the DRL recovery contribution.

Outputs:
- results/models/ppo_recovery_policy.zip
- results/csv/ppo_recovery_eval.csv
"""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd
from stable_baselines3 import PPO
from stable_baselines3.common.env_checker import check_env

from src.trust_swarm.recovery.mission_recovery_env import MissionRecoveryEnv, RecoveryConfig


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Train PPO recovery policy.")
    parser.add_argument("--timesteps", type=int, default=10000)
    parser.add_argument("--eval-episodes", type=int, default=50)
    parser.add_argument("--output-dir", type=str, default="results")
    parser.add_argument("--seed", type=int, default=42)
    return parser.parse_args()


def evaluate_policy(model: PPO, episodes: int, seed: int) -> pd.DataFrame:
    rows = []

    for episode in range(episodes):
        env = MissionRecoveryEnv(RecoveryConfig(seed=seed + episode))
        obs, info = env.reset(seed=seed + episode)

        total_reward = 0.0
        actions = []
        mai_values = [info["mai"]]

        terminated = False
        truncated = False

        while not (terminated or truncated):
            action, _ = model.predict(obs, deterministic=True)
            obs, reward, terminated, truncated, info = env.step(int(action))

            total_reward += reward
            actions.append(info["action_name"])
            mai_values.append(info["mai"])

        rows.append(
            {
                "episode": episode,
                "total_reward": total_reward,
                "steps": len(actions),
                "initial_mai": mai_values[0],
                "final_mai": mai_values[-1],
                "mai_improvement": mai_values[-1] - mai_values[0],
                "mission_success": float(mai_values[-1] >= 0.60),
                "terminated_success": float(terminated),
                "most_common_action": max(set(actions), key=actions.count) if actions else "none",
            }
        )

    return pd.DataFrame(rows)


def main() -> None:
    args = parse_args()

    output_dir = Path(args.output_dir)
    (output_dir / "models").mkdir(parents=True, exist_ok=True)
    (output_dir / "csv").mkdir(parents=True, exist_ok=True)

    env = MissionRecoveryEnv(RecoveryConfig(seed=args.seed))

    # Validate Gymnasium environment compatibility.
    check_env(env, warn=True)

    model = PPO(
        policy="MlpPolicy",
        env=env,
        verbose=1,
        seed=args.seed,
        learning_rate=3e-4,
        n_steps=1024,
        batch_size=64,
        gamma=0.99,
        gae_lambda=0.95,
        clip_range=0.2,
    )

    model.learn(total_timesteps=args.timesteps)

    model_path = output_dir / "models" / "ppo_recovery_policy.zip"
    model.save(model_path)

    eval_df = evaluate_policy(
        model=model,
        episodes=args.eval_episodes,
        seed=args.seed,
    )

    eval_path = output_dir / "csv" / "ppo_recovery_eval.csv"
    eval_df.to_csv(eval_path, index=False)

    summary = eval_df[
        ["total_reward", "steps", "initial_mai", "final_mai", "mai_improvement", "mission_success"]
    ].mean()

    print("Saved model:", model_path)
    print("Saved eval:", eval_path)
    print("Evaluation summary:")
    print(summary.to_string())


if __name__ == "__main__":
    main()

# main.py

from overcooked_env import OvercookedParallelEnv
from kindness import create_overcooked_kindness_opportunity

import numpy as np
import random

def main():
    # Create the Overcooked environment
    env = OvercookedParallelEnv(max_steps=50)

    # Create the KindnessOpportunity instance
    kindness_opportunity = create_overcooked_kindness_opportunity()
    print("[INFO] Created KindnessOpportunity:", kindness_opportunity)

    # Example: A simple random policy for each agent (for demonstration)
    # In practice, you'd replace with RLlib, stable-baselines, or a custom MARL approach.
    n_episodes = 5
    for ep in range(n_episodes):
        obs = env.reset()
        done = False
        step_count = 0

        # Because it's a ParallelEnv, we check if any agent is done to mark the episode as done
        while True:
            actions = {}
            for agent in env.agents:
                # Random action from the discrete space
                actions[agent] = env.action_spaces[agent].sample()

            next_obs, rewards, terminations, truncations, infos = env.step(actions)
            step_count += 1

            # Render
            env.render()

            if any(terminations.values()) or any(truncations.values()):
                print(f"Episode {ep} finished after {step_count} steps.")
                break

            obs = next_obs

    print("All episodes completed.")

if __name__ == "__main__":
    main()

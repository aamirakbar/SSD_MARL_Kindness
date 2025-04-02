from KindModel.overcooked_marl.overcooked_env import OvercookedParallelEnv
from KindModel.overcooked_marl.kindness import create_overcooked_kindness_opportunity

import numpy as np
import gymnasium as gym
from gymnasium.wrappers import FlattenObservation
from stable_baselines3 import PPO
from stable_baselines3.common.env_util import make_vec_env
from stable_baselines3.common.env_checker import check_env
from stable_baselines3.common.callbacks import EvalCallback

def main():
    print("[INFO] Initializing Overcooked environment...")
    # Initialize and flatten the observation space
    env = OvercookedParallelEnv()
    env = FlattenObservation(env)
    
    # Validate the environment
    check_env(env)

    # Create kindness opportunity
    kindness_opportunity = create_overcooked_kindness_opportunity()
    print("[INFO] Created KindnessOpportunity:", kindness_opportunity)

    # Create vectorized environment
    vec_env = make_vec_env(lambda: env, n_envs=1)

    print("[INFO] Defining PPO Model...")
    # Use regular PPO with MlpPolicy
    model = PPO(
        "MlpPolicy",
        vec_env,
        verbose=1,
        learning_rate=3e-4,
        n_steps=512,
        batch_size=64,
        gamma=0.99
    )

    print("[INFO] Training PPO Model on Overcooked environment...")
    eval_callback = EvalCallback(
        vec_env,
        eval_freq=10,
        verbose=1
    )
    model.learn(
        total_timesteps=100,
        callback=eval_callback,
        progress_bar=True
    )
    model.save("ppo_overcooked")

    # Load the trained model
    model = PPO.load("ppo_overcooked", env=vec_env)

    print("[INFO] Running trained policy...")
    n_episodes = 1
    total_rewards = []
    for ep in range(n_episodes):
        obs, _ = env.reset()
        done = False
        episode_reward = 0
        step_count = 0

        while not done:
            action, _states = model.predict(obs, deterministic=True)
            print(f"Episode {ep}, Step {step_count}: Action taken: {action}")

            obs, reward, terminated, truncated, info = env.step(action)
            done = terminated or truncated

            env.render()
            episode_reward += reward
            step_count += 1

            if done:
                total_rewards.append(episode_reward)
                print(f"Episode {ep} | Steps: {step_count} | Total Reward: {episode_reward:.2f}")
                break

    print(f"\nAverage reward over {n_episodes} episodes: {np.mean(total_rewards):.2f}")

if __name__ == "__main__":
    main()
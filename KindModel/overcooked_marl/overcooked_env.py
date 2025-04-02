# overcooked_env.py

import numpy as np
import gymnasium as gym
from gymnasium import spaces
from typing import Tuple

class OvercookedParallelEnv(gym.Env):
    """
    A Gym-compatible Overcooked environment where two agents (chefs) collaborate.
    The environment now uses a joint action space represented by a MultiDiscrete space.
    """
    metadata = {"render_modes": ["human"], "name": "OvercookedParallelEnv"}

    def __init__(self, max_steps=50):
        super().__init__()
        self.max_steps = max_steps

        # Instead of Tuple((Discrete(5), Discrete(5))), use MultiDiscrete:
        # This represents two discrete actions, each with 5 possibilities.
        self.action_space = spaces.MultiDiscrete([5, 5])
        
        # Define an individual observation space (e.g., [pos_x, pos_y, dish_burning, trust_metric])
        obs_space = spaces.Box(low=0, high=10, shape=(4,), dtype=np.float32)
        # For simplicity, we keep the observation space as a Tuple.
        self.observation_space = spaces.Tuple((obs_space, obs_space))

        self.agents = ["chef_0", "chef_1"]
        self.reset()

    def reset(self, seed=None, options=None) -> Tuple[Tuple[np.ndarray, np.ndarray], dict]:
        self.steps = 0

        self.state = {
            "chef_0_pos": np.array([0, 0]),
            "chef_1_pos": np.array([1, 0]),
            "dish_burning": False,
            "burn_timer": 5,
            "trust_metric": 1.0,
            "orders_completed": 0
        }

        obs = (self._make_observation("chef_0"), self._make_observation("chef_1"))
        return obs, {}

    def step(self, action: np.ndarray) -> Tuple[Tuple[np.ndarray, np.ndarray], float, bool, bool, dict]:
        """
        Execute a joint action represented as a numpy array with 2 elements.
        """
        self.steps += 1

        # Unpack joint action from the MultiDiscrete array.
        a0, a1 = action

        rewards = {"chef_0": 0.0, "chef_1": 0.0}

        self._handle_movement("chef_0", a0)
        self._handle_movement("chef_1", a1)

        if a0 == 3:
            rewards["chef_0"] += 0.5
            self.state["trust_metric"] = min(2.0, self.state["trust_metric"] + 0.1)
        elif a0 == 4:
            rewards["chef_0"] += 0.2
            if self.state["dish_burning"]:
                self.state["burn_timer"] = min(5, self.state["burn_timer"] + 1)
                self.state["trust_metric"] = min(2.0, self.state["trust_metric"] + 0.05)

        if a1 == 3:
            rewards["chef_1"] += 0.5
            self.state["trust_metric"] = min(2.0, self.state["trust_metric"] + 0.1)
        elif a1 == 4:
            rewards["chef_1"] += 0.2
            if self.state["dish_burning"]:
                self.state["burn_timer"] = min(5, self.state["burn_timer"] + 1)
                self.state["trust_metric"] = min(2.0, self.state["trust_metric"] + 0.05)

        cooking_speed_multiplier = 2.0 if self.state["trust_metric"] >= 1.5 else 1.0

        if (cooking_speed_multiplier == 2.0 and self.steps % 5 == 0) or \
           (cooking_speed_multiplier == 1.0 and self.steps % 10 == 0):
            self.state["orders_completed"] += 1
            rewards["chef_0"] += 2.0
            rewards["chef_1"] += 2.0

        if self.state["dish_burning"]:
            self.state["burn_timer"] -= 1
            if self.state["burn_timer"] <= 0:
                rewards["chef_0"] -= 1.0
                rewards["chef_1"] -= 1.0
                self.state["dish_burning"] = False
                self.state["burn_timer"] = 5
        else:
            if np.random.rand() < 0.1:
                self.state["dish_burning"] = True

        terminated = (self.steps >= self.max_steps)
        total_reward = rewards["chef_0"] + rewards["chef_1"]
        obs = (self._make_observation("chef_0"), self._make_observation("chef_1"))
        info = {"individual_rewards": rewards}

        return obs, total_reward, terminated, False, info

    def _handle_movement(self, agent_id: str, action: int):
        pos_key = f"{agent_id}_pos"
        if action == 0:  # Move left
            self.state[pos_key][0] = max(0, self.state[pos_key][0] - 1)
        elif action == 1:  # Move right
            self.state[pos_key][0] = min(10, self.state[pos_key][0] + 1)
        # Action 2: pick/drop ingredient (not modeled here)

    def _make_observation(self, agent_id: str) -> np.ndarray:
        pos = self.state[f"{agent_id}_pos"]
        dish_burning_flag = 1.0 if self.state["dish_burning"] else 0.0
        trust_metric = self.state["trust_metric"]
        return np.array([pos[0], pos[1], dish_burning_flag, trust_metric], dtype=np.float32)

    def render(self, mode="human"):
        print(f"Step: {self.steps}, State: {self.state}")

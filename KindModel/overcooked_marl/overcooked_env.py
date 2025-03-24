# overcooked_env.py

import numpy as np
from pettingzoo.utils.env import ParallelEnv
from gymnasium import spaces
from typing import Dict, Any

class OvercookedParallelEnv(ParallelEnv):
    """
    A simplified Overcooked-style environment where 2 agents collaborate to
    prepare dishes. Each agent can move, pick up ingredients, or do "kind" acts
    (e.g., share ingredients, prompt the other agent about burning food, etc.).
    """

    metadata = {"render_modes": ["human"], "name": "OvercookedParallelEnv"}

    def __init__(self, max_steps=50):
        super().__init__()
        self.max_steps = max_steps
        self.agents = ["chef_0", "chef_1"]
        self.possible_agents = self.agents
        self.num_agents = len(self.agents)

        # Example discrete actions:
        # 0: Move Left
        # 1: Move Right
        # 2: Pick/Drop Ingredient
        # 3: Share Ingredient (a "Kindness" act)
        # 4: Prompt about burning dish (a "Kindness" act)
        self.action_spaces = {
            agent: spaces.Discrete(5) for agent in self.agents
        }

        # Observations might include agent position, dish states, trust level, etc.
        # For simplicity, we'll say each agent's observation is a small vector:
        # [pos_x, pos_y, is_dish_burning, trust_metric].
        self.observation_spaces = {
            agent: spaces.Box(low=0, high=10, shape=(4,), dtype=np.float32)
            for agent in self.agents
        }

        # Initialize environment state
        self.reset()

    def reset(self, seed=None, return_info=False, options=None):
        """
        Reset the environment to a starting state.
        Return dict of observations, plus optional infos.
        """
        self.steps = 0
        self._terminated = False

        # Example minimal state
        self.state = {
            "chef_0_pos": np.array([0, 0]),
            "chef_1_pos": np.array([1, 0]),
            "dish_burning": False,
            "burn_timer": 5,       # If it goes to 0, dish is ruined
            "trust_metric": 1.0,   # Higher means better synergy => faster cooking
            "orders_completed": 0
        }

        observations = {}
        for agent in self.agents:
            observations[agent] = self._make_observation(agent)

        infos = {agent: {} for agent in self.agents}
        return (observations, infos) if return_info else observations

    def step(self, actions):
        """
        Each agent chooses an action. We update the environment, compute rewards,
        produce next observations, and check for termination.
        """
        self.steps += 1

        # Unpack actions
        a0 = actions["chef_0"]
        a1 = actions["chef_1"]

        # Default reward
        rewards = {"chef_0": 0.0, "chef_1": 0.0}

        # Update environment based on actions
        # (Simplified movement and dish cooking logic)
        self._handle_movement("chef_0", a0)
        self._handle_movement("chef_1", a1)

        # Check for "Kindness" acts
        # 3 -> Share Ingredient (SupportingAct)
        # 4 -> Prompt about burning dish (PromptAct)
        if a0 == 3:
            # Chef_0 shares ingredient => reward synergy
            rewards["chef_0"] += 0.5
            # Increase trust
            self.state["trust_metric"] = min(2.0, self.state["trust_metric"] + 0.1)
        elif a0 == 4:
            # Chef_0 prompts about burning dish => can reduce burn timer or help
            rewards["chef_0"] += 0.2
            if self.state["dish_burning"]:
                # If the dish is burning, a prompt can help salvage it
                self.state["burn_timer"] = min(5, self.state["burn_timer"] + 1)
                # Increase trust
                self.state["trust_metric"] = min(2.0, self.state["trust_metric"] + 0.05)

        if a1 == 3:
            rewards["chef_1"] += 0.5
            self.state["trust_metric"] = min(2.0, self.state["trust_metric"] + 0.1)
        elif a1 == 4:
            rewards["chef_1"] += 0.2
            if self.state["dish_burning"]:
                self.state["burn_timer"] = min(5, self.state["burn_timer"] + 1)
                self.state["trust_metric"] = min(2.0, self.state["trust_metric"] + 0.05)

        # Cooking speed depends on trust metric => if trust_metric >= 1.5,
        # cooking is 2x faster, so let's say orders complete more quickly.
        cooking_speed_multiplier = 2.0 if self.state["trust_metric"] >= 1.5 else 1.0

        # Example: every step, we increment "cooking_progress" by cooking_speed_multiplier
        # and if it crosses a threshold, an order is completed.
        # For simplicity, let's say every 5 steps we complete an order if cooking_speed_multiplier=2
        # or every 10 steps if cooking_speed_multiplier=1.
        # We'll do a quick check:
        if (cooking_speed_multiplier == 2.0 and self.steps % 5 == 0) or \
           (cooking_speed_multiplier == 1.0 and self.steps % 10 == 0):
            self.state["orders_completed"] += 1
            # Give team reward
            rewards["chef_0"] += 2.0
            rewards["chef_1"] += 2.0

        # Dish burning logic
        if self.state["dish_burning"]:
            self.state["burn_timer"] -= 1
            if self.state["burn_timer"] <= 0:
                # Dish is ruined => negative reward
                rewards["chef_0"] -= 1.0
                rewards["chef_1"] -= 1.0
                # Reset dish
                self.state["dish_burning"] = False
                self.state["burn_timer"] = 5
        else:
            # 10% chance each step the dish starts burning
            if np.random.rand() < 0.1:
                self.state["dish_burning"] = True

        # Check termination
        terminated = (self.steps >= self.max_steps)
        terminations = {"chef_0": terminated, "chef_1": terminated}
        truncations = {"chef_0": False, "chef_1": False}
        infos = {"chef_0": {}, "chef_1": {}}

        # Next observations
        observations = {
            "chef_0": self._make_observation("chef_0"),
            "chef_1": self._make_observation("chef_1")
        }

        return observations, rewards, terminations, truncations, infos

    def _handle_movement(self, agent_id, action):
        """
        Minimal movement logic for the agent.
        """
        pos_key = f"{agent_id}_pos"
        if action == 0:  # Move left
            self.state[pos_key][0] = max(0, self.state[pos_key][0] - 1)
        elif action == 1:  # Move right
            self.state[pos_key][0] = min(10, self.state[pos_key][0] + 1)
        # 2 -> pick or drop ingredient is not fully modeled here,
        # but you can expand as needed.

    def _make_observation(self, agent_id):
        """
        Convert the internal state into an observation vector for the agent.
        E.g. [pos_x, pos_y, dish_burning_flag, trust_metric].
        """
        pos = self.state[f"{agent_id}_pos"]
        dish_burning_flag = 1.0 if self.state["dish_burning"] else 0.0
        trust_metric = self.state["trust_metric"]
        return np.array([pos[0], pos[1], dish_burning_flag, trust_metric], dtype=np.float32)

    def render(self):
        print(f"Step: {self.steps}, State: {self.state}")

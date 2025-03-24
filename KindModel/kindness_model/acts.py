"""
acts.py

Defines the abstract KindnessAct class and its concrete subclasses:
AbilityAct, PromptAct, and SupportingAct.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional


@dataclass
class KindnessAct(ABC):
    """
    Abstract base class for all kinds of Kindness Acts.
    """
    @abstractmethod
    def perform_act(self) -> None:
        """
        Method to be overridden by subclasses indicating how the act is performed.
        """
        pass


@dataclass
class AbilityAct(KindnessAct):
    """
    Represents an act that leverages a specific ability.
    """
    act_type: str
    frequency: Optional[int] = None

    def perform_act(self) -> None:
        # Implementation or placeholder
        print(f"[AbilityAct] Performing {self.act_type} with frequency {self.frequency}.")


@dataclass
class PromptAct(KindnessAct):
    """
    Represents an act that involves prompting or nudging someone to do something.
    """
    prompt: str

    def perform_act(self) -> None:
        # Implementation or placeholder
        print(f"[PromptAct] Prompting with message: {self.prompt}")


@dataclass
class SupportingAct(KindnessAct):
    """
    Represents an act that supports or aids someone/something.
    """
    support_description: str

    def perform_act(self) -> None:
        # Implementation or placeholder
        print(f"[SupportingAct] Providing support: {self.support_description}")

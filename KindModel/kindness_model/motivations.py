"""
motivations.py

Defines classes and enumerations for capturing an Actor's motivations.
"""

from dataclasses import dataclass
from enum import Enum
from typing import Optional


class MotivationType(Enum):
    """
    Enumerates possible types of motivation.
    """
    OTHER_BETTERMENT_FOCUSED = "other_betterment_focused"
    SELF_BETTERMENT_FOCUSED = "self_betterment_focused"
    INDIFFERENT = "indifferent"
    #HARM_FOCUSED = "harm_focused"


@dataclass
class Motivation:
    """
    Represents an Actor's motivation for performing an act.
    The 'level' attribute can be in the range [-1..1].
    """
    motivation_type: MotivationType
    level: float  # -1 <= level <= 1

    def describe_motivation(self) -> str:
        """
        Describe the motivation focus based on the level score.

        Returns:
            A string indicating the strength and focus of the motivation:
            - "weak_betterment_focused" for positive levels in the range (0, 0.5].
            - "strong_betterment_focused" for positive levels in the range (0.5, 1].
            - "weak_harm_focused" for negative levels in the range [-0.5, 0).
            - "strong_harm_focused" for negative levels in the range [-1, -0.5).
            - The motivation type's value for levels exactly at 0 or 1/-1.
        """
        if 0 < self.level <= 0.5:
            return "weak_betterment_focused"
        elif 0.5 < self.level <= 1:
            return "strong_betterment_focused"
        elif -0.5 <= self.level < 0:
            return "weak_harm_focused"
        elif -1 <= self.level < -0.5:
            return "strong_harm_focused"
        else:
            return self.motivation_type.value

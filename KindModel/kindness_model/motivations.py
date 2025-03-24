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
    HARM_FOCUSED = "harm_focused"


@dataclass
class Motivation:
    """
    Represents an Actor's motivation for performing an act.
    The 'level' attribute can be in the range [-1..1].
    """
    motivation_type: MotivationType
    level: float  # -1 <= level <= 1

    def is_positive(self) -> bool:
        """Return True if the motivation level is above 0."""
        return self.level > 0

    def is_negative(self) -> bool:
        """Return True if the motivation level is below 0."""
        return self.level < 0

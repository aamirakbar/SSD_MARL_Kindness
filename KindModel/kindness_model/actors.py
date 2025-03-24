"""
actors.py

Defines the Actor class and any related enumerations or helper classes,
including roles (Giver, Receiver, Observer).
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional

from .factors import PsychologicalFactor, SocialFactor
from .motivations import Motivation


class ActorRole(Enum):
    """
    Possible roles for an Actor in a kindness scenario.
    """
    GIVER = "giver"
    RECEIVER = "receiver"
    OBSERVER = "observer"


@dataclass
class Actor:
    """
    Represents a participant in the kindness opportunity.
    An Actor can have multiple roles, a motivation, and associated factors.
    """
    name: str
    roles: List[ActorRole]
    motivation: Optional[Motivation] = None
    psychological_factors: List[PsychologicalFactor] = field(default_factory=list)
    social_factors: List[SocialFactor] = field(default_factory=list)

    def add_role(self, role: ActorRole) -> None:
        if role not in self.roles:
            self.roles.append(role)

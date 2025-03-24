"""
factors.py

Defines psychological and social factors that can influence an Actor's behavior.
"""

from dataclasses import dataclass


@dataclass
class PsychologicalFactor:
    """
    Represents a psychological factor influencing an Actor.
    Example: stress_level, empathy_level, mental_health_status, etc.
    """
    name: str
    value: float


@dataclass
class SocialFactor:
    """
    Represents a social factor influencing an Actor.
    Example: cultural_norm, peer_pressure, social_support, etc.
    """
    name: str
    value: float

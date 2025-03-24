"""
conditions.py

Defines the Condition class, which captures conditions.
"""

from dataclasses import dataclass


@dataclass
class Condition:
    """
    Represents a condition or precondition (e.g. "Needs volunteer presence",
    "Requires permission from authority", etc.).
    """
    description: str

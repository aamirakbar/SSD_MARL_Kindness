"""
conditions.py

Defines the Condition class, which captures conditions.
"""

from dataclasses import dataclass


@dataclass
class Condition:
    """
    Represents a condition or precondition/postcondition with a name and a value.
    The value refers to a specific formalization for representing the condition,
    e.g., Bigraphical Reactive Systems.
    """
    name: str
    value: str
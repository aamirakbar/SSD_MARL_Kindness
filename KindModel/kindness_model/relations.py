"""
relations.py

Defines relationships or associations between entities within the kindness model.
"""

from dataclasses import dataclass


@dataclass
class Relation:
    """
    Represents a relationship between two or more entities in the kindness model.
    Example: "Sibling", "Coworker", "Neighbor", or more specific relationships.
    """
    description: str

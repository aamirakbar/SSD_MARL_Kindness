"""
properties.py

Defines a Property class or classes representing additional attributes or
entities involved in the kindness scenario.
"""

from dataclasses import dataclass


@dataclass
class Property:
    """
    Represents a property or an entity relevant to the kindness opportunity.
    For example: 'item_to_donate', 'resource_needed', etc.
    """
    name: str
    value: str

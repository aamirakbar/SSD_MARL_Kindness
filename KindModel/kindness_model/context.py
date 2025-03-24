"""
context.py

Defines the Context class, which includes location, time(s), and other relevant
contextual information for a kindness opportunity.
"""

from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime


@dataclass
class Location:
    """
    Represents a geographical or conceptual location.
    """
    name: str


@dataclass
class Context:
    """
    Represents the broader context for a kindness opportunity, including
    location(s) and time(s).
    """
    locations: List[Location] = field(default_factory=list)
    times: List[datetime] = field(default_factory=list)

    def add_location(self, location: Location) -> None:
        self.locations.append(location)

    def add_time(self, time_point: datetime) -> None:
        self.times.append(time_point)

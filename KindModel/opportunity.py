"""
opportunity.py

Defines the core KindnessOpportunity class that ties together conditions,
actors, context, properties, relations, and potential kindness acts.
"""

from dataclasses import dataclass, field
from typing import List

from KindModel.kindness_model.conditions import Condition
from KindModel.kindness_model.context import Context
from KindModel.kindness_model.actors import Actor
from KindModel.kindness_model.acts import KindnessAct
from KindModel.kindness_model.properties import Property
from KindModel.kindness_model.relations import Relation


@dataclass
class KindnessOpportunity:
    """
    Represents a scenario in which kindness can be enacted.
    It ties together the conditions, actors, context, any relevant
    properties or relations, and the potential kindness acts that can occur.
    """
    conditions: List[Condition]
    context: Context
    actors: List[Actor]
    properties: List[Property] = field(default_factory=list)
    relations: List[Relation] = field(default_factory=list)
    possible_acts: List[KindnessAct] = field(default_factory=list)

    def add_actor(self, actor: Actor) -> None:
        """Add an actor to this kindness opportunity."""
        self.actors.append(actor)

    def add_property(self, prop: Property) -> None:
        """Add a property to this kindness opportunity."""
        self.properties.append(prop)

    def add_relation(self, relation: Relation) -> None:
        """Add a relation to this kindness opportunity."""
        self.relations.append(relation)

    def add_act(self, act: KindnessAct) -> None:
        """Add a potential kindness act to this kindness opportunity."""
        self.possible_acts.append(act)

    def check_conditions(self) -> bool:
        """
        Placeholder method to check if conditions are met.
        """
        return all(condition.name != "" for condition in self.conditions)

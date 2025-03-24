# kindness.py

from datetime import datetime
from ..opportunity import KindnessOpportunity
from kindness_model.context import Context, Location
from kindness_model.conditions import Condition
from kindness_model.actors import Actor, ActorRole
from kindness_model.acts import SupportingAct, PromptAct
from kindness_model.motivations import Motivation, MotivationType
from kindness_model.properties import Property
from kindness_model.relations import Relation


def create_overcooked_kindness_opportunity():
    """
    Example of how to create a KindnessOpportunity that aligns with
    the Overcooked scenario.
    """

    # Conditions might include "Dishes can burn if not attended"
    cond_burning = Condition(description="Dish can burn if left unattended.")

    # Context might be the 'Overcooked Kitchen'
    kitchen_loc = Location(name="Overcooked Kitchen")
    ctx = Context(locations=[kitchen_loc], times=[datetime.now()])

    # Actors: Chef0 (giver) and Chef1 (receiver), or both as potential givers
    chef0 = Actor(
        name="Chef0",
        roles=[ActorRole.GIVER, ActorRole.RECEIVER],
        motivation=Motivation(motivation_type=MotivationType.BETTERMENT_FOCUSED, level=0.8)
    )
    chef1 = Actor(
        name="Chef1",
        roles=[ActorRole.GIVER, ActorRole.RECEIVER],
        motivation=Motivation(motivation_type=MotivationType.BETTERMENT_FOCUSED, level=0.7)
    )

    # A property might be "Shared Ingredient" or "Dish"
    dish_property = Property(name="SharedDish", value="TomatoSoup")

    # A relation might be "Co-Chefs"
    rel = Relation(description="Co-chefs in the same kitchen")

    # Potential kindness acts:
    # - Share Ingredient (SupportingAct)
    # - Prompt about Burning Dish (PromptAct)
    share_ingredient_act = SupportingAct(support_description="Share ingredient with teammate")
    prompt_burn_act = PromptAct(prompt="Dish is burning! Please attend it.")

    opportunity = KindnessOpportunity(
        conditions=[cond_burning],
        context=ctx,
        actors=[chef0, chef1],
        properties=[dish_property],
        relations=[rel],
        possible_acts=[share_ingredient_act, prompt_burn_act]
    )

    return opportunity

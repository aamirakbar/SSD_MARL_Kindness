# kindness.py

from datetime import datetime
from KindModel.opportunity import KindnessOpportunity
from KindModel.kindness_model.context import Context, Location
from KindModel.kindness_model.conditions import Condition
from KindModel.kindness_model.actors import Actor, ActorRole
from KindModel.kindness_model.acts import SupportingAct, PromptAct
from KindModel.kindness_model.motivations import Motivation, MotivationType
from KindModel.kindness_model.properties import Property
from KindModel.kindness_model.relations import Relation


def create_overcooked_kindness_opportunity():
    """
    Example of how to create a KindnessOpportunity that aligns with
    the Overcooked scenario.
    """

    # Conditions might include "Dishes can burn if not attended"
    pre_cond_burning = Condition(name="Dish can burn or ruined if left unattended or ingredients not added at right time.", value="True")
    post_cond_burning = Condition(name="Dish is burnt, ruined or saved", value="True")

    # Context might be the 'Overcooked Kitchen'
    kitchen_loc = Location(name="Overcooked Kitchen")
    ctx = Context(locations=[kitchen_loc], times=[datetime.now()])

    # Actors: Chef0 and Chef1 - both as potential givers and receivers
    chef0 = Actor(
        name="Chef0",
        roles=[ActorRole.GIVER, ActorRole.RECEIVER],
        motivation=Motivation(motivation_type=MotivationType.OTHER_BETTERMENT_FOCUSED, level=0.8)
    )
    chef1 = Actor(
        name="Chef1",
        roles=[ActorRole.GIVER, ActorRole.RECEIVER],
        motivation=Motivation(motivation_type=MotivationType.OTHER_BETTERMENT_FOCUSED, level=0.7)
    )

    # A property might be "Shared Ingredient" or "Dish"
    Ing_property = Property(name="SharedIngredent", value="Spice")

    # A relation might be "Co-Chefs"
    rel = Relation(description="Co-chefs in the same kitchen")

    # Potential kindness acts:
    # - Share Ingredient (SupportingAct)
    # - Prompt about Burning Dish (PromptAct)
    share_ingredient_act = SupportingAct(support_description="Share ingredient with teammate")
    prompt_burn_act = PromptAct(prompt="Dish is burning! Please attend it.")

    opportunity = KindnessOpportunity(
        conditions=[pre_cond_burning, post_cond_burning],
        context=ctx,
        actors=[chef0, chef1],
        properties=[Ing_property],
        relations=[rel],
        possible_acts=[share_ingredient_act, prompt_burn_act]
    )

    return opportunity

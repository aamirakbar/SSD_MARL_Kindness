# main.py
from datetime import datetime

from KindModel.kindness_model.acts import AbilityAct, PromptAct
from KindModel.kindness_model.actors import Actor, ActorRole
from KindModel.kindness_model.context import Context, Location
from KindModel.kindness_model.conditions import Condition
from KindModel.kindness_model.motivations import Motivation, MotivationType
from KindModel.opportunity import KindnessOpportunity
from KindModel.kindness_model.properties import Property
from KindModel.kindness_model.relations import Relation

def main():
    # Create some conditions
    pre = Condition(name="VolunteerPresence", value="True")
    post = Condition(name="ManagerApproval", value="False")

    # Create a context
    loc = Location(name="Community Center")
    ctx = Context(locations=[loc], times=[datetime.now()])

    # Create actors
    giver = Actor(
        name="Alice",
        roles=[ActorRole.GIVER],
        motivation=Motivation(motivation_type=MotivationType.OTHER_BETTERMENT_FOCUSED, level=0.8)
    )
    receiver = Actor(
        name="Bob",
        roles=[ActorRole.RECEIVER],
        motivation=Motivation(motivation_type=MotivationType.INDIFFERENT, level=0.0)
    )

    # Create some properties
    prop_donation = Property(name="DonationItem", value="Canned Food")

    # Create a relation
    rel = Relation(description="Coworkers")

    # Create potential kindness acts
    act1 = AbilityAct(act_type="Delivering Goods", frequency=2)
    act2 = PromptAct(prompt="Please help with unloading the van.")

    # Create the opportunity
    opportunity = KindnessOpportunity(
        conditions=[pre, post],
        context=ctx,
        actors=[giver, receiver],
        properties=[prop_donation],
        relations=[rel],
        possible_acts=[act1, act2]
    )

    # Perform the acts
    for act in opportunity.possible_acts:
        act.perform_act()

if __name__ == "__main__":
    main()

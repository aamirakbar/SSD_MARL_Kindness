# main.py
from datetime import datetime

from kindness_model.acts import AbilityAct, PromptAct
from kindness_model.actors import Actor, ActorRole
from kindness_model.context import Context, Location
from kindness_model.conditions import Condition
from kindness_model.motivations import Motivation, MotivationType
from opportunity import KindnessOpportunity
from kindness_model.properties import Property
from kindness_model.relations import Relation

def main():
    # Create some conditions
    cond1 = Condition(description="Requires volunteer presence")
    cond2 = Condition(description="Needs approval from manager")

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
        conditions=[cond1, cond2],
        context=ctx,
        actors=[giver, receiver],
        properties=[prop_donation],
        relations=[rel],
        possible_acts=[act1, act2]
    )

    # Check if conditions are met
    if opportunity.check_conditions():
        print("All conditions are met. Proceed with kindness acts!")
        # Perform the acts
        for act in opportunity.possible_acts:
            act.perform_act()
    else:
        print("Some conditions are not met. Cannot proceed.")

if __name__ == "__main__":
    main()

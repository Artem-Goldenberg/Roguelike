import random

from Engine.entityLogic import EntityLogic, Behaviour
from Engine.eventSystem import Event, eventType


class ShinyLogicStand(Behaviour):
    def __init__(self, _data):
        Behaviour.__init__(self, _data)
        self.state_lasts = random.randint(0, 20)/20  # 0.0
        self.duration = 1.0

    def process(self, _dt):
        self.state_lasts += _dt
        self.data.animation_stage = (self.state_lasts % self.duration) / self.duration

        for event in self.data.env.pastEvents.getEvents(eventType.PickUp):
            if event.data == self.data.position:
                self.data.env.futureEvents.sendEvent(
                    Event(eventType.Pickable, self, self.data)
                )
                break


class ShinyLogic(EntityLogic):
    def __init__(self, _data):
        behaviors = {
            "Stand": ShinyLogicStand,
        }

        EntityLogic.__init__(self, _data, behaviors)

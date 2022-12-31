from Engine.entityLogic import EntityLogic, Behavior
from Engine.eventSystem import Event, eventType


class ShinyLogicStand(Behavior):
    def process(self, _dt):
        for event in self.data.env.pastEvents.getEvents(eventType.PickUp):
            if event.data == self.data.position:
                self.data.env.futureEvents.sendEvent(
                    Event(eventType.PickMe, self, self.data.inventory)
                )
                self.data.env.removeItem(self.data.id)


class ShinyLogic(EntityLogic):
    def __init__(self, _data):
        behaviors = {
            "Stand": ShinyLogicStand,
        }

        EntityLogic.__init__(self, _data, behaviors)

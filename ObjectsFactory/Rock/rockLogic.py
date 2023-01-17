from Engine.entityLogic import EntityLogic, Behaviour
from Engine.eventSystem import Event, eventType


class RockLogicStand(Behaviour):
    def process(self, _dt):
        for event in self.data.env.pastEvents.getEvents(eventType.Move):
            # print("Got event move to " + str(event.data) + ", but posiiton " + str(self.data.position))
            if event.data == self.data.position:
                self.data.env.futureEvents.sendEvent(
                    Event(
                        eventType.MoveProhibited,
                        self,
                        self.data.position
                    )
                )


class RockLogic(EntityLogic):
    def __init__(self, _data):
        behaviours = {
            "Stand": RockLogicStand
        }

        EntityLogic.__init__(self, _data, behaviours)

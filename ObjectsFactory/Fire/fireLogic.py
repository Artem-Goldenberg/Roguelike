from Engine.entityLogic import EntityLogic, Behaviour
from Engine.eventSystem import Event, eventType


class FireLogicStand(Behaviour):
    def __init__(self, _data):
        self.data = _data
        self.state_lasts = 0.0
        self.duration = 0.5
        self.atack_rate = 0.7
        self.time_since_last_attack = 0.0
        self.atacking = False

    def process(self, _dt):
        self.state_lasts += _dt
        self.time_since_last_attack += _dt
        self.data.animation_stage = (self.state_lasts % self.duration) / self.duration

        for event in self.data.env.pastEvents.getEvents(eventType.Moved):
            if event.data == self.data.position:
                self.atacking = True

        if self.atacking:
            if self.data.env.player.data.position != self.data.position:
                self.atacking = False

        if self.atacking and self.time_since_last_attack >= self.atack_rate:
            self.data.env.futureEvents.sendEvent(
                Event(
                    eventType.Atack,
                    self,
                    self.data.position
                )
            )
            self.time_since_last_attack = 0.0


class FireLogic(EntityLogic):
    def __init__(self, _data):
        behaviours = {
            "Burn": FireLogicStand
        }

        EntityLogic.__init__(self, _data, behaviours)

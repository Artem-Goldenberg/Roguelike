# import logging

from Engine.entityLogic import EntityLogic, Behaviour
from Engine.eventSystem import eventType, Event
# from Engine.entityData import Inventory


def direction(pos):
    if pos == (0, 1):
        return "Down"
    if pos == (0, -1):
        return "Up"
    if pos == (1, 0):
        return "Right"
    if pos == (-1, 0):
        return "Left"
    else:
        print("Wtf: " + str(pos))
        raise


class DefaultBehaviourStanding(Behaviour):
    def __init__(self, _data):
        self.data = _data
        self.state_lasts = 0.0
        self.duration = 1.0
        self.beginning_steady_time = 0.15

    def process(self, _dt):
        # normal behaviour
        self.state_lasts += _dt
        self.data.animation_stage = (self.state_lasts % self.duration) / self.duration

        for event in self.data.env.pastEvents.getEvents(eventType.Move):
            if event.data[0] == self.data.position[0] and event.data[1] == self.data.position[1]:
                self.data.env.futureEvents.sendEvent(
                    Event(
                        eventType.SomeoneThere,
                        self,
                        self.data.position
                    )
                )

        for event in self.data.env.pastEvents.getEvents(eventType.Atack):
            if event.data[:2] == self.data.position:
                self.data.state = "Hurt" + direction(self.data.custom)
                self.data.hp -= event.data[2]
                self.data.animation_stage = 0.0
                return

        if self.state_lasts < self.beginning_steady_time:
            # ignore everything
            return

        else:
            for event in self.data.getInstructions():
                if event.event_type == eventType.Move:
                    if event.data == self.data.custom:
                        self.data.state = "Walking" + direction(self.data.custom)
                        self.data.animation_stage = 0.0
                        self.data.env.futureEvents.sendEvent(
                            Event(
                                eventType.Move,
                                self,
                                [
                                    self.data.position[0] + self.data.custom[0] * self.data.env.grid_step,
                                    self.data.position[1] + self.data.custom[1] * self.data.env.grid_step
                                ]
                            )
                        )
                    else:
                        self.data.custom = event.data
                        self.data.state = "Standing" + direction(self.data.custom)

                if event.event_type == eventType.Atack:
                    if event.data == "Normal":
                        self.data.state = "Atacking" + direction(self.data.custom)
                        self.data.animation_stage = 0.0
                    if event.data == "Massive":
                        self.data.state = "MassiveAtacking" + direction(self.data.custom)
                        self.data.animation_stage = 0.0

                if event.event_type == eventType.PickUp:
                    self.data.state = "PickingUp" + direction(self.data.custom)
                    self.data.animation_stage = 0.0
                    self.data.env.futureEvents.sendEvent(
                        Event(
                            eventType.PickUp,
                            self,
                            [
                                self.data.position[0],
                                self.data.position[1]
                            ]
                        )
                    )


class DefaultBehaviourWalking(Behaviour):
    def __init__(self, _data):
        self.data = _data
        self.state_lasts = 0.0
        self.duration = _data.step_duration
        self.beginning_steady_time = 0.2

    def process(self, _dt):
        for event in self.data.env.pastEvents.getEvents(eventType.Move):
            if event.data[0] == self.data.position[0] and event.data[1] == self.data.position[1]:
                self.data.env.futureEvents.sendEvent(
                    Event(
                        eventType.SomeoneThere,
                        self,
                        self.data.position
                    )
                )

        for event in self.data.env.pastEvents.getEvents(eventType.MoveProhibited):
            if (
                    event.data == [
                        self.data.position[0] + self.data.custom[0] * self.data.env.grid_step,
                        self.data.position[1] + self.data.custom[1] * self.data.env.grid_step
                    ]
            ):
                self.data.state = "Standing" + direction(self.data.custom)
                self.data.animation_stage = 0.0
                return

        for event in self.data.env.pastEvents.getEvents(eventType.SomeoneThere):
            if (
                    event.data == [
                        self.data.position[0] + self.data.custom[0] * self.data.env.grid_step,
                        self.data.position[1] + self.data.custom[1] * self.data.env.grid_step
                    ]
            ):
                self.data.state = "Atacking" + direction(self.data.custom)
                self.data.animation_stage = 0.0
                return

        self.state_lasts += _dt
        self.data.animation_stage = self.state_lasts / self.duration

        continue_key_pressed = False
        for event in self.data.getInstructions():
            if event.event_type == eventType.Move and event.data == self.data.custom:
                continue_key_pressed = True

        if self.state_lasts <= self.beginning_steady_time:
            for event in self.data.env.pastEvents.getEvents(eventType.Atack):
                if event.data == self.data.position:
                    self.data.state = "Hurt" + direction(self.data.custom)
                    self.data.hp -= 10
                    self.data.animation_stage = 0.0
                    return

        if self.state_lasts >= self.duration:
            self.data.position[0] += self.data.custom[0] * self.data.env.grid_step
            self.data.position[1] += self.data.custom[1] * self.data.env.grid_step
            self.data.env.futureEvents.sendEvent(
                Event(
                    eventType.Moved,
                    self,
                    [
                        self.data.position[0],
                        self.data.position[1]
                    ]
                )
            )
            if continue_key_pressed:
                self.state_lasts = 0.0
                self.data.animation_stage = 0.0
                self.data.env.futureEvents.sendEvent(
                    Event(
                        eventType.Move,
                        self,
                        [
                            self.data.position[0] + self.data.custom[0] * self.data.env.grid_step,
                            self.data.position[1] + self.data.custom[1] * self.data.env.grid_step
                        ]
                    )
                )
            else:
                self.data.state = "Standing" + direction(self.data.custom)
                self.data.animation_stage = 0.0

        if self.state_lasts < self.beginning_steady_time and not continue_key_pressed:
            self.data.state = "Standing" + direction(self.data.custom)
            self.data.animation_stage = 0.0


class DefaultBehaviourAtacking(Behaviour):
    def __init__(self, _data):
        self.data = _data
        self.state_lasts = 0.0
        self.duration = 0.3

    def process(self, _dt):
        for event in self.data.env.pastEvents.getEvents(eventType.Move):
            if event.data[0] == self.data.position[0] and event.data[1] == self.data.position[1]:
                self.data.env.futureEvents.sendEvent(
                    Event(
                        eventType.SomeoneThere,
                        self,
                        self.data.position
                    )
                )

        for event in self.data.env.pastEvents.getEvents(eventType.Atack):
            if event.data[0] == self.data.position[0] and event.data[1] == self.data.position[1]:
                self.data.state = "Hurt" + direction(self.data.custom)
                self.data.hp -= event.data[2]
                self.data.animation_stage = 0.0
                return

        self.state_lasts += _dt
        self.data.animation_stage = self.state_lasts / self.duration

        if self.state_lasts >= self.duration:
            self.data.env.futureEvents.sendEvent(
                Event(
                    eventType.Atack,
                    self,
                    [
                        self.data.position[0] + self.data.custom[0] * self.data.env.grid_step,
                        self.data.position[1] + self.data.custom[1] * self.data.env.grid_step,
                        self.data.damage
                    ]
                )
            )
            self.data.state = "Standing" + direction(self.data.custom)
            self.data.animation_stage = 0.0


class DefaultBehaviourMassiveAtacking(Behaviour):
    def __init__(self, _data):
        self.data = _data
        self.state_lasts = 0.0
        self.duration = 0.5
        self.beginning_steady_time = 0.25

    def process(self, _dt):
        for event in self.data.env.pastEvents.getEvents(eventType.Move):
            if event.data[0] == self.data.position[0] and event.data[1] == self.data.position[1]:
                self.data.env.futureEvents.sendEvent(
                    Event(
                        eventType.SomeoneThere,
                        self,
                        self.data.position
                    )
                )

        for event in self.data.env.pastEvents.getEvents(eventType.Atack):
            if event.data == self.data.position:
                self.data.state = "Hurt" + direction(self.data.custom)
                self.data.hp -= 10
                self.data.animation_stage = 0.0
                return

        self.state_lasts += _dt
        self.data.animation_stage = self.state_lasts / self.duration

        continue_key_pressed = False
        for event in self.data.getInstructions():
            if event.event_type == eventType.Atack and event.data == "Massive":
                continue_key_pressed = True
                

        if self.state_lasts >= self.duration:
            # this is where we attack, I guess ...
            for d in [
                (0, 0), (0, 1), (0, -1), (1, 0), (-1, 0),
                (1, 1), (1, -1), (-1, 1), (-1, -1)
            ]:
                self.data.env.futureEvents.sendEvent( 
                    Event(
                        eventType.MassiveAttack, 
                        self, 
                        [
                            self.data.position[0] // self.data.env.grid_step + d[0],
                            self.data.position[1] // self.data.env.grid_step + d[1],
                            self.data.damage
                        ]
                    )
                )
            if continue_key_pressed:
                self.state_lasts = 0.0
                self.data.animation_stage = 0.0
            else:
                self.data.state = "Standing" + direction(self.data.custom)
                self.data.animation_stage = 0.0

        if self.state_lasts < self.beginning_steady_time and not continue_key_pressed:
            self.data.state = "Standing" + direction(self.data.custom)
            self.data.animation_stage = 0.0


class DefaultBehaviourHurt(Behaviour):
    def __init__(self, _data):
        self.data = _data
        self.state_lasts = 0.0
        self.duration = 0.3

    def process(self, _dt):
        for event in self.data.env.pastEvents.getEvents(eventType.Move):
            if event.data[0] == self.data.position[0] and event.data[1] == self.data.position[1]:
                self.data.env.futureEvents.sendEvent(
                    Event(
                        eventType.SomeoneThere,
                        self,
                        self.data.position
                    )
                )

        self.state_lasts += _dt
        self.data.animation_stage = self.state_lasts / self.duration

        if self.state_lasts >= self.duration:
            if self.data.hp > 0:
                self.data.state = "Standing" + direction(self.data.custom)
                self.data.animation_stage = 0.0
            else:
                self.data.state = "Dying" + direction(self.data.custom)
                self.data.animation_stage = 0.0


class DefaultBehaviourPickingUp(Behaviour):
    def __init__(self, _data):
        self.data = _data
        self.state_lasts = 0.0
        self.duration = 0.3
        self.items_to_take = []

    def process(self, _dt):
        for event in self.data.env.pastEvents.getEvents(eventType.Move):
            if event.data[0] == self.data.position[0] and event.data[1] == self.data.position[1]:
                self.data.env.futureEvents.sendEvent(
                    Event(
                        eventType.SomeoneThere,
                        self,
                        self.data.position
                    )
                )

        for event in self.data.env.pastEvents.getEvents(eventType.Atack):
            if event.data == self.data.position:
                self.data.state = "Hurt" + direction(self.data.custom)
                self.data.hp -= 10
                self.data.animation_stage = 0.0
                return

        for event in self.data.env.pastEvents.getEvents(eventType.Pickable):
            if event.data.position[0] == self.data.position[0] and event.data.position[1] == self.data.position[1]:
                self.items_to_take.append(event.data)

        self.state_lasts += _dt
        self.data.animation_stage = self.state_lasts / self.duration

        if self.state_lasts >= self.duration:
            if len(self.items_to_take) > 0:
                self.data.inventory.merge(self.items_to_take[0].inventory)
                if self.items_to_take[0].inventory.isEmpty():
                    self.data.env.removeItem(self.items_to_take[0])

            self.data.state = "Standing" + direction(self.data.custom)
            self.data.animation_stage = 0.0


class DefaultBehaviourDying(Behaviour):
    def __init__(self, _data):
        self.data = _data
        self.state_lasts = 0.0
        self.duration = 1.0

    def process(self, _dt):
        self.state_lasts += _dt

        if self.state_lasts >= self.duration:
            self.data.animation_stage = 0.8
        else:
            self.data.animation_stage = self.state_lasts / self.duration

        for event in self.data.env.pastEvents.getEvents(eventType.PickUp):
            if event.data == self.data.position:
                self.data.env.futureEvents.sendEvent(
                    Event(eventType.Pickable, self, self.data)
                )
                break


class DefaultEntityLogic(EntityLogic):
    def __init__(self, _data):
        behaviours = {
            "StandingUp": DefaultBehaviourStanding,
            "StandingDown": DefaultBehaviourStanding,
            "StandingLeft": DefaultBehaviourStanding,
            "StandingRight": DefaultBehaviourStanding,
            "WalkingUp": DefaultBehaviourWalking,
            "WalkingDown": DefaultBehaviourWalking,
            "WalkingRight": DefaultBehaviourWalking,
            "WalkingLeft": DefaultBehaviourWalking,
            "AtackingUp": DefaultBehaviourAtacking,
            "AtackingDown": DefaultBehaviourAtacking,
            "AtackingLeft": DefaultBehaviourAtacking,
            "AtackingRight": DefaultBehaviourAtacking,
            "MassiveAtackingUp": DefaultBehaviourMassiveAtacking,
            "MassiveAtackingDown": DefaultBehaviourMassiveAtacking,
            "MassiveAtackingLeft": DefaultBehaviourMassiveAtacking,
            "MassiveAtackingRight": DefaultBehaviourMassiveAtacking,
            "HurtUp": DefaultBehaviourHurt,
            "HurtDown": DefaultBehaviourHurt,
            "HurtLeft": DefaultBehaviourHurt,
            "HurtRight": DefaultBehaviourHurt,
            "PickingUpUp": DefaultBehaviourPickingUp,
            "PickingUpDown": DefaultBehaviourPickingUp,
            "PickingUpLeft": DefaultBehaviourPickingUp,
            "PickingUpRight": DefaultBehaviourPickingUp,
            "DyingUp": DefaultBehaviourDying,
            "DyingDown": DefaultBehaviourDying,
            "DyingLeft": DefaultBehaviourDying,
            "DyingRight": DefaultBehaviourDying
        }

        EntityLogic.__init__(self, _data, behaviours)
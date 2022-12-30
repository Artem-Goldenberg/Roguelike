# import logging

from Engine.entityLogic import EntityLogic, Behavior
from Engine.eventSystem import eventType, Event


class PlayerBehaviourStandingUp(Behavior):
    def __init__(self, _data):
        self.data = _data
        self.state_lasts = 0.0
        self.duration = 1.0
        self.beginning_steady_time = 0.15

    def process(self, _dt):
        # normal behaviour
        self.state_lasts += _dt
        self.data.animation_stage = (self.state_lasts % self.duration) / self.duration

        if self.state_lasts < self.beginning_steady_time:
            # ignore everything
            return

        else:
            for event in self.data.env.keyboardEvents.getEvents():
                if event.event_type == eventType.Move:
                    if event.data == (1, 0):
                        self.data.state = "StandingRight"
                        self.data.animation_stage = 0.0
                    if event.data == (-1, 0):
                        self.data.state = "StandingLeft"
                        self.data.animation_stage = 0.0
                    if event.data == (0, 1):
                        self.data.state = "StandingDown"
                        self.data.animation_stage = 0.0
                    if event.data == (0, -1):
                        self.data.state = "WalkingUp"
                        self.data.animation_stage = 0.0
                        self.data.env.futureEvents.sendEvent(
                            Event(
                                eventType.Move,
                                self,
                                [
                                    self.data.position[0],
                                    self.data.position[1] - self.data.env.grid_step
                                ]
                            )
                        )

                if event.event_type == eventType.Atack:
                    if event.data == "Normal":
                        self.data.state = "AtackingUp"
                        self.data.animation_stage = 0.0
                    if event.data == "Massive":
                        self.data.state = "MassiveAtackingUp"
                        self.data.animation_stage = 0.0


class PlayerBehaviourStandingDown(Behavior):
    def __init__(self, _data):
        self.data = _data
        self.state_lasts = 0.0
        self.duration = 1.0
        self.beginning_steady_time = 0.15

    def process(self, _dt):
        # normal behaviour
        self.state_lasts += _dt
        self.data.animation_stage = (self.state_lasts % self.duration) / self.duration

        if self.state_lasts < self.beginning_steady_time:
            # ignore everything
            return

        else:
            for event in self.data.env.keyboardEvents.getEvents():
                if event.event_type == eventType.Move:
                    if event.data == (1, 0):
                        self.data.state = "StandingRight"
                        self.data.animation_stage = 0.0
                    if event.data == (-1, 0):
                        self.data.state = "StandingLeft"
                        self.data.animation_stage = 0.0
                    if event.data == (0, 1):
                        self.data.state = "WalkingDown"
                        self.data.animation_stage = 0.0
                        self.data.env.futureEvents.sendEvent(
                            Event(
                                eventType.Move,
                                self,
                                [
                                    self.data.position[0],
                                    self.data.position[1] + self.data.env.grid_step
                                ]
                            )
                        )
                    if event.data == (0, -1):
                        self.data.state = "StandingUp"
                        self.data.animation_stage = 0.0

                if event.event_type == eventType.Atack:
                    if event.data == "Normal":
                        self.data.state = "AtackingDown"
                        self.data.animation_stage = 0.0
                    if event.data == "Massive":
                        self.data.state = "MassiveAtackingDown"
                        self.data.animation_stage = 0.0


class PlayerBehaviourStandingLeft(Behavior):
    def __init__(self, _data):
        self.data = _data
        self.state_lasts = 0.0
        self.duration = 1.0
        self.beginning_steady_time = 0.15

    def process(self, _dt):
        # normal behaviour
        self.state_lasts += _dt
        self.data.animation_stage = (self.state_lasts % self.duration) / self.duration

        if self.state_lasts < self.beginning_steady_time:
            # ignore everything
            return

        else:
            for event in self.data.env.keyboardEvents.getEvents():
                if event.event_type == eventType.Move:
                    if event.data == (1, 0):
                        self.data.state = "StandingRight"
                        self.data.animation_stage = 0.0
                    if event.data == (-1, 0):
                        self.data.state = "WalkingLeft"
                        self.data.animation_stage = 0.0
                        self.data.env.futureEvents.sendEvent(
                            Event(
                                eventType.Move,
                                self,
                                [
                                    self.data.position[0] - self.data.env.grid_step,
                                    self.data.position[1]
                                ]
                            )
                        )
                    if event.data == (0, 1):
                        self.data.state = "StandingDown"
                        self.data.animation_stage = 0.0
                    if event.data == (0, -1):
                        self.data.state = "StandingUp"
                        self.data.animation_stage = 0.0

                if event.event_type == eventType.Atack:
                    if event.data == "Normal":
                        self.data.state = "AtackingLeft"
                        self.data.animation_stage = 0.0
                    if event.data == "Massive":
                        self.data.state = "MassiveAtackingLeft"
                        self.data.animation_stage = 0.0


class PlayerBehaviourStandingRight(Behavior):
    def __init__(self, _data):
        self.data = _data
        self.state_lasts = 0.0
        self.duration = 1.0
        self.beginning_steady_time = 0.15

    def process(self, _dt):
        # normal behaviour
        self.state_lasts += _dt
        self.data.animation_stage = (self.state_lasts % self.duration) / self.duration

        if self.state_lasts < self.beginning_steady_time:
            # ignore everything
            return

        else:
            for event in self.data.env.keyboardEvents.getEvents():
                if event.event_type == eventType.Move:
                    if event.data == (1, 0):
                        self.data.state = "WalkingRight"
                        self.data.animation_stage = 0.0
                        self.data.env.futureEvents.sendEvent(
                            Event(
                                eventType.Move,
                                self,
                                [
                                    self.data.position[0] + self.data.env.grid_step,
                                    self.data.position[1]
                                ]
                            )
                        )
                    if event.data == (-1, 0):
                        self.data.state = "StandingLeft"
                        self.data.animation_stage = 0.0
                    if event.data == (0, 1):
                        self.data.state = "StandingDown"
                        self.data.animation_stage = 0.0
                    if event.data == (0, -1):
                        self.data.state = "StandingUp"
                        self.data.animation_stage = 0.0

                if event.event_type == eventType.Atack:
                    if event.data == "Normal":
                        self.data.state = "AtackingRight"
                        self.data.animation_stage = 0.0
                    if event.data == "Massive":
                        self.data.state = "MassiveAtackingRight"
                        self.data.animation_stage = 0.0


class PlayerBehaviourWalkingUp(Behavior):
    def __init__(self, _data):
        self.data = _data
        self.state_lasts = 0.0
        self.duration = 0.5
        self.beginning_steady_time = 0.15

    def process(self, _dt):
        for event in self.data.env.pastEvents.getEvents(eventType.MoveProhibited):
            if event.event_type == eventType.MoveProhibited and event.data == [self.data.position[0], self.data.position[1] - self.data.env.grid_step]:
                self.data.state = "StandingUp"
                return

        self.state_lasts += _dt
        self.data.animation_stage = self.state_lasts / self.duration

        continue_key_pressed = False
        for event in self.data.env.keyboardEvents.getEvents():
            if event.event_type == eventType.Move and event.data == (0, -1):
                continue_key_pressed = True

        if self.state_lasts >= self.duration:
            self.data.position[1] -= self.data.env.grid_step
            if continue_key_pressed:
                self.state_lasts = 0.0
                self.data.animation_stage = 0.0
                self.data.env.futureEvents.sendEvent(
                    Event(
                        eventType.Move,
                        self,
                        [
                            self.data.position[0],
                            self.data.position[1] - self.data.env.grid_step
                        ]
                    )
                )
            else:
                self.data.state = "StandingUp"
                self.data.animation_stage = 0.0

        if self.state_lasts < self.beginning_steady_time and not continue_key_pressed:
            self.data.state = "StandingUp"
            self.data.animation_stage = 0.0


class PlayerBehaviourWalkingDown(Behavior):
    def __init__(self, _data):
        self.data = _data
        self.state_lasts = 0.0
        self.duration = 0.5
        self.beginning_steady_time = 0.15

    def process(self, _dt):
        for event in self.data.env.pastEvents.getEvents(eventType.MoveProhibited):
            if event.event_type == eventType.MoveProhibited and event.data == [self.data.position[0], self.data.position[1] + self.data.env.grid_step]:
                self.data.state = "StandingDown"
                return

        self.state_lasts += _dt
        self.data.animation_stage = self.state_lasts / self.duration

        continue_key_pressed = False
        for event in self.data.env.keyboardEvents.getEvents():
            if event.event_type == eventType.Move and event.data == (0, 1):
                continue_key_pressed = True

        if self.state_lasts >= self.duration:
            self.data.position[1] += 75
            if continue_key_pressed:
                self.state_lasts = 0.0
                self.data.animation_stage = 0.0
                self.data.env.futureEvents.sendEvent(
                    Event(
                        eventType.Move,
                        self,
                        [
                            self.data.position[0],
                            self.data.position[1] + self.data.env.grid_step
                        ]
                    )
                )
            else:
                self.data.state = "StandingDown"
                self.data.animation_stage = 0.0

        if self.state_lasts < self.beginning_steady_time and not continue_key_pressed:
            self.data.state = "StandingDown"
            self.data.animation_stage = 0.0


class PlayerBehaviourWalkingLeft(Behavior):
    def __init__(self, _data):
        self.data = _data
        self.state_lasts = 0.0
        self.duration = 0.5
        self.beginning_steady_time = 0.2

    def process(self, _dt):
        for event in self.data.env.pastEvents.getEvents(eventType.MoveProhibited):
            if event.event_type == eventType.MoveProhibited and event.data == [self.data.position[0] - self.data.env.grid_step, self.data.position[1]]:
                self.data.state = "StandingLeft"
                return

        self.state_lasts += _dt
        self.data.animation_stage = self.state_lasts / self.duration

        continue_key_pressed = False
        for event in self.data.env.keyboardEvents.getEvents():
            if event.event_type == eventType.Move and event.data == (-1, 0):
                continue_key_pressed = True

        if self.state_lasts >= self.duration:
            self.data.position[0] -= 75
            if continue_key_pressed:
                self.state_lasts = 0.0
                self.data.animation_stage = 0.0
                self.data.env.futureEvents.sendEvent(
                    Event(
                        eventType.Move,
                        self,
                        [
                            self.data.position[0] - self.data.env.grid_step,
                            self.data.position[1]
                        ]
                    )
                )
            else:
                self.data.state = "StandingLeft"
                self.data.animation_stage = 0.0

        if self.state_lasts < self.beginning_steady_time and not continue_key_pressed:
            self.data.state = "StandingLeft"
            self.data.animation_stage = 0.0


class PlayerBehaviourWalkingRight(Behavior):
    def __init__(self, _data):
        self.data = _data
        self.state_lasts = 0.0
        self.duration = 0.5
        self.beginning_steady_time = 0.15

    def process(self, _dt):
        for event in self.data.env.pastEvents.getEvents(eventType.MoveProhibited):
            if event.event_type == eventType.MoveProhibited and event.data == [self.data.position[0] + self.data.env.grid_step, self.data.position[1]]:
                self.data.state = "StandingRight"
                return

        self.state_lasts += _dt
        self.data.animation_stage = self.state_lasts / self.duration

        continue_key_pressed = False
        for event in self.data.env.keyboardEvents.getEvents():
            if event.event_type == eventType.Move and event.data == (1, 0):
                continue_key_pressed = True

        if self.state_lasts >= self.duration:
            self.data.position[0] += 75
            if continue_key_pressed:
                self.state_lasts = 0.0
                self.data.animation_stage = 0.0
                self.data.env.futureEvents.sendEvent(
                    Event(
                        eventType.Move,
                        self,
                        [
                            self.data.position[0] + self.data.env.grid_step,
                            self.data.position[1]
                        ]
                    )
                )
            else:
                self.data.state = "StandingRight"
                self.data.animation_stage = 0.0

        if self.state_lasts < self.beginning_steady_time and not continue_key_pressed:
            self.data.state = "StandingRight"
            self.data.animation_stage = 0.0


class PlayerBehaviourAtackingUp(Behavior):
    def __init__(self, _data):
        self.data = _data
        self.state_lasts = 0.0
        self.duration = 0.3

    def process(self, _dt):
        self.state_lasts += _dt
        self.data.animation_stage = self.state_lasts / self.duration

        if self.state_lasts >= self.duration:
            self.data.state = "StandingUp"
            self.data.animation_stage = 0.0


class PlayerBehaviourAtackingDown(Behavior):
    def __init__(self, _data):
        self.data = _data
        self.state_lasts = 0.0
        self.duration = 0.3

    def process(self, _dt):
        self.state_lasts += _dt
        self.data.animation_stage = self.state_lasts / self.duration

        if self.state_lasts >= self.duration:
            self.data.state = "StandingDown"
            self.data.animation_stage = 0.0


class PlayerBehaviourAtackingLeft(Behavior):
    def __init__(self, _data):
        self.data = _data
        self.state_lasts = 0.0
        self.duration = 0.3

    def process(self, _dt):
        self.state_lasts += _dt
        self.data.animation_stage = self.state_lasts / self.duration

        if self.state_lasts >= self.duration:
            self.data.state = "StandingLeft"
            self.data.animation_stage = 0.0


class PlayerBehaviourAtackingRight(Behavior):
    def __init__(self, _data):
        self.data = _data
        self.state_lasts = 0.0
        self.duration = 0.3

    def process(self, _dt):
        self.state_lasts += _dt
        self.data.animation_stage = self.state_lasts / self.duration

        if self.state_lasts >= self.duration:
            self.data.state = "StandingRight"
            self.data.animation_stage = 0.0


class PlayerBehaviourMassiveAtackingUp(Behavior):
    def __init__(self, _data):
        self.data = _data
        self.state_lasts = 0.0
        self.duration = 0.5
        self.beginning_steady_time = 0.25

    def process(self, _dt):
        self.state_lasts += _dt
        self.data.animation_stage = self.state_lasts / self.duration

        continue_key_pressed = False
        for event in self.data.env.keyboardEvents.getEvents():
            if event.event_type == eventType.Atack and event.data == "Massive":
                continue_key_pressed = True

        if self.state_lasts >= self.duration:
            if continue_key_pressed:
                self.state_lasts = 0.0
                self.data.animation_stage = 0.0
            else:
                self.data.state = "StandingUp"
                self.data.animation_stage = 0.0

        if self.state_lasts < self.beginning_steady_time and not continue_key_pressed:
            self.data.state = "StandingUp"
            self.data.animation_stage = 0.0


class PlayerBehaviourMassiveAtackingDown(Behavior):
    def __init__(self, _data):
        self.data = _data
        self.state_lasts = 0.0
        self.duration = 0.5
        self.beginning_steady_time = 0.25

    def process(self, _dt):
        self.state_lasts += _dt
        self.data.animation_stage = self.state_lasts / self.duration

        continue_key_pressed = False
        for event in self.data.env.keyboardEvents.getEvents():
            if event.event_type == eventType.Atack and event.data == "Massive":
                continue_key_pressed = True

        if self.state_lasts >= self.duration:
            if continue_key_pressed:
                self.state_lasts = 0.0
                self.data.animation_stage = 0.0
            else:
                self.data.state = "StandingDown"
                self.data.animation_stage = 0.0

        if self.state_lasts < self.beginning_steady_time and not continue_key_pressed:
            self.data.state = "StandingDown"
            self.data.animation_stage = 0.0


class PlayerBehaviourMassiveAtackingLeft(Behavior):
    def __init__(self, _data):
        self.data = _data
        self.state_lasts = 0.0
        self.duration = 0.5
        self.beginning_steady_time = 0.25

    def process(self, _dt):
        self.state_lasts += _dt
        self.data.animation_stage = self.state_lasts / self.duration

        continue_key_pressed = False
        for event in self.data.env.keyboardEvents.getEvents():
            if event.event_type == eventType.Atack and event.data == "Massive":
                continue_key_pressed = True

        if self.state_lasts >= self.duration:
            if continue_key_pressed:
                self.state_lasts = 0.0
                self.data.animation_stage = 0.0
            else:
                self.data.state = "StandingLeft"
                self.data.animation_stage = 0.0

        if self.state_lasts < self.beginning_steady_time and not continue_key_pressed:
            self.data.state = "StandingLeft"
            self.data.animation_stage = 0.0


class PlayerBehaviourMassiveAtackingRight(Behavior):
    def __init__(self, _data):
        self.data = _data
        self.state_lasts = 0.0
        self.duration = 0.5
        self.beginning_steady_time = 0.25

    def process(self, _dt):
        self.state_lasts += _dt
        self.data.animation_stage = self.state_lasts / self.duration

        continue_key_pressed = False
        for event in self.data.env.keyboardEvents.getEvents():
            if event.event_type == eventType.Atack and event.data == "Massive":
                continue_key_pressed = True

        if self.state_lasts >= self.duration:
            if continue_key_pressed:
                self.state_lasts = 0.0
                self.data.animation_stage = 0.0
            else:
                self.data.state = "StandingRight"
                self.data.animation_stage = 0.0

        if self.state_lasts < self.beginning_steady_time and not continue_key_pressed:
            self.data.state = "StandingRight"
            self.data.animation_stage = 0.0


class PlayerEntityLogic(EntityLogic):
    def __init__(self, _data):
        behaviours = {
            "StandingUp": PlayerBehaviourStandingUp,
            "StandingDown": PlayerBehaviourStandingDown,
            "StandingLeft": PlayerBehaviourStandingLeft,
            "StandingRight": PlayerBehaviourStandingRight,
            "WalkingUp": PlayerBehaviourWalkingUp,
            "WalkingDown": PlayerBehaviourWalkingDown,
            "WalkingLeft": PlayerBehaviourWalkingLeft,
            "WalkingRight": PlayerBehaviourWalkingRight,
            "AtackingUp": PlayerBehaviourAtackingUp,
            "AtackingDown": PlayerBehaviourAtackingDown,
            "AtackingLeft": PlayerBehaviourAtackingLeft,
            "AtackingRight": PlayerBehaviourAtackingRight,
            "MassiveAtackingUp": PlayerBehaviourMassiveAtackingUp,
            "MassiveAtackingDown": PlayerBehaviourMassiveAtackingDown,
            "MassiveAtackingLeft": PlayerBehaviourMassiveAtackingLeft,
            "MassiveAtackingRight": PlayerBehaviourMassiveAtackingRight
        }

        EntityLogic.__init__(self, _data, behaviours)

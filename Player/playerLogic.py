# import logging

from Engine.entityLogic import EntityLogic, Behaviour
from Engine.eventSystem import eventType  # Event


class PlayerBehaviourStandingUp(Behaviour):
    def __init__(self, _env):
        self.env = _env
        self.state_lasts = 0.0
        self.duration = 1.0
        self.beginning_steady_time = 0.15

    def process(self, _data, _dt):
        # normal behaviour
        self.state_lasts += _dt
        _data.animation_stage = (self.state_lasts % self.duration) / self.duration

        if self.state_lasts < self.beginning_steady_time:
            # ignore everything
            return

        else:
            for event in self.env.keyboardEvents.getEvents():
                if event.event_type == eventType.Move:
                    if event.data == (1, 0):
                        _data.state = "StandingRight"
                        _data.animation_stage = 0.0
                    if event.data == (-1, 0):
                        _data.state = "StandingLeft"
                        _data.animation_stage = 0.0
                    if event.data == (0, 1):
                        _data.state = "StandingDown"
                        _data.animation_stage = 0.0
                    if event.data == (0, -1):
                        _data.state = "WalkingUp"
                        _data.animation_stage = 0.0

                if event.event_type == eventType.Atack:
                    if event.data == "Normal":
                        _data.state = "AtackingUp"
                        _data.animation_stage = 0.0
                    if event.data == "Massive":
                        _data.state = "MassiveAtackingUp"
                        _data.animation_stage = 0.0


class PlayerBehaviourStandingDown(Behaviour):
    def __init__(self, _env):
        self.env = _env
        self.state_lasts = 0.0
        self.duration = 1.0
        self.beginning_steady_time = 0.15

    def process(self, _data, _dt):
        # normal behaviour
        self.state_lasts += _dt
        _data.animation_stage = (self.state_lasts % self.duration) / self.duration

        if self.state_lasts < self.beginning_steady_time:
            # ignore everything
            return

        else:
            for event in self.env.keyboardEvents.getEvents():
                if event.event_type == eventType.Move:
                    if event.data == (1, 0):
                        _data.state = "StandingRight"
                        _data.animation_stage = 0.0
                    if event.data == (-1, 0):
                        _data.state = "StandingLeft"
                        _data.animation_stage = 0.0
                    if event.data == (0, 1):
                        _data.state = "WalkingDown"
                        _data.animation_stage = 0.0
                    if event.data == (0, -1):
                        _data.state = "StandingUp"
                        _data.animation_stage = 0.0

                if event.event_type == eventType.Atack:
                    if event.data == "Normal":
                        _data.state = "AtackingDown"
                        _data.animation_stage = 0.0
                    if event.data == "Massive":
                        _data.state = "MassiveAtackingDown"
                        _data.animation_stage = 0.0


class PlayerBehaviourStandingLeft(Behaviour):
    def __init__(self, _env):
        self.env = _env
        self.state_lasts = 0.0
        self.duration = 1.0
        self.beginning_steady_time = 0.15

    def process(self, _data, _dt):
        # normal behaviour
        self.state_lasts += _dt
        _data.animation_stage = (self.state_lasts % self.duration) / self.duration

        if self.state_lasts < self.beginning_steady_time:
            # ignore everything
            return

        else:
            for event in self.env.keyboardEvents.getEvents():
                if event.event_type == eventType.Move:
                    if event.data == (1, 0):
                        _data.state = "StandingRight"
                        _data.animation_stage = 0.0
                    if event.data == (-1, 0):
                        _data.state = "WalkingLeft"
                        _data.animation_stage = 0.0
                    if event.data == (0, 1):
                        _data.state = "StandingDown"
                        _data.animation_stage = 0.0
                    if event.data == (0, -1):
                        _data.state = "StandingUp"
                        _data.animation_stage = 0.0

                if event.event_type == eventType.Atack:
                    if event.data == "Normal":
                        _data.state = "AtackingLeft"
                        _data.animation_stage = 0.0
                    if event.data == "Massive":
                        _data.state = "MassiveAtackingLeft"
                        _data.animation_stage = 0.0


class PlayerBehaviourStandingRight(Behaviour):
    def __init__(self, _env):
        self.env = _env
        self.state_lasts = 0.0
        self.duration = 1.0
        self.beginning_steady_time = 0.15

    def process(self, _data, _dt):
        # normal behaviour
        self.state_lasts += _dt
        _data.animation_stage = (self.state_lasts % self.duration) / self.duration

        if self.state_lasts < self.beginning_steady_time:
            # ignore everything
            return

        else:
            for event in self.env.keyboardEvents.getEvents():
                if event.event_type == eventType.Move:
                    if event.data == (1, 0):
                        _data.state = "WalkingRight"
                        _data.animation_stage = 0.0
                    if event.data == (-1, 0):
                        _data.state = "StandingLeft"
                        _data.animation_stage = 0.0
                    if event.data == (0, 1):
                        _data.state = "StandingDown"
                        _data.animation_stage = 0.0
                    if event.data == (0, -1):
                        _data.state = "StandingUp"
                        _data.animation_stage = 0.0

                if event.event_type == eventType.Atack:
                    if event.data == "Normal":
                        _data.state = "AtackingRight"
                        _data.animation_stage = 0.0
                    if event.data == "Massive":
                        _data.state = "MassiveAtackingRight"
                        _data.animation_stage = 0.0


class PlayerBehaviourWalkingUp(Behaviour):
    def __init__(self, _env):
        self.env = _env
        self.state_lasts = 0.0
        self.duration = 0.5
        self.beginning_steady_time = 0.15

    def process(self, _data, _dt):
        self.state_lasts += _dt
        _data.animation_stage = self.state_lasts / self.duration

        continue_key_pressed = False
        for event in self.env.keyboardEvents.getEvents():
            if event.event_type == eventType.Move and event.data == (0, -1):
                continue_key_pressed = True

        if self.state_lasts >= self.duration:
            _data.position[1] -= 75
            if continue_key_pressed:
                self.state_lasts = 0.0
                _data.animation_stage = 0.0
            else:
                _data.state = "StandingUp"
                _data.animation_stage = 0.0

        if self.state_lasts < self.beginning_steady_time and not continue_key_pressed:
            _data.state = "StandingUp"
            _data.animation_stage = 0.0


class PlayerBehaviourWalkingDown(Behaviour):
    def __init__(self, _env):
        self.env = _env
        self.state_lasts = 0.0
        self.duration = 0.5
        self.beginning_steady_time = 0.15

    def process(self, _data, _dt):
        self.state_lasts += _dt
        _data.animation_stage = self.state_lasts / self.duration

        continue_key_pressed = False
        for event in self.env.keyboardEvents.getEvents():
            if event.event_type == eventType.Move and event.data == (0, 1):
                continue_key_pressed = True

        if self.state_lasts >= self.duration:
            _data.position[1] += 75
            if continue_key_pressed:
                self.state_lasts = 0.0
                _data.animation_stage = 0.0
            else:
                _data.state = "StandingDown"
                _data.animation_stage = 0.0

        if self.state_lasts < self.beginning_steady_time and not continue_key_pressed:
            _data.state = "StandingDown"
            _data.animation_stage = 0.0


class PlayerBehaviourWalkingLeft(Behaviour):
    def __init__(self, _env):
        self.env = _env
        self.state_lasts = 0.0
        self.duration = 0.5
        self.beginning_steady_time = 0.2

    def process(self, _data, _dt):
        self.state_lasts += _dt
        _data.animation_stage = self.state_lasts / self.duration

        continue_key_pressed = False
        for event in self.env.keyboardEvents.getEvents():
            if event.event_type == eventType.Move and event.data == (-1, 0):
                continue_key_pressed = True

        if self.state_lasts >= self.duration:
            _data.position[0] -= 75
            if continue_key_pressed:
                self.state_lasts = 0.0
                _data.animation_stage = 0.0
            else:
                _data.state = "StandingLeft"
                _data.animation_stage = 0.0

        if self.state_lasts < self.beginning_steady_time and not continue_key_pressed:
            _data.state = "StandingLeft"
            _data.animation_stage = 0.0


class PlayerBehaviourWalkingRight(Behaviour):
    def __init__(self, _env):
        self.env = _env
        self.state_lasts = 0.0
        self.duration = 0.5
        self.beginning_steady_time = 0.15

    def process(self, _data, _dt):
        self.state_lasts += _dt
        _data.animation_stage = self.state_lasts / self.duration

        continue_key_pressed = False
        for event in self.env.keyboardEvents.getEvents():
            if event.event_type == eventType.Move and event.data == (1, 0):
                continue_key_pressed = True

        if self.state_lasts >= self.duration:
            _data.position[0] += 75
            if continue_key_pressed:
                self.state_lasts = 0.0
                _data.animation_stage = 0.0
            else:
                _data.state = "StandingRight"
                _data.animation_stage = 0.0

        if self.state_lasts < self.beginning_steady_time and not continue_key_pressed:
            _data.state = "StandingRight"
            _data.animation_stage = 0.0


class PlayerBehaviourAtackingUp(Behaviour):
    def __init__(self, _env):
        self.env = _env
        self.state_lasts = 0.0
        self.duration = 0.3

    def process(self, _data, _dt):
        self.state_lasts += _dt
        _data.animation_stage = self.state_lasts / self.duration

        if self.state_lasts >= self.duration:
            _data.state = "StandingUp"
            _data.animation_stage = 0.0


class PlayerBehaviourAtackingDown(Behaviour):
    def __init__(self, _env):
        self.env = _env
        self.state_lasts = 0.0
        self.duration = 0.3

    def process(self, _data, _dt):
        self.state_lasts += _dt
        _data.animation_stage = self.state_lasts / self.duration

        if self.state_lasts >= self.duration:
            _data.state = "StandingDown"
            _data.animation_stage = 0.0


class PlayerBehaviourAtackingLeft(Behaviour):
    def __init__(self, _env):
        self.env = _env
        self.state_lasts = 0.0
        self.duration = 0.3

    def process(self, _data, _dt):
        self.state_lasts += _dt
        _data.animation_stage = self.state_lasts / self.duration

        if self.state_lasts >= self.duration:
            _data.state = "StandingLeft"
            _data.animation_stage = 0.0


class PlayerBehaviourAtackingRight(Behaviour):
    def __init__(self, _env):
        self.env = _env
        self.state_lasts = 0.0
        self.duration = 0.3

    def process(self, _data, _dt):
        self.state_lasts += _dt
        _data.animation_stage = self.state_lasts / self.duration

        if self.state_lasts >= self.duration:
            _data.state = "StandingRight"
            _data.animation_stage = 0.0


class PlayerBehaviourMassiveAtackingUp(Behaviour):
    def __init__(self, _env):
        self.env = _env
        self.state_lasts = 0.0
        self.duration = 0.5
        self.beginning_steady_time = 0.25

    def process(self, _data, _dt):
        self.state_lasts += _dt
        _data.animation_stage = self.state_lasts / self.duration

        continue_key_pressed = False
        for event in self.env.keyboardEvents.getEvents():
            if event.event_type == eventType.Atack and event.data == "Massive":
                continue_key_pressed = True

        if self.state_lasts >= self.duration:
            if continue_key_pressed:
                self.state_lasts = 0.0
                _data.animation_stage = 0.0
            else:
                _data.state = "StandingUp"
                _data.animation_stage = 0.0

        if self.state_lasts < self.beginning_steady_time and not continue_key_pressed:
            _data.state = "StandingUp"
            _data.animation_stage = 0.0


class PlayerBehaviourMassiveAtackingDown(Behaviour):
    def __init__(self, _env):
        self.env = _env
        self.state_lasts = 0.0
        self.duration = 0.5
        self.beginning_steady_time = 0.25

    def process(self, _data, _dt):
        self.state_lasts += _dt
        _data.animation_stage = self.state_lasts / self.duration

        continue_key_pressed = False
        for event in self.env.keyboardEvents.getEvents():
            if event.event_type == eventType.Atack and event.data == "Massive":
                continue_key_pressed = True

        if self.state_lasts >= self.duration:
            if continue_key_pressed:
                self.state_lasts = 0.0
                _data.animation_stage = 0.0
            else:
                _data.state = "StandingDown"
                _data.animation_stage = 0.0

        if self.state_lasts < self.beginning_steady_time and not continue_key_pressed:
            _data.state = "StandingDown"
            _data.animation_stage = 0.0


class PlayerBehaviourMassiveAtackingLeft(Behaviour):
    def __init__(self, _env):
        self.env = _env
        self.state_lasts = 0.0
        self.duration = 0.5
        self.beginning_steady_time = 0.25

    def process(self, _data, _dt):
        self.state_lasts += _dt
        _data.animation_stage = self.state_lasts / self.duration

        continue_key_pressed = False
        for event in self.env.keyboardEvents.getEvents():
            if event.event_type == eventType.Atack and event.data == "Massive":
                continue_key_pressed = True

        if self.state_lasts >= self.duration:
            if continue_key_pressed:
                self.state_lasts = 0.0
                _data.animation_stage = 0.0
            else:
                _data.state = "StandingLeft"
                _data.animation_stage = 0.0

        if self.state_lasts < self.beginning_steady_time and not continue_key_pressed:
            _data.state = "StandingLeft"
            _data.animation_stage = 0.0


class PlayerBehaviourMassiveAtackingRight(Behaviour):
    def __init__(self, _env):
        self.env = _env
        self.state_lasts = 0.0
        self.duration = 0.5
        self.beginning_steady_time = 0.25

    def process(self, _data, _dt):
        self.state_lasts += _dt
        _data.animation_stage = self.state_lasts / self.duration

        continue_key_pressed = False
        for event in self.env.keyboardEvents.getEvents():
            if event.event_type == eventType.Atack and event.data == "Massive":
                continue_key_pressed = True

        if self.state_lasts >= self.duration:
            if continue_key_pressed:
                self.state_lasts = 0.0
                _data.animation_stage = 0.0
            else:
                _data.state = "StandingRight"
                _data.animation_stage = 0.0

        if self.state_lasts < self.beginning_steady_time and not continue_key_pressed:
            _data.state = "StandingRight"
            _data.animation_stage = 0.0


class PlayerEntityLogic(EntityLogic):
    def __init__(self, _env, _data):
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

        EntityLogic.__init__(self, _env, _data, behaviours)

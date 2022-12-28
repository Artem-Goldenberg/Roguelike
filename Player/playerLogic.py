import logging

from Engine.entityLogic import EntityLogic, Behaviour
from Engine.eventSystem import eventType  # Event


class PlayerSpriteStandingUp(Behaviour):
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


class PlayerSpriteStandingDown(Behaviour):
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


class PlayerSpriteStandingLeft(Behaviour):
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


class PlayerSpriteStandingRight(Behaviour):
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


class PlayerSpriteWalkingUp(Behaviour):
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
            _data.position[1] -= 50
            if continue_key_pressed:
                self.state_lasts = 0.0
                _data.animation_stage = 0.0
            else:
                _data.state = "StandingUp"
                _data.animation_stage = 0.0

        if self.state_lasts < self.beginning_steady_time and not continue_key_pressed:
            _data.state = "StandingUp"
            _data.animation_stage = 0.0


class PlayerSpriteWalkingDown(Behaviour):
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
            _data.position[1] += 50
            if continue_key_pressed:
                self.state_lasts = 0.0
                _data.animation_stage = 0.0
            else:
                _data.state = "StandingDown"
                _data.animation_stage = 0.0

        if self.state_lasts < self.beginning_steady_time and not continue_key_pressed:
            _data.state = "StandingDown"
            _data.animation_stage = 0.0


class PlayerSpriteWalkingLeft(Behaviour):
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
            _data.position[0] -= 50
            if continue_key_pressed:
                self.state_lasts = 0.0
                _data.animation_stage = 0.0
            else:
                _data.state = "StandingLeft"
                _data.animation_stage = 0.0

        if self.state_lasts < self.beginning_steady_time and not continue_key_pressed:
            _data.state = "StandingLeft"
            _data.animation_stage = 0.0


class PlayerSpriteWalkingRight(Behaviour):
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
            _data.position[0] += 50
            if continue_key_pressed:
                self.state_lasts = 0.0
                _data.animation_stage = 0.0
            else:
                _data.state = "StandingRight"
                _data.animation_stage = 0.0

        if self.state_lasts < self.beginning_steady_time and not continue_key_pressed:
            _data.state = "StandingRight"
            _data.animation_stage = 0.0


class PlayerSpriteAtackingUp(Behaviour):
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


class PlayerSpriteAtackingDown(Behaviour):
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


class PlayerSpriteAtackingLeft(Behaviour):
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


class PlayerSpriteAtackingRight(Behaviour):
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


class PlayerSpriteMassiveAtackingUp(Behaviour):
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


class PlayerSpriteMassiveAtackingDown(Behaviour):
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


class PlayerSpriteMassiveAtackingLeft(Behaviour):
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


class PlayerSpriteMassiveAtackingRight(Behaviour):
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
            "StandingUp": PlayerSpriteStandingUp,
            "StandingDown": PlayerSpriteStandingDown,
            "StandingLeft": PlayerSpriteStandingLeft,
            "StandingRight": PlayerSpriteStandingRight,
            "WalkingUp": PlayerSpriteWalkingUp,
            "WalkingDown": PlayerSpriteWalkingDown,
            "WalkingLeft": PlayerSpriteWalkingLeft,
            "WalkingRight": PlayerSpriteWalkingRight,
            "AtackingUp": PlayerSpriteAtackingUp,
            "AtackingDown": PlayerSpriteAtackingDown,
            "AtackingLeft": PlayerSpriteAtackingLeft,
            "AtackingRight": PlayerSpriteAtackingRight,
            "MassiveAtackingUp": PlayerSpriteMassiveAtackingUp,
            "MassiveAtackingDown": PlayerSpriteMassiveAtackingDown,
            "MassiveAtackingLeft": PlayerSpriteMassiveAtackingLeft,
            "MassiveAtackingRight": PlayerSpriteMassiveAtackingRight
        }

        EntityLogic.__init__(
            self,
            _env,
            _data,
            behaviours
        )

        self.active_state_name = ""
        self.active_state = None

    def handleEvents(self, _dt):
        if self.active_state_name != self.data.state:
            if not self.behaviors.__contains__(self.data.state):
                logging.info("HandleEvents: state is not implemented: " + str(self.data.state) )
                raise
            self.active_state = self.behaviors[self.data.state](self.env)
            self.active_state_name = self.data.state

        self.active_state.process(self.data, _dt)

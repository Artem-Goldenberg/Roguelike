import logging

from Engine.entityLogic import EntityLogic, Behavior
from Engine.eventSystem import eventType, Event


class PlayerBehaviorStanding(Behavior):
    def __init__(self, _data):
        self.data = _data
        self.state_lasts = 0.0
        self.duration = 1.0
        self.beginning_steady_time = 0.15

    def moveUp(self):
        logging.critical(
            "PlayerBehaviorStanding: moveUp is not implemented: PlayerBehaviorStanding(" + str(
                self) + ")"
        )
        raise

    def moveDown(self):
        logging.critical(
            "PlayerBehaviorStanding: moveDown is not implemented: PlayerBehaviorStanding(" + str(
                self) + ")"
        )
        raise

    def moveLeft(self):
        logging.critical(
            "PlayerBehaviorStanding: moveLeft is not implemented: PlayerBehaviorStanding(" + str(
                self) + ")"
        )
        raise

    def moveRight(self):
        logging.critical(
            "PlayerBehaviorStanding: moveRight is not implemented: PlayerBehaviorStanding(" + str(
                self) + ")"
        )
        raise

    def normalAttack(self):
        logging.critical(
            "PlayerBehaviorStanding: normalAttack is not implemented: PlayerBehaviorStanding(" + str(
                self) + ")"
        )
        raise

    def massiveAttack(self):
        logging.critical(
            "PlayerBehaviorStanding: massiveAttack is not implemented: PlayerBehaviorStanding(" + str(
                self) + ")"
        )
        raise

    def process(self, _dt):
        # normal behavior
        self.state_lasts += _dt
        self.data.animation_stage = (
            self.state_lasts % self.duration) / self.duration

        if self.state_lasts < self.beginning_steady_time:
            # ignore everything
            return

        else:
            for event in self.data.env.keyboardEvents.getEvents():
                if event.event_type == eventType.Move:
                    if event.data == (1, 0):
                        self.moveRight()
                    if event.data == (-1, 0):
                        self.moveLeft()
                    if event.data == (0, 1):
                        self.moveDown()
                    if event.data == (0, -1):
                        self.moveUp()

                if event.event_type == eventType.Atack:
                    if event.data == "Normal":
                        self.normalAttack()
                    if event.data == "Massive":
                        self.massiveAttack()

                if event.event_type == eventType.PickUp:
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

                if event.event_type == eventType.PickMe:
                    self.data.inventory.merge(event.data)


class PlayerBehaviorStandingUp(PlayerBehaviorStanding):
    def moveUp(self):
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

    def moveDown(self):
        self.data.state = "StandingDown"
        self.data.animation_stage = 0.0

    def moveLeft(self):
        self.data.state = "StandingLeft"
        self.data.animation_stage = 0.0

    def moveRight(self):
        self.data.state = "StandingRight"
        self.data.animation_stage = 0.0

    def normalAttack(self):
        self.data.state = "AtackingUp"
        self.data.animation_stage = 0.0

    def massiveAttack(self):
        self.data.state = "MassiveAtackingUp"
        self.data.animation_stage = 0.0


class PlayerBehaviorStandingDown(PlayerBehaviorStanding):
    def moveUp(self):
        self.data.state = "StandingUp"
        self.data.animation_stage = 0.0

    def moveDown(self):
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

    def moveLeft(self):
        self.data.state = "StandingLeft"
        self.data.animation_stage = 0.0

    def moveRight(self):
        self.data.state = "StandingRight"
        self.data.animation_stage = 0.0

    def normalAttack(self):
        self.data.state = "AtackingDown"
        self.data.animation_stage = 0.0

    def massiveAttack(self):
        self.data.state = "MassiveAtackingDown"
        self.data.animation_stage = 0.0


class PlayerBehaviorStandingLeft(PlayerBehaviorStanding):
    def moveUp(self):
        self.data.state = "StandingUp"
        self.data.animation_stage = 0.0

    def moveDown(self):
        self.data.state = "StandingDown"
        self.data.animation_stage = 0.0

    def moveLeft(self):
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

    def moveRight(self):
        self.data.state = "StandingRight"
        self.data.animation_stage = 0.0

    def normalAttack(self):
        self.data.state = "AtackingLeft"
        self.data.animation_stage = 0.0

    def massiveAttack(self):
        self.data.state = "MassiveAtackingLeft"
        self.data.animation_stage = 0.0


class PlayerBehaviorStandingRight(PlayerBehaviorStanding):
    def moveUp(self):
        self.data.state = "StandingUp"
        self.data.animation_stage = 0.0

    def moveDown(self):
        self.data.state = "StandingDown"
        self.data.animation_stage = 0.0

    def moveLeft(self):
        self.data.state = "StandingLeft"
        self.data.animation_stage = 0.0

    def moveRight(self):
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

    def normalAttack(self):
        self.data.state = "AtackingRight"
        self.data.animation_stage = 0.0

    def massiveAttack(self):
        self.data.state = "MassiveAtackingRight"
        self.data.animation_stage = 0.0


class PlayerBehaviorWalking(Behavior):
    """ Abstract base class for all walking behaviors """

    def __init__(self, _data):
        self.data = _data
        self.state_lasts = 0.0
        self.duration = 0.5
        self.beginning_steady_time = 0.15

    def getDirection(self):
        """
        Abstract functions for getting current walking's 2D direction

        :returns: one of four directions: (0, 1) | (0, -1) | (1, 0) | (-1, 0)
        """

        logging.critical(
            "PlayerBehaviorWalking: getDirection is not implemented: PlayerBehaviorWalking(" + str(
                self) + ")"
        )
        raise

    def getNextPosition(self):
        """
        Calculates player's destination cell

        :returns: next cell's coordinates: [x, y]
        """

        d = self.getDirection()
        return [
            self.data.position[0] + d[0] * self.data.env.grid_step,
            self.data.position[1] + d[1] * self.data.env.grid_step
        ]

    def getStopState(self):
        """ 
        Abstract function to get the player's state if he is gonna stop walking

        :returns: standing state: string
        """

        logging.critical(
            "PlayerBehaviorWalking: getStopState is not implemented: PlayerBehaviorWalking(" + str(
                self) + ")"
        )
        raise

    def process(self, _dt):
        for event in self.data.env.pastEvents.getEvents(eventType.MoveProhibited):
            if event.event_type == eventType.MoveProhibited and event.data == self.getNextPosition():
                self.data.state = self.getStopState()
                return

        self.state_lasts += _dt
        self.data.animation_stage = self.state_lasts / self.duration

        continue_key_pressed = False
        for event in self.data.env.keyboardEvents.getEvents():
            if event.event_type == eventType.Move and event.data == self.getDirection():
                continue_key_pressed = True

        if self.state_lasts >= self.duration:
            self.data.position = self.getNextPosition()
            if continue_key_pressed:
                self.state_lasts = 0.0
                self.data.animation_stage = 0.0
                self.data.env.futureEvents.sendEvent(
                    Event(
                        eventType.Move,
                        self,
                        self.getNextPosition()
                    )
                )
            else:
                self.data.state = self.getStopState()
                self.data.animation_stage = 0.0

        if self.state_lasts < self.beginning_steady_time and not continue_key_pressed:
            self.data.state = self.getStopState()
            self.data.animation_stage = 0.0


class PlayerBehaviorWalkingUp(PlayerBehaviorWalking):
    def getDirection(self):
        return (0, -1)

    def getStopState(self):
        return "StandingUp"


class PlayerBehaviorWalkingDown(PlayerBehaviorWalking):
    def getDirection(self):
        return (0, 1)

    def getStopState(self):
        return "StandingDown"


class PlayerBehaviorWalkingLeft(PlayerBehaviorWalking):
    def getDirection(self):
        return (-1, 0)

    def getStopState(self):
        return "StandingLeft"


class PlayerBehaviorWalkingRight(PlayerBehaviorWalking):
    def getDirection(self):
        return (1, 0)

    def getStopState(self):
        return "StandingRight"


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
        behaviors = {
            "StandingUp": PlayerBehaviorStandingUp,
            "StandingDown": PlayerBehaviorStandingDown,
            "StandingLeft": PlayerBehaviorStandingLeft,
            "StandingRight": PlayerBehaviorStandingRight,
            "WalkingUp": PlayerBehaviorWalkingUp,
            "WalkingDown": PlayerBehaviorWalkingDown,
            "WalkingLeft": PlayerBehaviorWalkingLeft,
            "WalkingRight": PlayerBehaviorWalkingRight,
            "AtackingUp": PlayerBehaviourAtackingUp,
            "AtackingDown": PlayerBehaviourAtackingDown,
            "AtackingLeft": PlayerBehaviourAtackingLeft,
            "AtackingRight": PlayerBehaviourAtackingRight,
            "MassiveAtackingUp": PlayerBehaviourMassiveAtackingUp,
            "MassiveAtackingDown": PlayerBehaviourMassiveAtackingDown,
            "MassiveAtackingLeft": PlayerBehaviourMassiveAtackingLeft,
            "MassiveAtackingRight": PlayerBehaviourMassiveAtackingRight
        }

        EntityLogic.__init__(self, _data, behaviors)

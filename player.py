# import pygame
import time

from entityLogic import EntityLogic, Behaviour
from entityGraphics import EntityGraphics, UpgradedSprite
from entityData import EntityData, Inventory
from entity import Entity
from eventSystem import eventType  # Event

#    __                 _
#   / /   ___   ___ _  (_) ____
#  / /__ / _ \ / _ `/ / / / __/
# /____/ \___/ \_, / /_/  \__/
#             /___/


class PlayerStanding(Behaviour):
    # Actually overrides base class method
    def process(self, time: int):
        pass


class PlayerEntityLogic(EntityLogic):
    def __init__(self, _env, _data):
        self.nextTimeActive = 0.0
        behaviours = {
            "Standing": PlayerStanding
        }

        EntityLogic.__init__(
            self,
            _env,
            _data,
            behaviours
        )

    def handleEvents(self):
        if self.nextTimeActive > time.time():
            return

        # Actions in the end of event
        if self.data.state == "WalkingRight":
            self.data.position[0] += self.env.grid_step
            self.data.state = "StandingRight"
            return
        if self.data.state == "WalkingLeft":
            self.data.position[0] -= self.env.grid_step
            self.data.state = "StandingLeft"
            return
        if self.data.state == "WalkingDown":
            self.data.position[1] += self.env.grid_step
            self.data.state = "StandingDown"
            return
        if self.data.state == "WalkingUp":
            self.data.position[1] -= self.env.grid_step
            self.data.state = "StandingUp"
            return
        if self.data.state == "AtackingUp":
            self.data.state = "StandingUp"
            return
        if self.data.state == "AtackingDown":
            self.data.state = "StandingDown"
            return
        if self.data.state == "AtackingLeft":
            self.data.state = "StandingLeft"
            return
        if self.data.state == "AtackingRight":
            self.data.state = "StandingRight"
            return

        # Choosing next event
        for event in self.env.keyboardEvents.getEvents():
            if event.event_type == eventType.Move:
                if event.data == (1, 0):
                    if self.data.state == "StandingRight":
                        self.data.state = "WalkingRight"
                        self.nextTimeActive = time.time() + 0.5
                    else:
                        self.data.state = "StandingRight"
                        self.nextTimeActive = time.time() + 0.15
                if event.data == (-1, 0):
                    if self.data.state == "StandingLeft":
                        self.data.state = "WalkingLeft"
                        self.nextTimeActive = time.time() + 0.5
                    else:
                        self.data.state = "StandingLeft"
                        self.nextTimeActive = time.time() + 0.15
                if event.data == (0, 1):
                    if self.data.state == "StandingDown":
                        self.data.state = "WalkingDown"
                        self.nextTimeActive = time.time() + 0.5
                    else:
                        self.data.state = "StandingDown"
                        self.nextTimeActive = time.time() + 0.15
                if event.data == (0, -1):
                    if self.data.state == "StandingUp":
                        self.data.state = "WalkingUp"
                        self.nextTimeActive = time.time() + 0.5
                    else:
                        self.data.state = "StandingUp"
                        self.nextTimeActive = time.time() + 0.15
            if event.event_type == eventType.Atack:
                if self.data.state == "StandingUp":
                    self.data.state = "AtackingUp"
                    self.nextTimeActive = time.time() + 0.5
                if self.data.state == "StandingDown":
                    self.data.state = "AtackingDown"
                    self.nextTimeActive = time.time() + 0.5
                if self.data.state == "StandingLeft":
                    self.data.state = "AtackingLeft"
                    self.nextTimeActive = time.time() + 0.5
                if self.data.state == "StandingRight":
                    self.data.state = "AtackingRight"
                    self.nextTimeActive = time.time() + 0.5


#   _____                    __    _
#  / ___/ ____ ___ _  ___   / /   (_) ____  ___
# / (_ / / __// _ `/ / _ \ / _ \ / / / __/ (_-<
# \___/ /_/   \_,_/ / .__//_//_//_/  \__/ /___/
#                  /_/


class PlayerSpriteStandingUp(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'Sprites/Player/Up/WarriorUpIdle.png',
            2)

    def getPosition(self, _time: int):
        return [0, 25]


class PlayerSpriteStandingDown(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'Sprites/Player/Down/WarriorDownIdle.png',
            2)

    def getPosition(self, _time: int):
        return [0, 25]


class PlayerSpriteStandingLeft(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'Sprites/Player/Left/WarriorLeftIdle.png',
            2)

    def getPosition(self, _time: int):
        return [0, 25]


class PlayerSpriteStandingRight(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'Sprites/Player/Right/WarriorRightIdle.png',
            2)

    def getPosition(self, _time: int):
        return [0, 25]


class PlayerSpriteWalkingUp(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'Sprites/Player/Up/WarriorUpWalk.png',
            2,
            0.5)

    def getPosition(self, _time: int):
        return [0, 25 - _time * 100]


class PlayerSpriteWalkingDown(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'Sprites/Player/Down/WarriorDownWalk.png',
            2,
            0.5)

    def getPosition(self, _time: int):
        return [0, 25 + _time * 100]


class PlayerSpriteWalkingLeft(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'Sprites/Player/Left/WarriorLeftWalk.png',
            2,
            0.5)

    def getPosition(self, _time: int):
        return [- _time * 100, 25]


class PlayerSpriteWalkingRight(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'Sprites/Player/Right/WarriorRightWalk.png',
            2,
            0.5)

    def getPosition(self, _time: int):
        return [_time * 100, 25]


class PlayerSpriteAtackingUp(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'Sprites/Player/Up/WarriorUpAttack01.png',
            2,
            0.5)

    def getPosition(self, _time: int):
        return [0, 25]


class PlayerSpriteAtackingDown(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'Sprites/Player/Down/WarriorDownAttack01.png',
            2,
            0.5)

    def getPosition(self, _time: int):
        return [0, 25]


class PlayerSpriteAtackingLeft(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'Sprites/Player/Left/WarriorLeftAttack01.png',
            2,
            0.5)

    def getPosition(self, _time: int):
        return [0, 25]


class PlayerSpriteAtackingRight(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'Sprites/Player/Right/WarriorRightAttack01.png',
            2,
            0.5)

    def getPosition(self, _time: int):
        return [0, 25]


class PlayerEntityGraphics(EntityGraphics):
    def __init__(self, _data):
        sprites = {
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
            "AtackingRight": PlayerSpriteAtackingRight
        }

        EntityGraphics.__init__(self, _data, sprites)

#    ___    __
#   / _ \  / / ___ _  __ __ ___   ____
#  / ___/ / / / _ `/ / // // -_) / __/
# /_/    /_/  \_,_/  \_, / \__/ /_/
#                   /___/


class Player(Entity):
    def __init__(self, _env):
        entity_data = EntityData("WalkingDown", [0, 0], Inventory([]))

        Entity.__init__(
            self,
            _env,
            [0, 0],
            entity_data,
            PlayerEntityLogic(_env, entity_data),
            PlayerEntityGraphics(entity_data)
        )

        self.env = _env

# import pygame
import time

from entityLogic import EntityLogic, Behaviour
from entityData import EntityData, Inventory
from entity import Entity
from eventSystem import eventType  # Event

from playerGraphics import PlayerEntityGraphics

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
        if self.data.nextTimeAcceptingEvents > time.time():
            return

        # Choosing next enevt based on previous
        if self.data.state == "WalkingRight":
            self.data.state = "StandingRight"
        if self.data.state == "WalkingLeft":
            self.data.state = "StandingLeft"
        if self.data.state == "WalkingDown":
            self.data.state = "StandingDown"
        if self.data.state == "WalkingUp":
            self.data.state = "StandingUp"

        if self.data.state == "AtackingUp":
            self.data.state = "StandingUp"
        if self.data.state == "AtackingDown":
            self.data.state = "StandingDown"
        if self.data.state == "AtackingLeft":
            self.data.state = "StandingLeft"
        if self.data.state == "AtackingRight":
            self.data.state = "StandingRight"

        if self.data.state == "MassiveAtackingUp":
            self.data.state = "StandingUp"
        if self.data.state == "MassiveAtackingDown":
            self.data.state = "StandingDown"
        if self.data.state == "MassiveAtackingLeft":
            self.data.state = "StandingLeft"
        if self.data.state == "MassiveAtackingRight":
            self.data.state = "StandingRight"

        # Choosing next event
        for event in self.env.keyboardEvents.getEvents():
            if event.event_type == eventType.Move:
                if event.data == (1, 0):
                    if self.data.state == "StandingRight":
                        self.data.state = "WalkingRight"
                    else:
                        self.data.state = "StandingRight"
                if event.data == (-1, 0):
                    if self.data.state == "StandingLeft":
                        self.data.state = "WalkingLeft"
                    else:
                        self.data.state = "StandingLeft"
                if event.data == (0, 1):
                    if self.data.state == "StandingDown":
                        self.data.state = "WalkingDown"
                    else:
                        self.data.state = "StandingDown"
                if event.data == (0, -1):
                    if self.data.state == "StandingUp":
                        self.data.state = "WalkingUp"
                    else:
                        self.data.state = "StandingUp"

            if event.event_type == eventType.Atack and event.data == "Normal":
                if self.data.state == "StandingUp":
                    self.data.state = "AtackingUp"
                if self.data.state == "StandingDown":
                    self.data.state = "AtackingDown"
                if self.data.state == "StandingLeft":
                    self.data.state = "AtackingLeft"
                if self.data.state == "StandingRight":
                    self.data.state = "AtackingRight"

            if event.event_type == eventType.Atack and event.data == "Massive":
                if self.data.state == "StandingUp":
                    self.data.state = "MassiveAtackingUp"
                if self.data.state == "StandingDown":
                    self.data.state = "MassiveAtackingDown"
                if self.data.state == "StandingLeft":
                    self.data.state = "MassiveAtackingLeft"
                if self.data.state == "StandingRight":
                    self.data.state = "MassiveAtackingRight"


#   _____                    __    _
#  / ___/ ____ ___ _  ___   / /   (_) ____  ___
# / (_ / / __// _ `/ / _ \ / _ \ / / / __/ (_-<
# \___/ /_/   \_,_/ / .__//_//_//_/  \__/ /___/
#                  /_/



#    ___    __
#   / _ \  / / ___ _  __ __ ___   ____
#  / ___/ / / / _ `/ / // // -_) / __/
# /_/    /_/  \_,_/  \_, / \__/ /_/
#                   /___/


class Player(Entity):
    def __init__(self, _env):
        entity_data = EntityData("WalkingDown", [0, 0], 0.0, Inventory([]))

        Entity.__init__(
            self,
            _env,
            [0, 0],
            entity_data,
            PlayerEntityLogic(_env, entity_data),
            PlayerEntityGraphics(entity_data)
        )

        self.env = _env

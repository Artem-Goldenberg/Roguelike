from Engine.entityData import EntityData, Inventory
from Engine.entity import Entity

from Player.playerLogic import PlayerEntityLogic
from Player.playerGraphics import PlayerEntityGraphics


class Player(Entity):
    def __init__(self, _env):
        entity_data = EntityData(_env, "StandingDown", [0, 0], 0.0, Inventory([]), (0, 1))

        Entity.__init__(
            self,
            entity_data,
            PlayerEntityLogic(entity_data),
            PlayerEntityGraphics(entity_data)
        )

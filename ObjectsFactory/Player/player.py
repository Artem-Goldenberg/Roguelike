from Engine.entityData import Inventory
from Engine.entity import Entity

from .playerLogic import PlayerEntityLogic
from .playerGraphics import PlayerEntityGraphics
from .playerData import PlayerData


class Player(Entity):
    def __init__(self, _env):
        entity_data = PlayerData(
            _env,
            100,
            "StandingDown",
            [0, 0],
            0.0,
            Inventory(_capacity=9),
            (0, 1))

        Entity.__init__(
            self,
            entity_data,
            PlayerEntityLogic(entity_data),
            PlayerEntityGraphics(entity_data)
        )

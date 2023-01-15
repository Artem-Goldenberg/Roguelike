from Engine.entityData import Inventory
from Engine.activeEntity import ActiveEntity
from Engine.defaultActiveEntityLogic import DefaultEntityLogic

from .playerData import PlayerData
from .playerGraphics import PlayerEntityGraphics
from .playerMetaLogic import PlayerMetaLogic


class Player(ActiveEntity):
    def __init__(self, _env):
        entity_data = PlayerData(
            _env=_env,
            _hp=100,
            _state="StandingDown",
            _meta_instructions=[],
            _meta_state="Keyboard",
            _position=[0, 0],
            _animation_stage=0.0,
            _inventory=Inventory(_capacity=9),
            _custom=(0, 1))

        ActiveEntity.__init__(
            self,
            entity_data,
            PlayerMetaLogic(entity_data),
            DefaultEntityLogic(entity_data),
            PlayerEntityGraphics(entity_data)
        )

from Engine.entity import Entity
from Engine.entityData import EntityData
from ObjectsFactory.Rock.rockLogic import RockLogic
from ObjectsFactory.Rock.rockGraphics import RockGraphics


class Rock(Entity):
    def __init__(self, _env, _pos):
        entity_data = EntityData(_env, _state="Stand", _position=_pos)

        Entity.__init__(
            self,
            entity_data,
            RockLogic(entity_data),
            RockGraphics(entity_data)
        )

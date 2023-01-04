from Engine.entity import Entity
from Engine.entityData import EntityData
from ObjectsFactory.Fire.fireLogic import FireLogic
from ObjectsFactory.Fire.fireGraphics import FireGraphics


class Fire(Entity):
    def __init__(self, _env, _pos):
        entity_data = EntityData(_env, _state="Burn", _position=_pos)

        Entity.__init__(
            self,
            entity_data,
            FireLogic(entity_data),
            FireGraphics(entity_data)
        )

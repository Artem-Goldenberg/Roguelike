from Engine.entity import Entity
from Engine.entityData import EntityData
from ObjectsFactory.Shiny.shinyLogic import ShinyLogic
from ObjectsFactory.Shiny.shinyGraphics import ShinyGraphics


class Shiny(Entity):
    def __init__(self, _env, _pos):
        entity_data = EntityData(_env, _state="Stand", _position=_pos)
        entity_data.inventory.addItem(_env.item_factory.getItem("SampleItem"))

        Entity.__init__(
            self,
            entity_data,
            ShinyLogic(entity_data),
            ShinyGraphics(entity_data)
        )

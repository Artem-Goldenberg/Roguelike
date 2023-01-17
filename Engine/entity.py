import typing as tp

from Engine.entityLogic import EntityLogic
from Engine.entityGraphics import EntityGraphics
from Engine.entityData import EntityData

Point = tp.List[int]


class Entity:
    """ Main class for all objects in the game """

    def __init__(
            self,
            _entity_data: EntityData,
            _entity_logic: EntityLogic,
            _entity_graphics: EntityGraphics
    ):
        self.data = _entity_data
        self.logic = _entity_logic
        self.graphics = _entity_graphics

    def draw(self, _dt, _screen, _camera_position):
        self.graphics.draw(_dt, _screen, _camera_position)

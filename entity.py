import typing as tp
Point = tp.List[int]

from logic import EntityLogic
from graphics import EntityView
from data import EntityState, EntityData, Inventory


class Entity:
    """ Main class for all objects in the game """

    def __init__(self, position: Point, logic: EntityLogic, view: EntityView):
        inventory = Inventory([])
        self.data = EntityData(EntityState.idle, position, inventory)
        self.logic = logic
        self.view = view
    
    def draw(self, origin: Point):
        self.view.draw(origin)



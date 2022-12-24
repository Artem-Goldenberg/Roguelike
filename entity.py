from logic import EntityLogic
from graphics import EntityView
from data import EntityState, EntityData, Inventory


class Entity:
    """ Main class for all objects in the game """

    def __init__(self, logic: EntityLogic, view: EntityView):
        inventory = Inventory([])
        self.data = EntityData(EntityState.idle, [1, 2], inventory)
        self.logic = logic
        self.view = view

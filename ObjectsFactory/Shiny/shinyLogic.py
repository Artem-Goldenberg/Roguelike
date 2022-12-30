from Engine.entityLogic import EntityLogic, Behavior


class ShinyLogicStand(Behavior):
    def process(self, _dt):
        pass

class ShinyLogicPickUp(Behavior):
    def process(self, _dt):
        pass


class ShinyLogic(EntityLogic):
    def __init__(self, _data):
        behaviors = {
            "Stand": ShinyLogicStand,
            "PickUp": ShinyLogicPickUp
        }

        EntityLogic.__init__(self, _data, behaviors)
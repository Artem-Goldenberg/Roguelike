from Engine.entityLogic import EntityLogic, Behaviour


class RockLogicStand(Behaviour):
    def process(self, _dt):
        pass


class RockLogic(EntityLogic):
    def __init__(self, _data):
        behaviours = {
            "Stand": RockLogicStand
        }

        EntityLogic.__init__(self, _data, behaviours)

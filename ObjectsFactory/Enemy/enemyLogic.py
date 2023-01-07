from Engine.entityLogic import EntityLogic, Behaviour
from Engine.eventSystem import Event, eventType


class EnemyLogicNeutral(Behaviour):
    def __init__(self, _data):
        pass
    
    def process(self, _dt):
        pass


class EnemyLogicPanic(Behaviour):
    def __init__(self, _data):
        pass
    
    def process(self, _dt):
        pass


class EnemyLogicAttacking(Behaviour):
    def __init__(self, _data):
        pass

    def process(self, _dt):
        pass


class EnemyLogic(EntityLogic):
    def __init__(self, _data):
        behaviours = {
            "Stand": EnemyLogicNeutral,
        }

        EntityLogic.__init__(self, _data, behaviours)

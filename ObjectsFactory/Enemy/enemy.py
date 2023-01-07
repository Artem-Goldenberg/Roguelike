from Engine.entity import Entity
from Engine.entityData import EntityData
from ObjectsFactory.Enemy.enemyLogic import EnemyLogic
from ObjectsFactory.Enemy.enemyGraphics import EnemyGraphics

class Enemy(Entity):
    def __init__(self, _env, _pos):
        entity_data = EntityData(_env)

        Entity.__init__(
            self,
            entity_data,
            EntityLogic(entity_data),
            EntityGraphics(entity_data)
        )
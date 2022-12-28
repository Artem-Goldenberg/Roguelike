from Engine.entityData import EntityData, Inventory
from Engine.entity import Entity

from Player.playerLogic import PlayerEntityLogic
from Player.playerGraphics import PlayerEntityGraphics

#    __                 _
#   / /   ___   ___ _  (_) ____
#  / /__ / _ \ / _ `/ / / / __/
# /____/ \___/ \_, / /_/  \__/
#             /___/

#    ___    __
#   / _ \  / / ___ _  __ __ ___   ____
#  / ___/ / / / _ `/ / // // -_) / __/
# /_/    /_/  \_,_/  \_, / \__/ /_/
#                   /___/


class Player(Entity):
    def __init__(self, _env):
        entity_data = EntityData("WalkingDown", [0, 0], 0.0, Inventory([]))

        Entity.__init__(
            self,
            _env,
            [0, 0],
            entity_data,
            PlayerEntityLogic(_env, entity_data),
            PlayerEntityGraphics(entity_data)
        )

        self.env = _env

import pygame

from entityLogic import EntityLogic, Behaviour
from entityGraphics import EntityGraphics, Sprite
from entityData import EntityData, Inventory
from entity import Entity
from eventSystem import Event, eventType

#    __                 _
#   / /   ___   ___ _  (_) ____
#  / /__ / _ \ / _ `/ / / / __/
# /____/ \___/ \_, / /_/  \__/
#             /___/


class PlayerStanding(Behaviour):
    # Actually overrides base class method
    def process(self, time: int):
        pass


class PlayerEntityLogic(EntityLogic):
    def __init__(self, _env, _data):
        behaviours = {
            "Standing": PlayerStanding
        }

        EntityLogic.__init__(
            self,
            _env,
            _data,
            behaviours
        )

    def handleEvents(self):
        for event in self.env.keyboardEvents.getEvents():
            if event.event_type == eventType.Move:
                self.data.position[0] += event.data[0]*self.env.grid_step
                self.data.position[1] += event.data[1]*self.env.grid_step


#   _____                    __    _
#  / ___/ ____ ___ _  ___   / /   (_) ____  ___
# / (_ / / __// _ `/ / _ \ / _ \ / / / __/ (_-<
# \___/ /_/   \_,_/ / .__//_//_//_/  \__/ /___/
#                  /_/


class PlayerSpriteStanding(Sprite):
    # Actually overrides base class method
    def getImage(self, _time):
        texture = pygame.Surface((20, 20))
        texture.fill((250, 100, 100))
        return texture

    # Actually overrides base class method
    def getPosition(self, _time: int):
        return [-10, -10]


class PlayerEntityGraphics(EntityGraphics):
    def __init__(self, _data):
        sprites = {
            "Standing": PlayerSpriteStanding
        }

        EntityGraphics.__init__(self, _data, sprites)

#    ___    __
#   / _ \  / / ___ _  __ __ ___   ____
#  / ___/ / / / _ `/ / // // -_) / __/
# /_/    /_/  \_,_/  \_, / \__/ /_/
#                   /___/


class Player(Entity):
    def __init__(self, _env):
        entity_data = EntityData("Standing", [0, 0], Inventory([]))

        Entity.__init__(
            self,
            _env,
            [0, 0],
            entity_data,
            PlayerEntityLogic(_env, entity_data),
            PlayerEntityGraphics(entity_data)
        )

        self.env = _env


class oldPlayer:
    def __init__(self, env):
        self.env = env
        self.pos = [0, 0]
        self.temp_texture = pygame.Surface((20, 20))
        self.temp_texture.fill((250, 100, 100))

    def update(self, dt):
        pass

    def draw(self, screen, camera_position):
        screen.blit(self.temp_texture, [
                        -10 + self.pos[0] - camera_position[0],
                        -10 + self.pos[1] - camera_position[1]])

import pygame
from Engine.entityGraphics import EntityGraphics, UpgradedSprite



class ShinySpriteStand(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'ObjectsFactory/Shiny/Sprites/shiny.png',
            0.05)

    def getRelativePosition(self, _animation_stage):
        return [0, 0]



class ShinyGraphics(EntityGraphics):
    def __init__(self, _data):
        sprites = {
            "Stand": ShinySpriteStand
        }

        EntityGraphics.__init__(self, _data, sprites)

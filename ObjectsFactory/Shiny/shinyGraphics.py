from Engine.entityGraphics import EntityGraphics, UpgradedSprite
from math import sin, pi


def singleton(class_):
    instances = {}

    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getinstance


@singleton
class ShinySpriteStand(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'ObjectsFactory/Shiny/Sprites/shiny_new.png',
            0.05)

    def getRelativePosition(self, _animation_stage):
        return [-20, -30 + 8*sin(_animation_stage*2*pi)]


class ShinyGraphics(EntityGraphics):
    def __init__(self, _data):
        sprites = {
            "Stand": ShinySpriteStand()
        }

        EntityGraphics.__init__(self, _data, sprites)

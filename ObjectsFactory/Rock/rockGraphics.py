from Engine.entityGraphics import EntityGraphics, UpgradedSprite


def singleton(class_):
    instances = {}

    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getinstance


@singleton
class RockSpriteStand(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'ObjectsFactory/Rock/Sprites/rock_new.png',
            0.28)

    def getRelativePosition(self, _animation_stage):
        return [-40, -40]


class RockGraphics(EntityGraphics):
    def __init__(self, _data):
        sprites = {
            "Stand": RockSpriteStand()
        }

        EntityGraphics.__init__(self, _data, sprites)

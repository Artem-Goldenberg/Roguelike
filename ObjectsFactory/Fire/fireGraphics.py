from Engine.entityGraphics import EntityGraphics, UpgradedSprite


def singleton(class_):
    instances = {}

    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getinstance


@singleton
class FireSpriteBurn(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'ObjectsFactory/Fire/Sprites/fire_new.png',
            # 'ObjectsFactory/Rock/Sprites/rock_new.png',
            0.4)

    def getRelativePosition(self, _animation_stage):
        return [-53 - 4 * _animation_stage, -55]


class FireGraphics(EntityGraphics):
    def __init__(self, _data):
        sprites = {
            "Burn": FireSpriteBurn()
        }

        EntityGraphics.__init__(self, _data, sprites)

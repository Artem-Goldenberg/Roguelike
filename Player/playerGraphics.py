from Engine.entityGraphics import EntityGraphics, UpgradedSprite

standing_duration = 1.0
standing_stadiness = 0.15
walking_duration = 0.4
walking_stadiness = 0.4
atacking_duration = 0.3
atacking_stadiness = 0.3
massive_atacking_duration = 0.6
massive_atacking_stadiness = 0.6


def singleton(class_):
    instances = {}
    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getinstance


@singleton
class PlayerSpriteStandingUp(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'Player/Sprites/Up/WarriorUpIdle.png',
            3)

    def getRelativePosition(self, _animation_stage):
        return [-75, -100]


@singleton
class PlayerSpriteStandingDown(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'Player/Sprites/Down/WarriorDownIdle.png',
            3)

    def getRelativePosition(self, _animation_stage):
        return [-75, -100]


@singleton
class PlayerSpriteStandingLeft(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'Player/Sprites/Left/WarriorLeftIdle.png',
            3)

    def getRelativePosition(self, _animation_stage):
        return [-75, -100]


@singleton
class PlayerSpriteStandingRight(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'Player/Sprites/Right/WarriorRightIdle.png',
            3)

    def getRelativePosition(self, _animation_stage):
        return [-75, -100]


@singleton
class PlayerSpriteWalkingUp(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'Player/Sprites/Up/WarriorUpWalk.png',
            3)

    def getRelativePosition(self, _animation_stage):
        return [-75, -100 - 75 * _animation_stage]


@singleton
class PlayerSpriteWalkingDown(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'Player/Sprites/Down/WarriorDownWalk.png',
            3)

    def getRelativePosition(self, _animation_stage):
        return [-75, -100 + 75 * _animation_stage]


@singleton
class PlayerSpriteWalkingLeft(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'Player/Sprites/Left/WarriorLeftWalk.png',
            3)

    def getRelativePosition(self, _animation_stage):
        return [-75 - 75 * _animation_stage, -100]


@singleton
class PlayerSpriteWalkingRight(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'Player/Sprites/Right/WarriorRightWalk.png',
            3)

    def getRelativePosition(self, _animation_stage):
        return [-75 + 75 * _animation_stage, -100]


@singleton
class PlayerSpriteAtackingUp(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'Player/Sprites/Up/WarriorUpAttack01.png',
            3)

    def getRelativePosition(self, _animation_stage):
        return [-75, -100]


@singleton
class PlayerSpriteAtackingDown(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'Player/Sprites/Down/WarriorDownAttack01.png',
            3)

    def getRelativePosition(self, _animation_stage):
        return [-75, -100]


@singleton
class PlayerSpriteAtackingLeft(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'Player/Sprites/Left/WarriorLeftAttack01.png',
            3)

    def getRelativePosition(self, _animation_stage):
        return [-75, -100]


@singleton
class PlayerSpriteAtackingRight(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'Player/Sprites/Right/WarriorRightAttack01.png',
            3)

    def getRelativePosition(self, _animation_stage):
        return [-75, -100]


@singleton
class PlayerSpriteMassiveAtackingUp(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'Player/Sprites/Up/WarriorUpAttack02.png',
            3)

    def getRelativePosition(self, _animation_stage):
        return [-75, -100]


@singleton
class PlayerSpriteMassiveAtackingDown(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'Player/Sprites/Down/WarriorDownAttack02.png',
            3)

    def getRelativePosition(self, _animation_stage):
        return [-75, -100]


@singleton
class PlayerSpriteMassiveAtackingLeft(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'Player/Sprites/Left/WarriorLeftAttack02.png',
            3)

    def getRelativePosition(self, _animation_stage):
        return [-75, -100]


@singleton
class PlayerSpriteMassiveAtackingRight(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'Player/Sprites/Right/WarriorRightAttack02.png',
            3)

    def getRelativePosition(self, _animation_stage):
        return [-75, -100]


@singleton
class PlayerSpriteHurtUp(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'Player/Sprites/Up/WarriorUpHurt.png',
            3)

    def getRelativePosition(self, _animation_stage):
        return [-75, -100]


@singleton
class PlayerSpriteHurtDown(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'Player/Sprites/Down/WarriorDownHurt.png',
            3)

    def getRelativePosition(self, _animation_stage):
        return [-75, -100]


@singleton
class PlayerSpriteHurtLeft(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'Player/Sprites/Left/WarriorLeftHurt.png',
            3)

    def getRelativePosition(self, _animation_stage):
        return [-75, -100]


@singleton
class PlayerSpriteHurtRight(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'Player/Sprites/Right/WarriorRightHurt.png',
            3)

    def getRelativePosition(self, _animation_stage):
        return [-75, -100]


@singleton
class PlayerSpritePickingUpUp(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'Player/Sprites/Up/WarriorUpLand.png',
            3)

    def getRelativePosition(self, _animation_stage):
        return [-75, -100]


@singleton
class PlayerSpritePickingUpDown(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'Player/Sprites/Down/WarriorDownLand.png',
            3)

    def getRelativePosition(self, _animation_stage):
        return [-75, -100]


@singleton
class PlayerSpritePickingUpLeft(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'Player/Sprites/Left/WarriorLeftLand.png',
            3)

    def getRelativePosition(self, _animation_stage):
        return [-75, -100]


@singleton
class PlayerSpritePickingUpRight(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'Player/Sprites/Right/WarriorRightLand.png',
            3)

    def getRelativePosition(self, _animation_stage):
        return [-75, -100]


class PlayerEntityGraphics(EntityGraphics):
    def __init__(self, _data):
        sprites = {
            "StandingUp": PlayerSpriteStandingUp(),
            "StandingDown": PlayerSpriteStandingDown(),
            "StandingLeft": PlayerSpriteStandingLeft(),
            "StandingRight": PlayerSpriteStandingRight(),
            "WalkingUp": PlayerSpriteWalkingUp(),
            "WalkingDown": PlayerSpriteWalkingDown(),
            "WalkingLeft": PlayerSpriteWalkingLeft(),
            "WalkingRight": PlayerSpriteWalkingRight(),
            "AtackingUp": PlayerSpriteAtackingUp(),
            "AtackingDown": PlayerSpriteAtackingDown(),
            "AtackingLeft": PlayerSpriteAtackingLeft(),
            "AtackingRight": PlayerSpriteAtackingRight(),
            "MassiveAtackingUp": PlayerSpriteMassiveAtackingUp(),
            "MassiveAtackingDown": PlayerSpriteMassiveAtackingDown(),
            "MassiveAtackingLeft": PlayerSpriteMassiveAtackingLeft(),
            "MassiveAtackingRight": PlayerSpriteMassiveAtackingRight(),
            "HurtUp": PlayerSpriteHurtUp(),
            "HurtDown": PlayerSpriteHurtDown(),
            "HurtLeft": PlayerSpriteHurtLeft(),
            "HurtRight": PlayerSpriteHurtRight(),
            "PickingUpUp": PlayerSpritePickingUpUp(),
            "PickingUpDown": PlayerSpritePickingUpDown(),
            "PickingUpLeft": PlayerSpritePickingUpLeft(),
            "PickingUpRight": PlayerSpritePickingUpRight()
        }

        EntityGraphics.__init__(self, _data, sprites)

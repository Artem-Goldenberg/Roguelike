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
class SkeletonSpriteStandingUp(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'ObjectsFactory/Skeleton/Sprites/Up/SkeletonWithSwordUpIdle.png',
            2.5)

    def getRelativePosition(self, _animation_stage):
        return [-63, -90]


@singleton
class SkeletonSpriteStandingDown(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'ObjectsFactory/Skeleton/Sprites/Down/SkeletonWithSwordDownIdle.png',
            2.5)

    def getRelativePosition(self, _animation_stage):
        return [-63, -90]


@singleton
class SkeletonSpriteStandingLeft(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'ObjectsFactory/Skeleton/Sprites/Left/SkeletonWithSwordLeftIdle.png',
            2.5)

    def getRelativePosition(self, _animation_stage):
        return [-63, -90]


@singleton
class SkeletonSpriteStandingRight(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'ObjectsFactory/Skeleton/Sprites/Right/SkeletonWithSwordRightIdle.png',
            2.5)

    def getRelativePosition(self, _animation_stage):
        return [-63, -90]


@singleton
class SkeletonSpriteWalkingUp(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'ObjectsFactory/Skeleton/Sprites/Up/SkeletonWithSwordUpRun.png',
            2.5)

    def getRelativePosition(self, _animation_stage):
        return [-63, -90 - 75 * _animation_stage]


@singleton
class SkeletonSpriteWalkingDown(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'ObjectsFactory/Skeleton/Sprites/Down/SkeletonWithSwordDownRun.png',
            2.5)

    def getRelativePosition(self, _animation_stage):
        return [-63, -90 + 75 * _animation_stage]


@singleton
class SkeletonSpriteWalkingLeft(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'ObjectsFactory/Skeleton/Sprites/Left/SkeletonWithSwordLeftRun.png',
            2.5)

    def getRelativePosition(self, _animation_stage):
        return [-63 - 75 * _animation_stage, -90]


@singleton
class SkeletonSpriteWalkingRight(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'ObjectsFactory/Skeleton/Sprites/Right/SkeletonWithSwordRightRun.png',
            2.5)

    def getRelativePosition(self, _animation_stage):
        return [-63 + 75 * _animation_stage, -90]


@singleton
class SkeletonSpriteAtackingUp(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'ObjectsFactory/Skeleton/Sprites/Up/SkeletonWithSwordUpAttack01.png',
            2.5)

    def getRelativePosition(self, _animation_stage):
        return [-63, -90]


@singleton
class SkeletonSpriteAtackingDown(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'ObjectsFactory/Skeleton/Sprites/Down/SkeletonWithSwordDownAttack01.png',
            2.5)

    def getRelativePosition(self, _animation_stage):
        return [-63, -90]


@singleton
class SkeletonSpriteAtackingLeft(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'ObjectsFactory/Skeleton/Sprites/Left/SkeletonWithSwordLeftAttack01.png',
            2.5)

    def getRelativePosition(self, _animation_stage):
        return [-63, -90]


@singleton
class SkeletonSpriteAtackingRight(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'ObjectsFactory/Skeleton/Sprites/Right/SkeletonWithSwordRightAttack01.png',
            2.5)

    def getRelativePosition(self, _animation_stage):
        return [-63, -90]


@singleton
class SkeletonSpriteHurtUp(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'ObjectsFactory/Skeleton/Sprites/Up/SkeletonWithSwordUpHurt.png',
            2.5)

    def getRelativePosition(self, _animation_stage):
        return [-63, -90]


@singleton
class SkeletonSpriteHurtDown(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'ObjectsFactory/Skeleton/Sprites/Down/SkeletonWithSwordDownHurt.png',
            2.5)

    def getRelativePosition(self, _animation_stage):
        return [-63, -90]


@singleton
class SkeletonSpriteHurtLeft(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'ObjectsFactory/Skeleton/Sprites/Left/SkeletonWithSwordLeftHurt.png',
            2.5)

    def getRelativePosition(self, _animation_stage):
        return [-63, -90]


@singleton
class SkeletonSpriteHurtRight(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'ObjectsFactory/Skeleton/Sprites/Right/SkeletonWithSwordRightHurt.png',
            2.5)

    def getRelativePosition(self, _animation_stage):
        return [-63, -90]


@singleton
class SkeletonSpritePickingUpUp(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'ObjectsFactory/Skeleton/Sprites/Up/SkeletonWithSwordUpLand.png',
            2.5)

    def getRelativePosition(self, _animation_stage):
        return [-63, -90]


@singleton
class SkeletonSpritePickingUpDown(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'ObjectsFactory/Skeleton/Sprites/Down/SkeletonWithSwordDownLand.png',
            2.5)

    def getRelativePosition(self, _animation_stage):
        return [-63, -90]


@singleton
class SkeletonSpritePickingUpLeft(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'ObjectsFactory/Skeleton/Sprites/Left/SkeletonWithSwordLeftLand.png',
            2.5)

    def getRelativePosition(self, _animation_stage):
        return [-63, -90]


@singleton
class SkeletonSpritePickingUpRight(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'ObjectsFactory/Skeleton/Sprites/Right/SkeletonWithSwordRightLand.png',
            2.5)

    def getRelativePosition(self, _animation_stage):
        return [-63, -90]


@singleton
class SkeletonSpriteDyingUp(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'ObjectsFactory/Skeleton/Sprites/Up/SkeletonWithSwordUpDeath.png',
            2.5)

    def getRelativePosition(self, _animation_stage):
        return [-63, -90]


@singleton
class SkeletonSpriteDyingDown(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'ObjectsFactory/Skeleton/Sprites/Down/SkeletonWithSwordDownDeath.png',
            2.5)

    def getRelativePosition(self, _animation_stage):
        return [-63, -90]


@singleton
class SkeletonSpriteDyingLeft(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'ObjectsFactory/Skeleton/Sprites/Left/SkeletonWithSwordLeftDeath.png',
            2.5)

    def getRelativePosition(self, _animation_stage):
        return [-63, -90]


@singleton
class SkeletonSpriteDyingRight(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'ObjectsFactory/Skeleton/Sprites/Right/SkeletonWithSwordRightDeath.png',
            2.5)

    def getRelativePosition(self, _animation_stage):
        return [-63, -90]


class SkeletonGraphics(EntityGraphics):
    def __init__(self, _data):
        sprites = {
            "StandingUp": SkeletonSpriteStandingUp(),
            "StandingDown": SkeletonSpriteStandingDown(),
            "StandingLeft": SkeletonSpriteStandingLeft(),
            "StandingRight": SkeletonSpriteStandingRight(),
            "WalkingUp": SkeletonSpriteWalkingUp(),
            "WalkingDown": SkeletonSpriteWalkingDown(),
            "WalkingLeft": SkeletonSpriteWalkingLeft(),
            "WalkingRight": SkeletonSpriteWalkingRight(),
            "AtackingUp": SkeletonSpriteAtackingUp(),
            "AtackingDown": SkeletonSpriteAtackingDown(),
            "AtackingLeft": SkeletonSpriteAtackingLeft(),
            "AtackingRight": SkeletonSpriteAtackingRight(),
            "HurtUp": SkeletonSpriteHurtUp(),
            "HurtDown": SkeletonSpriteHurtDown(),
            "HurtLeft": SkeletonSpriteHurtLeft(),
            "HurtRight": SkeletonSpriteHurtRight(),
            "PickingUpUp": SkeletonSpritePickingUpUp(),
            "PickingUpDown": SkeletonSpritePickingUpDown(),
            "PickingUpLeft": SkeletonSpritePickingUpLeft(),
            "PickingUpRight": SkeletonSpritePickingUpRight(),
            "DyingUp": SkeletonSpriteDyingUp(),
            "DyingDown": SkeletonSpriteDyingDown(),
            "DyingLeft": SkeletonSpriteDyingLeft(),
            "DyingRight": SkeletonSpriteDyingRight()
        }

        EntityGraphics.__init__(self, _data, sprites)

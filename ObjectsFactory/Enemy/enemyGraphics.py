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
class EnemySpriteStandingUp(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'ObjectsFactory/Enemy/Sprites/Up/SkeletonWithSwordUpIdle.png',
            3)

    def getRelativePosition(self, _animation_stage):
        return [-75, -100]


@singleton
class EnemySpriteStandingDown(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'ObjectsFactory/Enemy/Sprites/Down/SkeletonWithSwordDownIdle.png',
            3)

    def getRelativePosition(self, _animation_stage):
        return [-75, -100]


@singleton
class EnemySpriteStandingLeft(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'ObjectsFactory/Enemy/Sprites/Left/SkeletonWithSwordLeftIdle.png',
            3)

    def getRelativePosition(self, _animation_stage):
        return [-75, -100]


@singleton
class EnemySpriteStandingRight(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'ObjectsFactory/Enemy/Sprites/Right/SkeletonWithSwordRightIdle.png',
            3)

    def getRelativePosition(self, _animation_stage):
        return [-75, -100]


@singleton
class EnemySpriteWalkingUp(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'ObjectsFactory/Enemy/Sprites/Up/SkeletonWithSwordUpRun.png',
            3)

    def getRelativePosition(self, _animation_stage):
        return [-75, -100 - 75 * _animation_stage]


@singleton
class EnemySpriteWalkingDown(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'ObjectsFactory/Enemy/Sprites/Down/SkeletonWithSwordDownRun.png',
            3)

    def getRelativePosition(self, _animation_stage):
        return [-75, -100 + 75 * _animation_stage]


@singleton
class EnemySpriteWalkingLeft(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'ObjectsFactory/Enemy/Sprites/Left/SkeletonWithSwordLeftRun.png',
            3)

    def getRelativePosition(self, _animation_stage):
        return [-75 - 75 * _animation_stage, -100]


@singleton
class EnemySpriteWalkingRight(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'ObjectsFactory/Enemy/Sprites/Right/SkeletonWithSwordRightRun.png',
            3)

    def getRelativePosition(self, _animation_stage):
        return [-75 + 75 * _animation_stage, -100]


@singleton
class EnemySpriteAtackingUp(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'ObjectsFactory/Enemy/Sprites/Up/SkeletonWithSwordUpAttack01.png',
            3)

    def getRelativePosition(self, _animation_stage):
        return [-75, -100]


@singleton
class EnemySpriteAtackingDown(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'ObjectsFactory/Enemy/Sprites/Down/SkeletonWithSwordDownAttack01.png',
            3)

    def getRelativePosition(self, _animation_stage):
        return [-75, -100]


@singleton
class EnemySpriteAtackingLeft(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'ObjectsFactory/Enemy/Sprites/Left/SkeletonWithSwordLeftAttack01.png',
            3)

    def getRelativePosition(self, _animation_stage):
        return [-75, -100]


@singleton
class EnemySpriteAtackingRight(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'ObjectsFactory/Enemy/Sprites/Right/SkeletonWithSwordRightAttack01.png',
            3)

    def getRelativePosition(self, _animation_stage):
        return [-75, -100]


@singleton
class EnemySpriteHurtUp(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'ObjectsFactory/Enemy/Sprites/Up/SkeletonWithSwordUpHurt.png',
            3)

    def getRelativePosition(self, _animation_stage):
        return [-75, -100]


@singleton
class EnemySpriteHurtDown(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'ObjectsFactory/Enemy/Sprites/Down/SkeletonWithSwordDownHurt.png',
            3)

    def getRelativePosition(self, _animation_stage):
        return [-75, -100]


@singleton
class EnemySpriteHurtLeft(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'ObjectsFactory/Enemy/Sprites/Left/SkeletonWithSwordLeftHurt.png',
            3)

    def getRelativePosition(self, _animation_stage):
        return [-75, -100]


@singleton
class EnemySpriteHurtRight(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'ObjectsFactory/Enemy/Sprites/Right/SkeletonWithSwordRightHurt.png',
            3)

    def getRelativePosition(self, _animation_stage):
        return [-75, -100]


@singleton
class EnemySpritePickingUpUp(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'ObjectsFactory/Enemy/Sprites/Up/SkeletonWithSwordUpLand.png',
            3)

    def getRelativePosition(self, _animation_stage):
        return [-75, -100]


@singleton
class EnemySpritePickingUpDown(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'ObjectsFactory/Enemy/Sprites/Down/SkeletonWithSwordDownLand.png',
            3)

    def getRelativePosition(self, _animation_stage):
        return [-75, -100]


@singleton
class EnemySpritePickingUpLeft(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'ObjectsFactory/Enemy/Sprites/Left/SkeletonWithSwordLeftLand.png',
            3)

    def getRelativePosition(self, _animation_stage):
        return [-75, -100]


@singleton
class EnemySpritePickingUpRight(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'ObjectsFactory/Enemy/Sprites/Right/SkeletonWithSwordRightLand.png',
            3)

    def getRelativePosition(self, _animation_stage):
        return [-75, -100]


@singleton
class EnemySpriteDyingUp(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'ObjectsFactory/Enemy/Sprites/Up/SkeletonWithSwordUpDeath.png',
            3)

    def getRelativePosition(self, _animation_stage):
        return [-75, -100]


@singleton
class EnemySpriteDyingDown(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'ObjectsFactory/Enemy/Sprites/Down/SkeletonWithSwordDownDeath.png',
            3)

    def getRelativePosition(self, _animation_stage):
        return [-75, -100]


@singleton
class EnemySpriteDyingLeft(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'ObjectsFactory/Enemy/Sprites/Left/SkeletonWithSwordLeftDeath.png',
            3)

    def getRelativePosition(self, _animation_stage):
        return [-75, -100]


@singleton
class EnemySpriteDyingRight(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'ObjectsFactory/Enemy/Sprites/Right/SkeletonWithSwordRightDeath.png',
            3)

    def getRelativePosition(self, _animation_stage):
        return [-75, -100]


class EnemyGraphics(EntityGraphics):
    def __init__(self, _data):
        sprites = {
            "StandingUp": EnemySpriteStandingUp(),
            "StandingDown": EnemySpriteStandingDown(),
            "StandingLeft": EnemySpriteStandingLeft(),
            "StandingRight": EnemySpriteStandingRight(),
            "WalkingUp": EnemySpriteWalkingUp(),
            "WalkingDown": EnemySpriteWalkingDown(),
            "WalkingLeft": EnemySpriteWalkingLeft(),
            "WalkingRight": EnemySpriteWalkingRight(),
            "AtackingUp": EnemySpriteAtackingUp(),
            "AtackingDown": EnemySpriteAtackingDown(),
            "AtackingLeft": EnemySpriteAtackingLeft(),
            "AtackingRight": EnemySpriteAtackingRight(),
            "HurtUp": EnemySpriteHurtUp(),
            "HurtDown": EnemySpriteHurtDown(),
            "HurtLeft": EnemySpriteHurtLeft(),
            "HurtRight": EnemySpriteHurtRight(),
            "PickingUpUp": EnemySpritePickingUpUp(),
            "PickingUpDown": EnemySpritePickingUpDown(),
            "PickingUpLeft": EnemySpritePickingUpLeft(),
            "PickingUpRight": EnemySpritePickingUpRight(),
            "DyingUp": EnemySpriteDyingUp(),
            "DyingDown": EnemySpriteDyingDown(),
            "DyingLeft": EnemySpriteDyingLeft(),
            "DyingRight": EnemySpriteDyingRight()
        }

        EntityGraphics.__init__(self, _data, sprites)

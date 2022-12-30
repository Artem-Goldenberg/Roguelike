from Engine.entityGraphics import EntityGraphics, UpgradedSprite

standing_duration = 1.0
standing_stadiness = 0.15
walking_duration = 0.4
walking_stadiness = 0.4
atacking_duration = 0.3
atacking_stadiness = 0.3
massive_atacking_duration = 0.6
massive_atacking_stadiness = 0.6


class PlayerSpriteStandingUp(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'Player/Sprites/Up/WarriorUpIdle.png',
            3)

    def getRelativePosition(self, _animation_stage):
        return [-75, -100]


class PlayerSpriteStandingDown(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'Player/Sprites/Down/WarriorDownIdle.png',
            3)

    def getRelativePosition(self, _animation_stage):
        return [-75, -100]


class PlayerSpriteStandingLeft(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'Player/Sprites/Left/WarriorLeftIdle.png',
            3)

    def getRelativePosition(self, _animation_stage):
        return [-75, -100]


class PlayerSpriteStandingRight(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'Player/Sprites/Right/WarriorRightIdle.png',
            3)

    def getRelativePosition(self, _animation_stage):
        return [-75, -100]


class PlayerSpriteWalkingUp(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'Player/Sprites/Up/WarriorUpWalk.png',
            3)

    def getRelativePosition(self, _animation_stage):
        return [-75, -100 - 75 * _animation_stage]


class PlayerSpriteWalkingDown(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'Player/Sprites/Down/WarriorDownWalk.png',
            3)

    def getRelativePosition(self, _animation_stage):
        return [-75, -100 + 75 * _animation_stage]


class PlayerSpriteWalkingLeft(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'Player/Sprites/Left/WarriorLeftWalk.png',
            3)

    def getRelativePosition(self, _animation_stage):
        return [-75 - 75 * _animation_stage, -100]


class PlayerSpriteWalkingRight(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'Player/Sprites/Right/WarriorRightWalk.png',
            3)

    def getRelativePosition(self, _animation_stage):
        return [-75 + 75 * _animation_stage, -100]


class PlayerSpriteAtackingUp(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'Player/Sprites/Up/WarriorUpAttack01.png',
            3)

    def getRelativePosition(self, _animation_stage):
        return [-75, -100]


class PlayerSpriteAtackingDown(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'Player/Sprites/Down/WarriorDownAttack01.png',
            3)

    def getRelativePosition(self, _animation_stage):
        return [-75, -100]


class PlayerSpriteAtackingLeft(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'Player/Sprites/Left/WarriorLeftAttack01.png',
            3)

    def getRelativePosition(self, _animation_stage):
        return [-75, -100]


class PlayerSpriteAtackingRight(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'Player/Sprites/Right/WarriorRightAttack01.png',
            3)

    def getRelativePosition(self, _animation_stage):
        return [-75, -100]


class PlayerSpriteMassiveAtackingUp(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'Player/Sprites/Up/WarriorUpAttack02.png',
            3)

    def getRelativePosition(self, _animation_stage):
        return [-75, -100]


class PlayerSpriteMassiveAtackingDown(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'Player/Sprites/Down/WarriorDownAttack02.png',
            3)

    def getRelativePosition(self, _animation_stage):
        return [-75, -100]


class PlayerSpriteMassiveAtackingLeft(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'Player/Sprites/Left/WarriorLeftAttack02.png',
            3)

    def getRelativePosition(self, _animation_stage):
        return [-75, -100]


class PlayerSpriteMassiveAtackingRight(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'Player/Sprites/Right/WarriorRightAttack02.png',
            3)

    def getRelativePosition(self, _animation_stage):
        return [-75, -100]


class PlayerSpriteHurtUp(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'Player/Sprites/Up/WarriorUpHurt.png',
            3)

    def getRelativePosition(self, _animation_stage):
        return [-75, -100]


class PlayerSpriteHurtDown(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'Player/Sprites/Down/WarriorDownHurt.png',
            3)

    def getRelativePosition(self, _animation_stage):
        return [-75, -100]


class PlayerSpriteHurtLeft(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'Player/Sprites/Left/WarriorLeftHurt.png',
            3)

    def getRelativePosition(self, _animation_stage):
        return [-75, -100]


class PlayerSpriteHurtRight(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'Player/Sprites/Right/WarriorRightHurt.png',
            3)

    def getRelativePosition(self, _animation_stage):
        return [-75, -100]


staticsInited = False
staticPlayerSpriteStandingUp = None
staticPlayerSpriteStandingDown = None
staticPlayerSpriteStandingLeft = None
staticPlayerSpriteStandingRight = None
staticPlayerSpriteWalkingUp = None
staticPlayerSpriteWalkingDown = None
staticPlayerSpriteWalkingLeft = None
staticPlayerSpriteWalkingRight = None
staticPlayerSpriteAtackingUp = None
staticPlayerSpriteAtackingDown = None
staticPlayerSpriteAtackingLeft = None
staticPlayerSpriteAtackingRight = None
staticPlayerSpriteMassiveAtackingUp = None
staticPlayerSpriteMassiveAtackingDown = None
staticPlayerSpriteMassiveAtackingLeft = None
staticPlayerSpriteMassiveAtackingRight = None
staticPlayerSpriteHurtUp = None
staticPlayerSpriteHurtDown = None
staticPlayerSpriteHurtLeft = None
staticPlayerSpriteHurtRight = None


def Singlton():
    if not staticsInited:
        staticPlayerSpriteStandingUp = PlayerSpriteStandingUp()
        staticPlayerSpriteStandingDown = PlayerSpriteStandingDown()
        staticPlayerSpriteStandingLeft = PlayerSpriteStandingLeft()
        staticPlayerSpriteStandingRight = PlayerSpriteStandingRight()
        staticPlayerSpriteWalkingUp = PlayerSpriteWalkingUp()
        staticPlayerSpriteWalkingDown = PlayerSpriteWalkingDown()
        staticPlayerSpriteWalkingLeft = PlayerSpriteWalkingLeft()
        staticPlayerSpriteWalkingRight = PlayerSpriteWalkingRight()
        staticPlayerSpriteAtackingUp = PlayerSpriteAtackingUp()
        staticPlayerSpriteAtackingDown = PlayerSpriteAtackingDown()
        staticPlayerSpriteAtackingLeft = PlayerSpriteAtackingLeft()
        staticPlayerSpriteAtackingRight = PlayerSpriteAtackingRight()
        staticPlayerSpriteMassiveAtackingUp = PlayerSpriteMassiveAtackingUp()
        staticPlayerSpriteMassiveAtackingDown = PlayerSpriteMassiveAtackingDown()
        staticPlayerSpriteMassiveAtackingLeft = PlayerSpriteMassiveAtackingLeft()
        staticPlayerSpriteMassiveAtackingRight = PlayerSpriteMassiveAtackingRight()
        staticPlayerSpriteHurtUp = PlayerSpriteHurtUp()
        staticPlayerSpriteHurtDown = PlayerSpriteHurtDown()
        staticPlayerSpriteHurtLeft = PlayerSpriteHurtLeft()
        staticPlayerSpriteHurtRight = PlayerSpriteHurtRight()
        staticsInited = True

    return {
        "StandingUp": staticPlayerSpriteStandingUp,
        "StandingDown": staticPlayerSpriteStandingDown,
        "StandingLeft": staticPlayerSpriteStandingLeft,
        "StandingRight": staticPlayerSpriteStandingRight,
        "WalkingUp": staticPlayerSpriteWalkingUp,
        "WalkingDown": staticPlayerSpriteWalkingDown,
        "WalkingLeft": staticPlayerSpriteWalkingLeft,
        "WalkingRight": staticPlayerSpriteWalkingRight,
        "AtackingUp": staticPlayerSpriteAtackingUp,
        "AtackingDown": staticPlayerSpriteAtackingDown,
        "AtackingLeft": staticPlayerSpriteAtackingLeft,
        "AtackingRight": staticPlayerSpriteAtackingRight,
        "MassiveAtackingUp": staticPlayerSpriteMassiveAtackingUp,
        "MassiveAtackingDown": staticPlayerSpriteMassiveAtackingDown,
        "MassiveAtackingLeft": staticPlayerSpriteMassiveAtackingLeft,
        "MassiveAtackingRight": staticPlayerSpriteMassiveAtackingRight,
        "HurtUp": staticPlayerSpriteHurtUp,
        "HurtDown": staticPlayerSpriteHurtDown,
        "HurtLeft": staticPlayerSpriteHurtLeft,
        "HurtRight": staticPlayerSpriteHurtRight
    }


class PlayerEntityGraphics(EntityGraphics):
    def __init__(self, _data):
        sprites = Singlton()

        EntityGraphics.__init__(self, _data, sprites)

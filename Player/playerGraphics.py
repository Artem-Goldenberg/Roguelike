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


class PlayerEntityGraphics(EntityGraphics):
    def __init__(self, _data):
        sprites = {
            "StandingUp": PlayerSpriteStandingUp,
            "StandingDown": PlayerSpriteStandingDown,
            "StandingLeft": PlayerSpriteStandingLeft,
            "StandingRight": PlayerSpriteStandingRight,
            "WalkingUp": PlayerSpriteWalkingUp,
            "WalkingDown": PlayerSpriteWalkingDown,
            "WalkingLeft": PlayerSpriteWalkingLeft,
            "WalkingRight": PlayerSpriteWalkingRight,
            "AtackingUp": PlayerSpriteAtackingUp,
            "AtackingDown": PlayerSpriteAtackingDown,
            "AtackingLeft": PlayerSpriteAtackingLeft,
            "AtackingRight": PlayerSpriteAtackingRight,
            "MassiveAtackingUp": PlayerSpriteMassiveAtackingUp,
            "MassiveAtackingDown": PlayerSpriteMassiveAtackingDown,
            "MassiveAtackingLeft": PlayerSpriteMassiveAtackingLeft,
            "MassiveAtackingRight": PlayerSpriteMassiveAtackingRight
        }

        EntityGraphics.__init__(self, _data, sprites)

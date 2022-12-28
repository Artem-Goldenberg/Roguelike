from entityGraphics import EntityGraphics, UpgradedSprite

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
            'Sprites/Player/Up/WarriorUpIdle.png',
            2,
            _steadiness_time=standing_stadiness)


class PlayerSpriteStandingDown(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'Sprites/Player/Down/WarriorDownIdle.png',
            2,
            _steadiness_time=standing_stadiness)


class PlayerSpriteStandingLeft(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'Sprites/Player/Left/WarriorLeftIdle.png',
            2,
            _steadiness_time=standing_stadiness)


class PlayerSpriteStandingRight(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'Sprites/Player/Right/WarriorRightIdle.png',
            2,
            _steadiness_time=standing_stadiness)


class PlayerSpriteWalkingUp(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'Sprites/Player/Up/WarriorUpWalk.png',
            2,
            walking_duration,
            walking_stadiness)

    def getPositionChange(self, _dt):
        return [0, - 100 * _dt]


class PlayerSpriteWalkingDown(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'Sprites/Player/Down/WarriorDownWalk.png',
            2,
            walking_duration,
            walking_stadiness)

    def getPositionChange(self, _dt):
        return [0, 100 * _dt]


class PlayerSpriteWalkingLeft(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'Sprites/Player/Left/WarriorLeftWalk.png',
            2,
            walking_duration,
            walking_stadiness)

    def getPositionChange(self, _dt):
        return [- 100 * _dt, 0]


class PlayerSpriteWalkingRight(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'Sprites/Player/Right/WarriorRightWalk.png',
            2,
            walking_duration,
            walking_stadiness)

    def getPositionChange(self, _dt):
        return [100 * _dt, 0]


class PlayerSpriteAtackingUp(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'Sprites/Player/Up/WarriorUpAttack01.png',
            2,
            atacking_duration,
            atacking_stadiness)


class PlayerSpriteAtackingDown(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'Sprites/Player/Down/WarriorDownAttack01.png',
            2,
            atacking_duration,
            atacking_stadiness)


class PlayerSpriteAtackingLeft(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'Sprites/Player/Left/WarriorLeftAttack01.png',
            2,
            atacking_duration,
            atacking_stadiness)


class PlayerSpriteAtackingRight(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'Sprites/Player/Right/WarriorRightAttack01.png',
            2,
            atacking_duration,
            atacking_stadiness)

class PlayerSpriteMassiveAtackingUp(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'Sprites/Player/Up/WarriorUpAttack02.png',
            2,
            massive_atacking_duration,
            massive_atacking_stadiness)


class PlayerSpriteMassiveAtackingDown(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'Sprites/Player/Down/WarriorDownAttack02.png',
            2,
            massive_atacking_duration,
            massive_atacking_stadiness)


class PlayerSpriteMassiveAtackingLeft(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'Sprites/Player/Left/WarriorLeftAttack02.png',
            2,
            massive_atacking_duration,
            massive_atacking_stadiness)


class PlayerSpriteMassiveAtackingRight(UpgradedSprite):
    def __init__(self):
        UpgradedSprite.__init__(
            self,
            'Sprites/Player/Right/WarriorRightAttack02.png',
            2,
            massive_atacking_duration,
            massive_atacking_stadiness)


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

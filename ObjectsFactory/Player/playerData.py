from Engine.activeEntityData import ActiveEntityData


class PlayerStats:
    def __init__(self):
        self.normal_damage = 10
        self.massive_damage = 10
        self.maximum_hp = 100


class PlayerData(ActiveEntityData):
    def __init__(
            self,
            _env,
            _hp=100,
            _state="",
            _meta_instructions=[],
            _meta_state="",
            _position=[0, 0],
            _animation_stage=0.0,
            _inventory=None,
            _custom=""
    ):
        ActiveEntityData.__init__(
            self,
            _env,
            _hp,
            _state,
            _meta_instructions,
            _meta_state,
            _position,
            _animation_stage,
            _inventory,
            _custom
        )

        self.exp = 0
        self.lvl = 0
        self.equipment = [None, None, None]
        self.stats = PlayerStats()

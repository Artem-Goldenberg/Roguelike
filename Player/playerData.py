from Engine.entityData import EntityData


class PlayerData(EntityData):
    def __init__(
            self,
            _env,
            _hp=100,
            _state="",
            _position=[0, 0],
            _animation_stage=0.0,
            _inventory=None,
            _custom=""
    ):
        EntityData.__init__(
            self,
            _env,
            _hp,
            _state,
            _position,
            _animation_stage,
            _inventory,
            _custom
        )

        self.exp = 0
        self.lvl = 0
        self.equipment = [None, None, None]

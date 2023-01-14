from Engine.entityData import EntityData


class ActiveEntityData(EntityData):
    def __init__(
        self,
        _env,
        _hp=100,
        _state="",
        _meta_instructions=[],
        _meta_state="",
        _position=(0, 0),
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
        self.meta_state = _meta_state
        self._meta_instructions = _meta_instructions
    
    def get_instructions(self):
        return self._meta_instructions
    
    def set_instructions(self, _instructions):
        self._meta_instructions = _instructions

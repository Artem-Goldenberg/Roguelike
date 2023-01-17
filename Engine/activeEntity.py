from Engine.entity import Entity


class ActiveEntity(Entity):
    def __init__(
        self,
        _entity_data,
        _entity_meta_logic,
        _entity_logic,
        _entity_graphics
    ):
        Entity.__init__(
            self,
            _entity_data,
            _entity_logic,
            _entity_graphics
        )

        self.meta_logic = _entity_meta_logic

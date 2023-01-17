from Engine.activeEntityMetaLogic import EntityMetaLogic, Strategy


class PlayerStrategyKeyboard(Strategy):
    def __init__(self, _data, _previous_state=None):
        Strategy.__init__(self, _data, _previous_state)

    def process(self, _dt: float):
        self.data.setInstructions(self.data.env.keyboardEvents.getEvents())


class PlayerMetaLogic(EntityMetaLogic):
    def __init__(self, _data):
        strategies = { 
            "Keyboard": PlayerStrategyKeyboard
        }

        EntityMetaLogic.__init__(self, _data, strategies)
    
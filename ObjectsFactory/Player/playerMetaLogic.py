from Engine.activeEntityMetaLogic import EntityMetaLogic, Strategy


class PlayerStrategyKeyboard(Strategy):
    def __init__(self, _data):
        Strategy.__init__(self, _data)

    def process(self, _dt: float):
        self.data.set_instructions(self.data.env.keyboardEvents.getEvents())



class PlayerMetaLogic(EntityMetaLogic):
    def __init__(self, _data):
        strategies = { 
            "Keyboard": PlayerStrategyKeyboard
        }

        EntityMetaLogic.__init__(self, _data, strategies)
    
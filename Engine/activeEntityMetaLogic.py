import logging


class Strategy():
    def __init__(self, _data):
        self.data = _data

    def process(self, _dt: float):
        logging.critical("Entity strategy is not implemented")
        raise


class EntityMetaLogic():
    def __init__(self, _data, _strategies):
        self.data = _data
        self.strategies = _strategies
        self.active_meta_state_name = ""
        self.active_meta_state = None

    def updateMetaInstructions(self, _dt):
        if self.active_meta_state_name != self.data.meta_state:
            if not self.strategies.__contains__(self.data.meta_state):
                logging.critical(f"getMetaInstructions: strategy is not implemented: {self.data.meta_state}")
                raise

            self.active_meta_state = self.strategies[self.data.meta_state](self.data)
            self.active_meta_state_name = self.data.meta_state

        self.active_meta_state.updateMetaInstructions(_dt)
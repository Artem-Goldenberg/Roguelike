import logging

from Engine.entityData import EntityData


class Behaviour():
    def __init__(self, _data):
        self.data = _data

    def process(self, _dt: float):
        logging.critical("Entity behaviour is not implemented")
        raise


class EntityLogic():
    def __init__(self, _data: EntityData, _behaviors):
        self.data = _data
        self.behaviors = _behaviors
        self.active_state_name = ""
        self.active_state = None

    def handleEvents(self, _dt):
        if self.active_state_name != self.data.state:
            if not self.behaviors.__contains__(self.data.state):
                logging.critical("HandleEvents: state is not implemented: " + str(self.data.state) )
                raise

            self.active_state = self.behaviors[self.data.state](self.data)
            self.active_state_name = self.data.state
            logging.info("EntityLogic: handleEvents: new sprite: \"" + str(self.active_state_name) + "\"")

        self.active_state.process(_dt)

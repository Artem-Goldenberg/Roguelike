import logging

from Engine.entityData import EntityData


class Behaviour():
    def process(self, _dt: float):
        logging.critical("Entity behaviour is not implemented")
        raise


class EntityLogic():
    def __init__(self, _env, _data: EntityData, _behaviors):
        self.env = _env
        self.data = _data
        self.behaviors = _behaviors
        self.active_state_name = ""
        self.active_state = None

    def handleEvents(self, _dt):
        if self.active_state_name != self.data.state:
            if not self.behaviors.__contains__(self.data.state):
                logging.critical("HandleEvents: state is not implemented: " + str(self.data.state) )
                raise

            self.active_state = self.behaviors[self.data.state](self.env)
            self.active_state_name = self.data.state
            logging.info("EntityLogic: draw: new sprite: \"" + str(self.active_state_name) + "\"")

        self.active_state.process(self.data, _dt)

import logging
import typing as tp
from entityData import EntityData


class Behaviour():
    def process(self, time: int):
        logging.info("Entity behaviour is not implemented")


class EntityLogic():
    def __init__(self, _env, _data: EntityData, behaviors: tp.Dict[str, Behaviour]):
        self.env = _env
        self.data = _data
        self.behaviors = behaviors

    def handleEvents(self):
        logging.info("Entity logic is not implemented: Logic(" + str(self) + "), Data(" + str(self.data) + ")")

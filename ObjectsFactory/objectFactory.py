import logging

from ObjectsFactory.Rock.rock import Rock
from ObjectsFactory.Shiny.shiny import Shiny


class ObjectFactory:
    def __init__(self):
        self.known_objects = {
            "Rock": Rock,
            "Shiny": Shiny
        }

    def getObject(self, _name, _env, _pos):
        if not self.known_objects.__contains__(_name):
            logging.critical("ObjectsFactory: no known objects with name \"" + _name + "\"")
            raise

        obj = self.known_objects[_name](_env, _pos)
        return obj

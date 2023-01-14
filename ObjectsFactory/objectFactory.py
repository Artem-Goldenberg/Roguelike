import logging

from ObjectsFactory.Rock.rock import Rock
from ObjectsFactory.Rock.rockGraphics import RockGraphics
from ObjectsFactory.Rock.rockLogic import RockLogic

from ObjectsFactory.Fire.fire import Fire
from ObjectsFactory.Fire.fireGraphics import FireGraphics
from ObjectsFactory.Fire.fireLogic import FireLogic

from ObjectsFactory.Shiny.shiny import Shiny
from ObjectsFactory.Shiny.shinyGraphics import ShinyGraphics
from ObjectsFactory.Shiny.shinyLogic import ShinyLogic

from ObjectsFactory.Player.player import Player
from ObjectsFactory.Player.playerGraphics import PlayerEntityGraphics

from Engine.entity import Entity
from Engine.activeEntity import ActiveEntity
from Engine.defaultActiveEntityLogic import DefaultEntityLogic


class ObjectFactory:
    def __init__(self):
        self.known_objects = {
            "Rock": Rock,
            "Fire": Fire,
            "Shiny": Shiny
        }
        self.known_entities = {
            "Passive": Entity,
            "Active": ActiveEntity
        }
        self.known_graphics = {
            "Rock": Rock,
            "Fire": Fire,
            "Shiny": Shiny,
            "Player": Player
        }

    def getObject(self, _name, _env, _pos):
        if not self.known_objects.__contains__(_name):
            logging.critical("ObjectsFactory: no known objects with name \"" + _name + "\"")
            raise

        obj = self.known_objects[_name](_env, _pos)

        return obj

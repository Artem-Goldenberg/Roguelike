import copy
import logging

from ObjectsFactory.Rock.rockGraphics import RockGraphics
from ObjectsFactory.Rock.rockLogic import RockLogic

from ObjectsFactory.Fire.fireGraphics import FireGraphics
from ObjectsFactory.Fire.fireLogic import FireLogic

from ObjectsFactory.Shiny.shinyGraphics import ShinyGraphics
from ObjectsFactory.Shiny.shinyLogic import ShinyLogic

from ObjectsFactory.Player.playerData import PlayerData
from ObjectsFactory.Player.playerGraphics import PlayerEntityGraphics
from ObjectsFactory.Player.playerMetaLogic import PlayerMetaLogic

from Engine.entity import Entity
from Engine.activeEntity import ActiveEntity
from Engine.entityData import EntityData, Inventory
from Engine.defaultActiveEntityLogic import DefaultEntityLogic


class ObjectFactory:
    def __init__(self, _env): # _env ?
        self.known_graphics = {
            "Rock": RockGraphics,
            "Fire": FireGraphics,
            "Shiny": ShinyGraphics,
            "Player": PlayerEntityGraphics
        }
        self.known_logics = { 
            "RockLogic": RockLogic,
            "FireLogic": FireLogic,
            "ShinyLogic": ShinyLogic,
            "PlayerLogic": DefaultEntityLogic
        }
        self.known_meta_logics = { 
            "PlayerMetaLogic": PlayerMetaLogic
        }
        # ?
        self.default_data = { 
            "RockLogic": EntityData(_env, _state="Stand"),
            "FireLogic": EntityData(_env, _state="Burn"),
            "ShinyLogic": EntityData(_env, _state="Stand"),
            "PlayerLogic": PlayerData(
                _env,
                _state="StandingDown",
                _meta_state="Keyboard",
                _inventory=Inventory(_capacity=9),
                _custom=(0, 1)
            )
        }

    # def getSimpleEntity(
    #         self,
    #         _env,
    #         _logic,
    #         _graphics,
    #         _hp=100,
    #         _state="",
    #         _pos=(0, 0),
    #         _inventory=None,
    #         _custom=""
    # ):
    #     if _logic not in self.known_logics:
    #         logging.critical("ObjectsFactory: no known logics with id \"" + _logic + "\"")
    #         raise 
    #     if _graphics not in self.known_graphics:
    #         logging.critical("ObjectsFactory: no known graphics with id \"" + _graphics + "\"")
    #         raise 

    #     data = EntityData(
    #         _env,
    #         _hp=_hp,
    #         _state=_state,
    #         _position=_pos,
    #         _inventory=_inventory,
    #         _custom=_custom
    #     )
        
    #     return Entity(
    #         data,
    #         self.known_logics[_logic](_data),
    #         self.known_graphics[_graphics](_data)
    #     )

    # def getActiveEntity(
    #         self,
    #         _env,
    #         _meta_logic,
    #         _logic,
    #         _graphics,
    #         _hp=100,
    #         _state="",
    #         _meta_instructions=[],
    #         _meta_state="",
    #         _pos=(0, 0),
    #         _inventory=None,
    #         _custom=""
    # ):
    #     if _logic not in self.known_logics:
    #         logging.critical("ObjectsFactory: no known logics with id \"" + _logic + "\"")
    #         raise 
    #     if _graphics not in self.known_graphics:
    #         logging.critical("ObjectsFactory: no known graphics with id \"" + _graphics + "\"")
    #         raise 
    #     if _meta_logic not in self.known_meta_logics:
    #         logging.critical("ObjectsFactory: no known meta logics with id \"" + _meta_logic + "\"")
    #         raise  

    #     data = ActiveEntityData(
    #         _env,
    #         _hp=_hp,
    #         _state=_state,
    #         _meta_instructions=_meta_instructions,
    #         _meta_state=_meta_state,
    #         _position=_pos,
    #         _inventory=_inventory,
    #         _custom=_custom
    #     )
        
    #     return ActiveEntity(
    #         data,
    #         self.known_meta_logics[_meta_logic](_data),
    #         self.known_logics[_logic](_data),
    #         self.known_graphics[_graphics](_data)
    #     )

    def getSimpleEntity(self, _logic, _graphics, _data=None, _pos=None):
        """ Builds new Entity object with with given parameters

        Method accepts parameters ids, it then looks them up in the pre-defined dictionaries
        Raises an exception if hasn't found a parameter for id

        :param _logic: id of a new entity's logic
        :param _graphics: id for the entity's graphics
        :param _data: an actual object with all information about entity, default is None
            if None, the default data will be used
        :param _pos: position on the map, only used if _data is None
            
        :type _logic: str
        :type _graphics: str
        :type _data: EntityData | None
        :type _pos: tuple of 2 ints | None
        """
        if _logic not in self.known_logics:
            logging.critical("ObjectsFactory: no known logics with id \"" + _logic + "\"")
            raise
        if _graphics not in self.known_graphics:
            logging.critical("ObjectsFactory: no known graphics with id \"" + _graphics + "\"")
            raise

        if _data is None:
            if _logic not in self.default_data:
                logging.critical("ObjectsFactory: no default data for logic id \"" + _logic + "\"")
                raise
            _data = copy.copy(self.default_data[_logic])
            if _pos is not None:
                _data.position = _pos

        return Entity(
            _data, 
            self.known_logics[_logic](_data),
            self.known_graphics[_graphics](_data)
        )
    
    def getActiveEntity(self, _meta_logic, _logic, _graphics, _data=None, _pos=None):
        """ Builds a new ActiveEntity object with given parameters

        Method accepts parameters ids, it then looks them up in the pre-defined dictionaries
        Raises an exception if hasn't found a parameter for id

        :param _meta_logic: meta logic id for an active entity
        :param _logic: id of a new entity's logic
        :param _graphics: id for the entity's graphics
        :param _data: an actual object with all information about entity, default is None
            if None, the default data will be used
        :param _pos: position on the map, only used if _data is None

        :type _meta_logic: str
        :type _logic: str
        :type _graphics: str
        :type _data: EntityData | None
        :type _pos: tuple of 2 ints | None
        """
        obj = self.getSimpleEntity(_logic, _graphics, _data, _pos)
        if _meta_logic not in self.known_meta_logics:
            logging.critical("ObjectsFactory: no known meta logics with id \"" + _meta_logic + "\"")
            raise

        return ActiveEntity(
            obj.data,
            self.known_meta_logics[_meta_logic](obj.data),
            obj.logic,
            obj.graphics
        )

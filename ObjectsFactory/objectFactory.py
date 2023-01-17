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
from ObjectsFactory.Player.playerLogic import PlayerLogic

from ObjectsFactory.Skeleton.skeletonGraphics import SkeletonGraphics
from ObjectsFactory.Enemy.enemyMetaLogic import EnemyMetaLogic

from Engine.entity import Entity
from Engine.activeEntity import ActiveEntity
from Engine.entityData import EntityData, Inventory
from Engine.activeEntityData import ActiveEntityData
from Engine.defaultActiveEntityLogic import DefaultEntityLogic


class ObjectFactory:
    def __init__(self, _env):
        self.env = _env
        self.known_graphics = {
            "Rock": RockGraphics,
            "Fire": FireGraphics,
            "Shiny": ShinyGraphics,
            "Player": PlayerEntityGraphics,
            "Skeleton": SkeletonGraphics
        }

        self.known_simple_logics = {
            "Rock": RockLogic,
            "Fire": FireLogic,
            "Shiny": ShinyLogic
        }

        self.known_active_logics = {
            "Player": PlayerLogic,
            "Skeleton": DefaultEntityLogic
        }

        self.known_meta_logics = { 
            "Player": PlayerMetaLogic,
            "Skeleton": EnemyMetaLogic
        }

        self.default_data = {
            "Rock": EntityData(_env, _state="Stand"),
            "Fire": EntityData(_env, _state="Burn"),
            "Shiny": EntityData(_env, _state="Stand"),
            "Player": PlayerData(
                _env,
                _state="StandingDown",
                _meta_state="Keyboard",
                _inventory=Inventory(_capacity=9),
                _custom=(0, 1)
            ),
            "Skeleton": ActiveEntityData(
                _env,
                _state="StandingDown",
                _meta_state="Aggressive",
                _inventory=Inventory(_capacity=3),
                _damage=5,
                _custom=(0, 1),
                _hp=40
            )
        }

    def getSimpleEntity(self, _logic_name, _graphics_name, _pos=None, _items_names=[]):
        """ Builds new Entity object with with given parameters

        Method accepts parameters ids, it then looks them up in the pre-defined dictionaries
        Raises an exception if hasn't found a parameter for id

        :param _logic: id of a new entity's logic
        :param _graphics: id for the entity's graphics
        :param _pos: position on the map, only used if _data is None

        :type _logic: str
        :type _graphics: str
        :type _pos: tuple of 2 ints | None
        """
        if _logic_name not in self.known_simple_logics:
            logging.critical(f'ObjectsFactory: no known/suitable logic named "{_logic_name}" found')
            raise

        if _graphics_name not in self.known_graphics:
            logging.critical(f'ObjectsFactory: no known graphics named "{_graphics_name}" found')
            raise

        if _logic_name not in self.default_data:
            logging.critical(f'ObjectsFactory: no default data for logic named "{_logic_name}" found')
            raise

        _data = copy.copy(self.default_data[_logic_name])

        if _pos is not None:
            _data.position = _pos

        _data.inventory = Inventory(_capacity=len(_items_names))
        for item_name in _items_names:
            _data.inventory.addItem(self.env.item_factory.getItem(item_name))

        return Entity(
            _data,
            self.known_simple_logics[_logic_name](_data),
            self.known_graphics[_graphics_name](_data)
        )

    def getActiveEntity(self, _meta_logic_name, _logic_name, _graphics_name, _pos=None, _items_names=[]):
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

        if _logic_name not in self.known_active_logics:
            logging.critical(f'ObjectsFactory: no known/suitable logic named "{_logic_name}" found')
            raise

        if _graphics_name not in self.known_graphics:
            logging.critical(f'ObjectsFactory: no known graphics named "{_graphics_name}" found')
            raise

        if _meta_logic_name not in self.known_meta_logics:
            logging.critical(f'ObjectsFactory: no known meta logic named "{_meta_logic_name}" found')
            raise

        if _logic_name not in self.default_data:
            logging.critical(f'ObjectsFactory: no default data for logic named "{_logic_name}" found')
            raise

        _data = copy.copy(self.default_data[_logic_name])

        if _pos is not None:
            _data.position = _pos

        _data.inventory = Inventory(_capacity=len(_items_names))
        for item_name in _items_names:
            _data.inventory.addItem(self.env.item_factory.getItem(item_name))

        return ActiveEntity(
            _data,
            self.known_meta_logics[_meta_logic_name](_data),
            self.known_active_logics[_logic_name](_data),
            self.known_graphics[_graphics_name](_data)
        )

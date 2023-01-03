# import random
import typing as tp
# from uuid import UUID
# from enum import Enum, auto
from dataclasses import dataclass, field


class Item:
    def __init__(
            self,
            _name,
            _cost,
            _texture,
            _quantity=1
    ):
        self.name = _name
        self.cost = _cost
        self.quantity = _quantity
        self.texture = _texture


@dataclass
class Inventory:
    items: tp.List[Item] = field(default_factory=list)

    def addItem(self, _item):
        self._items.append(_item)

    def removeItem(self, _item):
        self._items.remove(_item)

    def merge(self, _other):
        self.items += _other.items




class EntityData:
    def __init__(
            self,
            _env,
            _state="",
            _position=(0, 0),
            _animation_stage=0.0,
            _inventory=Inventory([]),
            _custom=""
    ):
        self.env = _env
        self.state = _state
        self.position = _position
        self.animation_stage = _animation_stage
        self.inventory = _inventory
        self.custom = _custom

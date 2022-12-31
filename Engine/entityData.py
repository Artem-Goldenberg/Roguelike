import random
import typing as tp
from uuid import UUID
# from enum import Enum, auto
from dataclasses import dataclass, field

def get_unique_id():
    return UUID(int=random.getrandbits(128))


@dataclass
class Item:
    _id = get_unique_id()
    name: str
    cost: int
    quantity: int = 1
    texture: str = "default"

    def __eq__(self, other):
        return self._id == other.id


@dataclass
class Inventory:
    _items: tp.List[Item] = field(default_factory=list)

    def merge(self, other: 'Inventory'):
        # TODO: do checks whether we have space and so on...
        self._items += other._items

    def addItem(self, item: Item):
        self._items.append(item)

    def removeItem(self, item: Item):
        self._items.remove(item)


class EntityData:
    def __init__(
            self,
            _env,
            _state="",
            _position=(0, 0),
            _animation_stage=0.0,
            _inventory=Inventory([])
    ):
        self.id = get_unique_id()
        self.env = _env
        self.state = _state
        self.position = _position
        self.animation_stage = _animation_stage
        self.inventory = _inventory

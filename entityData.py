import random
import typing as tp
from uuid import UUID
# from enum import Enum, auto
from dataclasses import dataclass, field


# class EntityState(Enum):
#     idle = auto()


@dataclass
class Item:
    _id = UUID(int=random.getrandbits(128))
    name: str
    cost: int
    quantity: int = 1
    texture: str = "default"

    def __eq__(self, other):
        return self._id == other.id


@dataclass
class Inventory:
    _items: tp.List[Item] = field(default_factory=list)

    def addItem(self, item: Item):
        self._items.append(item)

    def removeItem(self, item: Item):
        self._items.remove(item)


@dataclass
class EntityData:
    state: str
    position: tp.List[int]
    inventory: Inventory
    custom: str = ""

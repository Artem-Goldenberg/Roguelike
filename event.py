from dataclasses import dataclass
from enum import Enum, auto
import typing as tp
from entity import Entity


class ConsumerGroup(Enum):
    everyone = auto()
    direct = auto()

    def __init__(self, consumer: tp.Optional[Entity]):
        self.consumer = consumer


@dataclass
class Event:
    class Type(Enum):
        pickUp = auto()
        attack = auto()
        move = auto()
        cannotMove = auto()
        custom = auto()

    event: Type
    consumers: ConsumerGroup
    origin: tp.Optional[Entity] = None

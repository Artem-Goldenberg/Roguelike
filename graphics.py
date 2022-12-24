import typing as tp
from abc import ABC, abstractmethod
from data import EntityData, EntityState


class Sprite:
    @abstractmethod
    def draw(self, time: int):
        ...

    @abstractmethod
    def getImage(self, time: int) -> str:
        ...

    @abstractmethod
    def getPosition(self, time: int) -> tp.List[int]:
        ...


class EntityView(ABC):
    @abstractmethod
    def __init__(self, data: EntityData, sprites: tp.Dict[EntityState, Sprite]):
        self.data = data
        self.sprites = sprites

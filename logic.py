import typing as tp
from abc import ABC, abstractmethod
from data import EntityState, EntityData


class Behavior(ABC):
    @abstractmethod
    def process(self, time: int):
        ...


class EntityLogic(ABC):
    def __init__(self, data: EntityData, behaviors: tp.Dict[EntityState, Behavior]):
        self.data = data
        self.behaviors = behaviors

    @abstractmethod
    def handleEvents(self, events: tp.List['Event']):
        ...

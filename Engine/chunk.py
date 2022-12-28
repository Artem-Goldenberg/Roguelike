import pygame
import random

import typing as tp
from Engine.entity import Entity


class Chunk:
    def __init__(self, _env, _pos=[0, 0], _entities: tp.List[Entity] = []):
        self.env = _env
        self.ceil = pygame.Surface((46, 46))
        self.ceil.fill((
            random.randint(50, 250),
            random.randint(50, 250),
            random.randint(50, 250)))
        self.pos = _pos
        self.entities = _entities

    def drawChunk(self, _screen, _camera_position):
        for i in range(-5, 6):
            for j in range(-6, 7):
                _screen.blit(
                    self.ceil,
                    [
                        self.pos[0] - 23 + 50*i - _camera_position[0],
                        self.pos[1] - 23 + 50*j - _camera_position[1]
                    ]
                )

    def drawEntities(self, _time, _screen, _camera_position):
        for entity in self.entities:
            entity.draw(_time, _screen, _camera_position)

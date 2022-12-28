import pygame
import logging
import random

# from Engine.entity import Entity


class Chunk:
    def __init__(self, _env, _pos=(0, 0)):
        self.env = _env
        self.ceil = pygame.Surface(
            (
                self.env.grid_step - 2 * self.env.chunk_gap,
                self.env.grid_step - 2 * self.env.chunk_gap
            )
        )
        self.ceil.fill((
            random.randint(50, 250),
            random.randint(50, 250),
            random.randint(50, 250)))
        self.pos = _pos
        self.entities = []  # none yet

        if self.env.chunk_width % 2 != 1:
            logging.critical("Chunk: chunk width must be odd !!!")
        if self.env.chunk_height % 2 != 1:
            logging.critical("Chunk: chunk height must be odd !!!")

    def drawChunk(self, _screen, _camera_position):
        for i in range(int((1-self.env.chunk_width)/2), int((1+self.env.chunk_width)/2)):
            for j in range(int((1-self.env.chunk_height)/2), int((1+self.env.chunk_height)/2)):
                _screen.blit(
                    self.ceil,
                    [
                        self.pos[0] - self.env.chunk_gap + self.env.grid_step * (i - 0.5) - _camera_position[0],
                        self.pos[1] - self.env.chunk_gap + self.env.grid_step * (j - 0.5) - _camera_position[1]
                    ]
                )

    def drawEntities(self, _time, _screen, _camera_position):
        for entity in self.entities:
            entity.draw(_time, _screen, _camera_position)

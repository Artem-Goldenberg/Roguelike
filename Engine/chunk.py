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
        self.bg_entities = []
        self.fg_entities = []

        random_positions = []
        while len(random_positions) < 20:
            new_pos = (
                random.randint(int((1-self.env.chunk_width)/2), int(self.env.chunk_width/2)),
                random.randint(int((1-self.env.chunk_height)/2), int(self.env.chunk_height/2))
            )
            if not random_positions.__contains__(new_pos):
                random_positions.append(new_pos)

        for rock_pos in random_positions[:10]:
            self.bg_entities.append(
                self.env.object_factory.getObject(
                    "Rock",
                    self.env,
                    [
                        rock_pos[0] * self.env.grid_step + self.pos[0],
                        rock_pos[1] * self.env.grid_step + self.pos[1]
                    ]
                )
            )

        for rock_pos in random_positions[10:]:
            self.fg_entities.append(
                self.env.object_factory.getObject(
                    "Fire",
                    self.env,
                    [
                        rock_pos[0] * self.env.grid_step + self.pos[0],
                        rock_pos[1] * self.env.grid_step + self.pos[1]
                    ]
                )
            )

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

    def drawBgEntities(self, _dt, _screen, _camera_position):
        for entity in self.bg_entities:
            entity.draw(_dt, _screen, _camera_position)

    def drawFgEntities(self, _dt, _screen, _camera_position):
        for entity in self.fg_entities:
            entity.draw(_dt, _screen, _camera_position)

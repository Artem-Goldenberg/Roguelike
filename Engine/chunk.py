import pygame
import logging
import random

# from Engine.entity import Entity


def addTestItems(chunk):
    NUM_SHINY = 10
    dx = range((1 - chunk.env.chunk_width) // 2, chunk.env.chunk_width // 2)
    dy = range((1 - chunk.env.chunk_height) // 2, chunk.env.chunk_height // 2)
    print(dx)
    print(dy)
    for x, y in zip(random.sample(dx, NUM_SHINY), random.sample(dy, NUM_SHINY)):
        chunk.entities.append(
            chunk.env.object_factory.getObject(
                "Shiny",
                chunk.env,
                [
                    x * chunk.env.grid_step + chunk.pos[0],
                    y * chunk.env.grid_step + chunk.pos[1]
                ]
            )
        )


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

        positions_for_rocks = []
        while len(positions_for_rocks) < 10:
            new_pos = (
                random.randint(int((1-self.env.chunk_width)/2), int(self.env.chunk_width/2)),
                random.randint(int((1-self.env.chunk_height)/2), int(self.env.chunk_height/2))
            )
            if not positions_for_rocks.__contains__(new_pos):
                positions_for_rocks.append(new_pos)
        for rock_pos in positions_for_rocks:
            self.entities.append(
                self.env.object_factory.getObject(
                    "Rock",
                    self.env,
                    [
                        rock_pos[0] * self.env.grid_step + self.pos[0],
                        rock_pos[1] * self.env.grid_step + self.pos[1]
                    ]
                )
            )

        addTestItems(self)

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
                        self.pos[0] - self.env.chunk_gap +
                        self.env.grid_step * (i - 0.5) - _camera_position[0],
                        self.pos[1] - self.env.chunk_gap +
                        self.env.grid_step * (j - 0.5) - _camera_position[1]
                    ]
                )

    def drawEntities(self, _dt, _screen, _camera_position):
        for entity in self.entities:
            entity.draw(_dt, _screen, _camera_position)

    def removeEntity(self, id):
        for i, entity in enumerate(self.entities):
            if entity.data.id == id:
                self.entities.pop(i)
                break

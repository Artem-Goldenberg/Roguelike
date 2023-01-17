import pygame
import logging
import random

# from Engine.entity import EntityData


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

        if self.env.chunk_width % 2 != 1:
            logging.critical("Chunk: chunk width must be odd !!!")
            raise
        if self.env.chunk_height % 2 != 1:
            logging.critical("Chunk: chunk height must be odd !!!")
            raise

        # self.random_init()

    def drawChunk(self, _screen, _camera_position):
        for i in range((1-self.env.chunk_width) // 2, (1+self.env.chunk_width) // 2):
            for j in range((1-self.env.chunk_height) // 2, (1+self.env.chunk_height) // 2):
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

    def removeEntity(self, _data):
        for i, entity in enumerate(self.bg_entities):
            if entity.data == _data:
                self.bg_entities.pop(i)
        for i, entity in enumerate(self.fg_entities):
            if entity.data == _data:
                self.fg_entities.pop(i)

    def addToBG(self, _entity):
        self.bg_entities.append(_entity)

    def addToFG(self, _entity):
        self.fg_entities.append(_entity)

    def random_init(self):
        random_positions = []
        while len(random_positions) < 40:
            new_pos = (
                random.randint((1-self.env.chunk_width) // 2, self.env.chunk_width // 2),
                random.randint((1-self.env.chunk_height) // 2, self.env.chunk_height // 2)
            )
            if not random_positions.__contains__(new_pos):
                random_positions.append(new_pos)

        for rock_pos in random_positions[:10]:
            self.bg_entities.append(
                self.env.object_factory.getSimpleEntity(
                    _logic_name="Rock",
                    _graphics_name="Rock",
                    _pos=[
                        rock_pos[0] * self.env.grid_step + self.pos[0],
                        rock_pos[1] * self.env.grid_step + self.pos[1]
                    ]
                )
            )

        for fire_pos in random_positions[10:20]:
            self.fg_entities.append(
                self.env.object_factory.getSimpleEntity(
                    _logic_name="Fire",
                    _graphics_name="Fire",
                    _pos=[
                        fire_pos[0] * self.env.grid_step + self.pos[0],
                        fire_pos[1] * self.env.grid_step + self.pos[1]
                    ]
                )
            )

        for item_pos in random_positions[20:35]:
            shiny = self.env.object_factory.getSimpleEntity(
                _logic_name="Shiny",
                _graphics_name="Shiny",
                _pos=[
                    item_pos[0] * self.env.grid_step + self.pos[0],
                    item_pos[1] * self.env.grid_step + self.pos[1]],
                _items_names=["SampleItem"]
            )
            shiny.data.inventory.addItem(
                self.env.item_factory.getItem("SampleItem")
            )
            self.fg_entities.append(shiny)

        for enemy_pos in random_positions[35:]:
            enemy = self.env.object_factory.getActiveEntity(
                _meta_logic_name="Skeleton",
                _logic_name="Skeleton",
                _graphics_name="Skeleton",
                _pos=[
                    enemy_pos[0] * self.env.grid_step + self.pos[0],
                    enemy_pos[1] * self.env.grid_step + self.pos[1]],
                _items_names=["SampleItem"]
            )
            self.fg_entities.append(enemy)


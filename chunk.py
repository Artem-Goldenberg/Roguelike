import pygame
import random


class Chunk:
    def __init__(self, _env, _pos=[0, 0]):
        self.env = _env
        self.ceil = pygame.Surface((46, 46))
        self.ceil.fill((
            random.randint(50, 250),
            random.randint(50, 250),
            random.randint(50, 250)))
        self.pos = _pos

    def draw(self, screen, camera_position):
        for i in range(-5, 6):
            for j in range(-6, 7):
                screen.blit(
                    self.ceil,
                    [
                        self.pos[0] - 23 + 50*i - camera_position[0],
                        self.pos[1] - 23 + 50*j - camera_position[1]
                    ]
                )

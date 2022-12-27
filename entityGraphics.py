import logging
import typing as tp
from entityData import EntityData

# temporal
import pygame
import time

Point = tp.List[int]


class Sprite:
    def __init__(self, _duration=1.0):
        self.duration = _duration

    # Basic function that draws sprite with respect to getImage, getPosition
    # and base position
    def draw(self, _time, _screen, _base_position):
        _screen.blit(
            self.getImage(_time),
            [
                self.getPosition(_time)[0] + _base_position[0],
                self.getPosition(_time)[1] + _base_position[1]
            ]
        )

    # Abstract function that returns image (texture) at specified time
    def getImage(self, _time) -> str:
        logging.info("Sprite: getImage is not implemented: Sprite(" + str(self) + ")")

    # Abstract function that returns position of texture at specified time
    # This point is considered to be relative to the base position -- beginning
    #  of corresponding animation
    def getPosition(self, _time) -> Point:
        logging.info("Sprite: getPosition is not implemented: Sprite(" + str(self) + ")")


class EntityGraphics():
    def __init__(self, _data: EntityData, _sprites: tp.Dict[str, Sprite]):
        self.data = _data
        self.sprites = _sprites
        self.active_sprite_name = ""
        self.active_sprite_create_time = 0.0
        self.active_sprite = None

    def draw(self, _time, _screen, _camera_position):
        if self.data.state != self.active_sprite_name or time.time() - self.active_sprite_create_time >= self.active_sprite.duration:
            if not self.sprites.__contains__(self.data.state):
                logging.info("EntityGraphics: draw: sprite \"" + str(self.data.state) + "\" is not implemented")
                raise
            self.active_sprite = self.sprites[self.data.state]()
            self.active_sprite_name = self.data.state
            self.active_sprite_create_time = time.time()

        self.active_sprite.draw(
            time.time() - self.active_sprite_create_time,
            _screen,
            [
                self.data.position[0] - _camera_position[0],
                self.data.position[1] - _camera_position[1]
            ]
        )


# Predefined Sprite that automatically loads Sprites with given name
# This template works only with sprites being a row of frames glued together
# Remember that you steel need to implement getPosition by yourself
class UpgradedSprite(Sprite):
    def __init__(self, _filename, _scale, _duration=1.0):
        Sprite.__init__(self, _duration)

        image = pygame.image.load(_filename).convert_alpha()
        self.frame_count = image.get_width() / image.get_height()
        self.texture_sheet = pygame.Surface(
            [
                _scale * image.get_width(),
                _scale * image.get_height()
            ],
            pygame.SRCALPHA
        )
        self.texture_sheet.blit(
            pygame.transform.scale(
                image,
                (
                    self.texture_sheet.get_width(),
                    self.texture_sheet.get_height()
                )
            ),
            (0, 0)
        )

    # Actually overrides base class method
    def getImage(self, _time):
        real_duration = 1.0 if self.duration == 0 else self.duration
        stage = int(_time * self.frame_count / real_duration) % self.frame_count
        image = pygame.Surface(
            [
                self.texture_sheet.get_height(),
                self.texture_sheet.get_height()
            ],
            pygame.SRCALPHA
        )
        image.blit(
            self.texture_sheet,
            (0, 0),
            (
                stage * self.texture_sheet.get_height(),
                0,
                self.texture_sheet.get_height() * (stage+1),
                self.texture_sheet.get_height()
            )
        )
        return image

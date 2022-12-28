import logging
import typing as tp
from entityData import EntityData

# temporal
import pygame
import time

Point = tp.List[int]


class Sprite:
    def __init__(self, _steadiness_time=0.0):
        self.steadiness_time = _steadiness_time

    # Basic function that draws sprite with respect to getImage, getPosition
    # and base position
    def draw(self, _duration_time, _screen, _position):
        _screen.blit(
            self.getImage(_duration_time),
            [
                _position[0] + self.getOffset()[0],
                _position[1] + self.getOffset()[1]
            ]
        )

    # Abstract function that returns image (texture) at specified time
    def getImage(self, _time) -> str:
        logging.info("Sprite: getImage is not implemented: Sprite(" + str(self) + ")")
        raise

    # Abstract function that returns position of texture at specified time
    # This point is considered to be relative to the base position -- beginning
    #  of corresponding animation
    #  DEPRECATED

    def getOffset(self) -> Point:
        logging.info("Sprite: getPosition is not implemented: Sprite(" + str(self) + ")")
        raise

    def getPositionChange(self, _dt) -> Point:
        logging.info("Sprite: getPosition is not implemented: Sprite(" + str(self) + ")")
        raise


class EntityGraphics():
    def __init__(self, _data: EntityData, _sprites: tp.Dict[str, Sprite]):
        self.data = _data
        self.sprites = _sprites

        self.active_sprite_name = ""
        self.active_sprite = None
        self.active_sprite_lasts = 0.0

    def draw(self, _dt, _screen, _camera_position):
        if self.data.state != self.active_sprite_name:
            if not self.sprites.__contains__(self.data.state):
                logging.info("EntityGraphics: draw: sprite \"" + str(self.data.state) + "\" is not implemented")
                raise
            self.data.position[0] = round(self.data.position[0] / 50) * 50
            self.data.position[1] = round(self.data.position[1] / 50) * 50

            self.active_sprite = self.sprites[self.data.state]()
            self.active_sprite_name = self.data.state
            self.active_sprite_lasts = 0.0

            self.data.nextTimeAcceptingEvents = time.time() + self.active_sprite.steadiness_time

        else:
            self.active_sprite_lasts += _dt
            self.data.position[0] += self.active_sprite.getPositionChange(_dt)[0]
            self.data.position[1] += self.active_sprite.getPositionChange(_dt)[1]

        self.active_sprite.draw(
            self.active_sprite_lasts,
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
    def __init__(self, _filename, _scale, _duration=1.0, _steadiness_time=1.0):
        Sprite.__init__(self, _steadiness_time)
        self.duration = _duration

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
        stage = int(_time * self.frame_count / self.duration) % self.frame_count
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

    # TODO: needs more general solution
    def getOffset(self):
        return [0, 25]

    def getPositionChange(self, _dt):
        return [0, 0]

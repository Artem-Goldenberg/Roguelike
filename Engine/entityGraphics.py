import logging
import pygame

from math import floor

from Engine.entityData import EntityData


class Sprite:
    def __init__(self):
        pass

    # Basic function that draws sprite with respect to getImage, getPosition
    # and base position
    def draw(self, _animation_stage, _screen, _position):
        _screen.blit(
            self.getImage(_animation_stage),
            [
                _position[0] + self.getRelativePosition(_animation_stage)[0],
                _position[1] + self.getRelativePosition(_animation_stage)[1]
            ]
        )

    # Abstract function that returns image (texture) at specified time
    def getImage(self, _animation_stage):
        logging.critical("Sprite: getImage is not implemented: Sprite(" + str(self) + ")")
        raise

    # Abstract function that returns position of texture at specified time
    # This point is considered to be relative to the base position -- beginning
    #  of corresponding animation
    def getRelativePosition(self, _animation_stage):
        logging.critical("Sprite: getPosition is not implemented: Sprite(" + str(self) + ")")
        raise


class EntityGraphics():
    def __init__(self, _data: EntityData, _sprites):
        self.data = _data
        self.sprites = _sprites

        self.active_sprite_name = ""
        self.active_sprite = None

    def draw(self, _dt, _screen, _camera_position):
        if self.data.state != self.active_sprite_name:
            if not self.sprites.__contains__(self.data.state):
                logging.critical("EntityGraphics: draw: sprite \"" + str(self.data.state) + "\" is not implemented")
                raise

            self.active_sprite = self.sprites[self.data.state]()
            self.active_sprite_name = self.data.state
            logging.info("EntityGraphics: draw: new sprite: \"" + str(self.active_sprite_name) + "\"")

        self.active_sprite.draw(
            self.data.animation_stage,
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
    def __init__(self, _filename, _scale):
        Sprite.__init__(self)

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
    def getImage(self, _animation_stage):
        stage = floor(_animation_stage * self.frame_count)

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

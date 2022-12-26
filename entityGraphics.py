import logging
import typing as tp
from entityData import EntityData

Point = tp.List[int]


class Sprite:
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

    def draw(self, _time, _screen, _camera_position):
        if not self.sprites.__contains__(self.data.state):
            logging.info("EntityGraphics: draw: sprite \"" + str(self.data.state) + "\" is not implemented")

        self.sprites[self.data.state]().draw(
            _time,
            _screen,
            [
                self.data.position[0] - _camera_position[0],
                self.data.position[1] - _camera_position[1]
            ]
        )

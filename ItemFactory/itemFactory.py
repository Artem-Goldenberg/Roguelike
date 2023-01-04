import pygame
import logging
from Engine.entityData import Item


class UpgradedItem(Item):
    def __init__(
            self,
            _name,
            _cost,
            _texture_name="Default.png",
            _quantity=1
    ):
        image = pygame.image.load("ItemFactory/Textures/" + _texture_name).convert_alpha()
        resized_image = pygame.Surface(
            [
                80,
                80
            ],
            pygame.SRCALPHA
        )
        resized_image.blit(
            pygame.transform.scale(
                image,
                (
                    80,
                    80
                )
            ),
            (0, 0)
        )

        Item.__init__(
            self,
            _name,
            _cost,
            resized_image
        )


class ItemFactory():
    def __init__(self):
        self.known_items = {
            "SampleItem": UpgradedItem(
                "SampleItem",
                100
            )
        }

    def getItem(self, _name):
        if not self.known_items.__contains__(_name):
            logging.critical("ItemFactory: getName: no known objwct with name \"" + _name + "\"")
            raise

        else:
            item = self.known_items[_name]

            return Item(
                item.name,
                item.cost,
                item.texture
            )

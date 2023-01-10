import pygame
import logging
from Engine.entityData import Item, itemType


class UpgradedItem(Item):
    def __init__(
        self,
        _name,
        _cost,
        _texture_name="Default.png",
        _quantity=1,
        _item_type=itemType.Potion
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
            resized_image,
            _quantity,
            _item_type
        )


class ItemFactory():
    def __init__(self):
        self.known_items = {
            "SampleItem": UpgradedItem(
                "SampleItem",
                100
            ),
            "HealthRune": UpgradedItem(
                "HealthRune",
                100,
                "Rune1.png",
                1,
                itemType.Rune1
            ),
            "HealthRuneLvl1": UpgradedItem(
                "HealthRune",
                100,
                "Rune1lvl1.png",
                1,
                itemType.Rune1
            ),
            "HealthRuneLvl2": UpgradedItem(
                "HealthRune",
                100,
                "Rune1lvl2.png",
                1,
                itemType.Rune1
            ),
            "HealthRuneLvl3": UpgradedItem(
                "HealthRune",
                100,
                "Rune1lvl3.png",
                1,
                itemType.Rune1
            ),
            "NormalAttackRune": UpgradedItem(
                "NormalAttackRune",
                100,
                "Rune2.png",
                1,
                itemType.Rune2
            ),
            "NormalAttackRuneLvl1": UpgradedItem(
                "NormalAttackRune",
                100,
                "Rune2lvl1.png",
                1,
                itemType.Rune2
            ),
            "NormalAttackRuneLvl2": UpgradedItem(
                "NormalAttackRune",
                100,
                "Rune2lvl2.png",
                1,
                itemType.Rune2
            ),
            "NormalAttackRuneLvl3": UpgradedItem(
                "NormalAttackRune",
                100,
                "Rune2lvl3.png",
                1,
                itemType.Rune2
            ),
            "MassiveAttackRune": UpgradedItem(
                "MassiveAttackRune",
                100,
                "Rune3.png",
                1,
                itemType.Rune3
            ),
            "MassiveAttackRuneLvl1": UpgradedItem(
                "MassiveAttackRune",
                100,
                "Rune3lvl1.png",
                1,
                itemType.Rune3
            ),
            "MassiveAttackRuneLvl2": UpgradedItem(
                "MassiveAttackRune",
                100,
                "Rune3lvl3.png",
                1,
                itemType.Rune3
            ),
            "MassiveAttackRuneLvl3": UpgradedItem(
                "MassiveAttackRune",
                100,
                "Rune3lvl3.png",
                1,
                itemType.Rune3
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
                item.texture,
                item.quantity,
                item.item_type
            )

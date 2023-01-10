import pygame
from Engine.eventSystem import eventType
from Engine.entityData import itemType


class InventoryGraphics:
    def __init__(self, _data):
        self.data = _data
        self.width = self.data.env.window_width
        self.height = self.data.env.window_height
        self.gaps = (self.data.env.window_width - 9 * 90 - 10) // 2
        self.inventory_board = pygame.Rect(
            (
                self.gaps,
                self.data.env.window_height - 150,
                self.data.env.window_width - 2 * self.gaps,
                100
            )
        )
        self.item = pygame.Surface((80, 80))
        self.item.fill((200, 200, 200))
        self.choosen_one = 1
        self.time_since_last_interaction = 0.0
        self.click_duration = 0.3

    def update(self, _dt):
        self.time_since_last_interaction += _dt
        if self.time_since_last_interaction < self.click_duration:
            return

        if self.width != self.data.env.window_width or self.height != self.data.env.window_height:
            self.width = self.data.env.window_width
            self.height = self.data.env.window_height
            self.gaps = (self.data.env.window_width - 9 * 90 - 10) // 2
            self.inventory_board = pygame.Rect(
                (
                    self.gaps,
                    self.data.env.window_height - 150,
                    self.data.env.window_width - 2 * self.gaps,
                    100
                )
            )

        for event in self.data.env.keyboardEvents.getEvents(eventType.Custom):
            if event.data[:13] == "InventoryItem":
                if len(event.data) == 14 and event.data[13].isnumeric():
                    self.choosen_one = int(event.data[13])
                    self.time_since_last_interaction = 0.0
            if event.data == "UseItem":
                self.time_since_last_interaction = 0.0

                if self.data.inventory.items[self.choosen_one-1] is None:
                    continue

                if self.data.inventory.items[self.choosen_one-1].item_type == itemType.Potion:
                    # TODO: use potion
                    if self.choosen_one <= len(self.data.inventory.items):
                        self.data.inventory.items[self.choosen_one-1] = None
                        self.data.hp += 10
                        if self.data.hp > 100:
                            self.data.hp = 100
                    continue

                if self.data.inventory.items[self.choosen_one-1].item_type == itemType.Rune1:
                    old_item = self.data.equipment[0]
                    new_item = self.data.inventory.items[self.choosen_one-1]
                    self.data.equipment[0] = new_item
                    self.data.inventory.items[self.choosen_one-1] = old_item
                    continue

                if self.data.inventory.items[self.choosen_one-1].item_type == itemType.Rune2:
                    old_item = self.data.equipment[1]
                    new_item = self.data.inventory.items[self.choosen_one-1]
                    self.data.equipment[1] = new_item
                    self.data.inventory.items[self.choosen_one-1] = old_item
                    continue

                if self.data.inventory.items[self.choosen_one-1].item_type == itemType.Rune3:
                    old_item = self.data.equipment[2]
                    new_item = self.data.inventory.items[self.choosen_one-1]
                    self.data.equipment[2] = new_item
                    self.data.inventory.items[self.choosen_one-1] = old_item
                    continue

    def draw(self):
        # draw inventory bar
        pygame.draw.rect(
            self.data.env.screen,
            (0, 0, 0),
            self.inventory_board,
            border_top_left_radius=7,
            border_top_right_radius=7,
            border_bottom_left_radius=7,
            border_bottom_right_radius=7
        )

        # draw cells
        for i in range(-4, 5):
            self.data.env.screen.blit(
                self.item,
                [
                    self.data.env.window_width // 2 + i * 90 - 40,
                    self.data.env.window_height - 140
                ]
            )

        # draw items
        for i in range(0, len(self.data.inventory.items)):
            if self.data.inventory.items[i] is not None:
                self.data.env.screen.blit(
                    self.data.inventory.items[i].texture,
                    [
                        self.data.env.window_width // 2 + (i-4) * 90 - 40,
                        self.data.env.window_height - 140
                    ]
                )

        # highlight active item
        pygame.draw.rect(
            self.data.env.screen,
            (100, 200, 100),
            pygame.Rect(
                (
                    self.data.env.window_width // 2 + (self.choosen_one-5) * 90 - 45,
                    self.data.env.window_height - 146,
                    90,
                    92
                )
            ),
            2,
            7,
            7,
            7,
            7
        )

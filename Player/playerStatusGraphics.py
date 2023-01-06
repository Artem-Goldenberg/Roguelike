import pygame


class PlayerStatusBar:
    def __init__(self, _data):
        self.data = _data
        self.health_board = pygame.Rect(
            (
                30,
                30,
                600,
                30
            )
        )
        self.health_bg = pygame.Rect(
            (
                35,
                35,
                590,
                20
            )
        )
        self.exp_board = pygame.Rect(
            (
                30,
                60,
                500,
                26
            )
        )
        self.exp_bg = pygame.Rect(
            (
                35,
                65,
                490,
                15
            )
        )
        self.equipment_board = pygame.Rect(
            (
                30,
                86,
                170,
                60
            )
        )
        self.equipment_cell = pygame.Surface((
            50,
            50
        ))
        self.equipment_cell.fill((200, 200, 200))

    def draw(self):
        # Health bar
        pygame.draw.rect(
            self.data.env.screen,
            (0, 0, 0),
            self.health_board,
            border_top_left_radius=7,
            border_top_right_radius=7,
            border_bottom_left_radius=7,
            border_bottom_right_radius=7
        )

        # Health line bg
        pygame.draw.rect(
            self.data.env.screen,
            (100, 100, 100),
            self.health_bg,
            border_top_left_radius=7,
            border_top_right_radius=7,
            border_bottom_left_radius=7,
            border_bottom_right_radius=7
        )

        # Health line (actual)
        pygame.draw.rect(
            self.data.env.screen,
            (0, 200, 0),
            pygame.Rect(
                (
                    35,
                    35,
                    590 * self.data.hp / 100,
                    20
                )
            ),
            border_top_left_radius=7,
            border_top_right_radius=7,
            border_bottom_left_radius=7,
            border_bottom_right_radius=7
        )

        # Exp bar
        pygame.draw.rect(
            self.data.env.screen,
            (0, 0, 0),
            self.exp_board,
            border_top_left_radius=7,
            border_top_right_radius=7,
            border_bottom_left_radius=7,
            border_bottom_right_radius=7
        )

        # Exp line bg
        pygame.draw.rect(
            self.data.env.screen,
            (100, 100, 100),
            self.exp_bg,
            border_top_left_radius=7,
            border_top_right_radius=7,
            border_bottom_left_radius=7,
            border_bottom_right_radius=7
        )

        # TODO: actual exp line

        # Equipment bar
        pygame.draw.rect(
            self.data.env.screen,
            (0, 0, 0),
            self.equipment_board,
            border_top_left_radius=7,
            border_top_right_radius=7,
            border_bottom_left_radius=7,
            border_bottom_right_radius=7
        )

        for i in range(3):
            self.data.env.screen.blit(
                self.equipment_cell,
                (35 + 55 * i, 91)
            )

        for i in range(3):
            if self.data.equipment[i] is not None:
                # TODO: draw
                resized_image = pygame.Surface(
                    [
                        50,
                        50
                    ],
                    pygame.SRCALPHA
                )
                resized_image.blit(
                    pygame.transform.scale(
                        self.data.equipment[i].texture,
                        (
                            50,
                            50
                        )
                    ),
                    (0, 0)
                )
                self.data.env.screen.blit(
                    resized_image,
                    (35 + 55 * i, 91)
                )

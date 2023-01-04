import pygame


class PlayerHealth:
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

    def draw(self):
        pygame.draw.rect(
            self.data.env.screen,
            (0, 0, 0),
            self.health_board,
            border_top_left_radius=7,
            border_top_right_radius=7,
            border_bottom_left_radius=7,
            border_bottom_right_radius=7
        )

        pygame.draw.rect(
            self.data.env.screen,
            (100, 100, 100),
            pygame.Rect(
                (
                    35,
                    35,
                    590,
                    20
                )
            ),
            border_top_left_radius=7,
            border_top_right_radius=7,
            border_bottom_left_radius=7,
            border_bottom_right_radius=7
        )

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

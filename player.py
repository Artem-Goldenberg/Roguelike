import pygame


class Player:
    def __init__(self, env):
        self.env = env
        self.pos = [0, 0]
        self.temp_texture = pygame.Surface((20, 20))
        self.temp_texture.fill((250, 100, 100))

    def update(self, dt):
        pass
        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_UP]:
        #     self.pos[1] -= 300*dt
        # if keys[pygame.K_DOWN]:
        #     self.pos[1] += 300*dt
        # if keys[pygame.K_LEFT]:
        #     self.pos[0] -= 300*dt
        # if keys[pygame.K_RIGHT]:
        #     self.pos[0] += 300*dt
        # for event in pygame.event.get():
        #     print("Gotcha")
        #     if event.type == pygame.KEYDOWN:
        #         if event.key == pygame.K_UP:
        #             self.pos[1] -= self.env.grid_step
        #         if event.key == pygame.K_DOWN:
        #             self.pos[1] += self.env.grid_step
        #         if event.key == pygame.K_LEFT:
        #             self.pos[0] -= self.env.grid_step
        #         if event.key == pygame.K_RIGHT:
        #             self.pos[0] += self.env.grid_step

    def draw(self, screen, camera_position):
        screen.blit(self.temp_texture, [
                        -10 + self.pos[0] - camera_position[0],
                        -10 + self.pos[1] - camera_position[1]])

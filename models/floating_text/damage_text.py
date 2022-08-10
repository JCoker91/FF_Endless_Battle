import pygame
from random import randint


class DamageText(pygame.sprite.Sprite):
    def __init__(self, text, center, group):
        pygame.sprite.Sprite.__init__(self)
        self.center = (center[0], center[1] - 25)
        self.color = 'White'
        self.width = 32
        self.height = 32
        # crit = randint(0, 100)
        # self.crit = crit < 30
        # if self.crit:
        #     self.font = pygame.font.SysFont(
        #         "resources/fonts/Roboto/Roboto-Bold.ttf", 24)
        #     self.color = 'Yellow'
        # else:
        #     self.font = pygame.font.SysFont(
        #         "resources/fonts/Roboto/Roboto-Regular.ttf", 24)
        self.font = pygame.font.SysFont(
            "resources/fonts/Roboto/Roboto-Regular.ttf", 24)
        self.textSurf = self.font.render(text, 1, self.color)
        self.image = pygame.Surface((self.width, self.height)).convert_alpha()
        self.image.set_colorkey('Black')
        self.rect = self.image.get_rect(center=self.center)
        self.starting_pos = self.center
        W = self.textSurf.get_width()
        H = self.textSurf.get_height()
        self.image.blit(
            self.textSurf, [self.width/2 - W/2, self.height/2 - H/2])
        self.gravity = 1
        self.first_run = True
        self.x_direction = randint(-1, 1)
        # self.x_direction = 1
        group.add(self)

    def update(self):
        if self.first_run:
            self.gravity = randint(-6, -5)
            self.first_run = False
        else:
            self.gravity += .5
        self.rect.y += self.gravity
        self.rect.x += self.x_direction
        if self.rect.top > self.starting_pos[1]:
            self.kill()

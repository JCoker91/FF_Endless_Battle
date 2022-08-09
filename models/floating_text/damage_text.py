import pygame
from random import randint


class Text(pygame.sprite.Sprite):
    def __init__(self, text, size, color, width, height, center):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        crit = randint(0, 100)
        self.color = 'White'
        self.crit = crit < 30
        if self.crit:
            self.font = pygame.font.SysFont(
                "resources/fonts/Roboto/Roboto-Bold.ttf", size)
            self.color = 'Yellow'
        else:
            self.font = pygame.font.SysFont(
                "resources/fonts/Roboto/Roboto-Regular.ttf", size)

        self.textSurf = self.font.render(text, 1, self.color)
        self.image = pygame.Surface((width, height)).convert_alpha()
        self.image.set_colorkey('Black')
        self.rect = self.image.get_rect(center=center)
        self.starting_pos = center
        W = self.textSurf.get_width()
        H = self.textSurf.get_height()
        self.image.blit(self.textSurf, [width/2 - W/2, height/2 - H/2])
        self.gravity = 1
        self.first_run = True
        self.x_direction = randint(-1, 1)

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

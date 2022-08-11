import pygame


class DamageText(pygame.sprite.Sprite):
    def __init__(self, text, center, group):
        pygame.sprite.Sprite.__init__(self)
        self.center = (center[0], center[1] - 35)
        self.color = (255, 255, 255)
        self.outline_color = (1, 1, 1)
        self.text_size = 24
        self.is_waiting_count = 8
        self.width = self.text_size * 4
        self.height = self.text_size * 2
        self.is_first_run = True
        self.is_floating = True
        self.is_fading = False
        self.is_waiting = False
        self.font_outline = pygame.font.Font(
            "resources/fonts/SeymourOne/SeymourOne-Regular.ttf", self.text_size + 4)
        self.font = pygame.font.Font(
            "resources/fonts/SeymourOne/SeymourOne-Regular.ttf", self.text_size)
        self.textSurfOutline = self.font_outline.render(
            text, 1, self.outline_color)
        self.textSurf = self.font.render(text, 1, self.color)
        self.image = pygame.Surface((self.width, self.height)).convert_alpha()
        self.image.set_colorkey('Black')
        self.rect = self.image.get_rect(center=self.center)
        self.starting_pos = self.center
        W = self.textSurf.get_width()
        H = self.textSurf.get_height()
        self.image.blit(
            self.textSurfOutline, [(self.width/2 - W/2) - 2, (self.height/2 - H/2)-2])
        self.image.blit(
            self.textSurf, [self.width/2 - W/2, self.height/2 - H/2])
        self.gravity = 1
        group.add(self)

    def update(self):
        if self.is_floating:
            if self.is_first_run:
                self.gravity = -6
                self.is_first_run = False
            else:
                self.gravity += .5
            self.rect.y += self.gravity
        if self.rect.top > self.starting_pos[1]:
            self.is_floating = False
            self.is_waiting = True
        if self.is_waiting:
            self.is_waiting_count -= 1
            if self.is_waiting_count == 0:
                self.is_waiting = False
                self.is_fading = True
        if self.is_fading:
            self.image.set_alpha(self.image.get_alpha() - 10)
            self.rect.x += 1
            self.rect.y -= 1.5
            if self.image.get_alpha() == 0:
                self.kill()

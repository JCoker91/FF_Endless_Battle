import pygame
from settings import MENU_SECONDARY_COLOR
from source.util.custom_enum import DamageType


class DamageText(pygame.sprite.Sprite):
    def __init__(self, text: str, center: tuple, group: pygame.sprite.Group, damage_type: DamageType = None):
        pygame.sprite.Sprite.__init__(self)
        self.center = (center[0], center[1] - 35)
        self.damage_type = damage_type
        self.color = (255, 255, 255)
        self.outline_color = (1, 1, 1)
        self.text_size = 24
        self.set_color(damage_type)
        self.is_waiting_count = 8
        self.width = self.text_size * 4
        if len(text) > 3:
            self.width = self.text_size *8
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
        # self.textSurfRect =self.textSurf.get_rect()

        # self.text_mask = pygame.mask.from_surface(self.textSurf)
        # self.text_mask_surf = self.text_mask.to_surface().set_colorkey((0,0,0))
        # pixel_range = []
        # x_size, y_size = self.text_mask_surf.get_size()
        # for x in range(x_size):
        #     for y in range(y_size):
        #         if self.text_mask_surf.get_at((x, y)) == (255, 255, 255):
        #             pixel_range.append((x-1, y-1))
        #             pixel_range.append((x-1, y+1))
        #             pixel_range.append((x-1, y+1))
        #             pixel_range.append((x+1, y))
        #             pixel_range.append((x-1, y))
        #             pixel_range.append((x, y+1))
        #             pixel_range.append((x, y-1))
        # outline_color = (255, 255, 255)
        # for pixel_pos in pixel_range:
        #     self.text_mask_surf.set_at(pixel_pos, (outline_color))


        
        self.image = pygame.Surface((self.width, self.height)).convert_alpha()
        self.image.set_colorkey('Black')
        self.rect = self.image.get_rect(center=self.center)
        self.starting_pos = self.center
        W = self.textSurf.get_width()
        H = self.textSurf.get_height()

        self.image.blit(
            self.textSurfOutline, [(self.width/2 - W/2) - 2, (self.height/2 - H/2)-2])
        # self.image.blit(self.text_mask_surf, self.textSurf.get_rect())
        self.image.blit(
            self.textSurf, [self.width/2 - W/2, self.height/2 - H/2])
        self.gravity = 1
        group.add(self)

    def set_color(self, damage_type: DamageType):
        match damage_type:
            case DamageType.BREAK:
                self.color = (255, 0, 0)
                self.outline_color = (255, 255, 0)
                self.text_size = 28
            case DamageType.LIGHTNING:
                self.color = ('Yellow')
            case DamageType.FIRE:
                self.color = ('Red')
            case DamageType.WATER:
                self.color = ('Blue')
            case DamageType.ICE:
                self.color = ('Blue')
            case DamageType.WIND:
                self.color = ('Green')
            case DamageType.EARTH:
                self.color = ('Orange')
            case DamageType.DARK:
                self.color = ('Purple')
            case DamageType.LIGHT:
                self.color = ('White')
            case DamageType.NEUTRAL:
                self.color = ('White')
            case _:
                self.color = ('White')

    def update(self):
        if self.is_floating:
            if self.is_first_run:
                if self.damage_type == DamageType.BREAK:
                    self.gravity = -8
                else:
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

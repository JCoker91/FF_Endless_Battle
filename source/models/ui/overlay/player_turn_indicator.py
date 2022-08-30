import pygame
from source.models.character.character import Character
from source.util.custom_enum import PlayerSide, CurrentState
from settings import *


class PlayerTurnIndicator:
    def __init__(self) -> None:
        self.display_surface = pygame.display.get_surface()
        self.color_change_rate = 3
        self.r = 256 - 256 % self.color_change_rate
        self.g = 0
        self.b = 0
        self.outline_size = 1
        self.color = 'red'
        self.COLOR_DICT = {
            'red' : (256 - 256 % self.color_change_rate,0,0),
            'green' : (0,256 - 256 % self.color_change_rate,0),
            'blue' : (0,0,256  - 256 % self.color_change_rate),
            }
    def draw(self, player: Character):
        if player.side == PlayerSide.LEFT and player.current_state == CurrentState.IDLE or player.current_state == CurrentState.LIMIT_BREAK:
            image_mask = pygame.mask.from_surface(player.image)
            image_mask_surf = image_mask.to_surface()
            image_mask_surf = pygame.transform.scale(
                image_mask_surf, (player.image.get_width(), player.image.get_height()))
            image_mask_surf.set_colorkey((0, 0, 0))

            pixel_range = []
            x_size, y_size = image_mask_surf.get_size()
                
            for x in range(x_size):
                for y in range(y_size):
                    if image_mask_surf.get_at((x, y)) == (255, 255, 255):
                        pixel_range.append((x-self.outline_size, y-self.outline_size))
                        pixel_range.append((x-self.outline_size, y+self.outline_size))
                        pixel_range.append((x-self.outline_size, y+self.outline_size))
                        pixel_range.append((x+self.outline_size, y))
                        pixel_range.append((x-self.outline_size, y))
                        pixel_range.append((x, y+self.outline_size))
                        pixel_range.append((x, y-self.outline_size))
            
            if player.limit_break_gauge > 99:
                self.outline_size = 2
                if self.color == 'red':
                    if self.r < 256 -self.color_change_rate:
                        self.r += self.color_change_rate
                    else:
                        if self.g > 0:
                            self.g -=self.color_change_rate
                        if self.b > 0:
                            self.b -= self.color_change_rate
                    if (self.r, self.g, self.b) == self.COLOR_DICT['red']:
                        self.color = 'green'
                if self.color == 'green':
                    if self.g < 256-self.color_change_rate:
                        self.g +=self.color_change_rate
                    else:
                        if self.b > 0:
                            self.b -= self.color_change_rate
                        if self.r > 0:
                            self.r -= self.color_change_rate
                    if (self.r, self.g, self.b) == self.COLOR_DICT['green']:
                        self.color = 'blue'
                if self.color == 'blue':
                    if self.b < 256-self.color_change_rate:
                        self.b += self.color_change_rate
                    else:
                        if self.r > 0:
                            self.r -= self.color_change_rate
                        if self.g > 0:
                            self.g -=self.color_change_rate
                    if (self.r, self.g, self.b) == self.COLOR_DICT['blue']:
                        self.color = 'red'
                if self.r < 0:
                    self.r = 0
                if self.g < 0:
                    self.g = 0
                if self.b < 0:
                    self.b = 0
            else:
                self.outline_size = 1
                self.r=255
                self.g=255
                self.b=255
            outline_color = (self.r, self.g, self.b)
            for pixel_pos in pixel_range:
                image_mask_surf.set_at(pixel_pos, (outline_color))

            image_mask_rect = image_mask_surf.get_rect(
                center=(player.rect.center[0], player.rect.center[1]))
            if player.is_limit_breaking:
                print(player.off_set['limit_break'][0],player.off_set['limit_break'][1])
                image_mask_rect.x += player.off_set['limit_break'][0]
                image_mask_rect.y += player.off_set['limit_break'][1]
            self.display_surface.blit(image_mask_surf, image_mask_rect)

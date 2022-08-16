import pygame
from settings import *
from source.models.character.character import Character


class MPBar:
    def __init__(self, player: Character, x_pos: int, y_pos: int, text_overlay: bool = False, draw_point: str = "topleft") -> None:
        self.player = player
        self.text_overlay = text_overlay
        self.display_surf = pygame.display.get_surface()
        MAX_WIDTH = 150
        MAX_HEIGHT = 13
        mp_width = (player.current_stats['mp'] /
                    player.base_stats['mp']) * MAX_WIDTH
        self.current_hp_bar = pygame.Rect(x_pos, y_pos, mp_width, MAX_HEIGHT)

        self.max_mp_bar = pygame.Rect(x_pos, y_pos, MAX_WIDTH, MAX_HEIGHT)
        if draw_point == 'topleft':
            self.max_mp_bar.topleft = (x_pos, y_pos)
        elif draw_point == 'topright':
            self.max_mp_bar.topright = (x_pos, y_pos)
        elif draw_point == 'bottomleft':
            self.max_mp_bar.bottomleft = (x_pos, y_pos)
        elif draw_point == 'bottomright':
            self.max_mp_bar.bottomright = (x_pos, y_pos)
        self.current_hp_bar = pygame.Rect(
            x_pos, y_pos, mp_width, MAX_HEIGHT)
        self.current_hp_bar.topleft = self.max_mp_bar.topleft

    def draw_text_overlay(self):
        font = pygame.font.Font('resources/fonts/Pixeltype/Pixeltype.ttf', 16)
        mp_overlay_text = font.render(
            f"{self.player.current_stats['mp']}/{self.player.base_stats['mp']}", True, MENU_TEXT_COLOR)
        mp_overlay_rect = mp_overlay_text.get_rect(
            center=(self.max_mp_bar.center[0], self.max_mp_bar.center[1] + 2))
        self.display_surf.blit(mp_overlay_text, mp_overlay_rect)

    def draw(self):
        MP_COLOR = (0, 0, 200)
        pygame.draw.rect(self.display_surf, 'Black',
                         self.max_mp_bar)
        pygame.draw.rect(self.display_surf, MP_COLOR,
                         self.current_hp_bar)
        pygame.draw.rect(self.display_surf, 'White',
                         self.max_mp_bar, 1)
        if self.text_overlay:
            self.draw_text_overlay()

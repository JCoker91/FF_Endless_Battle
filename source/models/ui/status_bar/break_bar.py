import pygame
from settings import *
from source.models.character.character import Character


class BreakBar:
    def __init__(self, player: Character, x_pos: int, y_pos: int, text_overlay: bool = False, draw_point: str = 'topleft') -> None:
        self.player = player
        self.text_overlay = text_overlay
        self.display_surf = pygame.display.get_surface()
        MAX_WIDTH = 150
        MAX_HEIGHT = 13
        break_width = (player.break_bar /
                       100) * MAX_WIDTH
        self.max_break_bar = pygame.Rect(x_pos, y_pos, MAX_WIDTH, MAX_HEIGHT)
        self.current_break_bar = pygame.Rect(
            x_pos, y_pos, break_width, MAX_HEIGHT)
        if draw_point == 'topleft':
            self.max_break_bar.topleft = (x_pos, y_pos)
        elif draw_point == 'topright':
            self.max_break_bar.topright = (x_pos, y_pos)
        elif draw_point == 'bottomleft':
            self.max_break_bar.bottomleft = (x_pos, y_pos)
        elif draw_point == 'bottomright':
            self.max_break_bar.bottomright = (x_pos, y_pos)
        self.current_break_bar = pygame.Rect(
            x_pos, y_pos, break_width, MAX_HEIGHT)
        self.current_break_bar.topleft = self.max_break_bar.topleft

    def draw_text_overlay(self):
        font = pygame.font.Font('resources/fonts/Pixeltype/Pixeltype.ttf', 16)
        break_overlay_text = font.render(
            f"{self.player.break_bar}/100", True, MENU_TEXT_COLOR)
        break_overlay_rect = break_overlay_text.get_rect(
            center=(self.max_break_bar.center[0], self.max_break_bar.center[1] + 2))
        self.display_surf.blit(break_overlay_text, break_overlay_rect)

    def draw(self):
        BREAK_COLOR = (230, 150, 0)
        pygame.draw.rect(self.display_surf, 'Black',
                         self.max_break_bar)
        pygame.draw.rect(self.display_surf, BREAK_COLOR,
                         self.current_break_bar)
        pygame.draw.rect(self.display_surf, 'White', self.max_break_bar,
                         1)
        if self.text_overlay:
            self.draw_text_overlay()

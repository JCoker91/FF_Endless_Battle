import pygame
from settings import MENU_TEXT_COLOR
from source.models.character.character import Character


class HPBar:
    def __init__(self, player: Character, x_pos: int, y_pos: int, text_overlay: bool = False, draw_point: str = 'topleft', show_border: bool = True, show_background: bool = True, size: str = "large") -> None:
        self.player = player
        self.text_overlay = text_overlay
        self.show_border = show_border
        self.show_background = show_background
        self.display_surf = pygame.display.get_surface()
        if size == "large":
            MAX_WIDTH = 150
            MAX_HEIGHT = 13
        if size == "medium":
            MAX_WIDTH = 150
            MAX_HEIGHT = 13
        if size == "small":
            MAX_WIDTH = 30
            MAX_HEIGHT = 3
        hp_width = (player.current_stats['hp'] /
                    player.base_stats['hp']) * MAX_WIDTH
        self.max_hp_bar = pygame.Rect(x_pos, y_pos, MAX_WIDTH, MAX_HEIGHT)
        if draw_point == 'topleft':
            self.max_hp_bar.topleft = (x_pos, y_pos)
        elif draw_point == 'topright':
            self.max_hp_bar.topright = (x_pos, y_pos)
        elif draw_point == 'bottomleft':
            self.max_hp_bar.bottomleft = (x_pos, y_pos)
        elif draw_point == 'bottomright':
            self.max_hp_bar.bottomright = (x_pos, y_pos)
        elif draw_point == 'center':
            self.max_hp_bar.center = (x_pos, y_pos)
        self.current_hp_bar = pygame.Rect(
            x_pos, y_pos, hp_width, MAX_HEIGHT)
        self.current_hp_bar.topleft = self.max_hp_bar.topleft

    def draw_text_overlay(self):
        font = pygame.font.Font('resources/fonts/Pixeltype/Pixeltype.ttf', 16)
        hp_overlay_text = font.render(
            f"{self.player.current_stats['hp']}/{self.player.base_stats['hp']}", True, MENU_TEXT_COLOR)
        hp_overlay_rect = hp_overlay_text.get_rect(
            center=(self.max_hp_bar.center[0], self.max_hp_bar.center[1] + 2))
        self.display_surf.blit(hp_overlay_text, hp_overlay_rect)

    def draw(self):
        HP_COLOR = (0, 200, 0)
        if self.player.current_stats['hp'] < .5 * self.player.base_stats['hp']:
            HP_COLOR = 'Yellow'
        if self.player.current_stats['hp'] < .3 * self.player.base_stats['hp']:
            HP_COLOR = 'Red'
        if self.show_background:
            pygame.draw.rect(self.display_surf, 'Black',
                             self.max_hp_bar)
        pygame.draw.rect(self.display_surf, HP_COLOR,
                         self.current_hp_bar)
        if self.show_border:
            pygame.draw.rect(self.display_surf, 'White',
                             self.max_hp_bar, 1)
        if self.text_overlay:
            self.draw_text_overlay()

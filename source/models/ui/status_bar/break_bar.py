import pygame
from source.models.character.character import Character


class BreakBar:
    def __init__(self, player: Character, x_pos, y_pos) -> None:
        self.player = player
        self.display_surf = pygame.display.get_surface()
        MAX_WIDTH = 150
        MAX_HEIGHT = 13
        break_width = (player.break_bar /
                       100) * MAX_WIDTH
        self.max_hp_bar = pygame.Rect(x_pos, y_pos, MAX_WIDTH, MAX_HEIGHT)
        self.current_hp_bar = pygame.Rect(
            x_pos, y_pos, break_width, MAX_HEIGHT)

    def draw(self):
        BREAK_COLOR = (230,150,0)
        pygame.draw.rect(self.display_surf, 'Black',
                         self.max_hp_bar, border_top_right_radius=10, border_bottom_right_radius=10)
        pygame.draw.rect(self.display_surf, BREAK_COLOR,
                         self.current_hp_bar, border_top_right_radius=10, border_bottom_right_radius=10)
        pygame.draw.rect(self.display_surf, 'White', self.max_hp_bar,
                         1, border_top_right_radius=10, border_bottom_right_radius=10)

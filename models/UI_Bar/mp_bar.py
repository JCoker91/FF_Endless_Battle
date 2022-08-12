import pygame
from models.character.character import Character


class MPBar:
    def __init__(self, player: Character, x_pos, y_pos) -> None:
        self.player = player
        self.display_surf = pygame.display.get_surface()
        MAX_WIDTH = 150
        MAX_HEIGHT = 13
        mp_width = (player.current_stats['mp'] /
                    player.base_stats['mp']) * MAX_WIDTH
        self.max_mp_bar = pygame.Rect(x_pos, y_pos, MAX_WIDTH, MAX_HEIGHT)
        self.current_hp_bar = pygame.Rect(x_pos, y_pos, mp_width, MAX_HEIGHT)

    def draw(self):
        MP_COLOR = 'Blue'
        pygame.draw.rect(self.display_surf, 'Black',
                         self.max_mp_bar, border_top_right_radius=10, border_bottom_right_radius=10)
        pygame.draw.rect(self.display_surf, MP_COLOR,
                         self.current_hp_bar, border_top_right_radius=10, border_bottom_right_radius=10)
        pygame.draw.rect(self.display_surf, 'White',
                         self.max_mp_bar, 1, border_top_right_radius=10, border_bottom_right_radius=10)

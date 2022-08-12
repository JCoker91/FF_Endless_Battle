import pygame
from models.character.character import Character


class HPBar:
    def __init__(self, player: Character, x_pos, y_pos) -> None:
        self.player = player
        self.display_surf = pygame.display.get_surface()
        MAX_WIDTH = 150
        MAX_HEIGHT = 13
        hp_width = (player.current_stats['hp'] /
                    player.base_stats['hp']) * MAX_WIDTH
        self.max_hp_bar = pygame.Rect(x_pos, y_pos, MAX_WIDTH, MAX_HEIGHT)
        self.current_hp_bar = pygame.Rect(x_pos, y_pos, hp_width, MAX_HEIGHT)

    def draw(self):
        HP_COLOR = 'Green'
        if self.player.current_stats['hp'] < .5 * self.player.base_stats['hp']:
            HP_COLOR = 'Yellow'
        if self.player.current_stats['hp'] < .3 * self.player.base_stats['hp']:
            HP_COLOR = 'Red'
        pygame.draw.rect(self.display_surf, 'Black',
                         self.max_hp_bar, border_top_right_radius=10, border_bottom_right_radius=10)
        pygame.draw.rect(self.display_surf, HP_COLOR,
                         self.current_hp_bar, border_top_right_radius=10, border_bottom_right_radius=10)
        pygame.draw.rect(self.display_surf, 'White',
                         self.max_hp_bar, 1, border_top_right_radius=10, border_bottom_right_radius=10)

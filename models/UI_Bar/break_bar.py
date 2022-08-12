import pygame
from models.character.character import Character


class BreakBar:
    def __init__(self, player: Character, x_pos, y_pos) -> None:
        self.player = player
        self.display_surf = pygame.display.get_surface()
        MAX_WIDTH = 150
        MAX_HEIGHT = 20
        break_width = (player.current_stats['hp'] /
                    player.base_stats['hp']) * MAX_WIDTH
        self.max_hp_bar = pygame.Rect(x_pos, y_pos, MAX_WIDTH, MAX_HEIGHT)
        self.current_hp_bar = pygame.Rect(x_pos, y_pos, break_width, MAX_HEIGHT)

    def draw(self):
        BREAK_COLOR = 'Yellow'
        pygame.draw.rect(self.display_surf, 'Black', self.max_hp_bar)
        pygame.draw.rect(self.display_surf, BREAK_COLOR, self.current_hp_bar)
        pygame.draw.rect(self.display_surf, 'White', self.max_hp_bar, 3)

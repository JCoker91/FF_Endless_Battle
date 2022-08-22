import pygame
from source.models.character.character import Character
from settings import *


class PlayerTurnIndicator:
    def __init__(self) -> None:
        self.display_surface = pygame.display.get_surface()

    def draw(self, player: Character, width: int = 0):
        x_pos = player.rect.left
        y_pos = player.rect.bottom
        width = player.rect.width
        rect = pygame.Rect(x_pos, y_pos, width, 10)
        pygame.draw.rect(self.display_surface,
                         MENU_BORDER_COLOR, rect, MENU_BORDER_WIDTH, MENU_BORDER_RADIUS)

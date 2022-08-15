import pygame
from settings import *
from source.models.character.character import Character


class CommandMenu:
    def __init__(self) -> None:
        self.display_surface = pygame.display.get_surface()
        self.WIDTH = self.display_surface.get_width()
        self.HEIGHT = int(self.display_surface.get_height() * .3)
        self.font = pygame.font.Font(
            'resources/fonts/Pixeltype/Pixeltype.ttf', 24)
        self.full_menu = pygame.Rect(
            0, self.display_surface.get_height() - self.HEIGHT, self.WIDTH, self.HEIGHT)
        self.left_menu = pygame.Rect(
            0, self.display_surface.get_height() - self.HEIGHT, self.WIDTH * .4, self.HEIGHT)

    def draw(self, player: Character):
        pygame.draw.rect(self.display_surface, MENU_COLOR, self.full_menu)
        pygame.draw.rect(self.display_surface,
                         MENU_BORDER_COLOR, self.full_menu, MENU_BORDER_WIDTH, MENU_BORDER_RADIUS)
        pygame.draw.rect(self.display_surface, MENU_COLOR, self.left_menu)
        pygame.draw.rect(self.display_surface,
                         MENU_BORDER_COLOR, self.left_menu, MENU_BORDER_WIDTH, MENU_BORDER_RADIUS)
        y = (self.display_surface.get_height() - self.HEIGHT) + 30
        x = 50
        player_name_text = self.font.render(player.name, True, 'White')
        action_description_text = "Launches a basic attack at an enemy."
        self.display_surface.blit(player_name_text, (x, y))
        action_description_text_rendered = self.font.render(
            action_description_text, True, 'White')
        self.display_surface.blit(action_description_text_rendered, (275, y))
        y += 25
        divider = pygame.Rect(x - 30, y, 150, 1)
        y += 20
        selected_option = pygame.Rect(x - 30, y, 175, 20)
        selected_option = pygame.Surface((150, 20))
        selected_option.fill('White')
        selected_option.set_alpha(100)
        pygame.draw.rect(self.display_surface, 'White',
                         divider, width=10)
        self.display_surface.blit(selected_option, (x - 30, y - 5))
        for action in player.menu_action:
            action_text = self.font.render(action, True, 'White')
            self.display_surface.blit(action_text, (x, y))
            y += 25

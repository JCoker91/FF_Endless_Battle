import pygame
from source.models.character.character import Character


class PlayerTurnList:
    def __init__(self, player_turn_list: list[Character], starting_x: int, starting_y: int):
        self.display_surface = pygame.display.get_surface()
        self.player_turn_list = player_turn_list
        self.starting_x = starting_x
        self.starting_y = starting_y

    def draw(self):
        x_pos = self.starting_x
        y_pos = self.starting_y
        player_turn = None
        mouse_pos = pygame.mouse.get_pos()
        for i, player in enumerate(self.player_turn_list[:20]):
            icon = player.icon
            if i == 0:
                icon = player.icon
                player_turn = player
            else:
                if player == player_turn:
                    icon = pygame.transform.scale(
                        player.icon, (player.icon.get_width() * .75, player.icon.get_height() * .75))
                else:
                    icon = pygame.transform.scale(
                        player.icon, (player.icon.get_width() * .5, player.icon.get_height() * .5))
            icon_rect = icon.get_rect(topleft=(x_pos, y_pos))
            if icon_rect.collidepoint(mouse_pos):
                icon = pygame.transform.scale(
                    player.icon, (player.icon.get_width(), player.icon.get_height()))
            self.display_surface.blit(icon, icon_rect)
            x_pos += icon.get_width()

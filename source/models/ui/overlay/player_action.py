
import pygame
from settings import *
from source.util.custom_enum import PlayerSide
from source.models.character.character import Character


class PlayerAction(pygame.sprite.Sprite):
    def __init__(self, player: Character, action_name: str = "No Action") -> None:
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(
            'resources/fonts/Pixeltype/Pixeltype.ttf', 24).render(action_name, False, MENU_TEXT_COLOR)
        if player is None:
            self.icon = None
            self.player = None
        else:
            self.player = player
            self.action_name = action_name
            if player.side == PlayerSide.RIGHT:
                self.icon = player.icon
                self.x_pos = SCREEN_WIDTH
            else:
                self.icon = pygame.transform.flip(player.icon, True, False)
                self.x_pos = 0

    def draw(self):
        if self.player is None:
            return
        rect = pygame.Rect(0, 0, SCREEN_WIDTH/2 + 100,
                           self.icon.get_height() + 10)
        rect.bottom = SCREEN_HEIGHT / 4
        if self.player.side == PlayerSide.RIGHT:
            rect.left = self.x_pos
            icon_rect = self.icon.get_rect(
                centery=rect.centery, left=rect.left + 10)
            if self.x_pos > SCREEN_WIDTH / 2:
                self.x_pos -= 30
            font_coordinates = (icon_rect.right + 20, icon_rect.centery)
        elif self.player.side == PlayerSide.LEFT:
            rect.right = self.x_pos
            icon_rect = self.icon.get_rect(
                centery=rect.centery, right=rect.right - 10)
            if self.x_pos < SCREEN_WIDTH / 2:
                self.x_pos += 30
            font_coordinates = (
                icon_rect.left - (self.font.get_width() + 20), icon_rect.centery)

        pygame.draw.rect(self.display_surface, rect=rect, color=MENU_COLOR)
        pygame.draw.rect(self.display_surface, rect=rect, color=MENU_BORDER_COLOR,
                         border_radius=MENU_BORDER_RADIUS, width=MENU_BORDER_WIDTH)
        self.display_surface.blit(self.icon, icon_rect)
        self.display_surface.blit(
            self.font, font_coordinates)

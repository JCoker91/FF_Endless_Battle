import pygame
from settings import *
from source.models.character.character import Character
from source.models.ui.status_bar.hp_bar import HPBar
from source.models.ui.status_bar.mp_bar import MPBar
from source.models.ui.status_bar.break_bar import BreakBar


class DrawTargetInfo:
    def __init__(self) -> None:
        self.display_surface = pygame.display.get_surface()

    def draw(self, player: Character):
        rect_width = self.display_surface.get_width()/2.5
        rect_height = 75
        rect = pygame.Rect(0, 0,rect_width,rect_height)
        rect.top= self.display_surface.get_height()/3.5
        rect.right = self.display_surface.get_width()
        if player:
            pygame.draw.rect(self.display_surface, rect=rect, color=MENU_COLOR)
            pygame.draw.rect(self.display_surface, rect=rect, color=MENU_BORDER_COLOR,
                            border_radius=MENU_BORDER_RADIUS, width=MENU_BORDER_WIDTH)
            icon_rect = player.icon.get_rect()
            icon_rect.centery = rect.centery
            icon_rect.right = self.display_surface.get_width() - MENU_PADDING
            self.display_surface.blit(
                player.icon, icon_rect)
            HPBar(player, icon_rect.left, icon_rect.top, text_overlay=True,draw_point='topright').draw()
            BreakBar(
                player, icon_rect.left, icon_rect.top + 14,text_overlay=True,draw_point='topright').draw()
            MPBar(player, icon_rect.left, icon_rect.top+28,text_overlay=True,draw_point='topright').draw()
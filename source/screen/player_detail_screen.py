from turtle import width
import pygame
from settings import *
from source.util.custom_enum import PlayerSide
from source.models.character.character import Character

class PlayerDetailScreen:
    def __init__(self, player: Character) -> None:
        self.display_surface = pygame.display.get_surface()
        self.display_surf_width = self.display_surface.get_width()
        self.display_surf_height = self.display_surface.get_height()
        self.player = player
    
    def draw_opacity(self):
        opac_rect= pygame.Surface((self.display_surf_width, self.display_surf_height)).convert_alpha()
        opac_rect_rc = opac_rect.get_rect()
        pygame.draw.rect(opac_rect,'Black', opac_rect_rc)
        opac_rect.set_alpha(100)
        self.display_surface.blit(opac_rect,(0,0))
    
    def draw_screen(self):
        width = SCREEN_WIDTH / 2
        height = SCREEN_HEIGHT / 2
        details_screen = pygame.Rect(
            self.display_surf_width/4, self.display_surf_height/4, width, height)
        pygame.draw.rect(self.display_surface, MENU_COLOR, details_screen)
        pygame.draw.rect(self.display_surface,
                         MENU_BORDER_COLOR, details_screen, MENU_BORDER_WIDTH, MENU_BORDER_RADIUS)
        image = self.player.animations['idle'][0]
        if self.player.side == PlayerSide.RIGHT:
            image = pygame.transform.smoothscale(image, (image.get_width() *1.5,image.get_height() * 1.5))
        else:
            image = pygame.transform.smoothscale(image, (image.get_width() *1.5,image.get_height() * 1.5))
            image = pygame.transform.flip(image, True, False)
        self.display_surface.blit(image,((self.display_surf_width/2) - (image.get_width() /2),(self.display_surf_height/2) - (image.get_height() / 2)))

    def draw(self):
        self.draw_opacity()
        self.draw_screen()
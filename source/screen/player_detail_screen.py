from tkinter import XView
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
        self.font = pygame.font.Font(
            'resources/fonts/Pixeltype/Pixeltype.ttf', 24)

    def draw_opacity(self):
        opac_rect = pygame.Surface(
            (self.display_surf_width, self.display_surf_height)).convert_alpha()
        opac_rect_rc = opac_rect.get_rect()
        pygame.draw.rect(opac_rect, 'Black', opac_rect_rc)
        opac_rect.set_alpha(100)
        self.display_surface.blit(opac_rect, (0, 0))

    def draw_screen(self):
        width = SCREEN_WIDTH / 1.2
        height = SCREEN_HEIGHT / 2
        details_screen = pygame.Rect(
            self.display_surf_width/2 - width/2, self.display_surf_height/4, width, height)
        pygame.draw.rect(self.display_surface, MENU_COLOR, details_screen)
        pygame.draw.rect(self.display_surface,
                         MENU_BORDER_COLOR, details_screen, MENU_BORDER_WIDTH, MENU_BORDER_RADIUS)

    def draw_elements(self):
        self.draw_sprite()
        self.draw_name()
        self.draw_stats()

    def draw_sprite(self):
        sprite_image = self.player.animations['idle'][0]
        sprite_image = pygame.transform.smoothscale(
            sprite_image, (sprite_image.get_width() * 1.5, sprite_image.get_height() * 1.5))
        sprite_background = pygame.Rect(
            self.display_surf_width - (SCREEN_WIDTH/3 + MENU_PADDING), self.display_surf_height/4 + MENU_PADDING, sprite_image.get_width() + MENU_PADDING, sprite_image.get_height() + MENU_PADDING)
        sprite_rect = sprite_image.get_rect(center=sprite_background.center)
        pygame.draw.rect(self.display_surface,
                         MENU_SECONDARY_COLOR, sprite_background)
        pygame.draw.rect(self.display_surface, MENU_BORDER_COLOR,
                         sprite_background, MENU_BORDER_WIDTH, MENU_BORDER_RADIUS)
        self.display_surface.blit(sprite_image, sprite_rect)

    def draw_stats(self):
        pass

    def draw_name(self):
        player_name_text = self.font.render(
            self.player.name, True, MENU_TEXT_COLOR)
        player_name_rect = player_name_text.get_rect(
            center=(self.display_surf_width/2, self.display_surf_height/4 + MENU_PADDING))
        self.display_surface.blit(player_name_text, player_name_rect)

    def draw(self):
        self.draw_opacity()
        self.draw_screen()
        self.draw_elements()

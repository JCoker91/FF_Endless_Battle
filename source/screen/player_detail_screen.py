import pygame
from settings import *
from source.models.character.character import Character
from source.models.ui.status_bar.hp_bar import HPBar
from source.models.ui.status_bar.mp_bar import MPBar
from source.models.ui.status_bar.break_bar import BreakBar


class PlayerDetailScreen:
    def __init__(self, player: Character) -> None:
        self.display_surface = pygame.display.get_surface()
        self.display_surf_width = self.display_surface.get_width()
        self.display_surf_height = self.display_surface.get_height()
        self.player = player
        self.col_1 = self.display_surf_width/6
        self.col_2 = self.display_surf_width/2 - MENU_PADDING * 2
        self.menu_screen_width = SCREEN_WIDTH / 1.2
        self.menu_screen_height = SCREEN_HEIGHT / 2.5
        self.details_screen = pygame.Rect(
            self.display_surf_width/2 - self.menu_screen_width/2, self.display_surf_height/4, self.menu_screen_width, self.menu_screen_height)
        self.right_justified_x = self.details_screen.topright[0] - \
            MENU_PADDING * 2
        self.font = pygame.font.Font(
            'resources/fonts/Pixeltype/Pixeltype.ttf', 24)
        self.small_font = pygame.font.Font(
            'resources/fonts/Pixeltype/Pixeltype.ttf', 20)

    def draw_opacity(self):
        opac_rect = pygame.Surface(
            (self.display_surf_width, self.display_surf_height)).convert_alpha()
        opac_rect_rc = opac_rect.get_rect()
        pygame.draw.rect(opac_rect, 'Black', opac_rect_rc)
        opac_rect.set_alpha(100)
        self.display_surface.blit(opac_rect, (0, 0))

    def draw_screen(self):
        pygame.draw.rect(self.display_surface, MENU_COLOR, self.details_screen)
        pygame.draw.rect(self.display_surface,
                         MENU_BORDER_COLOR, self.details_screen, MENU_BORDER_WIDTH, MENU_BORDER_RADIUS)

    def draw_elements(self):
        self.draw_sprite()
        self.draw_name()
        self.draw_stats()
        self.draw_status_bars()
        self.draw_resistances()

    def draw_sprite(self):
        sprite_image = self.player.animations['idle'][0]
        sprite_image = pygame.transform.smoothscale(
            sprite_image, (sprite_image.get_width() * 1.5, sprite_image.get_height() * 1.5))
        sprite_background = pygame.Rect(
            self.display_surf_width - (SCREEN_WIDTH/3 + MENU_PADDING), self.display_surf_height/4 + MENU_PADDING, sprite_image.get_width() + MENU_PADDING, sprite_image.get_height() + MENU_PADDING)
        sprite_background.topright = (
            self.right_justified_x, self.details_screen.topright[1] + MENU_PADDING * 2)
        sprite_rect = sprite_image.get_rect(center=sprite_background.center)
        pygame.draw.rect(self.display_surface,
                         MENU_SECONDARY_COLOR, sprite_background)
        pygame.draw.rect(self.display_surface, MENU_BORDER_COLOR,
                         sprite_background, MENU_BORDER_WIDTH, MENU_BORDER_RADIUS)
        self.display_surface.blit(sprite_image, sprite_rect)

    def draw_stats(self):
        labels = ['STRENGTH', 'MAGIC', 'DEFENSE', 'MAGIC DEFENSE', 'SPEED']
        player_stats = [self.player.current_stats['strength'], self.player.current_stats['magic'],
                        self.player.current_stats['defense'], self.player.current_stats['magic_defense'], self.player.current_stats['speed']]
        y_offset = 40
        for i, label in enumerate(labels):
            y_pos = (self.display_surf_height/4 +
                     MENU_PADDING * 2 + y_offset)
            label_text = self.font.render(label, True, MENU_TEXT_COLOR)
            label_rect = label_text.get_rect(topleft=(self.col_1, y_pos))
            player_stat_text = self.font.render(
                str(player_stats[i]), True, MENU_TEXT_COLOR)
            player_stat_rect = player_stat_text.get_rect(
                topleft=(self.col_2, y_pos))
            y_offset += MENU_PADDING
            self.display_surface.blit(label_text, label_rect)
            self.display_surface.blit(player_stat_text, player_stat_rect)

    def draw_status_bars(self):
        HPBar(self.player, self.right_justified_x,
              400, True, draw_point='topright').draw()
        MPBar(self.player, self.right_justified_x,
              425, True, draw_point='topright').draw()
        BreakBar(self.player, self.right_justified_x, 450,
                 True, draw_point='topright').draw()

    def draw_resistances(self):
        resistance_list = [
            'fire',
            'lightning',
            'ice',
            'wind',
            'water',
            'earth',
            'light',
            'dark',
        ]
        x_pos = self.col_1
        for element in resistance_list:
            text_color = MENU_TEXT_COLOR
            if self.player.current_resistance[element] < 0:
                text_color = 'Red'
            if self.player.current_resistance[element] > 0:
                text_color = 'Green'
            resistance_icon = pygame.image.load(
                f'resources/images/icons/elements/{element}.png').convert_alpha()
            resistance_text = self.small_font.render(
                f"{self.player.current_resistance[element]}%", False, text_color)
            resistance_text_rect = resistance_text.get_rect(
                center=(x_pos, 410))
            resistance_icon_rect = resistance_icon.get_rect(
                center=(resistance_text_rect.centerx, 440))
            self.display_surface.blit(resistance_icon, resistance_icon_rect)
            self.display_surface.blit(resistance_text, resistance_text_rect)
            x_pos += 35

    def draw_name(self):
        player_name_text = self.font.render(
            self.player.name, True, MENU_TEXT_COLOR)
        player_name_rect = player_name_text.get_rect(
            topleft=(self.col_1, self.display_surf_height/4 + MENU_PADDING * 2))
        self.display_surface.blit(player_name_text, player_name_rect)

    def draw(self):
        self.draw_opacity()
        self.draw_screen()
        self.draw_elements()

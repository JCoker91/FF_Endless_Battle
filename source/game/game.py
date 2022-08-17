from distutils.log import debug
import pygame
from settings import *
from random import choice
from source.util.custom_enum import PlayerSide
from source.models.ui.status_bar.break_bar import BreakBar
from source.models.ui.status_bar.mp_bar import MPBar
from source.models.ui.status_bar.hp_bar import HPBar
from source.models.ui.menu.menu import CommandMenu
from source.models.abilities.abilities import basic_attack
from source.models.character.character import Character
from source.screen.player_detail_screen import PlayerDetailScreen
from source.game.load_characters import load_characters
from source.util.debug import debug
from source.models.sprite_groups.sprite_groups import YSortedGroup
from source.models.ui.overlay.player_hp import PlayerHP


class Game:
    def __init__(self) -> None:
        pygame.init()
        # screen setup
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        # sprite group setup
        self.players_group = YSortedGroup()
        self.particles_group = pygame.sprite.Group()
        self.floating_text_group = pygame.sprite.Group()

        # clock and timer setup
        self.mouse_click_timer = pygame.time.get_ticks()
        self.get_next_player_timer = pygame.time.get_ticks()
        self.can_click = True  # used with the mouse timer
        self.attack_animation_time = 0
        self.get_next_player = True  # used with get next player timer
        self.clock = pygame.time.Clock()

        # game variable setup
        # determines which player is focused on either side
        self.left_focused = None
        self.right_focused = None
        self.selection_arrow = self.create_selection_arrow()
        self.showing_player_details = False
        self.showing_player = None
        self.player_turn = None
        self.player_turn_list = []

    def run(self):
        load_characters(self.players_group)
        command_menu = CommandMenu()
        background = self.load_background()
        pygame.display.set_caption("Final Fantasy Endless Battle")

        while True:
            self.screen.blit(background, (0, 0))
            self.process_events(players_group=self.players_group)
            self.get_player_turn_list()
            self.run_enemy_action()
            # self.draw_status_bars(players_group=self.players_group)
            self.update_groups()
            self.draw_groups()
            command_menu.draw(self.players_group.sprites()[0])
            self.check_for_player_focus()
            self.display_turn_list()
            self.show_player_details_screen()
            self.cool_downs()
            debug(self.player_turn)
            pygame.display.update()
            self.clock.tick(FPS)

    def load_background(self):
        background = pygame.image.load(
            'resources/images/backgrounds/water_temple.png').convert()
        return background

    def run_enemy_action(self):
        if self.player_turn:
            if self.player_turn.side == PlayerSide.RIGHT and not self.player_turn.is_attacking:
                self.left_focused = choice(list(filter(
                    lambda player: player.side == PlayerSide.LEFT, self.players_group.sprites())))
                basic_attack(self.player_turn, self.left_focused,
                             self.particles_group, self.floating_text_group)
                self.get_next_player_timer = pygame.time.get_ticks()
                self.get_next_player = False
                self.attack_animation_time = self.player_turn.attack_animation_time

    def get_player_turn_list(self):
        def get_turn_count(player):
            return player.turn_count
        if not self.player_turn and self.get_next_player:
            for player in self.players_group.sprites():
                player.turn_count += player.current_stats['speed']
            self.player_turn_list = list(filter(
                lambda player: not player.has_fallen, self.players_group.sprites()))
            self.player_turn_list.sort(key=get_turn_count, reverse=True)
            self.player_turn = self.player_turn_list[0]
            if self.player_turn.is_broken:
                self.player_turn.is_broken = False
                self.player_turn.break_bar = 100

    def display_turn_list(self):
        x = SCREEN_WIDTH / 4
        y = 10
        for i, player in enumerate(self.player_turn_list):
            icon = player.icon
            if self.player_turn == player:
                icon = pygame.transform.scale(
                    player.icon, (player.icon.get_width() * 1.25, player.icon.get_height() * 1.25))
            else:
                icon = pygame.transform.scale(
                    player.icon, (player.icon.get_width() * (1 - (i * .05)), player.icon.get_height() * (1 - (i * .05))))
            icon_rect = icon.get_rect(topright=(x, y))
            self.screen.blit(icon, icon_rect)
            x += icon.get_width()

    def create_selection_arrow(self):
        selection_arrow = pygame.image.load(
            'resources/images/misc/arrows/menu_arrow.png')
        selection_arrow = pygame.transform.rotate(selection_arrow, -90.0)
        return selection_arrow

    def update_groups(self):
        self.players_group.update()
        self.particles_group.update()
        self.floating_text_group.update()

    def draw_groups(self):
        self.players_group.draw(self.screen)
        self.particles_group.draw(self.screen)
        hp_bars = PlayerHP(self.players_group.sprites())
        hp_bars.draw()
        self.floating_text_group.draw(self.screen)

    def check_for_player_focus(self):
        left_x_offset = 20
        left_y_offset = -110
        right_x_offset = -50
        right_y_offset = -110
        selection_arrow = self.create_selection_arrow()
        for player in self.players_group:
            if self.left_focused == player or self.right_focused == player:
                player.is_focused = True
            else:
                player.is_focused = False
            if player.has_fallen:
                player.is_focused = False
        if self.left_focused:
            if self.left_focused.has_fallen:
                self.left_focused = None
            # else:
            #     self.screen.blit(selection_arrow,
            #                      (self.left_focused.starting_spot[0] + left_x_offset, self.left_focused.starting_spot[1] + left_y_offset))
        if self.right_focused:
            if self.right_focused.has_fallen:
                self.right_focused = None
            else:
                self.screen.blit(selection_arrow,
                                 (self.right_focused.starting_spot[0] + right_x_offset, self.right_focused.starting_spot[1] + right_y_offset))

    def cool_downs(self):
        if not self.can_click:
            timer = pygame.time.get_ticks()
            if timer - self.mouse_click_timer > 300:
                self.can_click = True
        if not self.get_next_player:
            timer = pygame.time.get_ticks()
            if timer - self.get_next_player_timer > self.attack_animation_time:
                self.get_next_player = True
                self.player_turn.turn_count = 0
                self.player_turn = None

    def draw_status_bars(self, players_group: pygame.sprite.Group):
        left_y_offset = 10
        right_y_offset = 10
        left_x_offset = 70
        right_x_offset = self.screen.get_width() - 225

        for player in players_group:
            if player.icon is not None:
                if player.side == PlayerSide.RIGHT:
                    self.screen.blit(
                        player.icon, (self.screen.get_width() - 66, right_y_offset))
                    hp_bar = HPBar(player, right_x_offset, right_y_offset)
                    break_bar = BreakBar(
                        player, right_x_offset, right_y_offset+14)
                    mp_bar = MPBar(player, right_x_offset, right_y_offset+28)
                    hp_bar.draw()
                    break_bar.draw()
                    mp_bar.draw()
                    right_y_offset += 60
                else:
                    self.screen.blit(pygame.transform.flip(
                        player.icon, 1, 0), (10, left_y_offset))
                    hp_bar = HPBar(player, left_x_offset, left_y_offset)
                    break_bar = BreakBar(
                        player, left_x_offset, left_y_offset + 14)
                    mp_bar = MPBar(player, left_x_offset, left_y_offset + 28)
                    hp_bar.draw()
                    break_bar.draw()
                    mp_bar.draw()
                    left_y_offset += 60

    def process_events(self, players_group: pygame.sprite.Group):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.showing_player_details:
                    width = SCREEN_WIDTH / 2
                    height = SCREEN_HEIGHT / 2
                    details_screen = pygame.Rect(
                        self.screen.get_width()/4, self.screen.get_height()/4, width, height)
                    if not details_screen.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                        self.showing_player_details = 0
                        self.showing_player = None

                else:
                    for player in players_group.sprites():
                        if player.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                            if self.can_click:
                                if self.left_focused == player or self.right_focused == player:
                                    self.showing_player_details = True
                                    self.showing_player = player
                                else:
                                    if player.side == PlayerSide.LEFT:
                                        self.left_focused = player
                                    else:
                                        self.right_focused = player
                                    self.can_click = False
                                    self.mouse_click_timer = pygame.time.get_ticks()

            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
                if event.key == pygame.K_j:
                    if self.left_focused and self.right_focused:
                        basic_attack(self.right_focused,
                                     self.left_focused, self.particles_group, self.floating_text_group)
                if event.key == pygame.K_f:
                    if self.left_focused and self.right_focused:
                        basic_attack(self.left_focused,
                                     self.right_focused, self.particles_group, self.floating_text_group)
                if event.key == pygame.K_SPACE:
                    if self.player_turn:
                        if not self.player_turn.is_attacking:
                            if self.player_turn.side == PlayerSide.LEFT:
                                if self.right_focused:
                                    basic_attack(self.player_turn,
                                                 self.right_focused, self.particles_group, self.floating_text_group)
                                    self.get_next_player_timer = pygame.time.get_ticks()
                                    self.get_next_player = False
                                    # self.player_turn.turn_count = 0
                                    self.attack_animation_time = self.player_turn.attack_animation_time

                            else:
                                if self.left_focused:
                                    basic_attack(self.player_turn,
                                                 self.left_focused, self.particles_group, self.floating_text_group)
                                    self.get_next_player_timer = pygame.time.get_ticks()
                                    self.get_next_player = False
                                    # self.player_turn.turn_count = 0
                                    self.attack_animation_time = self.player_turn.attack_animation_time

    def show_player_details_screen(self):
        if self.showing_player_details:
            player_details_screen = PlayerDetailScreen(self.showing_player)
            player_details_screen.draw()
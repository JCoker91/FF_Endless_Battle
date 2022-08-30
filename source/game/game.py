from distutils.log import debug
import pygame
from settings import *
from random import choice
from source.models.ui.overlay import player_turn_indicator
from source.util.custom_enum import CurrentState, PlayerSide
from source.models.ui.status_bar.break_bar import BreakBar
from source.models.ui.status_bar.mp_bar import MPBar
from source.models.ui.status_bar.hp_bar import HPBar
from source.models.ui.overlay.player_turn_list import PlayerTurnList
from source.models.ui.menu.menu import CommandMenu
from source.models.character.character import Character
from source.screen.player_detail_screen import PlayerDetailScreen
from source.game.load_characters import load_characters, load_single
from source.util.debug import debug
from source.models.ui.overlay.player_action import PlayerAction
from source.models.sprite_groups.sprite_groups import YSortedGroup
from source.models.ui.overlay.player_hp import PlayerHP
from source.models.ui.overlay.draw_target_info import DrawTargetInfo
from source.models.ui.overlay.player_turn_indicator import PlayerTurnIndicator


class Game:
    def __init__(self) -> None:
        pygame.init()
        # screen setup
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        # sprite group setup
        self.players_group = YSortedGroup()
        self.particles_group = pygame.sprite.Group()
        self.floating_text_group = pygame.sprite.Group()

        # Command passing
        self.command_menu = CommandMenu()
        self.action_command = None

        # clock and timer setup
        self.mouse_click_timer = pygame.time.get_ticks()
        self.get_next_player_timer = pygame.time.get_ticks()
        self.player_turn_indicator = PlayerTurnIndicator()
        self.turn_buffer_timer = pygame.time.get_ticks()
        self.can_click = True  # used with the mouse timer
        self.attack_animation_time = 0
        self.get_next_player = True  # used with get next player timer
        self.clock = pygame.time.Clock()
        self.double_click_clock = pygame.time.Clock()
        self.left_staging_area = (275,500)
        self.right_staging_area = (400,500)

        # game variable setup
        # determines which player is focused on either side
        self.left_focused = None
        self.right_focused = None

        self.limit_break_happening = False
        self.selection_arrow = self.create_selection_arrow()
        self.showing_player_details = False
        self.showing_player = None
        self.player_action = None
        self.player_turn = None
        self.player_turn_list = []

    def run(self):
        load_characters(self.players_group,
                        self.floating_text_group, self.particles_group)
        # load_single('Tidus',self.players_group,
        #                 self.floating_text_group, self.particles_group)

        background = self.load_background()
        pygame.display.set_caption("Final Fantasy Endless Battle")

        while True:
            self.screen.blit(background, (0, 0))
            self.process_events(players_group=self.players_group)
            self.process_commands()
            self.get_player_turn_list()
            self.get_player_turn()
            self.run_enemy_action()
            self.update_groups()
            self.draw_opacity()
            self.draw_groups()

            self.check_for_player_focus()
            self.show_player_details_screen()
            self.cool_downs()

            # debug(self.player_turn_indicator.r_dir)
            pygame.display.update()
            self.clock.tick(FPS)

    def draw_opacity(self):
        opac_rect = pygame.Surface(
            (self.screen.get_width(), self.screen.get_height())).convert_alpha()
        opac_rect_rc = opac_rect.get_rect()
        pygame.draw.rect(opac_rect, 'Black', opac_rect_rc)
        opac_rect.set_alpha(100)
        if self.limit_break_happening:
            self.screen.blit(opac_rect, (0, 0))

    def load_background(self):
        background = pygame.image.load(
            'resources/images/backgrounds/water_temple.png').convert()
        return background

    def run_enemy_action(self):
        if self.player_turn:
            if self.player_turn.side == PlayerSide.RIGHT and not self.player_turn.is_attacking and self.attack_animation_time == 0:
                self.player_turn.rect.bottomright = self.right_staging_area
                self.left_focused = choice(list(filter(
                    lambda player: player.side == PlayerSide.LEFT, self.players_group.sprites())))
                self.player_turn.attack['attack'].execute(
                    self.player_turn, self.left_focused)
                self.get_next_player_timer = pygame.time.get_ticks()
                self.get_next_player = False
                self.attack_animation_time = self.player_turn.attack_animation_time + TURN_BUFFER
                self.player_action = PlayerAction(action_name=self.player_turn.attack['attack'].name,
                                                  player=self.player_turn)

    def get_player_turn_list(self):
        def get_player_speed(player):
            return player.current_stats['speed']
        player_speed_list = list(filter(
            lambda player: not player.has_fallen, self.players_group.sprites()))
        player_speed_list = self.players_group.sprites()

        player_speed_list.sort(key=get_player_speed, reverse=True)

        for player in player_speed_list:
            player.turn_count += player.current_stats['speed']
            if player.turn_count >= TURN_COUNT_LIMIT:
                if len(self.player_turn_list) < 999:
                    self.player_turn_list.append(player)
                player.turn_count -= TURN_COUNT_LIMIT
        remove_player = []
        for i, player in enumerate(self.player_turn_list):
            if player.has_fallen:
                remove_player.append(i)
        for player in reversed(remove_player):
            self.player_turn_list.pop(player)

    def get_player_turn(self):
        if len(self.player_turn_list) > 0 and self.player_turn is None:
            self.player_turn = self.player_turn_list[0]
            self.player_update_status(self.player_turn)
            if self.player_turn.is_broken:
                self.player_turn.is_broken = False
                self.player_turn.break_bar = 100

    def player_update_status(self, player):
        player.current_stats['mp'] += player.current_stats['mp_regen']
        if player.current_stats['mp'] > player.base_stats['mp']:
            player.current_stats['mp'] = player.base_stats['mp']

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
        if self.player_turn:
            self.player_turn_indicator.draw(self.player_turn)
        self.players_group.draw(self.screen)
        self.particles_group.draw(self.screen)
        PlayerTurnList(self.player_turn_list, 10, 10).draw()
        PlayerHP(self.players_group.sprites()).draw()
        mouse_pos = pygame.mouse.get_pos()
        draw_player = self.right_focused
        for player in self.players_group.sprites():
            if player.rect.collidepoint(mouse_pos):
                draw_player = player

        DrawTargetInfo().draw(draw_player)
        action_command = self.command_menu.draw(self.player_turn)
        if action_command and self.get_next_player and self.right_focused:
            self.action_command = action_command
        if self.player_action:
            self.player_action.draw()

        self.floating_text_group.draw(self.screen)

    def process_commands(self):
        if self.action_command:
            if self.action_command == 'attack':
                if self.player_turn:
                    if not self.player_turn.is_attacking:
                        if self.player_turn.side == PlayerSide.LEFT:
                            if self.right_focused:
                                self.player_turn.rect.bottomleft = self.left_staging_area
                                self.player_turn.attack['attack'].execute(
                                    self.player_turn, self.right_focused)
                                self.get_next_player_timer = pygame.time.get_ticks()
                                self.get_next_player = False
                                self.player_action = PlayerAction(
                                    action_name=self.player_turn.attack['attack'].name, player=self.player_turn)
                                self.attack_animation_time = self.player_turn.attack_animation_time + TURN_BUFFER
                                self.action_command = None
            elif self.action_command.startswith('skill_'):
                if self.player_turn:
                    if not self.player_turn.is_attacking:
                        if self.player_turn.side == PlayerSide.LEFT:
                            if self.player_turn.skills[self.action_command].target_count == 'single':
                                if self.right_focused:
                                    self.player_turn.rect.bottomleft = self.left_staging_area
                                    self.player_turn.skills[self.action_command].execute(
                                        self.player_turn, self.right_focused)
                                    self.get_next_player_timer = pygame.time.get_ticks()
                                    self.get_next_player = False
                                    self.player_action = PlayerAction(
                                        action_name=self.player_turn.skills[self.action_command].name, player=self.player_turn)
                                    self.attack_animation_time = self.player_turn.attack_animation_time + TURN_BUFFER
                                    self.action_command = None
                            elif self.player_turn.skills[self.action_command].target_count == 'all':
                                enemy_list = list(filter(lambda player: player.side ==
                                                         PlayerSide.RIGHT, self.players_group))
                                self.player_turn.skills[self.action_command].execute(
                                    self.player_turn, enemy_list)
                                self.get_next_player_timer = pygame.time.get_ticks()
                                self.get_next_player = False
                                self.player_action = PlayerAction(
                                    action_name=self.player_turn.skills[self.action_command].name, player=self.player_turn)
                                self.attack_animation_time = self.player_turn.attack_animation_time + TURN_BUFFER
                                self.action_command = None
            elif self.action_command == 'limit_break':
                if self.player_turn:
                    self.limit_break_happening = True
                    if not self.player_turn.is_limit_breaking:
                        if self.player_turn.side == PlayerSide.LEFT:
                            if self.player_turn.limit_break['limit_break'].target_count == 'single':
                                if self.right_focused:
                                    self.player_turn.rect.bottomleft = self.left_staging_area
                                    self.player_turn.limit_break['limit_break'].execute(self.player_turn,self.right_focused)
                                    self.get_next_player_timer = pygame.time.get_ticks()
                                    self.get_next_player = False
                                    self.player_action = PlayerAction(action_name=self.player_turn.limit_break['limit_break'].name, player=self.player_turn)
                                    self.attack_animation_time = self.player_turn.limit_break_animation_time + TURN_BUFFER
                                    self.action_command = None

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
        if self.right_focused:
            if self.right_focused.has_fallen:
                self.right_focused = None
            else:
                self.screen.blit(selection_arrow,
                                 (self.right_focused.starting_spot[0] + right_x_offset, self.right_focused.starting_spot[1] + right_y_offset))

    def cool_downs(self):
        if not self.can_click:
            timer = pygame.time.get_ticks()
            if timer - self.mouse_click_timer > MOUSE_CLICK_TIMER:
                self.can_click = True
        if not self.get_next_player:
            timer = pygame.time.get_ticks()
            self.turn_adjust()
            if timer - self.get_next_player_timer > self.attack_animation_time:
                if self.player_turn.side == PlayerSide.LEFT:
                    self.player_turn.rect.bottomleft = self.player_turn.starting_spot
                if self.player_turn.side == PlayerSide.RIGHT:
                    self.player_turn.rect.bottomright = self.player_turn.starting_spot
                self.player_action = None
                self.player_turn.turn_count = 0
                self.player_turn = None
                self.turn_buffer_timer = pygame.time.get_ticks()
                self.get_next_player = True
                self.player_turn_list.pop(0)
                self.attack_animation_time = 0
                self.limit_break_happening = False
                

    def turn_adjust(self):
        for player in self.players_group.sprites():
            if player.turn_adjust == BREAK_TURN_ADJUST:
                self.turn_adjust_break(player)
            if player.turn_adjust == INSTANT_TURN_ADJUST:
                self.turn_adjust_instant(player)
            if player.turn_adjust != 0:
                insert_index = []
                for i, _player in enumerate(self.player_turn_list):
                    if _player == player and i != 0:
                        self.player_turn_list.pop(i)
                        insert_index.append(i)
                for index in insert_index:
                    self.player_turn_list.insert(
                        index - player.turn_adjust, player)
                player.turn_adjust = 0

    def turn_adjust_break(self, player):
        for i, _player in enumerate(self.player_turn_list):
            if _player == player and i != 0:
                self.player_turn_list.pop(i)
                player.turn_adjust = 0
                break

    def turn_adjust_instant(self, player):
        self.player_turn_list.insert(1, player)
        player.turn_adjust = 0

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
                    if self.double_click_clock.tick() < DOUBLE_CLICK_TIME:
                        for player in players_group.sprites():
                            if player.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                                self.showing_player_details = True
                                self.showing_player = player
                    else:
                        for player in players_group.sprites():
                            if player.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                                if self.can_click:
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
                # if event.key == pygame.K_f:
                #     for player in players_group.sprites():
                #         if player.current_state == CurrentState.IDLE:
                #             player.switch_animation(CurrentState.DEAD)
                #         else: player.switch_animation(CurrentState.IDLE)


    def show_player_details_screen(self):
        if self.showing_player_details:
            player_details_screen = PlayerDetailScreen(self.showing_player)
            player_details_screen.draw()

from re import L, fullmatch
import pygame
from settings import *
from source.models.character.character import Character
from source.util.custom_enum import PlayerSide


class CommandMenu:
    def __init__(self) -> None:
        self.display_surface = pygame.display.get_surface()
        self.WIDTH = self.display_surface.get_width()
        self.showing_main_menu = True
        self.can_click = True
        self.mouse_click_timer = pygame.time.get_ticks()
        self.current_player = None
        self.HEIGHT = int(self.display_surface.get_height() * .3)
        self.font = pygame.font.Font(
            'resources/fonts/Pixeltype/Pixeltype.ttf', 24)

        self.left_menu = pygame.Rect(
            0, self.display_surface.get_height() - self.HEIGHT, self.WIDTH * .4, self.HEIGHT)
        self.action_commands = {
            'attack': {'label': 'ATTACK', 'description': 'Launches a basic attack at an enemy.', 'is_selected': False, 'is_hovered': False, 'mp_cost': 0},
            'skills': {'label': 'SKILLS', 'description': 'Special skills unique to each character.', 'is_selected': False, 'is_hovered': False, 'mp_cost': 0},
            'defend': {'label': 'DEFEND', 'description': 'Enter a defensive stance reducing damage taken by 50\% until next turn.', 'is_selected': False, 'is_hovered': False, 'mp_cost': 0},
            'item': {'label': 'ITEM', 'description': 'Use an item in stock.', 'is_selected': False, 'is_hovered': False, 'mp_cost': 0},
            'limit_break': {'label': 'LIMIT BREAK', 'description': 'Uses limit break against an enemy.', 'is_selected': False, 'is_hovered': False, 'mp_cost': 0}
        }
        self.skill_commands = {}

    def draw(self, player: Character):
        return_value = None
        self.draw_menu_background()
        if player is not None and player.side == PlayerSide.LEFT:
            if self.current_player !=  player:
                self.showing_main_menu = True
                self.current_player = player
                for skill in player.skills:
                    self.skill_commands[skill] = {'label': player.skills[skill].name,
                                            'description': player.skills[skill].description, 'is_selected': False, 'is_hovered': False, 'mp_cost': player.skills[skill].mp_cost}
            if self.showing_main_menu:
                return_value = self.draw_main_menu(player)
            else:
                return_value = self.draw_skill_menu(player)
        self.mouse_click_cooldown()
        return return_value
    
    def mouse_click_cooldown(self):
        if not self.can_click:
            timer = pygame.time.get_ticks()
            if timer - self.mouse_click_timer > MOUSE_CLICK_TIMER:
                self.can_click = True


    def draw_main_menu(self, player: Character):
        # self.action_commands = {
        #     'attack': {'label': 'ATTACK', 'description': 'Launches a basic attack at an enemy.', 'is_selected': False, 'is_hovered': False, 'mp_cost': 0},
        #     'skills': {'label': 'SKILLS', 'description': 'Special skills unique to each character.', 'is_selected': False, 'is_hovered': False, 'mp_cost': 0},
        #     'defend': {'label': 'DEFEND', 'description': 'Enter a defensive stance reducing damage taken by 50\% until next turn.', 'is_selected': False, 'is_hovered': False, 'mp_cost': 0},
        #     'item': {'label': 'ITEM', 'description': 'Use an item in stock.', 'is_selected': False, 'is_hovered': False, 'mp_cost': 0},
        #     'limit_break': {'label': 'LIMIT BREAK', 'description': 'Uses limit break against an enemy.', 'is_selected': False, 'is_hovered': False, 'mp_cost': 0}
        # }
        limit_break_ready = player.limit_break_gauge >= 100
        pygame.draw.rect(self.display_surface, MENU_COLOR, self.left_menu)
        pygame.draw.rect(self.display_surface,
                         MENU_BORDER_COLOR, self.left_menu, MENU_BORDER_WIDTH, MENU_BORDER_RADIUS)
        y = (self.display_surface.get_height() - self.HEIGHT) + 30
        x = 50
        player_name_text = self.font.render(player.name, True, 'White')
        self.display_surface.blit(player_name_text, (x, y))
        y += 25
        divider = pygame.Rect(x - 30, y, 150, 1)
        y += 20
        pygame.draw.rect(self.display_surface, 'White',
                         divider, width=10)
        mouse_pos = pygame.mouse.get_pos()
        mouse_clicked = pygame.mouse.get_pressed()[0]

        for command in self.action_commands:
            self.action_commands[command]['is_hovered'] = False
            if command == 'limit_break':
                if limit_break_ready:
                    self.draw_menu_item(self.action_commands,
                        command, mouse_pos, mouse_clicked, 100, y, text_color='Green')
                else:
                    self.draw_menu_item(self.action_commands,
                        command, mouse_pos, mouse_clicked, 100, y, disabled=True)
            else:
                self.draw_menu_item(self.action_commands,command, mouse_pos,
                                    mouse_clicked, 100, y)
            y += 25

        action_description_text = ""
        for command in self.action_commands:
            if self.action_commands[command]['is_hovered']:
                action_description_text = self.action_commands[command]['description']
        action_description_text_rendered = self.font.render(
            action_description_text, True, 'White')
        self.display_surface.blit(
            action_description_text_rendered, (275, (self.display_surface.get_height() - self.HEIGHT) + 30))
        for _command in self.action_commands:
            if self.action_commands[_command]['is_selected']:
                self.action_commands[_command]['is_selected'] = False
                if _command == 'skills':
                    self.showing_main_menu = False
                    self.can_click = False
                    self.mouse_click_timer = pygame.time.get_ticks()
                else:
                    self.can_click = False
                    self.mouse_click_timer = pygame.time.get_ticks()
                    return _command

    def draw_menu_item(self, action_dict: dict, command: dict, mouse_pos: tuple, mouse_pressed: bool, x_pos: int, y_pos: int, text_color=MENU_TEXT_COLOR, disabled: bool = False, draw_mp_cost: bool = False):
        if disabled:
            text_color = 'Grey'
        command_text = self.font.render(
            action_dict[command]['label'], True, text_color)
        mp_text = self.font.render(
            str(action_dict[command]['mp_cost']).upper(), True, text_color)
        mp_text_rect = mp_text.get_rect(topleft=(250,y_pos))
        mp_text_rect.inflate_ip(100,10)
        command_text_rect = command_text.get_rect(topleft=(x_pos, y_pos))
        command_text_rect.inflate_ip(100, 10)
        selected_option = pygame.Surface((150, 20))
        selected_option.fill('White')
        selected_option.set_alpha(100)
        selected_option_rect = selected_option.get_rect()

        if action_dict[command]['is_selected']:
            selected_option_rect.topleft = (
                (command_text_rect.topleft[0] - 20, command_text_rect.topleft[1] - 5))
            self.display_surface.blit(selected_option, selected_option_rect)

        # define hover behavior
        if command_text_rect.collidepoint(mouse_pos):
            if mouse_pressed and not disabled:
                for _command in action_dict:
                    action_dict[_command]['is_selected'] = False
                action_dict[command]['is_selected'] = True
                self.can_click = False
                self.mouse_click_timer = pygame.time.get_ticks()

            else:
                action_dict[command]['is_hovered'] = True
                selected_option_rect.topleft = (
                    (command_text_rect.topleft[0] - 20, command_text_rect.topleft[1] - 5))
                self.display_surface.blit(
                    selected_option, selected_option_rect)
        hovered = False
        for _command in action_dict:
            if action_dict[_command]['is_hovered']:
                hovered = True
                break
        if not hovered:
            for _command in action_dict:
                if action_dict[_command]['is_selected']:
                    action_dict[_command]['is_hovered'] = True
                    break
        self.display_surface.blit(command_text, command_text_rect)
        if draw_mp_cost:
            self.display_surface.blit(mp_text, mp_text_rect)


    def draw_menu_background(self):
        full_menu_border = pygame.Rect(
            0, self.display_surface.get_height() - self.HEIGHT, self.WIDTH, self.HEIGHT)
        full_menu = pygame.Surface(size=(self.WIDTH, self.HEIGHT))
        full_menu.fill(MENU_SECONDARY_COLOR)
        self.display_surface.blit(
            full_menu, (0, self.display_surface.get_height() - self.HEIGHT))
        pygame.draw.rect(self.display_surface,
                         MENU_BORDER_COLOR, full_menu_border, MENU_BORDER_WIDTH, MENU_BORDER_RADIUS)

    def draw_skill_menu(self, player):
        for skill in player.skills:
            self.skill_commands[skill] = {'label': player.skills[skill].name,
                                     'description': player.skills[skill].description, 'is_selected': False, 'is_hovered': False, 'mp_cost': player.skills[skill].mp_cost}
        pygame.draw.rect(self.display_surface, MENU_COLOR, self.left_menu)
        pygame.draw.rect(self.display_surface,
                         MENU_BORDER_COLOR, self.left_menu, MENU_BORDER_WIDTH, MENU_BORDER_RADIUS)
        y = (self.display_surface.get_height() - self.HEIGHT) + 30
        x = 50
        player_name_text = self.font.render('Skills', True, 'White')
        self.display_surface.blit(player_name_text, (x, y))
        y += 25
        divider = pygame.Rect(x - 30, y, 150, 1)
        y += 20
        pygame.draw.rect(self.display_surface, 'White',
                         divider, width=10)
        mouse_pos = pygame.mouse.get_pos()
        mouse_clicked = pygame.mouse.get_pressed()[0]

        for command in self.skill_commands:
            self.skill_commands[command]['is_hovered'] = False

            if player.current_stats['mp'] - self.skill_commands[command]['mp_cost'] < 0:
                self.draw_menu_item(self.skill_commands,command, mouse_pos,
                                    mouse_clicked, 100, y, disabled=True, draw_mp_cost=True)
            else:
                self.draw_menu_item(self.skill_commands,command, mouse_pos,
                                    mouse_clicked, 100, y, draw_mp_cost=True)
            y += 25
        self.skill_commands['back'] = {'label': 'BACK', 'description': 'Back to main menu.',
                                        'is_selected': False, 'is_hovered': False, 'mp_cost': 0}
        self.draw_menu_item(self.skill_commands,'back', mouse_pos, mouse_clicked,
                            100, self.display_surface.get_height()-50)
        action_description_text = ""
        for command in self.skill_commands:
            if self.skill_commands[command]['is_hovered']:
                action_description_text = self.skill_commands[command]['description']
        action_description_text_rendered = self.font.render(
            action_description_text, True, 'White')
        self.display_surface.blit(
            action_description_text_rendered, (275, (self.display_surface.get_height() - self.HEIGHT) + 30))
        if self.can_click:
            for _command in self.skill_commands:
                if self.skill_commands[_command]['is_selected']:
                
                    self.skill_commands[_command]['is_selected'] = False
                    if self.skill_commands[_command]['label'] == 'BACK':
                        self.showing_main_menu = True
                        # self.can_click = False
                        # self.mouse_click_timer = pygame.time.get_ticks()
                    else:
                        # self.can_click = False
                        # self.mouse_click_timer = pygame.time.get_ticks()
                        return _command
                    

from re import L
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
        self.action_commands = {
            'attack': {'label':'ATTACK', 'is_selected' : False},
            'skills' : {'label':'SKILLS', 'is_selected' : False}, 
            'defend': {'label': 'DEFEND', 'is_selected' : False}, 
            'item' : {'label': 'ITEM', 'is_selected' : False}, 
            'limit_break' : {'label' : 'LIMIT BREAK', 'is_selected' : False}
            }


    def draw(self, player: Character):
        pygame.draw.rect(self.display_surface, MENU_COLOR, self.full_menu)
        pygame.draw.rect(self.display_surface,
                         MENU_BORDER_COLOR, self.full_menu, MENU_BORDER_WIDTH, MENU_BORDER_RADIUS)
        if player is not None:
            limit_break_ready = player.limit_break_gauge >= 100
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
            self.display_surface.blit(
                action_description_text_rendered, (275, y))
            y += 25
            divider = pygame.Rect(x - 30, y, 150, 1)
            y += 20
            pygame.draw.rect(self.display_surface, 'White',
                             divider, width=10)
            mouse_pos = pygame.mouse.get_pos()
            mouse_clicked = pygame.mouse.get_pressed()[0]
            for command in self.action_commands.keys():
                if command == 'limit_break':
                    if limit_break_ready:
                        self.draw_menu_item(command, mouse_pos, mouse_clicked, 100,y, text_color='Green')
                    else:
                        self.draw_menu_item(command, mouse_pos, mouse_clicked, 100,y,disabled=True)
                else: 
                    self.draw_menu_item(command, mouse_pos, mouse_clicked, 100,y)

                y += 25

    def draw_menu_item(self, command: dict, mouse_pos: tuple, mouse_pressed: bool, x_pos: int, y_pos: int, text_color = MENU_TEXT_COLOR, disabled: bool = False):
        if disabled:
            text_color = 'Grey'
        command_text = self.font.render(self.action_commands[command]['label'].upper(), True, text_color)
        command_text_rect = command_text.get_rect(topleft = (x_pos,y_pos))
        command_text_rect.inflate_ip(100,10)
        selected_option = pygame.Surface((150, 30))
        selected_option.fill('White')
        selected_option.set_alpha(100)
        selected_option_rect = selected_option.get_rect()
        if not disabled:
            if command_text_rect.collidepoint(mouse_pos) or self.action_commands[command]['is_selected']:
                if mouse_pressed:
                    for _command in self.action_commands:
                        self.action_commands[_command]['is_selected'] = False
                    self.action_commands[command]['is_selected'] = True
                selected_option_rect.topleft = ((command_text_rect.topleft[0] -20,command_text_rect.topleft[1] -10) )
                self.display_surface.blit(selected_option,selected_option_rect)
        
        self.display_surface.blit(command_text,command_text_rect)

    


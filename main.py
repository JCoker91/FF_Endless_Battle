import pygame
from sys import exit
from random import choice
from models.character.character import Character, YSortedGroup
from util.custom_enum import PlayerSide
from settings import CHARACTERS
from util.debug import debug
from models.abilities.abilities import basic_attack
from models.UI_Bar.hp_bar import HPBar
from models.UI_Bar.mp_bar import MPBar
from models.UI_Bar.break_bar import BreakBar

pygame.init()

# Constants
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 800
LEFT_SIDE = {
    "front_middle": (200, 500),
    "front_top": (200, 450),
    "front_bot": (200, 550),
    "middle_middle": (150, 500),
    "middle_top": (150, 450),
    "middle_bot": (150, 550),
    "back_middle": (100, 500),
    "back_top": (100, 450),
    "back_bot": (100, 550),
}
RIGHT_SIDE = {
    "front_middle": (450, 500),
    "front_top": (450, 450),
    "front_bot": (450, 550),
    "middle_middle": (500, 500),
    "middle_top": (500, 450),
    "middle_bot": (500, 550),
    "back_middle": (550, 500),
    "back_top": (550, 450),
    "back_bot": (550, 550),
}

# Setup Screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Setup Groups
players_group = YSortedGroup()
particles_group = pygame.sprite.Group()
floating_text_group = pygame.sprite.Group()

player1 = choice(CHARACTERS)
player_1 = Character(
    character_name=player1['name'],
    stats=player1['stats'],
    off_set=player1['off_set'],
    attack_effects=player1['abilities'],
    side=PlayerSide.LEFT,
    position=LEFT_SIDE['front_middle'],
    group=players_group
)
player2 = choice(CHARACTERS)
player_2 = Character(
    character_name=player2['name'],
    stats=player2['stats'],
    off_set=player2['off_set'],
    attack_effects=player2['abilities'],
    side=PlayerSide.RIGHT,
    position=RIGHT_SIDE['front_middle'],
    group=players_group
)
# Setup Characters
# for character in CHARACTERS:
#     if character['name'] == 'Squall':
#         Character(
#             character_name=character['name'],
#             off_set=character['off_set'],
#             attack_effects=character['abilities'],
#             side=PlayerSide.LEFT,
#             position=LEFT_SIDE['front_middle'],
#             group = players_group
#         )
#         Character(
#             character_name=character['name'],
#             off_set=character['off_set'],
#             attack_effects=character['abilities'],
#             side=PlayerSide.RIGHT,
#             position=RIGHT_SIDE['front_middle'],
#             group = players_group
#         )

custom_font = pygame.font.Font('resources/fonts/Pixeltype.ttf', 32)

clock = pygame.time.Clock()
background = pygame.image.load(
    'resources/images/backgrounds/training_grounds.png').convert()

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
            if event.key == pygame.K_j:
                right_focused = list(filter(
                    lambda character: character.focused and character.side == PlayerSide.RIGHT, players_group))
                left_focused = list(filter(
                    lambda character: character.focused and character.side == PlayerSide.LEFT, players_group))
                if len(right_focused) > 0 and len(left_focused) > 0:
                    basic_attack(right_focused[0],
                                 left_focused[0], particles_group, floating_text_group)

            if event.key == pygame.K_f:
                right_focused = list(filter(
                    lambda character: character.focused and character.side == PlayerSide.RIGHT, players_group))
                left_focused = list(filter(
                    lambda character: character.focused and character.side == PlayerSide.LEFT, players_group))
                if len(right_focused) > 0 and len(left_focused) > 0:
                    basic_attack(left_focused[0],
                                 right_focused[0], particles_group, floating_text_group)

    screen.blit(background, (0, 0))
    y1 = 10
    y2 = 10

    for player in players_group:
        if player.icon is not None:
            if player.side == PlayerSide.RIGHT:
                screen.blit(player.icon, (screen.get_width() - 66, y2))
                hp_bar = HPBar(player, screen.get_width() - 216, y2)
                break_bar = BreakBar(player, screen.get_width() - 216, y2+14)
                mp_bar = MPBar(player, screen.get_width() - 216, y2+28)
                hp_bar.draw()
                break_bar.draw()
                mp_bar.draw()
                y2 += 40
            else:
                screen.blit(pygame.transform.flip(player.icon, 1, 0), (10, y1))
                hp_bar = HPBar(player, 70, y1)
                break_bar = BreakBar(player, 70, y1 + 14)
                mp_bar = MPBar(player, 70, y1 + 28)
                hp_bar.draw()
                break_bar.draw()
                mp_bar.draw()
                y1 += 40

    players_group.update()
    particles_group.update()
    floating_text_group.update()
    players_group.draw(screen)
    particles_group.draw(screen)
    floating_text_group.draw(screen)
    pygame.display.update()
    clock.tick(60)

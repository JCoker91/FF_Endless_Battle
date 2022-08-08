from tkinter import RIGHT
from turtle import pos
import pygame
from sys import exit
from models.character.character import Character, YSortedGroup
from util.custom_enum import PlayerSide
from settings import CHARACTERS
from util.debug import debug

pygame.init()


SCREEN_WIDTH = 640
SCREEN_HEIGHT = 800
LEFT_SIDE = {
    "front_middle": (float(200.0), float(500.0)),
    "front_top": (float(200.0), float(450.0)),
    "front_bot": (float(200.0), float(550.0)),
    "middle_middle": (float(150.0), float(500.0)),
    "middle_top": (float(150.0), float(450.0)),
    "middle_bot": (float(150.0), float(550.0)),
    "back_middle": (float(100.0), float(500.0)),
    "back_top": (float(100.0), float(450.0)),
    "back_bot": (float(100.0), float(550.0)),
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
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
players = YSortedGroup()
particles = pygame.sprite.Group()
for i, character in enumerate(CHARACTERS):
    try:
        if character['side'] == PlayerSide.LEFT:
            players.add(
                Character(
                    character_name=character['name'],
                    off_set=character['off_set'],
                    side=character['side'],
                    position=LEFT_SIDE[list(LEFT_SIDE.keys())[i]]
                )
            )
        else:
            players.add(
                Character(
                    character_name=character['name'],
                    off_set=character['off_set'],
                    side=character['side'],
                    position=RIGHT_SIDE[list(LEFT_SIDE.keys())[i]]
                )
            )
    except IndexError:
        pass


# cloud = Character("Cloud", RIGHT_SIDE['front_middle'], PlayerSide.RIGHT)
# tera = Character("Tera", RIGHT_SIDE['middle_top'], PlayerSide.RIGHT)
# squall = Character("Squall", RIGHT_SIDE['middle_bot'], PlayerSide.RIGHT)
# cecil = Character("Cecil", RIGHT_SIDE['back_top'], PlayerSide.RIGHT)
# noctis = Character("Noctis", RIGHT_SIDE['back_bot'], PlayerSide.RIGHT)
# lightning = Character("Lightning", LEFT_SIDE['front_middle'], PlayerSide.LEFT)
# firion = Character("Firion", LEFT_SIDE['middle_top'], PlayerSide.LEFT)
# bartz = Character("Bartz", LEFT_SIDE['middle_bot'], PlayerSide.LEFT)
# tidus = Character("Tidus", LEFT_SIDE['back_top'], PlayerSide.LEFT)
# zidane = Character("Zidane", LEFT_SIDE['back_bot'], PlayerSide.LEFT)
# # players = pygame.sprite.Group()
# players.add(tidus)
# players.add(cloud)
# players.add(lightning)
# players.add(noctis)
# players.add(squall)
# players.add(bartz)
# players.add(cecil)
# players.add(firion)
# players.add(tera)
# players.add(zidane)

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
                    lambda character: character.focused and character.side == PlayerSide.RIGHT, players))
                left_focused = list(filter(
                    lambda character: character.focused and character.side == PlayerSide.LEFT, players))
                if len(right_focused) > 0 and len(left_focused) > 0:
                    right_focused[0].basic_attack(left_focused[0],particles)
                    # debug(right_focused[0].rect.bottomright)
            if event.key == pygame.K_f:
                right_focused = list(filter(
                    lambda character: character.focused and character.side == PlayerSide.RIGHT, players))
                left_focused = list(filter(
                    lambda character: character.focused and character.side == PlayerSide.LEFT, players))
                if len(right_focused) > 0 and len(left_focused) > 0:
                    left_focused[0].basic_attack(right_focused[0], particles)
                    # debug(left_focused[0].rect.bottomleft)

    screen.blit(background, (0, 0))

    players.update()
    particles.update()
    players.draw(screen)
    particles.draw(screen)
    y1 = 10
    y2 = 10
    for player in players:
        if player.icon is not None:
            if player.side == PlayerSide.RIGHT:
                screen.blit(player.icon, (screen.get_width() - 66, y2))
                screen.blit(custom_font.render(
                    str(player.rect.center), False, 'Red'), (screen.get_width() - 166, y2+15))
                y2 += 40
            else:
                screen.blit(pygame.transform.flip(player.icon, 1, 0), (10, y1))
                screen.blit(custom_font.render(
                    str(player.rect.center), False, 'Red'), (80, y1+15))
                y1 += 40

    pygame.display.update()

    clock.tick(60)

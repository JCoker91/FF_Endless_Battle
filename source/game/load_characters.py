import pygame
from random import choice
from player_data import CHARACTERS
from source.models.character.character import Character
from settings import LEFT_SIDE_POSITIONS, RIGHT_SIDE_POSITIONS
from source.util.custom_enum import PlayerSide


def load_characters(players_group: pygame.sprite.Group):
    positions = [
        LEFT_SIDE_POSITIONS['middle_middle'],
        LEFT_SIDE_POSITIONS['front_bottom'],
        LEFT_SIDE_POSITIONS['front_top'],
        LEFT_SIDE_POSITIONS['back_bottom'],
        LEFT_SIDE_POSITIONS['back_top'],
        RIGHT_SIDE_POSITIONS['middle_middle'],
        RIGHT_SIDE_POSITIONS['front_bottom'],
        RIGHT_SIDE_POSITIONS['front_top'],
        RIGHT_SIDE_POSITIONS['back_bottom'],
        RIGHT_SIDE_POSITIONS['back_top'],
    ]
    for i, player in enumerate(CHARACTERS):
        if i > 4:
            player_side = PlayerSide.RIGHT
        else:
            player_side = PlayerSide.LEFT
        Character(
            character_name=player['name'],
            stats=player['stats'],
            off_set=player['off_set'],
            attack_effects=player['abilities'],
            position=positions[i],
            group=players_group,
            abilities=player['abilities'],
            side=player_side
        )
    # player = CHARACTERS[0]
    # Character(
    #     character_name=player['name'],
    #     stats=player['stats'],
    #     off_set=player['off_set'],
    #     attack_effects=player['abilities'],
    #     side=PlayerSide.LEFT,
    #     position=LEFT_SIDE_POSITIONS['middle_middle'],
    #     group=players_group,
    #     abilities=player['abilities']
    # )
    # player = CHARACTERS[1]
    # Character(
    #     character_name=player['name'],
    #     stats=player['stats'],
    #     off_set=player['off_set'],
    #     attack_effects=player['abilities'],
    #     side=PlayerSide.LEFT,
    #     position=LEFT_SIDE_POSITIONS['front_bottom'],
    #     group=players_group,
    #     abilities=player['abilities']
    # )
    # player = CHARACTERS[2]
    # Character(
    #     character_name=player['name'],
    #     stats=player['stats'],
    #     off_set=player['off_set'],
    #     attack_effects=player['abilities'],
    #     side=PlayerSide.LEFT,
    #     position=LEFT_SIDE_POSITIONS['front_top'],
    #     group=players_group,
    #     abilities=player['abilities']
    # )
    # player = CHARACTERS[3]
    # Character(
    #     character_name=player['name'],
    #     stats=player['stats'],
    #     off_set=player['off_set'],
    #     attack_effects=player['abilities'],
    #     side=PlayerSide.LEFT,
    #     position=LEFT_SIDE_POSITIONS['back_top'],
    #     group=players_group,
    #     abilities=player['abilities']
    # )
    # player = CHARACTERS[4]
    # Character(
    #     character_name=player['name'],
    #     stats=player['stats'],
    #     off_set=player['off_set'],
    #     attack_effects=player['abilities'],
    #     side=PlayerSide.LEFT,
    #     position=LEFT_SIDE_POSITIONS['back_bottom'],
    #     group=players_group,
    #     abilities=player['abilities']
    # )

    # player = CHARACTERS[5]
    # Character(
    #     character_name=player['name'],
    #     stats=player['stats'],
    #     off_set=player['off_set'],
    #     attack_effects=player['abilities'],
    #     side=PlayerSide.RIGHT,
    #     position=RIGHT_SIDE_POSITIONS['front_top'],
    #     group=players_group,
    #     abilities=player['abilities']
    # )
    # player = CHARACTERS[6]
    # Character(
    #     character_name=player['name'],
    #     stats=player['stats'],
    #     off_set=player['off_set'],
    #     attack_effects=player['abilities'],
    #     side=PlayerSide.RIGHT,
    #     position=RIGHT_SIDE_POSITIONS['front_bottom'],
    #     group=players_group,
    #     abilities=player['abilities']
    # )
    # player = CHARACTERS[7]
    # Character(
    #     character_name=player['name'],
    #     stats=player['stats'],
    #     off_set=player['off_set'],
    #     attack_effects=player['abilities'],
    #     side=PlayerSide.RIGHT,
    #     position=RIGHT_SIDE_POSITIONS['middle_middle'],
    #     group=players_group,
    #     abilities=player['abilities']
    # )
    # player = CHARACTERS[8]
    # Character(
    #     character_name=player['name'],
    #     stats=player['stats'],
    #     off_set=player['off_set'],
    #     attack_effects=player['abilities'],
    #     side=PlayerSide.RIGHT,
    #     position=RIGHT_SIDE_POSITIONS['back_top'],
    #     group=players_group,
    #     abilities=player['abilities']
    # )
    # player = CHARACTERS[9]
    # Character(
    #     character_name=player['name'],
    #     stats=player['stats'],
    #     off_set=player['off_set'],
    #     attack_effects=player['abilities'],
    #     side=PlayerSide.RIGHT,
    #     position=RIGHT_SIDE_POSITIONS['back_bottom'],
    #     group=players_group,
    #     abilities=player['abilities']
    # )

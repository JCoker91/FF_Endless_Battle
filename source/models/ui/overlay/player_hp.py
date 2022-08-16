import pygame
from source.models.ui.status_bar.hp_bar import HPBar
from source.models.character.character import Character


class PlayerHP:
    def __init__(self, players: list[Character]) -> None:
        self.players = players

    def draw(self):
        for player in self.players:
            hp_bar = HPBar(player, player.rect.topright[0] - player.image.get_width()/2, player.rect.topright[1] - 5,
                           False, draw_point='center', show_border=False, show_background=False, size="small")
            hp_bar.draw()

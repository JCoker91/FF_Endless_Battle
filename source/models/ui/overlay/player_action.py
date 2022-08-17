import pygame
from source.models.character.character import Character


class PlayerAction(pygame.sprite.Sprite):
    def __init__(self, player: Character, action_name: str, group: pygame.sprite.Group) -> None:
        self.icon = player.icon
        self.player = player
        self.action_name = action_name
        group.add(self)

    def draw(self):
        pass

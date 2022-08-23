import pygame
from source.models.character.character import Character
from source.util.custom_enum import PlayerSide, CurrentState
from settings import *


class PlayerTurnIndicator:
    def __init__(self) -> None:
        self.display_surface = pygame.display.get_surface()

    def draw(self, player: Character, width: int = 0):
        if player.side == PlayerSide.LEFT and player.current_state == CurrentState.IDLE:
            image = pygame.transform.scale(player.image, (100,100))
            image_mask = pygame.mask.from_surface(image).fill()
            # image.fill((255,255,255))
            image_rect = image.get_rect()
            self.display_surface.blit(image, image_rect)
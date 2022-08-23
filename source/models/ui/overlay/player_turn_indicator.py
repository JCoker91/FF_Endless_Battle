import pygame
from source.models.character.character import Character
from source.util.custom_enum import PlayerSide, CurrentState
from settings import *


class PlayerTurnIndicator:
    def __init__(self) -> None:
        self.display_surface = pygame.display.get_surface()

    def draw(self, player: Character):
        if player.side == PlayerSide.LEFT and player.current_state == CurrentState.IDLE:
            image_mask = pygame.mask.from_surface(player.image)
            image_mask_surf = image_mask.to_surface()
            image_mask_surf = pygame.transform.scale(
                image_mask_surf, (player.image.get_width(), player.image.get_height()))
            image_mask_surf.set_colorkey((0, 0, 0))

            pixel_range = []
            x_size, y_size = image_mask_surf.get_size()
            for x in range(x_size):
                for y in range(y_size):
                    if image_mask_surf.get_at((x, y)) == (255, 255, 255):
                        pixel_range.append((x-1, y-1))
                        pixel_range.append((x-1, y+1))
                        pixel_range.append((x-1, y+1))
                        pixel_range.append((x+1, y))
                        pixel_range.append((x-1, y))
                        pixel_range.append((x, y+1))
                        pixel_range.append((x, y-1))
            outline_color = (255, 255, 255)
            for pixel_pos in pixel_range:
                image_mask_surf.set_at(pixel_pos, (outline_color))

            image_mask_rect = image_mask_surf.get_rect(
                center=(player.rect.center[0], player.rect.center[1]))
            self.display_surface.blit(image_mask_surf, image_mask_rect)

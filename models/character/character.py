from __future__ import annotations

import pygame
import os
from util.custom_enum import CurrentState, PlayerSide
from util.util_functions import load_image_folder


class Character(pygame.sprite.Sprite):
    def __init__(self, character_name: str, position: tuple, side: PlayerSide) -> None:
        super().__init__()
        self.name = character_name # Character name
        self.side = side # Which side the character is on (left or right)
        self.starting_spot = position # Determines where the character will load on the screen
        self.current_state = CurrentState.IDLE # Determines animation states
        self.animation_frame_count = 0 # The count used to loop through the animations
        self.focused = False # Determines if the player has focus on the character

        # Load sprite animations
        self.animations = {
            'icon': [],
            'idle':[],
            'attack':[],
            'attack_standby':[],
            'magic_attack':[],
            'magic_standby':[],
            'dying':[],
            'dead':[],
            'limit_break':[],
            'move':[],
            'jump':[],
            'win':[],
            'win_end': []
            }
        self.load_images()        

        if self.side == PlayerSide.RIGHT:
            self.image = self.animations['idle'][0]
            self.rect = self.image.get_rect(bottomright=self.starting_spot)
        else:
            self.image = pygame.transform.flip(
                self.animations['idle'][0], True, False)
            self.rect = self.image.get_rect(bottomleft=self.starting_spot)
        
        # Timers
        self.mouse_click_timer = None
        self.mouse_click_cool_down = 300
        self.can_click = True






    def load_images(self):
        self.icon = pygame.image.load(
                f'resources/images/sprites/{self.name}/skin_1/icon/tile000.png')
        for animation in list(self.animations.keys()):
            animation_images = load_image_folder(f'resources/images/sprites/{self.name}/skin_1/{animation}')
            for image in animation_images:
                self.animations[animation].append(image)

    def animate(self):
        if self.focused:
            match self.current_state:
                case CurrentState.IDLE:
                    if self.side == PlayerSide.RIGHT:
                        self.image = self.animations['idle'][int(
                            self.animation_frame_count)]
                        self.rect = self.image.get_rect(
                            bottomright=self.starting_spot)
                    else:
                        self.image = pygame.transform.flip(
                            self.animations['idle'][int(self.animation_frame_count)], 1, 0)
                        self.rect = self.image.get_rect(
                            bottomleft=self.starting_spot)
                    self.animation_frame_count += .08
                    if self.animation_frame_count >= len(self.animations['idle']):
                        self.animation_frame_count = 0
                case CurrentState.ATTACK:
                    if self.side == PlayerSide.RIGHT:
                        self.image = self.animations['attack'][int(
                            self.animation_frame_count)]
                        self.rect = self.image.get_rect(
                            bottomright=self.starting_spot)
                    else:
                        self.image = pygame.transform.flip(
                            self.animations['attack'][int(self.animation_frame_count)], 1, 0)
                        self.rect = self.image.get_rect(bottomleft=self.starting_spot)
                    self.animation_frame_count += .25
                    if self.animation_frame_count >= len(self.animations['attack']):
                        self.animation_frame_count = 0
                        self.current_state = CurrentState.IDLE
                case CurrentState.LIMIT_BREAK:
                    if self.side == PlayerSide.RIGHT:
                        self.image = self.animations['limit_break'][int(
                            self.animation_frame_count)]
                        self.rect = self.image.get_rect(
                            bottomright=self.starting_spot)
                    else:
                        self.image = pygame.transform.flip(
                            self.animations['limit_break'][int(self.animation_frame_count)], 1, 0)
                        self.rect = self.image.get_rect(
                            bottomleft=self.starting_spot)
                    self.animation_frame_count += .25
                    if self.animation_frame_count >= len(self.animations['limit_break']):
                        self.animation_frame_count = 0
                        self.current_state = CurrentState.IDLE
                case CurrentState.ATTACK_STANDBY:
                    if self.side == PlayerSide.RIGHT:
                        self.image = self.animations['attack_standby'][int(
                            self.animation_frame_count)]
                        self.rect = self.image.get_rect(
                            bottomright=self.starting_spot)
                    else:
                        self.image = pygame.transform.flip(
                            self.animations['attack_standby'][int(self.animation_frame_count)], 1, 0)
                        self.rect = self.image.get_rect(
                            bottomleft=self.starting_spot)
                    self.animation_frame_count += .08
                    if self.animation_frame_count >= len(self.animations['attack_standby']):
                        self.animation_frame_count = 0
                case CurrentState.MAGIC_STANDBY:
                    if self.side == PlayerSide.RIGHT:
                        self.image = self.animations['magic_standby'][int(
                            self.animation_frame_count)]
                        self.rect = self.image.get_rect(
                            bottomright=self.starting_spot)
                    else:
                        self.image = pygame.transform.flip(
                            self.animations['magic_standby'][int(self.animation_frame_count)], 1, 0)
                        self.rect = self.image.get_rect(bottomleft=(
                            (self.starting_spot[0]), (self.starting_spot[1])))
                    self.animation_frame_count += .08
                    if self.animation_frame_count >= len(self.animations['magic_standby']):
                        self.animation_frame_count = 0
                case CurrentState.MAGIC_ATTACK:
                    if self.side == PlayerSide.RIGHT:
                        self.image = self.animations['magic_attack'][int(
                            self.animation_frame_count)]
                        self.rect = self.image.get_rect(
                            bottomright=self.starting_spot)
                    else:
                        self.image = pygame.transform.flip(
                            self.animations['magic_attack'][int(self.animation_frame_count)], 1, 0)
                        self.rect = self.image.get_rect(
                            bottomleft=self.starting_spot)
                    self.animation_frame_count += .08
                    if self.animation_frame_count >= len(self.animations['magic_attack']):
                        self.animation_frame_count = 0
                        self.current_state = CurrentState.IDLE
                case CurrentState.DYING:
                    if self.side == PlayerSide.RIGHT:
                        self.image = self.animations['dying'][int(
                            self.animation_frame_count)]
                        self.rect = self.image.get_rect(
                            bottomright=self.starting_spot)
                    else:
                        self.image = pygame.transform.flip(
                            self.animations['dying'][int(self.animation_frame_count)], 1, 0)
                        self.rect = self.image.get_rect(
                            bottomleft=self.starting_spot)
                    self.animation_frame_count += .08
                    if self.animation_frame_count >= len(self.animations['dying']):
                        self.animation_frame_count = 0
                case CurrentState.DEAD:
                    if self.side == PlayerSide.RIGHT:
                        self.image = self.animations['dead'][int(
                            self.animation_frame_count)]
                        self.rect = self.image.get_rect(
                            bottomright=self.starting_spot)
                    else:
                        self.image = pygame.transform.flip(
                            self.animations['dead'][int(self.animation_frame_count)], 1, 0)
                        self.rect = self.image.get_rect(
                            bottomleft=self.starting_spot)
                    self.animation_frame_count += .08
                    if self.animation_frame_count >= len(self.animations['dead']):
                        self.animation_frame_count = 0
                case CurrentState.JUMP:
                    if self.side == PlayerSide.RIGHT:
                        self.image = self.animations['jump'][int(
                            self.animation_frame_count)]
                        self.rect = self.image.get_rect(
                            bottomright=self.starting_spot)
                    else:
                        self.image = pygame.transform.flip(
                            self.animations['jump'][int(self.animation_frame_count)], 1, 0)
                        self.rect = self.image.get_rect(
                            bottomleft=self.starting_spot)
                    self.animation_frame_count += .08
                    if self.animation_frame_count >= len(self.animations['jump']):
                        self.animation_frame_count = 0
                case CurrentState.MOVE:
                    if self.side == PlayerSide.RIGHT:
                        self.image = self.animations['move'][int(
                            self.animation_frame_count)]
                        self.rect = self.image.get_rect(
                            bottomright=self.starting_spot)
                    else:
                        self.image = pygame.transform.flip(
                            self.animations['move'][int(self.animation_frame_count)], 1, 0)
                        self.rect = self.image.get_rect(
                            bottomleft=self.starting_spot)
                    self.animation_frame_count += .08
                    if self.animation_frame_count >= len(self.animations['move']):
                        self.animation_frame_count = 0
                case CurrentState.WIN:
                    if self.side == PlayerSide.RIGHT:
                        self.image = self.animations['win'][int(
                            self.animation_frame_count)]
                        self.rect = self.image.get_rect(
                            bottomright=self.starting_spot)
                    else:
                        self.image = pygame.transform.flip(
                            self.animations['win'][int(self.animation_frame_count)], 1, 0)
                        self.rect = self.image.get_rect(
                            bottomleft=self.starting_spot)
                    self.animation_frame_count += .15
                    if self.animation_frame_count >= len(self.animations['win']):
                        self.animation_frame_count = 0
                        self.current_state = CurrentState.WIN_END
                case CurrentState.WIN_END:
                    if self.side == PlayerSide.RIGHT:
                        self.image = self.animations['win_end'][int(
                            self.animation_frame_count)]
                        self.rect = self.image.get_rect(
                            bottomright=self.starting_spot)
                    else:
                        self.image = pygame.transform.flip(
                            self.animations['win_end'][int(self.animation_frame_count)], 1, 0)
                        self.rect = self.image.get_rect(
                            bottomleft=self.starting_spot)
                    self.animation_frame_count += .15
                    if self.animation_frame_count >= len(self.animations['win_end']):
                        self.animation_frame_count = 0

    def input(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            if self.can_click:
                self.focused = not self.focused
                self.can_click = False
                self.mouse_click_timer = pygame.time.get_ticks()


        if self.focused:
            pressed_keys = pygame.key.get_pressed()
            if pressed_keys[pygame.K_1]:
                self.animation_frame_count = 0
                self.current_state = CurrentState.IDLE
            if pressed_keys[pygame.K_2]:
                self.animation_frame_count = 0
                self.current_state = CurrentState.JUMP
            if pressed_keys[pygame.K_3]:
                self.animation_frame_count = 0
                self.current_state = CurrentState.MOVE
            if pressed_keys[pygame.K_4]:
                self.animation_frame_count = 0
                self.current_state = CurrentState.ATTACK_STANDBY
            if pressed_keys[pygame.K_5]:
                self.animation_frame_count = 0
                self.current_state = CurrentState.ATTACK
            if pressed_keys[pygame.K_6]:
                self.animation_frame_count = 0
                self.current_state = CurrentState.MAGIC_STANDBY
            if pressed_keys[pygame.K_7]:
                self.animation_frame_count = 0
                self.current_state = CurrentState.MAGIC_ATTACK
            if pressed_keys[pygame.K_8]:
                self.animation_frame_count = 0
                self.current_state = CurrentState.LIMIT_BREAK
            if pressed_keys[pygame.K_q]:
                self.animation_frame_count = 0
                self.current_state = CurrentState.DYING
            if pressed_keys[pygame.K_w]:
                self.animation_frame_count = 0
                self.current_state = CurrentState.DEAD
            if pressed_keys[pygame.K_e]:
                self.animation_frame_count = 0
                self.current_state = CurrentState.WIN
            if pressed_keys[pygame.K_r]:
                self.animation_frame_count = 0
                self.current_state = CurrentState.WIN_END

    def basic_attack(self, enemy: Character):
        self.rect.move_ip(100,100)
        self.current_state = CurrentState.ATTACK

    def cool_downs(self):
        if not self.can_click:
            timer = pygame.time.get_ticks()
            if timer - self.mouse_click_timer > self.mouse_click_cool_down:
                self.can_click = True

    def update(self):
        self.input()
        self.animate()
        self.cool_downs()

class YSortedGroup(pygame.sprite.Group):
    def __init__(self) -> None:
        super().__init__()
        self.display_surface = pygame.display.get_surface()

    def draw(self, surface):
        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            self.display_surface.blit(sprite.image, sprite.rect)

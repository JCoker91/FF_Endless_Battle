from __future__ import annotations
from unicodedata import name

import pygame
import os
from util.custom_enum import CurrentState, PlayerSide


class Character(pygame.sprite.Sprite):
    def __init__(self, character_name: str, position: tuple, side: PlayerSide) -> None:
        super().__init__()
        self.name = character_name
        self.side = side
        self.move_count = 0
        self.starting_spot = position
        self.current_state = CurrentState.IDLE
        try:
            self.icon = pygame.image.load(
                f'resources/images/sprites/{character_name}/skin_1/icon/tile000.png')
        except:
            self.icon = None
        self.idle_animation = []
        self.attack_animation = []
        self.attack_standby_animation = []
        self.dead_animation = []
        self.dying_animation = []
        self.limit_break_animation = []
        self.magic_standby_animation = []
        self.magic_attack_animation = []
        self.move_animation = []
        self.win_animation = []
        self.win_end_animation = []
        self.jump_animation = []
        self.focused = False
        for image in sorted(os.listdir(f'resources/images/sprites/{character_name}/skin_1/idle/')):
            _image = pygame.image.load(
                f'resources/images/sprites/{character_name}/skin_1/idle/{image}').convert_alpha()
            self.idle_animation.append(_image)
        for image in sorted(os.listdir(f'resources/images/sprites/{character_name}/skin_1/attack/')):
            _image = pygame.image.load(
                f'resources/images/sprites/{character_name}/skin_1/attack/{image}').convert_alpha()
            self.attack_animation.append(_image)
        for image in sorted(os.listdir(f'resources/images/sprites/{character_name}/skin_1/attack_standby/')):
            _image = pygame.image.load(
                f'resources/images/sprites/{character_name}/skin_1/attack_standby/{image}').convert_alpha()
            self.attack_standby_animation.append(_image)
        for image in sorted(os.listdir(f'resources/images/sprites/{character_name}/skin_1/dead/')):
            _image = pygame.image.load(
                f'resources/images/sprites/{character_name}/skin_1/dead/{image}').convert_alpha()
            self.dead_animation.append(_image)
        for image in sorted(os.listdir(f'resources/images/sprites/{character_name}/skin_1/dying/')):
            _image = pygame.image.load(
                f'resources/images/sprites/{character_name}/skin_1/dying/{image}').convert_alpha()
            self.dying_animation.append(_image)
        for image in sorted(os.listdir(f'resources/images/sprites/{character_name}/skin_1/limit_break/')):
            _image = pygame.image.load(
                f'resources/images/sprites/{character_name}/skin_1/limit_break/{image}').convert_alpha()
            self.limit_break_animation.append(_image)
        for image in sorted(os.listdir(f'resources/images/sprites/{character_name}/skin_1/magic_standby/')):
            _image = pygame.image.load(
                f'resources/images/sprites/{character_name}/skin_1/magic_standby/{image}').convert_alpha()
            self.magic_standby_animation.append(_image)
        for image in sorted(os.listdir(f'resources/images/sprites/{character_name}/skin_1/magic_attack/')):
            _image = pygame.image.load(
                f'resources/images/sprites/{character_name}/skin_1/magic_attack/{image}').convert_alpha()
            self.magic_attack_animation.append(_image)
        for image in sorted(os.listdir(f'resources/images/sprites/{character_name}/skin_1/move/')):
            _image = pygame.image.load(
                f'resources/images/sprites/{character_name}/skin_1/move/{image}').convert_alpha()
            self.move_animation.append(_image)
        for image in sorted(os.listdir(f'resources/images/sprites/{character_name}/skin_1/jump/')):
            _image = pygame.image.load(
                f'resources/images/sprites/{character_name}/skin_1/jump/{image}').convert_alpha()
            self.jump_animation.append(_image)
        for image in sorted(os.listdir(f'resources/images/sprites/{character_name}/skin_1/win/')):
            _image = pygame.image.load(
                f'resources/images/sprites/{character_name}/skin_1/win/{image}').convert_alpha()
            self.win_animation.append(_image)
        for image in sorted(os.listdir(f'resources/images/sprites/{character_name}/skin_1/win_end/')):
            _image = pygame.image.load(
                f'resources/images/sprites/{character_name}/skin_1/win_end/{image}').convert_alpha()
            self.win_end_animation.append(_image)

        if self.side == PlayerSide.RIGHT:
            self.image = self.idle_animation[0]
            self.rect = self.image.get_rect(bottomright=self.starting_spot)
        else:
            self.image = pygame.transform.flip(
                self.idle_animation[0], True, False)
            self.rect = self.image.get_rect(bottomleft=self.starting_spot)
        
        self.animation_frame_count = 0

    def update(self):
        self.input()
        self.animate()

    def animate(self):
        if self.focused:
            match self.current_state:
                case CurrentState.IDLE:
                    if self.side == PlayerSide.RIGHT:
                        self.image = self.idle_animation[int(
                            self.animation_frame_count)]
                        self.rect = self.image.get_rect(
                            bottomright=self.starting_spot)
                    else:
                        self.image = pygame.transform.flip(
                            self.idle_animation[int(self.animation_frame_count)], 1, 0)
                        self.rect = self.image.get_rect(
                            bottomleft=self.starting_spot)
                    self.animation_frame_count += .08
                    if self.animation_frame_count >= len(self.idle_animation):
                        self.animation_frame_count = 0
                case CurrentState.ATTACK:
                    if self.side == PlayerSide.RIGHT:
                        self.image = self.attack_animation[int(
                            self.animation_frame_count)]
                        self.rect = self.image.get_rect(
                            bottomright=self.starting_spot)
                    else:
                        self.image = pygame.transform.flip(
                            self.attack_animation[int(self.animation_frame_count)], 1, 0)
                        self.rect = self.image.get_rect(
                            bottomleft=self.starting_spot)
                    self.animation_frame_count += .25
                    if self.animation_frame_count >= len(self.attack_animation):
                        self.animation_frame_count = 0
                        self.current_state = CurrentState.IDLE
                case CurrentState.LIMIT_BREAK:
                    if self.side == PlayerSide.RIGHT:
                        self.image = self.limit_break_animation[int(
                            self.animation_frame_count)]
                        self.rect = self.image.get_rect(
                            bottomright=self.starting_spot)
                    else:
                        self.image = pygame.transform.flip(
                            self.limit_break_animation[int(self.animation_frame_count)], 1, 0)
                        self.rect = self.image.get_rect(
                            bottomleft=self.starting_spot)
                    self.animation_frame_count += .25
                    if self.animation_frame_count >= len(self.limit_break_animation):
                        self.animation_frame_count = 0
                        self.current_state = CurrentState.IDLE
                case CurrentState.ATTACK_STANDBY:
                    if self.side == PlayerSide.RIGHT:
                        self.image = self.attack_standby_animation[int(
                            self.animation_frame_count)]
                        self.rect = self.image.get_rect(
                            bottomright=self.starting_spot)
                    else:
                        self.image = pygame.transform.flip(
                            self.attack_standby_animation[int(self.animation_frame_count)], 1, 0)
                        self.rect = self.image.get_rect(
                            bottomleft=self.starting_spot)
                    self.animation_frame_count += .08
                    if self.animation_frame_count >= len(self.attack_standby_animation):
                        self.animation_frame_count = 0
                case CurrentState.MAGIC_STANDBY:
                    if self.side == PlayerSide.RIGHT:
                        self.image = self.magic_standby_animation[int(
                            self.animation_frame_count)]
                        self.rect = self.image.get_rect(
                            bottomright=self.starting_spot)
                    else:
                        self.image = pygame.transform.flip(
                            self.magic_standby_animation[int(self.animation_frame_count)], 1, 0)
                        self.rect = self.image.get_rect(bottomleft=(
                            (self.starting_spot[0] - 17), (self.starting_spot[1] + 13)))
                    self.animation_frame_count += .08
                    if self.animation_frame_count >= len(self.magic_standby_animation):
                        self.animation_frame_count = 0
                case CurrentState.MAGIC_ATTACK:
                    if self.side == PlayerSide.RIGHT:
                        self.image = self.magic_attack_animation[int(
                            self.animation_frame_count)]
                        self.rect = self.image.get_rect(
                            bottomright=self.starting_spot)
                    else:
                        self.image = pygame.transform.flip(
                            self.magic_attack_animation[int(self.animation_frame_count)], 1, 0)
                        self.rect = self.image.get_rect(
                            bottomleft=self.starting_spot)
                    self.animation_frame_count += .08
                    if self.animation_frame_count >= len(self.magic_attack_animation):
                        self.animation_frame_count = 0
                        self.current_state = CurrentState.IDLE
                case CurrentState.DYING:
                    if self.side == PlayerSide.RIGHT:
                        self.image = self.dying_animation[int(
                            self.animation_frame_count)]
                        self.rect = self.image.get_rect(
                            bottomright=self.starting_spot)
                    else:
                        self.image = pygame.transform.flip(
                            self.dying_animation[int(self.animation_frame_count)], 1, 0)
                        self.rect = self.image.get_rect(
                            bottomleft=self.starting_spot)
                    self.animation_frame_count += .08
                    if self.animation_frame_count >= len(self.dying_animation):
                        self.animation_frame_count = 0
                case CurrentState.DEAD:
                    if self.side == PlayerSide.RIGHT:
                        self.image = self.dead_animation[int(
                            self.animation_frame_count)]
                        self.rect = self.image.get_rect(
                            bottomright=self.starting_spot)
                    else:
                        self.image = pygame.transform.flip(
                            self.dead_animation[int(self.animation_frame_count)], 1, 0)
                        self.rect = self.image.get_rect(
                            bottomleft=self.starting_spot)
                    self.animation_frame_count += .08
                    if self.animation_frame_count >= len(self.dead_animation):
                        self.animation_frame_count = 0
                case CurrentState.JUMP:
                    if self.side == PlayerSide.RIGHT:
                        self.image = self.jump_animation[int(
                            self.animation_frame_count)]
                        self.rect = self.image.get_rect(
                            bottomright=self.starting_spot)
                    else:
                        self.image = pygame.transform.flip(
                            self.jump_animation[int(self.animation_frame_count)], 1, 0)
                        self.rect = self.image.get_rect(
                            bottomleft=self.starting_spot)
                    self.animation_frame_count += .08
                    if self.animation_frame_count >= len(self.jump_animation):
                        self.animation_frame_count = 0
                case CurrentState.MOVE:
                    if self.side == PlayerSide.RIGHT:
                        self.image = self.move_animation[int(
                            self.animation_frame_count)]
                        self.rect = self.image.get_rect(
                            bottomright=self.starting_spot)
                    else:
                        self.image = pygame.transform.flip(
                            self.move_animation[int(self.animation_frame_count)], 1, 0)
                        self.rect = self.image.get_rect(
                            bottomleft=self.starting_spot)
                    self.animation_frame_count += .08
                    if self.animation_frame_count >= len(self.move_animation):
                        self.animation_frame_count = 0
                case CurrentState.WIN:
                    if self.side == PlayerSide.RIGHT:
                        self.image = self.win_animation[int(
                            self.animation_frame_count)]
                        self.rect = self.image.get_rect(
                            bottomright=self.starting_spot)
                    else:
                        self.image = pygame.transform.flip(
                            self.win_animation[int(self.animation_frame_count)], 1, 0)
                        self.rect = self.image.get_rect(
                            bottomleft=self.starting_spot)
                    self.animation_frame_count += .15
                    if self.animation_frame_count >= len(self.win_animation):
                        self.animation_frame_count = 0
                        self.current_state = CurrentState.WIN_END
                case CurrentState.WIN_END:
                    if self.side == PlayerSide.RIGHT:
                        self.image = self.win_end_animation[int(
                            self.animation_frame_count)]
                        self.rect = self.image.get_rect(
                            bottomright=self.starting_spot)
                    else:
                        self.image = pygame.transform.flip(
                            self.win_end_animation[int(self.animation_frame_count)], 1, 0)
                        self.rect = self.image.get_rect(
                            bottomleft=self.starting_spot)
                    self.animation_frame_count += .15
                    if self.animation_frame_count >= len(self.win_end_animation):
                        self.animation_frame_count = 0

    def input(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            self.focused = not self.focused

        if self.focused:
            if pygame.key.get_pressed()[pygame.K_1]:
                self.animation_frame_count = 0
                self.current_state = CurrentState.IDLE
            if pygame.key.get_pressed()[pygame.K_2]:
                self.animation_frame_count = 0
                self.current_state = CurrentState.JUMP
            if pygame.key.get_pressed()[pygame.K_3]:
                self.animation_frame_count = 0
                self.current_state = CurrentState.MOVE
            if pygame.key.get_pressed()[pygame.K_4]:
                self.animation_frame_count = 0
                self.current_state = CurrentState.ATTACK_STANDBY
            if pygame.key.get_pressed()[pygame.K_5]:
                self.animation_frame_count = 0
                self.current_state = CurrentState.ATTACK
            if pygame.key.get_pressed()[pygame.K_6]:
                self.animation_frame_count = 0
                self.current_state = CurrentState.MAGIC_STANDBY
            if pygame.key.get_pressed()[pygame.K_7]:
                self.animation_frame_count = 0
                self.current_state = CurrentState.MAGIC_ATTACK
            if pygame.key.get_pressed()[pygame.K_8]:
                self.animation_frame_count = 0
                self.current_state = CurrentState.LIMIT_BREAK
            if pygame.key.get_pressed()[pygame.K_q]:
                self.animation_frame_count = 0
                self.current_state = CurrentState.DYING
            if pygame.key.get_pressed()[pygame.K_w]:
                self.animation_frame_count = 0
                self.current_state = CurrentState.DEAD
            if pygame.key.get_pressed()[pygame.K_e]:
                self.animation_frame_count = 0
                self.current_state = CurrentState.WIN
            if pygame.key.get_pressed()[pygame.K_r]:
                self.animation_frame_count = 0
                self.current_state = CurrentState.WIN_END

    def attack(self, enemy: Character):
        pass


class YSortedGroup(pygame.sprite.Group):
    def __init__(self) -> None:
        super().__init__()
        self.display_surface = pygame.display.get_surface()

    def draw(self, surface):
        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            self.display_surface.blit(sprite.image, sprite.rect)

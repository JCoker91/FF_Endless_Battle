from __future__ import annotations

import pygame
from random import randint
from util.custom_enum import CurrentState, PlayerSide
from util.util_functions import load_image_folder
from models.particle.particle import Particle
from models.floating_text.damage_text import DamageText


class Character(pygame.sprite.Sprite):
    def __init__(self, character_name: str, stats: dict, position: tuple, side: PlayerSide, off_set: dict, attack_effects: dict, group: pygame.sprite.Group) -> None:
        super().__init__()
        self.base_stats = stats.copy()
        self.current_stats = stats.copy()
        self.attack_effects = attack_effects
        self.name = character_name  # Character name
        self.side = side  # Which side the character is on (left or right)
        # Determines where the character will load on the screen
        self.starting_spot = position
        self.current_state = CurrentState.IDLE  # Determines animation states
        self.animation_frame_count = 0  # The count used to loop through the animations
        self.focused = False  # Determines if the player has focus on the character
        self.direction = pygame.math.Vector2()
        self.damage_taken_frame = []
        self.is_moving = False
        self.damage_frame = False
        self.has_fallen = False
        self.is_taking_damage = False
        self.is_attacking = False
        self.is_dying = False
        self.move_speed = 10
        self.floating_text_group = None
        self.set_offset = None
        self.particle_action_count = 0
        self.move_to = None
        self.particle_list = []
        if self.side == PlayerSide.RIGHT:

            self.off_set = off_set['right']
        else:
            self.off_set = off_set['left']
        # Load sprite animations
        self.animations = {
            'icon': [],
            'idle': [],
            'attack': [],
            'attack_standby': [],
            'magic_attack': [],
            'magic_standby': [],
            'dying': [],
            'dead': [],
            'limit_break': [],
            'move': [],
            'jump': [],
            'win': [],
            'win_end': []
        }
        self.load_images()
        self.base_rect = None

        if self.side == PlayerSide.RIGHT:
            self.image = self.animations['idle'][0]
            self.rect = self.image.get_rect(bottomright=self.starting_spot)
            self.hit_area = (
                self.starting_spot[0] - 200, self.starting_spot[1])
        else:
            self.image = pygame.transform.flip(
                self.animations['idle'][0], True, False)
            self.rect = self.image.get_rect(bottomleft=self.starting_spot)
            self.hit_area = (
                self.starting_spot[0] + 200, self.starting_spot[1])

        # Timers
        self.mouse_click_timer = None
        self.mouse_click_cool_down = 300
        self.can_click = True
        group.add(self)

    def __str__(self):
        return self.name

    def load_images(self):
        self.icon = pygame.image.load(
            f'resources/images/sprites/{self.name}/skin_1/icon/tile000.png')
        for animation in list(self.animations.keys()):
            animation_images = load_image_folder(
                f'resources/images/sprites/{self.name}/skin_1/{animation}')
            for image in animation_images:
                self.animations[animation].append(image)

    def animate(self):
        if self.focused:
            match self.current_state:
                case CurrentState.IDLE:
                    if self.side == PlayerSide.RIGHT:
                        self.image = self.animations['idle'][int(
                            self.animation_frame_count)]
                    else:
                        self.image = pygame.transform.flip(
                            self.animations['idle'][int(self.animation_frame_count)], 1, 0)
                    self.animation_frame_count += .08
                    if self.animation_frame_count >= len(self.animations['idle']):
                        self.animation_frame_count = 0
                case CurrentState.ATTACK:
                    if self.side == PlayerSide.RIGHT:
                        self.image = self.animations['attack'][int(
                            self.animation_frame_count)]

                    elif self.side == PlayerSide.LEFT:
                        self.image = pygame.transform.flip(
                            self.animations['attack'][int(self.animation_frame_count)], 1, 0)

                    self.animation_frame_count += .25
                    if self.animation_frame_count >= len(self.animations['attack']):
                        self.animation_frame_count = 0
                        self.is_attacking = False
                case CurrentState.LIMIT_BREAK:
                    if self.side == PlayerSide.RIGHT:
                        self.image = self.animations['limit_break'][int(
                            self.animation_frame_count)]
                    else:
                        self.image = pygame.transform.flip(
                            self.animations['limit_break'][int(self.animation_frame_count)], 1, 0)
                    self.animation_frame_count += .25
                    if self.animation_frame_count >= len(self.animations['limit_break']):
                        self.animation_frame_count = 0
                        self.current_state = CurrentState.IDLE
                case CurrentState.ATTACK_STANDBY:
                    if self.side == PlayerSide.RIGHT:
                        self.image = self.animations['attack_standby'][int(
                            self.animation_frame_count)]
                    else:
                        self.image = pygame.transform.flip(
                            self.animations['attack_standby'][int(self.animation_frame_count)], 1, 0)
                    self.animation_frame_count += .08
                    if self.animation_frame_count >= len(self.animations['attack_standby']):
                        self.animation_frame_count = 0
                case CurrentState.MAGIC_STANDBY:
                    if self.side == PlayerSide.RIGHT:
                        self.image = self.animations['magic_standby'][int(
                            self.animation_frame_count)]
                    else:
                        self.image = pygame.transform.flip(
                            self.animations['magic_standby'][int(self.animation_frame_count)], 1, 0)
                    self.animation_frame_count += .08
                    if self.animation_frame_count >= len(self.animations['magic_standby']):
                        self.animation_frame_count = 0
                case CurrentState.MAGIC_ATTACK:
                    if self.side == PlayerSide.RIGHT:
                        self.image = self.animations['magic_attack'][int(
                            self.animation_frame_count)]
                    else:
                        self.image = pygame.transform.flip(
                            self.animations['magic_attack'][int(self.animation_frame_count)], 1, 0)
                    self.animation_frame_count += .08
                    if self.animation_frame_count >= len(self.animations['magic_attack']):
                        self.animation_frame_count = 0
                        self.current_state = CurrentState.IDLE
                case CurrentState.DYING:
                    if self.side == PlayerSide.RIGHT:
                        self.image = self.animations['dying'][int(
                            self.animation_frame_count)]
                    else:
                        self.image = pygame.transform.flip(
                            self.animations['dying'][int(self.animation_frame_count)], 1, 0)
                    self.animation_frame_count += .08
                    if self.animation_frame_count >= len(self.animations['dying']):
                        self.animation_frame_count = 0
                case CurrentState.DEAD:
                    if self.side == PlayerSide.RIGHT:
                        self.image = self.animations['dead'][int(
                            self.animation_frame_count)]
                    else:
                        self.image = pygame.transform.flip(
                            self.animations['dead'][int(self.animation_frame_count)], 1, 0)
                    self.animation_frame_count += .08
                    if self.animation_frame_count >= len(self.animations['dead']):
                        self.animation_frame_count = 0
                case CurrentState.JUMP:
                    if self.side == PlayerSide.RIGHT:
                        self.image = self.animations['jump'][int(
                            self.animation_frame_count)]
                    else:
                        self.image = pygame.transform.flip(
                            self.animations['jump'][int(self.animation_frame_count)], 1, 0)
                    self.animation_frame_count += .08
                    if self.animation_frame_count >= len(self.animations['jump']):
                        self.animation_frame_count = 0
                case CurrentState.MOVE:
                    if self.side == PlayerSide.RIGHT:
                        self.image = self.animations['move'][int(
                            self.animation_frame_count)]
                    else:
                        self.image = pygame.transform.flip(
                            self.animations['move'][int(self.animation_frame_count)], 1, 0)
                    self.animation_frame_count += .08
                    if self.animation_frame_count >= len(self.animations['move']):
                        self.animation_frame_count = 0
                case CurrentState.WIN:
                    if self.side == PlayerSide.RIGHT:
                        self.image = self.animations['win'][int(
                            self.animation_frame_count)]
                    else:
                        self.image = pygame.transform.flip(
                            self.animations['win'][int(self.animation_frame_count)], 1, 0)
                    self.animation_frame_count += .15
                    if self.animation_frame_count >= len(self.animations['win']):
                        self.animation_frame_count = 0
                        self.current_state = CurrentState.WIN_END
                case CurrentState.WIN_END:
                    if self.side == PlayerSide.RIGHT:
                        self.image = self.animations['win_end'][int(
                            self.animation_frame_count)]
                    else:
                        self.image = pygame.transform.flip(
                            self.animations['win_end'][int(self.animation_frame_count)], 1, 0)
                    self.animation_frame_count += .15
                    if self.animation_frame_count >= len(self.animations['win_end']):
                        self.animation_frame_count = 0

    def adjust_offset(self):
        if self.set_offset:
            self.rect.x += self.off_set[self.set_offset][0]
            self.rect.y += self.off_set[self.set_offset][1]
            self.set_offset = None

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
                self.is_attacking = True
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

    def take_damage(self, damage_data: dict):
        self.is_taking_damage = True
        self.taking_damage_duration = damage_data['attack_len']
        self.particle_action_frames = damage_data['particle_action_frames']
        self.damage_taken = damage_data['damage']
        self.damage_weight = damage_data['damage_weight']
        self.floating_text_group = damage_data['floating_text_group']
        for i, particle in enumerate(damage_data['particle_effects']):
            self.damage_taken_frame.append(self.calculate_weighted_damage(
                self.damage_weight, i, self.damage_taken))
            new_particle = Particle(
                particle, damage_data['particle_list_group'])
            self.particle_list.append(new_particle)

    def calculate_weighted_damage(self, damage_weight: list, index: int, total_damage: int):
        total_weight = 0
        for damage in damage_weight:
            total_weight += damage
        damage = int((damage_weight[index]/total_weight) * total_damage)
        modifier = randint(-20, 20)
        return int((100 + modifier)/100 * damage)

    def display_damage(self):
        if self.is_taking_damage:
            if self.damage_frame == self.particle_action_frames[self.particle_action_count]:
                self.particle_list[self.particle_action_count].create(
                    self.rect.center)
                DamageText(
                    str(self.damage_taken_frame[self.particle_action_count]), self.rect.center, self.floating_text_group)
                self.current_stats['hp'] -= self.damage_taken_frame[self.particle_action_count]
                if self.current_stats['hp'] < 0.3 * self.base_stats['hp']:
                    self.is_dying = True
                if self.current_stats['hp'] < 1:
                    self.has_fallen = True
                    self.is_dying = False
                self.particle_action_count += 1
            self.damage_frame += .25
            if self.particle_action_count >= len(self.particle_action_frames):
                self.damage_frame = 0
                self.particle_action_frames = 0
                self.is_taking_damage = False
                self.particle_action_count = 0
                self.taking_damage_duration = 0
                self.particle_list.clear()

    def cool_downs(self):
        if not self.can_click:
            timer = pygame.time.get_ticks()
            if timer - self.mouse_click_timer > self.mouse_click_cool_down:
                self.can_click = True

    def switch_animation(self, animation: CurrentState):
        if self.current_state != animation:
            self.animation_frame_count = 0
            self.current_state = animation
            if animation == CurrentState.ATTACK:
                if not self.base_rect:
                    self.base_rect = self.rect.copy()
                    self.set_offset = 'attack'
            if animation == CurrentState.DYING:
                self.set_offset = 'dying'
                if self.base_rect:
                    self.rect = self.base_rect
                    self.base_rect = None
            if animation == CurrentState.DEAD:
                self.set_offset = 'dead'
                if self.base_rect:
                    self.rect = self.base_rect
                    self.base_rect = None
            if animation == CurrentState.IDLE:
                self.set_offset = 'idle'
                if self.base_rect:
                    self.rect = self.base_rect
                    self.base_rect = None

    # def get_distance_to_move_point(self, move_point: tuple):
    #     move_point_vector = pygame.math.Vector2(move_point)
    #     player_vector = pygame.math.Vector2(self.rect.midbottom)
    #     distance = (player_vector - move_point_vector).magnitude()

    #     if distance > 0:
    #         direction = (move_point_vector - player_vector).normalize()
    #     else:
    #         distance = 0
    #         direction = pygame.math.Vector2()
    #     return (distance, direction)

    # def move(self, move_point: tuple):
    #     if self.direction.magnitude() != 0:
    #         self.direction = self.direction.normalize()
    #     vector = self.get_distance_to_move_point(move_point)
    #     self.direction = vector[1]
    #     self.distance = vector[0]
    #     self.move_to = (move_point[0], move_point[1])
    #     self.is_moving = True

    # def move_sprite(self):
    #     if self.is_moving and self.move_to:
    #         self.switch_animation(CurrentState.MOVE)
    #         self.rect.x += self.direction.x * self.move_speed
    #         self.rect.y += self.direction.y * self.move_speed
    #         if self.rect.collidepoint(self.move_to):
    #             self.is_moving = False
    #             self.move_to = None

    def switch_action(self):
        if self.is_attacking:
            self.switch_animation(CurrentState.ATTACK)
        elif self.is_dying:
            self.switch_animation(CurrentState.DYING)
        elif self.has_fallen:
            self.switch_animation(CurrentState.DEAD)
        else:
            self.switch_animation(CurrentState.IDLE)

    def update(self):
        self.adjust_offset()
        self.input()
        self.display_damage()
        self.switch_action()
        self.animate()
        self.cool_downs()


class YSortedGroup(pygame.sprite.Group):
    def __init__(self) -> None:
        super().__init__()
        self.display_surface = pygame.display.get_surface()

    def draw(self, surface):
        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            self.display_surface.blit(sprite.image, sprite.rect)

from __future__ import annotations

import pygame
from random import randint
from source.util.custom_enum import CurrentState, PlayerSide, DamageType
from source.util.util_functions import load_image_folder
from source.models.particle.particle import Particle
from source.models.floating_text.damage_text import DamageText


class Character(pygame.sprite.Sprite):
    def __init__(self, character_name: str, stats: dict, position: tuple, side: PlayerSide, off_set: dict, attack_effects: dict, group: pygame.sprite.Group) -> None:
        super().__init__()
        self.base_stats = stats.copy()
        self.current_stats = stats.copy()
        self.attack_effects = attack_effects
        self.break_bar = 100
        self.name = character_name  # Character name
        self.side = side  # Which side the character is on (left or right)
        # Determines where the character will load on the screen
        self.starting_spot = position
        self.current_state = CurrentState.IDLE  # Determines animation states
        self.animation_frame_count = 0  # The count used to loop through the animations
        self.focused = False  # Determines if the player has focus on the character
        self.direction = pygame.math.Vector2()
        self.damage_taken_frame = []
        self.break_damage_taken_frame = []
        self.is_moving = False
        self.damage_frame = False
        self.has_fallen = False
        self.is_taking_damage = False
        self.is_broken = False
        self.is_attacking = False
        self.is_dying = False
        self.move_speed = 10
        self.floating_text_group = None
        self.color_counter = 150
        self.color_counter_2 = 150
        self.color_counter_3 = 150
        self.color_counter_increment = True
        self.color_counter_increment_2 = True
        self.color_counter_increment_3 = True
        self.set_offset = None
        self.particle_action_count = 0
        self.move_to = None
        self.menu_action = ['ATTACK', 'SPECIAL',
                            'MAGIC', 'DEFEND', 'ITEM', 'LIMIT BREAK']
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
            case CurrentState.BROKEN:
                if self.side == PlayerSide.RIGHT:
                    self.image = self.animations['dying'][int(
                        self.animation_frame_count)]
                else:
                    self.image = pygame.transform.flip(
                        self.animations['dying'][int(self.animation_frame_count)], 1, 0)
                self.animation_frame_count += .15
                if self.animation_frame_count >= len(self.animations['dying']):
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

    # def change_sprite_color(self):
    #     if self.is_broken:
    #         if self.color_counter_increment:
    #             self.color_counter += 2
    #             if self.color_counter >= 253:
    #                 self.color_counter_increment = False
    #         else: 
    #             self.color_counter -=2
    #             if self.color_counter < 150:
    #                 self.color_counter = 150
    #                 self.color_counter_increment = True
    #         coloured_image = pygame.Surface(self.image.get_size())
    #         coloured_image.fill((self.color_counter,0,0))

    #         final_image = self.image.copy()
    #         final_image.blit(coloured_image, (0, 0), special_flags = pygame.BLEND_MULT)
    #         self.image = final_image

    def change_sprite_color(self):
        if self.is_broken:
            if self.color_counter_increment:
                self.color_counter += 2
                if self.color_counter >= 253:
                    self.color_counter_increment = False
            else: 
                self.color_counter -=2
                if self.color_counter < 0:
                    self.color_counter = 0
                    self.color_counter_increment = True
            if self.color_counter_increment_2:
                self.color_counter_2 += 4
                if self.color_counter_2 >= 250:
                    self.color_counter_increment_2 = False
            else: 
                self.color_counter_2 -=4
                if self.color_counter_2 < 0:
                    self.color_counter_2 = 0
                    self.color_counter_increment_2 = True
            if self.color_counter_increment_3:
                self.color_counter_3 += 6
                if self.color_counter_3 >= 248:
                    self.color_counter_increment_3 = False
            else: 
                self.color_counter_3 -=6
                if self.color_counter_3 < 0:
                    self.color_counter_3= 0
                    self.color_counter_increment_3 = True
            coloured_image = pygame.Surface(self.image.get_size())
            coloured_image.fill((self.color_counter,self.color_counter_2,self.color_counter_3))

            final_image = self.image.copy()
            final_image.blit(coloured_image, (0, 0), special_flags = pygame.BLEND_MULT)
            self.image = final_image
            

    def adjust_offset(self):
        if self.set_offset:
            self.rect.x += self.off_set[self.set_offset][0]
            self.rect.y += self.off_set[self.set_offset][1]
            self.set_offset = None

    def input(self):
        pass


    def take_damage(self, damage_data: dict):
        self.is_taking_damage = True
        self.taking_damage_duration = damage_data['attack_len']
        self.particle_action_frames = damage_data['particle_action_frames']
        self.damage_weight = damage_data['damage_weight']
        self.floating_text_group = damage_data['floating_text_group']
        for i, particle in enumerate(damage_data['particle_effects']):
            self.damage_taken_frame.append(self.calculate_weighted_damage(
                self.damage_weight, i, damage_data['damage']))
            self.break_damage_taken_frame.append(self.calculate_weighted_damage(
                self.damage_weight, i, damage_data['break_damage']))
            new_particle = Particle(
                particle, damage_data['particle_list_group'])
            self.particle_list.append(new_particle)

    def calculate_weighted_damage(self, damage_weight: list, index: int, total_damage: int):
        total_weight = 0
        for damage in damage_weight:
            total_weight += damage
        damage = int((damage_weight[index]/total_weight) * total_damage)
        modifier = randint(-20, 20)
        return max(1, int((100 + modifier)/100 * damage))

    def display_damage(self):
        if self.is_taking_damage:
            if self.damage_frame == self.particle_action_frames[self.particle_action_count]:
                self.particle_list[self.particle_action_count].create(
                    self.rect.center)
                damage = self.damage_taken_frame[self.particle_action_count]
                damage_type = None
                if self.is_broken:
                    damage += int(damage * .5)
                    damage_type = DamageType.BREAK
                if self.break_bar > 0 and self.break_bar - self.break_damage_taken_frame[self.particle_action_count] < 0:
                    DamageText("BREAK", self.rect.center,
                               self.floating_text_group, DamageType.BREAK)
                DamageText(
                    str(damage), self.rect.center, self.floating_text_group, damage_type)
                self.current_stats['hp'] -= damage
                self.break_bar -= self.break_damage_taken_frame[self.particle_action_count]
                if self.break_bar < 0:
                    self.is_broken = True
                    self.break_bar = 0
                if self.current_stats['hp'] < 0.3 * self.base_stats['hp']:
                    self.is_dying = True
                if self.current_stats['hp'] < 1:
                    self.has_fallen = True
                    self.is_broken = False
                    self.is_dying = False
                    self.current_stats['hp'] = 0
                self.particle_action_count += 1
            self.damage_frame += .25
            if self.particle_action_count >= len(self.particle_action_frames):
                self.damage_frame = 0
                self.particle_action_frames = 0
                self.is_taking_damage = False
                self.particle_action_count = 0
                self.taking_damage_duration = 0
                self.particle_list.clear()
                self.damage_taken_frame.clear()

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
            if animation == CurrentState.DYING or animation == CurrentState.BROKEN:
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

    def switch_action(self):
        if self.is_attacking:
            self.switch_animation(CurrentState.ATTACK)
        elif self.has_fallen:
            self.switch_animation(CurrentState.DEAD)
        elif self.is_dying:
            self.switch_animation(CurrentState.DYING)
        elif self.is_broken:
            self.switch_animation(CurrentState.BROKEN)
        else:
            self.switch_animation(CurrentState.IDLE)

    def update(self):
        self.adjust_offset()
        self.input()
        self.display_damage()
        self.switch_action()
        self.animate()
        self.change_sprite_color()
        self.cool_downs()

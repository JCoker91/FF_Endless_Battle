import pygame
from settings import *
from source.models.character.character import Character


class Attack:
    def __init__(self, particle_effects: list, particle_action_frames: list, damage_weight: list, particle_list_group: pygame.sprite.Group, floating_text_group: pygame.sprite.Group):
        self.particle_effects = particle_effects
        self.particle_action_frames = particle_action_frames
        self.damage_weight = damage_weight
        self.name = "Attack"
        self.particle_list_group = particle_list_group
        self.floating_text_group = floating_text_group
        self.turn_adjust = 0

    def execute(self, caster: Character, enemy: Character, ):
        caster.is_attacking = True
        damage = max(
            int(caster.current_stats['strength'] - (enemy.current_stats['defense'] * DEFENSE_MOD)), 1)
        break_damage = caster.current_stats['break_power']
        damage_data = {
            'damage': damage,
            'break_damage': break_damage,
            'attack_len': len(caster.animations['attack']),
            'particle_effects': self.particle_effects,
            'particle_action_frames': self.particle_action_frames,
            'damage_weight': self.damage_weight,
            'particle_list_group': self.particle_list_group,
            'floating_text_group': self.floating_text_group,
        }
        caster.turn_adjust += self.turn_adjust
        enemy.take_damage(damage_data)


class SparkStrike:
    def __init__(self, particle_effects: list, particle_action_frames: list, damage_weight: list, particle_list_group: pygame.sprite.Group, floating_text_group: pygame.sprite.Group) -> None:
        self.particle_effects = particle_effects
        self.particle_action_frames = particle_action_frames
        self.damage_weight = damage_weight
        self.name = "Spark Strike"
        self.particle_list_group = particle_list_group
        self.floating_text_group = floating_text_group
        self.turn_adjust = 1
        self.mp_cost = 20

        self.description = "Attack with high break power. If the target is broken from this ability, instantly gain another turn."

    def execute(self, caster: Character, enemy: Character):
        caster.is_attacking = True
        damage = max(int(
            caster.current_stats['strength'] - (enemy.current_stats['defense'] * DEFENSE_MOD)), 1)
        break_damage = caster.current_stats['break_power'] * 3
        damage_data = {
            'damage': damage,
            'break_damage': break_damage,
            'attack_len': len(caster.animations['attack']),
            'particle_effects': self.particle_effects,
            'particle_action_frames': self.particle_action_frames,
            'damage_weight': self.damage_weight,
            'particle_list_group': self.particle_list_group,
            'floating_text_group': self.floating_text_group,
            'damage_type': 'lightning'
        }
        caster.turn_adjust += self.turn_adjust
        caster.current_stats['mp'] -= self.mp_cost
        assert(caster.current_stats['mp'] >= 0)
        if enemy.break_bar > 0 and enemy.break_bar - break_damage <= 0:
            caster.turn_adjust = INSTANT_TURN_ADJUST
        enemy.take_damage(damage_data)

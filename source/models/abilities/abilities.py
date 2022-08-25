import pygame
from settings import *
from source.models.character.character import Character
from source.util.custom_enum import DamageType


class Ability:
    def __init__(self, particle_effects: list, particle_action_frames: list, damage_weight: list, particle_list_group: pygame.sprite.Group, floating_text_group: pygame.sprite.Group) -> None:
        self.particle_effects = particle_effects
        self.particle_action_frames = particle_action_frames
        self.damage_weight = damage_weight
        self.particle_list_group = particle_list_group
        self.floating_text_group = floating_text_group
        self.turn_adjust = 0
        self.mp_cost = 0
        self.damage_type = DamageType.NEUTRAL
        self.name = "None"
        self.description = "None"
        self.target_count = "single"

    def calculate_resistance(self, damage: int, enemy: Character) -> int:
        match self.damage_type:
            case DamageType.LIGHTNING:
                final_damage = int(
                    damage * enemy.current_resistance['lightning']/100)
            case DamageType.WATER:
                final_damage = int(
                    damage * enemy.current_resistance['water']/100)
        return final_damage


class Attack(Ability):
    def __init__(self, particle_effects: list, particle_action_frames: list, damage_weight: list, particle_list_group: pygame.sprite.Group, floating_text_group: pygame.sprite.Group) -> None:
        super().__init__(particle_effects, particle_action_frames,
                         damage_weight, particle_list_group, floating_text_group)
        self.name = "Attack"

    def execute(self, caster: Character, enemy: Character):
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
            'damage_type': DamageType.NEUTRAL
        }
        caster.turn_adjust += self.turn_adjust
        enemy.take_damage(damage_data)


class SparkStrike(Ability):
    def __init__(self, particle_effects: list, particle_action_frames: list, damage_weight: list, particle_list_group: pygame.sprite.Group, floating_text_group: pygame.sprite.Group) -> None:
        super().__init__(particle_effects, particle_action_frames,
                         damage_weight, particle_list_group, floating_text_group)
        self.name = "Spark Strike"
        self.description = "Attack with high break power. If the target is broken from this ability, instantly gain another turn."
        self.turn_adjust = 1
        self.mp_cost = 20
        self.damage_type = DamageType.LIGHTNING
        self.damage_mod = 100
        self.break_mod = 300

    def execute(self, caster: Character, enemy: Character):
        caster.is_attacking = True
        break_damage = caster.current_stats['break_power'] * (self.break_mod/100)
        base_damage = caster.current_stats['strength'] * (self.damage_mod/100)
        base_damage = int(
            base_damage - ((enemy.current_stats['defense'] * DEFENSE_MOD)))
        resisted_damage = self.calculate_resistance(
            base_damage, enemy)
        final_damage = max(base_damage - resisted_damage, 1)
        damage_data = {
            'damage': final_damage,
            'break_damage': break_damage,
            'attack_len': len(caster.animations['attack']),
            'particle_effects': self.particle_effects,
            'particle_action_frames': self.particle_action_frames,
            'damage_weight': self.damage_weight,
            'particle_list_group': self.particle_list_group,
            'floating_text_group': self.floating_text_group,
            'damage_type': self.damage_type
        }
        caster.turn_adjust += self.turn_adjust
        caster.current_stats['mp'] -= self.mp_cost
        assert(caster.current_stats['mp'] >= 0)
        if enemy.break_bar > 0 and enemy.break_bar - break_damage <= 0:
            caster.turn_adjust = INSTANT_TURN_ADJUST
        enemy.take_damage(damage_data)


class JechtShot(Ability):
    def __init__(self, particle_effects: list, particle_action_frames: list, damage_weight: list, particle_list_group: pygame.sprite.Group, floating_text_group: pygame.sprite.Group) -> None:
        super().__init__(particle_effects, particle_action_frames,
                         damage_weight, particle_list_group, floating_text_group)
        self.name = "Jecht Shot"
        self.description = "Deal physical water damage to all enemies and reduce water resistance by 20% for 3 turns."
        self.turn_adjust = 0
        self.mp_cost = 30
        self.damage_type = DamageType.WATER
        self.target_count = 'all'
        self.damage_mod = 50
        self.break_mod = 50

    def execute(self, caster: Character, enemies: list[Character]):

        caster.is_attacking = True
        break_damage = caster.current_stats['break_power'] * (self.break_mod/100)
        for enemy in enemies:
            enemy.current_resistance['water'] -= 30
            base_damage = int(
                (caster.current_stats['strength'] * .5) - ((enemy.current_stats['defense'] * DEFENSE_MOD)))
            resisted_damage = self.calculate_resistance(
                base_damage, enemy)
            final_damage = max(base_damage - resisted_damage, 1)
            damage_data = {
                'damage': final_damage,
                'break_damage': break_damage,
                'attack_len': len(caster.animations['attack']),
                'particle_effects': self.particle_effects,
                'particle_action_frames': self.particle_action_frames,
                'damage_weight': self.damage_weight,
                'particle_list_group': self.particle_list_group,
                'floating_text_group': self.floating_text_group,
                'damage_type': self.damage_type
            }
            enemy.take_damage(damage_data)
        caster.turn_adjust += self.turn_adjust
        caster.current_stats['mp'] -= self.mp_cost
        assert(caster.current_stats['mp'] >= 0)

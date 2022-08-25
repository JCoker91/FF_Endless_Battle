
import pygame
from source.models.character.character import Character
from source.util.custom_enum import DamageType
from source.models.abilities.abilities import *


class LimitBreak:
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

class ArmyOfOne(LimitBreak):
    def __init__(self, particle_effects: list, particle_action_frames: list, damage_weight: list, particle_list_group: pygame.sprite.Group, floating_text_group: pygame.sprite.Group) -> None:
        super().__init__(particle_effects, particle_action_frames, damage_weight, particle_list_group, floating_text_group)
        self.description = "Deals lightning damage to a single enemy, reduces their lightning resistance by 50%, and increases speed and grants lightning attribute to basic attacks for 5 turns."
        self.name = 'Army of One'
        self.turn_adjust = 1
        self.damage_type = DamageType.LIGHTNING
        self.damage_mod = 150
        self.break_mod = 300

    def execute(self, caster: Character, enemy: Character):
        caster.is_limit_breaking = True
        break_damage = caster.current_stats['break_power'] * (self.break_mod/100)

        enemy.current_resistance['lightning'] -= 50
        
        base_damage = int(
            (caster.current_stats['strength'] * 1) - ((enemy.current_stats['defense'] * DEFENSE_MOD)))
        resisted_damage = self.calculate_resistance(
            base_damage, enemy)
        final_damage = max(base_damage - resisted_damage, 1)
        damage_data = {
            'damage': final_damage,
            'break_damage': break_damage,
            'attack_len': len(caster.animations['limit_break']),
            'particle_effects': self.particle_effects,
            'particle_action_frames': self.particle_action_frames,
            'damage_weight': self.damage_weight,
            'particle_list_group': self.particle_list_group,
            'floating_text_group': self.floating_text_group,
            'damage_type': self.damage_type
        }
        enemy.take_damage(damage_data)
        caster.turn_adjust += self.turn_adjust
        caster.attack['attack'] = AttackPlusLightning(caster.attack['attack'].particle_effects, caster.attack['attack'].particle_action_frames, caster.attack['attack'].damage_weight, caster.attack['attack'].particle_list_group, caster.attack['attack'].floating_text_group)
        caster.limit_break_gauge = 0

        



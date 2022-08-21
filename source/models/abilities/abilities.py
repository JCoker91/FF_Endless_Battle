import pygame
from source.models.character.character import Character


class Attack:
    def __init__(self, particle_effects: list, partcicle_action_frames: list, damage_weight: list, particle_list_group: pygame.sprite.Group, floating_text_group: pygame.sprite.Group):
        self.particle_effects = particle_effects
        self.partcicle_action_frames = partcicle_action_frames
        self.damage_weight = damage_weight
        self.name = "Attack"
        self.particle_list_group = particle_list_group
        self.floating_text_group = floating_text_group
        self.turn_adjust = 2

    def execute(self, caster: Character, enemy: Character, ):
        caster.is_attacking = True
        damage = max(
            int(caster.current_stats['strength'] - (enemy.current_stats['defense'] * 0.3)), 1)
        damage_data = {
            'damage': damage,
            'break_damage': caster.current_stats['break_power'],
            'attack_len': len(caster.animations['attack']),
            'particle_effects': self.particle_effects,
            'particle_action_frames': self.partcicle_action_frames,
            'damage_weight': self.damage_weight,
            'particle_list_group': self.particle_list_group,
            'floating_text_group': self.floating_text_group,
        }
        caster.turn_adjust = self.turn_adjust
        enemy.take_damage(damage_data)


# def basic_attack(caster: Character, enemy: Character, particle_list_group: pygame.sprite.Group, floating_text_group: pygame.sprite.Group):
#     caster.is_attacking = True
#     damage = max(
#         int(caster.current_stats['strength'] - (enemy.current_stats['defense'] * 0.3)), 1)
#     damage_data = {
#         'damage': damage,
#         'break_damage': caster.current_stats['break_power'],
#         'attack_len': len(caster.animations['attack']),
#         'particle_effects': caster.attack_effects[0]['particle_effects'],
#         'particle_action_frames': caster.attack_effects[0]['particle_action_frames'],
#         'damage_weight': caster.attack_effects[0]['damage_weight'],
#         'particle_list_group': particle_list_group,
#         'floating_text_group': floating_text_group,
#     }
#     enemy.take_damage(damage_data)

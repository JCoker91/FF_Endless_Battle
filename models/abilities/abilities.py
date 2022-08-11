import pygame
from models.character.character import Character

def basic_attack(caster:Character, enemy: Character, particle_list_group: pygame.sprite.Group, floating_text_group: pygame.sprite.Group):
    caster.is_attacking = True
    damage_data = {
            'damage': 500,
            'attack_len': len(caster.animations['attack']),
            'particle_effects': caster.attack_effects['basic_attack']['particle_effects'],
            'particle_action_frames': caster.attack_effects['basic_attack']['particle_action_frames'],
            'damage_weight': caster.attack_effects['basic_attack']['damage_weight'],
            'particle_list_group': particle_list_group,
            'floating_text_group': floating_text_group,
        }
    enemy.take_damage(damage_data)

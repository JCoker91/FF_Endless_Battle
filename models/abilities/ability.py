import pygame
from models.character.character import Character

class Ability:
    def __init__(self,name:str,caster:Character, enemy: Character, particle_list_group: pygame.sprite.Group, floating_text_group: pygame.sprite.Group) -> None:
        self.name=name
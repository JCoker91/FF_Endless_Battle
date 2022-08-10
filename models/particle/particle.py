from tkinter import CENTER
import pygame
from util.util_functions import load_image_folder


class Particle(pygame.sprite.Sprite):
    def __init__(self, name, group) -> None:
        super().__init__()
        self.name = name
        self.animations = []
        self.load_images()
        self.image = self.animations[0]
        self.rect = self.image.get_rect()
        self.play_count = 0
        self.playing = False
        group.add(self)

    def create(self, pos):
        self.rect = self.image.get_rect(center=pos)
        self.playing = True

    def display(self):
        if self.playing:
            self.image = self.animations[self.play_count]
            self.play_count += 1
            if self.play_count >= len(self.animations):
                self.play_count = 0
                self.playing = False
                self.kill()

    def update(self) -> None:
        self.display()

    def load_images(self):
        self.animations = load_image_folder(
            f'resources/images/particle_effects/{self.name}/')

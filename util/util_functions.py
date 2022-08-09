import os
import pygame


def load_image_folder(folder_path: str):
    images = []
    for file in sorted(os.listdir(folder_path)):
        if file.endswith('.png') or file.endswith('.jpeg'):
            _image = pygame.image.load(
                os.path.join(folder_path, file)).convert()
            images.append(_image)
    return images

import pygame
import time


class Entity:
    texture = None
    rect = None
   
    def __init__(self, size, texturePath, position, opaque):
        self.rect = pygame.Rect(position, size)

        if len(texturePath) > 0 :
            if not opaque:
                self.texture = pygame.image.load(texturePath)
            elif opaque:
                self.texture = pygame.image.load(texturePath).convert_alpha()    


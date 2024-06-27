import pygame
import time


class Entity:
    texture = None
    invertedTexture = None
    rightTexture = None
    ID = None
    rect = None
    color = ""
   
    def __init__(self, size, texturePath, position, opaque, color="", scale=1, ID=0):
        self.rect = pygame.Rect(position, size)
        self.color = color
        self.ID = ID

        if len(texturePath) > 0 :
            if not opaque:
                self.texture = pygame.image.load(texturePath)
            elif opaque:
                self.texture = pygame.image.load(texturePath).convert_alpha()  

            self.texture = pygame.transform.scale(self.texture, (self.rect.w * scale, self.rect.h * scale))
        
# comment
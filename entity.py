import pygame
import time


class Entity:
    texture = None
    invertedTexture = None
    rightTexture = None
    ID = None
    rect = None
    color = ""
   
    def __init__(self, size, texturePath, position, opaque, color="", scale=1, ID=-1):
        self.rect = pygame.Rect(position, size)
        self.color = color
        self.ID = ID

        if len(texturePath) > 0 :
            if not opaque:
                self.texture = pygame.image.load(texturePath)
            elif opaque:
                self.texture = pygame.image.load(texturePath).convert_alpha()  

            self.texture = pygame.transform.scale(self.texture, (self.rect.w * scale, self.rect.h * scale))

    def getImage(self, spriteSheet, width, height, scale, color, frame):
        image = pygame.Surface((width, height)).convert_alpha()        
        image.blit(spriteSheet, (0, 0), ((frame * width), 0, width, height))    
       
        image = pygame.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(color)

        return image        
        
# comment
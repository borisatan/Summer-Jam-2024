import pygame
import entity

import pygame
import time


class Player(entity.Entity):
    rect = None
    animationType = 0
    velocity = None
    
    isMoving = False
    idle = True
    isInteracting = False
    invertSprite = False
    dead = False
    delete = False



    def jump(self):
        if self.isJumping:
            self.rect.y -= self.velocity.y
            self.velocity.y -= self.gravity

            if self.velocity.y < -self.jumpHeight:
                self.isJumping = False
                self.velocity.y = self.jumpHeight   


    def getImage(self, spriteSheet, width, height, scale, color, frame):
        image = pygame.Surface((width, height)).convert_alpha()        
        image.blit(spriteSheet, (0, 0), ((frame * width), 0, width, height))    
       
        image = pygame.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(color)

        return image
    
    def getPlayerSpriteSubFunction(self, imagePath,  listRange):    
        black = (0, 0, 0)
        spriteList = []

        imagePathLocal = "images/Player/.png"[:14] + imagePath + "images/Player/.png"[14:]
        image = pygame.image.load(imagePathLocal)
        for i in range(listRange):
            spriteList.append(self.getImage(image, 200, 200, 3, black, i)) # load sprites to list

        return spriteList    
     
    def getPlayerSprites(self):
        self.idleSprites = self.getPlayerSpriteSubFunction("idle", 8)
        # self.jumpSprites = self.getPlayerSpriteSubFunction("Jump", 2)
        # self.interactSprites = self.getPlayerSpriteSubFunction("Interact", 2)
        # self.runSprites = self.getPlayerSpriteSubFunction("Run", 8)

        return self.idleSprites[0] # for initialization

    def invert(self):
        # if self.rect.x > player.rect.x:    on click a, d
        #     self.invertSprite = True
        # else:
        #     self.invertSprite = False

        if self.invertSprite:
            self.texture = pygame.transform.flip(self.texture, True, False)
            self.texture.set_colorkey((0, 0, 0))

    def setAnimation(self):
        if self.isInteracting:
            self.animationType = 0

        elif self.isJumping: 
            self.animationType = 1
            
        elif self.isMoving:
            self.animationType = 2   

        elif self.idle: 
            self.animationType = 3



    def createAnimations(self, currentSprite, spriteList, animationSpeed):
        currentSprite += animationSpeed

        if currentSprite >= len(spriteList):
            currentSprite = 0

        self.texture = spriteList[int(currentSprite)]    
        return currentSprite 
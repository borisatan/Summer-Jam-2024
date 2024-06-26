import pygame
import entity

import time

# LINE 66

class Player(entity.Entity):
    rect = None
    animationType = 0
    velocity = pygame.Vector2(10, 17)
    
    isMoving = False
    idle = True
    isInteracting = False
    invertSprite = False
    dead = False
    delete = False
    
    currentIdleSprite = 0
    idleSprites = []


    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rect.x -= self.velocity.x
            self.invertSprite = True
            self.isMoving = True

        elif keys[pygame.K_d]:
            self.rect.x += self.velocity.x
            self.invertSprite = False
            self.isMoving = True

        else:
            self.isMoving = False

        if keys[pygame.K_SPACE]:
            self.isJumping = True  


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
    
    def getPlayerSpriteSubFunction(self, imagePath, listRange):    
        black = (0, 0, 0)
        spriteList = []

        image = pygame.image.load(imagePath)
        for i in range(listRange):
            spriteList.append(self.getImage(image, 24, 24, 3.5, black, i)) # load sprites to list 

        return spriteList    
     
    def getPlayerSprites(self):
        self.idleSprites = self.getPlayerSpriteSubFunction("Assets/Blue/idle.png", 4)
        # self.jumpSprites = self.getPlayerSpriteSubFunction("Jump", 2)
        # self.interactSprites = self.getPlayerSpriteSubFunction("Interact", 2)
        self.runSprites = self.getPlayerSpriteSubFunction("Assets/Blue/run.png", 5)

        return self.idleSprites[0] # for initialization

    def invert(self):
        if self.invertSprite:
            self.texture = self.invertedTexture
        else:
            self.texture = self.rightTexture    
            
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
    

    def animate(self):
        self.texture = self.createAnimations(self.currentIdleSprite, self.idleSprites, 0.2)
        
        self.texture = self.createAnimations(self.currentRunSprite, self.runSprites, 0.2)
        
        
    def playerActions(self, game):
        self.update()
        self.invert()
        game.draw(self, (self.rect.x, self.rect.y))
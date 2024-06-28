import pygame
import entity

class Lever(entity.Entity):
    animationType = 0
    currentSprite = 0

    def interact(self, player):
        if player.isInteracting and player.color == self.color and self.rect.colliderect(player.rect):
            return True
        return False


    def getSpriteSubFunction(self, imagePath, listRange):    
        black = (0, 0, 0)
        spriteList = []

        image = pygame.image.load(imagePath)
        for i in range(listRange):
            spriteList.append(self.getImage(image, 32, 20, 3.5, black, i)) # load sprites to list 

        return spriteList    
    
    def getSprites(self):      
        self.blueToRedSprites = self.getSpriteSubFunction("Assets/Switch/Blue_To_Red.png", 4)
        self.redToBlueSprites = self.getSpriteSubFunction("Assets/Switch/Red_To_Blue.png", 4)
        self.greenToYellowSprites = self.getSpriteSubFunction("Assets/Switch/Green_To_Yellow.png", 4)
        self.yellowToGreenSprites = self.getSpriteSubFunction("Assets/Switch/Yellow_To_Green.png", 4)

        match self.color:
            case "Blue":
                return self.blueToRedSprites[0]
            case "Red":
                return self.redToBlueSprites[0]
            case "Green":
                return self.greenToYellowSprites[0]
            case "Yellow":
                return self.yellowToGreenSprites[0]

        return 1   
    
    def setAnimations(self, player):
        if self.interact(player):
            match self.color:
                case "Blue":
                    self.animationType = 1
                case "Red":
                    self.animationType = 2
                case "Green":
                    self.animationType = 3
                case "Yellow":
                    self.animationType = 4


    def createAnimations(self, currentSprite, spriteList, animationSpeed):
        currentSprite += animationSpeed

        if currentSprite >= len(spriteList):
            currentSprite = 0
            match self.animationType:
                case 1:
                    self.color = "Red"
                    self.texture = self.redToBlueSprites[0]
                    
                case 2:
                    self.color = "Blue"
                    self.texture = self.blueToRedSprites[0]
                
                case 3:
                    self.color = "Yellow"
                    self.texture = self.yellowToGreenSprites[0]
                
                case 4:
                    self.color = "Green"
                    self.texture = self.greenToYellowSprites[0]
                
    

            self.animationType = 0
            self.currentSprite = 0
            return currentSprite


        self.texture = spriteList[int(currentSprite)]    
        return currentSprite     

    def animate(self):
        match self.animationType:
            case 1:
                self.currentSprite = self.createAnimations(self.currentSprite, self.blueToRedSprites, 0.2) 
            case 2:
                self.currentSprite = self.createAnimations(self.currentSprite, self.redToBlueSprites, 0.2)    
            case 3:
                self.currentSprite = self.createAnimations(self.currentSprite, self.greenToYellowSprites, 0.15)    
            case 4:
                self.currentSprite = self.createAnimations(self.currentSprite, self.yellowToGreenSprites, 0.15)   

    def leverActions(self, player, game):
        self.interact(player)
        self.setAnimations(player)
        self.animate()    
        game.draw(self, (self.rect.x, self.rect.y))                               
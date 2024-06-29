import pygame
import entity

class Box(entity.Entity):
    animationType = 0
    currentSprite = 0
    sprites = []

    def interact(self, player):
        if player.color == self.color and self.rect.colliderect(player.rect):
            return True 
        return False

    def getImage(self, spriteSheet, width, height, scale, color, frame):
        image = pygame.Surface((width, height)).convert_alpha()        
        image.blit(spriteSheet, (0, 0), (16, (frame * height), width, height))    
       
        image = pygame.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(color)

        return image    

    def getSpriteSubFunction(self, imagePath, listRange):    
        black = (0, 0, 0)
        spriteList = []

        image = pygame.image.load(imagePath)
        for i in range(listRange):
            spriteList.append(self.getImage(image, 16, 16, 5, black, i)) # load sprites to list 

        return spriteList    
    
    def getSprites(self):      
        self.sprites = self.getSpriteSubFunction("Assets/Switch/Color_Blocks.png", 4)

        match self.color:
            case "Red":
                self.texture = self.sprites[0]
            case "Blue":
                self.texture = self.sprites[1]
            case "Green":
                self.texture = self.sprites[2]
            case "Yellow":
                self.texture = self.sprites[3]

        return 1
    
    def update(self, player):
        if self.interact(player):
            if self.rect.x > player.rect.x:
                self.rect.x += player.velocity.x
            elif self.rect.x < player.rect.x:
                self.rect.x -= player.velocity.x
                    

    def boxActions(self, player, game):
        self.update(player)
        game.draw(self, (self.rect.x, self.rect.y))                

import pygame
import random
import game
import entity
import player
import lever

# Before Starting the Game
game = game.Game()

def loadEntities(): 
    global player3, player4, ground, lever

    player3 = player.Player((75 - 8 * 3.5, 132 - 8 * 3.5), "", (25, game.resolution.y - 167), False, "Green", ID=1)  # place (0, 0) in the position variable
    player3.texture = player3.getPlayerSprites() 
    player4 = player.Player((75 - 8 * 3.5, 132 - 8 * 3.5), "", (25, game.resolution.y - 167), False, "Yellow", ID=2)  # place (0, 0) in the position variable
    player4.texture = player4.getPlayerSprites() 

    ground = entity.Entity((1797, 32), "Assets\Tiles\Ground.png", (0, game.resolution.y - 32 * 2), False, scale=2)
    lever = lever.Lever((70, 70), "", (200, game.resolution.y - (32 * 2 + 60)), False, "Green")
    lever.texture = lever.getSprites()
    
def collisions(players, solidObjects):
    for i in players:
        for j in solidObjects:
            if i.rect.colliderect(j):
                
                if i.rect.y + i.rect.h > j.rect.y:
                    print("collision")
                    i.rect.y = j.rect.y - i.rect.h


loadEntities()
while True:
    while game.startMenu:       
        game.startMenu()
    
    game.getEvent()
    game.draw(game.background)
    collisions([player3, player4], [ground])
    player3.playerActions(game)
    lever.leverActions(player3, game)   

    player4.playerActions(game)
    lever.leverActions(player4, game)  
    game.draw(ground, (ground.rect.x, ground.rect.y))



    game.gameActions([player3, player4])

# Animaciite bachkat i mojesh da skachash, sega v construktura kazvash cvqt kato string (see line 12 in main.py) i tva vzima suotvetnite spritove
# ID kato int v entity classa ot 1-4 se setva v construktora, 0 - default i pokazva che ne e dinozavur a e drugo entity primerno lever/tile 
# 1 - Blue
# 2 - Red 
# 3 - Green
# 4 - Yellow   
import pygame
import random
import game
import entity
import player
import lever

# Before Starting the Game
game = game.Game()

def loadEntities(): 
    match game.level:
        case 1:
            global player3, player4, ground, lever, players, levers

            player3 = player.Player((75 - 8 * 3.5, 132 - 8 * 3.5), "", (25, game.resolution.y - 167), False, "Green", ID=0)  # place (0, 0) in the position variable
            player3.texture = player3.getPlayerSprites() 
            player4 = player.Player((75 - 8 * 3.5, 132 - 8 * 3.5), "", (25, game.resolution.y - 167), False, "Yellow", ID=1)  # place (0, 0) in the position variable
            player4.texture = player4.getPlayerSprites() 

            players = [player3, player4]

            ground = entity.Entity((1797, 32), "Assets\Tiles\Ground.png", (0, game.resolution.y - 32 * 2), False, scale=2)
            lever1 = lever.Lever((70, 70), "", (200, game.resolution.y - (32 * 2 + 60)), False, "Green")
            lever1.texture = lever1.getSprites()

            levers = [lever1]
    
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
    collisions(players, [ground])

    for i in players:
        i.playerActions(game)
        for j in levers:
            j.leverActions(i, game)

    game.draw(ground, (ground.rect.x, ground.rect.y))



    game.gameActions(players)

# Animaciite bachkat i mojesh da skachash, sega v construktura kazvash cvqt kato string (see line 12 in main.py) i tva vzima suotvetnite spritove
# ID kato int v entity classa ot 0-3 se setva v construktora, -1 - default i pokazva che ne e dinozavur a e drugo entity primerno lever/tile 
# 0 - Green
# 1 - Yellow   
# 2 - Blue
# 3 - Red 
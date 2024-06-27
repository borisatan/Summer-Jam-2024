import pygame
import random
import game
import entity
import player
import lever

# Before Starting the Game
game = game.Game()

def loadEntities(): 
    global player, ground, lever

    player = player.Player((75 - 8 * 3.5, 132 - 8 * 3.5), "", (25, game.resolution.y - 167), False, "Green", 2)  # place (0, 0) in the position variable
    player.texture = player.getPlayerSprites() 

    ground = entity.Entity((1797, 32), "Assets\Tiles\Ground.png", (0, game.resolution.y - 32 * 2), False, scale=2)
    lever = lever.Lever((70, 70), "", (200, game.resolution.y - (32 * 2 + 60)), False, "Green")
    lever.texture = lever.getSprites()
    


loadEntities()
while True:
    while game.startMenu:       
        game.startMenu()
    
    game.getEvent()
    game.draw(game.background)
    player.playerActions(game)
    lever.leverActions(player, game)    
    game.draw(ground, (ground.rect.x, ground.rect.y))



    game.gameActions()

# Animaciite bachkat i mojesh da skachash, sega v construktura kazvash cvqt kato string (see line 12 in main.py) i tva vzima suotvetnite spritove
# ID kato int v entity classa ot 1-4 se setva v construktora, 0 - default i pokazva che ne e dinozavur a e drugo entity primerno lever/tile 
# 1 - Blue
# 2 - Green
# 3 - Red 
# 4 - Yellow   
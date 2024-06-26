import pygame
import random
import game
import entity
import player
import platform
# Before Starting the Game
game = game.Game()

def loadEntities():
    global player
    player = player.Player((75, 132), "", (25, game.resolution.y - 131), False, "Blue", 1)  # place (0, 0) in the position variable
    player.texture = player.getPlayerSprites() 


loadEntities()
while True:
    while game.startMenu:       
        game.startMenu()
    
    game.getEvent()
    game.draw(game.background)
    player.playerActions(game)
    
    game.gameActions()

# Animaciite bachkat i mojesh da skachash, sega v construktura kazvash cvqt i tva zima suotvetnite spritove
# ID kato int v entity classa ot 0-3 se setva v construktora i 
# 1 - Blue
# 2 - Green
# 3 - Red 
# 4 - Yellow   
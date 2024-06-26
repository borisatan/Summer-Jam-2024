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
    player = player.Player((75, 132), "", (25, game.resolution.y - 131), False)  # place (0, 0) in the position variable
    player.texture = player.getPlayerSprites()


loadEntities()
while True:
    while game.startMenu:       
        game.startMenu()
    
    game.getEvent()
    game.draw(game.background)
    player.playerActions(game)
    
    game.gameActions()
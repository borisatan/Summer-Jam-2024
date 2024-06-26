import pygame
import random
import game
import entity
import player

# Before Starting the Game
game = game.Game()

def loadEntities():
    global player
    player = player.Player((75, 132), "", (25, game.resolution.y - 131), False)  # place (0, 0) in the position variable
    player.texture = player.getPlayerSprites()

    player.rightTexture = player.texture
    player.invertedTexture = pygame.transform.flip(player.texture, True, False).convert_alpha()   

loadEntities()
while True:
    while game.startMenu:       
        game.startMenu()
    
    game.getEvent()
    game.draw(game.background)
    player.playerActions(game)
    
    game.gameActions()
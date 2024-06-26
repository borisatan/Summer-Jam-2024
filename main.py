import pygame
import random
import game

# Before Starting the Game
game = game.Game()

while True:
    while game.startMenu:    
        game.startMenu()
    
        
    
    game.getEvent()
    game.update()
    game.clock.tick(60)
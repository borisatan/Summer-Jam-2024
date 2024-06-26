import pygame
import random
import game
import button
import entity

def staticloadEntities():
    global PlayBtn, ControlsBtn, QuitBtn, backgrounds

    backgrounds = [] 
    
    for i in range(2):
        backgrounds.append(entity.Entity(game.resolution, "Assets/background/Background.png",(i * game.resolution.x, 0), True))
        
def draw():
    game.drawMultiple(backgrounds, (0, 0))
        
def scrollBackgrounds(backgrounds, player, game):
    if player.outOfBounds(game):
        if backgrounds[1].rect.x <= 0:
            backgrounds[0].rect.x = backgrounds[1].rect.x + backgrounds[1].rect.width
        if backgrounds[0].rect.x <= 0:
            backgrounds[1].rect.x = backgrounds[0].rect.x + backgrounds[0].rect.width    
        

        for i in range(0, 2):
            backgrounds[i].rect.x -= backgrounds[i].scrollSpeed
# Before Starting the Game
game = game.Game()
staticloadEntities()

while True:
    while game.startMenu:       
        game.startMenu()
    
    game.getEvent()

    draw()
    # scrollBackgrounds(backgrounds,)

    game.update()
    game.clock.tick(60)
 
import pygame
import menuButton
import entity
import time

class Game:
    resolution = pygame.Vector2(1797, 1009)
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(resolution)
    delay = time.time()
    currentID = 0
    level = 1
    startMenu = True
    PlayBtn = None
    CreditsBtn = None
    QuitBtn = None
    background = None
    platform = None

    def __init__(self):
        pygame.init()  
        pygame.display.set_caption("game")
        self.background = entity.Entity(self.resolution, "Assets/background/Background.png", (0, 0), False)

        self.PlayBtn = menuButton.Button(image=None, pos=(self.resolution.x / 2, 400), text_input="Play", font=self.get_font(75), base_color="#da5e53", hover_color="#683b4c")           
        self.CreditsBtn = menuButton.Button(image=None, pos=(self.resolution.x / 2, 500), text_input="Credits", font=self.get_font(75), base_color="#da5e53", hover_color="#683b4c")       
        self.QuitBtn = menuButton.Button(image=None, pos=(self.resolution.x / 2, 600), text_input="Quit", font=self.get_font(75), base_color="#da5e53", hover_color="#683b4c")

    def get_font(self, size):
        return pygame.font.Font("Font/retro_computer_personal_use.ttf", size)        
        
    def getEvent(self): # This is how you get keyboard input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

    def draw(self, subject, position=(0, 0)):
        self.screen.blit(subject.texture, position) 

    def startMenu(self):
        MenuMousePosition = pygame.mouse.get_pos()
        MenuText = self.get_font(100).render("main menu", True, "#ffffff")
        MenuRect = MenuText.get_rect(center = (self.resolution.x / 2, 300))

                
        self.screen.blit(MenuText, MenuRect)

        for button in [self.PlayBtn, self.CreditsBtn, self.QuitBtn]:
            button.changeColor(MenuMousePosition)
            button.update(self.screen)
        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.PlayBtn.checkForInput(MenuMousePosition):
                        self.startMenu = 0
                        pygame.time.delay(200)
                    if self.CreditsBtn.checkForInput(MenuMousePosition):
                        pass
                    if self.QuitBtn.checkForInput(MenuMousePosition):
                        pygame.quit()
                        exit()

        pygame.display.update()         

    def changePlayer(self, players):
        keys = pygame.key.get_pressed()
        someoneJumping = False
        someoneInteracting = False

        for i in players:
            if i.isJumping:
                someoneJumping = True
            if i.isInteracting:
                someoneInteracting = True    

        if keys[pygame.K_TAB] and not someoneJumping and not someoneInteracting and time.time() - self.delay > 0.2:
            for i in players:
                i.idle = True
                i.isRunning = False
                i.velocity = pygame.Vector2(6, 17)
                i.gravity = 1
                i.jumpHeight = 17
            
            self.delay = time.time()
            self.currentID += 1

    def update(self):
        pygame.display.update()

    def gameActions(self, players):
        self.update()
        self.changePlayer(players)
        self.clock.tick(60)  

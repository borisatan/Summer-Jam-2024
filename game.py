import pygame
import button


class Game:
    resolution = pygame.Vector2(1800, 950)
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(resolution)
    startMenu = True
    PlayBtn = None
    CreditsBtn = None
    QuitBtn = None

    def __init__(self):
        pygame.init()  
        pygame.display.set_caption("game")

        self.PlayBtn = button.Button(image=None, pos=(self.resolution.x / 2, 400), text_input="Play", font=self.get_font(75), base_color="#da5e53", hover_color="#683b4c")           
        self.CreditsBtn = button.Button(image=None, pos=(self.resolution.x / 2, 500), text_input="Credits", font=self.get_font(75), base_color="#da5e53", hover_color="#683b4c")       
        self.QuitBtn = button.Button(image=None, pos=(self.resolution.x / 2, 600), text_input="Quit", font=self.get_font(75), base_color="#da5e53", hover_color="#683b4c")

    def get_font(self, size):
        return pygame.font.Font("Font/retro_computer_personal_use.ttf", size)        
        
    def getEvent(self): # This is how you get keyboard input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()


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


    def update(self):
        pygame.display.update()

"""
Main module
Mainly used for controlling pygame events and dusplays
"""
# pygame doc: https://www.pygame.org/docs/
import pygame
import os

# Pycharm runs an interactive session, therefore it must reach a pygame.quit statement
# Otherwise, pycharm freezes and closes the game window
# Therefore, needs a while loop listening for events, such as pygame.quit
# Taken from http://pygametutorials.wikidot.com/tutorials-basic
# EVERYTHING IN PYGAME IS A SURFACE
# All colors in pygame are rgb
# Never forget to pygame.display.update so that new generated surfaces can be seen



# Must pass the desired width and height of the game window when creating a new instance of Game
class Game:
    def __init__(self, width, height):
        '''
        @param width: width of the game window
        @param height: height of the game window
        '''
        self.running=True
        self.display_stuff = None
        self.size = self.width, self.height = width, height

    def on_init(self):
        pygame.init()

        # pygame.display.set_caption sets the name of the window that opened
        pygame.display.set_caption("A Beautiful Game")

        # Everything in the game will be layered on that screen
        self.screen = pygame.display.set_mode(self.size)

        # Clock to keep time in the game (delays, turns, etc.)
        self.clock = pygame.time.Clock()

        # Set big and small fonts for the display
        self.bigFont = pygame.font.SysFont("monospace", 50)
        self.smallFont = pygame.font.SysFont("monospace", 30)

        # Set the button colors
        self.brightButton = (255,0,0)
        self.darkButton = (200,0,0)

        # Set the button size
        self.buttonWidth = 0.3 * self.width
        self.buttonHeight = 0.15 * self.height

        # Home screen text alignement
        self.alignLeft = (0.1*self.width)
        self.alignCenter = (0.5*self.width)

        # Display home screen where we select the game to play
        self.displayHomeScreen()

        # Ready to run the Game
        self.running = True

    def on_event(self, event):
        # pygame.QUIT is the event for pressing the big red X in the corner of the page
        if event.type == pygame.QUIT:
            self.running = False

        # Brighten up the game buttons on the home screen when hovered
        if event.type == pygame.MOUSEMOTION and self.homeScreen:
            posi_mouse = event.pos
            self.BrightenUpButtons(posi_mouse)




    def BrightenUpButtons(self, posi_mouse):
        """
        Based on the position of the mouse, brightens up the buttons on the home screen
        Adds an interactive effect
        """
        mouse_x = posi_mouse[0]
        mouse_y = posi_mouse[1]

        # Is the self.game_1_button being hovered?
        if (self.game_1_button.x < mouse_x < self.game_1_button.x + self.buttonWidth) and (
                self.game_1_button.y < mouse_y < self.game_1_button.y + self.buttonHeight):
            self.game_1_button = pygame.draw.rect(self.screen, self.brightButton,
                                                  (self.alignLeft, 200, self.buttonWidth, self.buttonHeight))
            self.screen.blit(self.nameGame1, (self.alignLeft, (200 + 0.25 * self.buttonHeight)))
            pygame.display.update()
        else:
            self.game_1_button = pygame.draw.rect(self.screen, self.darkButton,
                                                  (self.alignLeft, 200, self.buttonWidth, self.buttonHeight))
            self.screen.blit(self.nameGame1, (self.alignLeft, (200 + 0.25 * self.buttonHeight)))
            pygame.display.update()

        # Is the self.game_2_button being hovered?
        if (self.game_2_button.x < mouse_x < self.game_2_button.x + self.buttonWidth) and (
                self.game_2_button.y < mouse_y < self.game_2_button.y + self.buttonHeight):
            self.game_2_button = pygame.draw.rect(self.screen, self.brightButton,
                                                  (self.alignCenter, 200, self.buttonWidth, self.buttonHeight))
            self.screen.blit(self.nameGame2, (self.alignCenter, (200 + 0.25 * self.buttonHeight)))
            pygame.display.update()

        else:
            self.game_2_button = pygame.draw.rect(self.screen, self.darkButton,(self.alignCenter, 200, self.buttonWidth, self.buttonHeight))
            self.screen.blit(self.nameGame2, (self.alignCenter, (200 + 0.25 * self.buttonHeight)))
            pygame.display.update()





    def on_loop(self):
        pass

    def on_render(self):
        pass

    def on_cleanup(self):
        # ends everything and closes the program
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self.running = False

        # while we want to run the program, listen for events (e.g. mouse clicks)
        # after this loop, cleanup everything (meaning simply execute pygame.quit)
        while(self.running):
            for event in pygame.event.get():
                self.on_event(event)

            self.on_loop()
            self.on_render()
        self.on_cleanup()

    def displayHomeScreen(self):
        """
        Presents the Welcome screen.
        Lets the user choose what game he wants to play
        """
        # Registering that we are on the home screen
        self.homeScreen = True

        # background color
        self.screen.fill((0,128,0))

        # Text to display
        title = self.bigFont.render("Welcome to A Beautiful Game", True, (255,255,255))
        selection = self.smallFont.render("Please select a Game", True, (255,255,255))
        self.screen.blit(title, (self.alignLeft,0))
        self.screen.blit(selection, (self.alignLeft,100))

        # Create buttons to select the games (eventually, refactor into a list)
        self.game_1_button = pygame.draw.rect(self.screen, self.darkButton, (self.alignLeft, 200, self.buttonWidth, self.buttonHeight))
        self.game_2_button = pygame.draw.rect(self.screen, self.darkButton, (self.alignCenter, 200, self.buttonWidth, self.buttonHeight))

        # Add the text
        self.nameGame1 = self.smallFont.render("7 Cards Game", True, (255,255,255))
        self.nameGame2 = self.smallFont.render("Other Game", True, (255,255,255))
        self.screen.blit(self.nameGame1, (self.alignLeft,(200 + 0.25*self.buttonHeight)))
        self.screen.blit(self.nameGame2, (self.alignCenter,(200 + 0.25*self.buttonHeight)))

        # Update the whole display
        pygame.display.update()





# Executing the Game (creating an instance of the ''Game'' class)
if __name__ == "__main__":
    theGame = Game(1000,500)
    theGame.on_execute()





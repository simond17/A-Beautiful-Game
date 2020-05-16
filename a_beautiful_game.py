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

        # Display home screen where we select the game to play
        self.firstStart()

        # Ready to run the Game
        self.running = True

    def on_event(self, event):
        # pygame.QUIT is the event for pressing the big red X in the corner of the page
        if event.type == pygame.QUIT:
            self.running = False



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

    def firstStart(self):
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
        align_left = (0.1*self.width)
        align_center = (0.5*self.width)
        self.screen.blit(title, (align_left,0))
        self.screen.blit(selection, (align_left,100))

        # Create buttons to select the games (eventually, refactor into a list)
        button_width = 0.3*self.width
        button_height = 0.15*self.height
        self.game_1_button = pygame.draw.rect(self.screen, self.darkButton, (align_left, 200, button_width, button_height))
        self.game_2_button = pygame.draw.rect(self.screen, self.darkButton, (align_center, 200, button_width, button_height))

        # Add the text
        name_game_1 = self.smallFont.render("7 Cards Game", True, (255,255,255))
        name_game_2 = self.smallFont.render("Other Game", True, (255,255,255))
        self.screen.blit(name_game_1, (align_left,(200 + 0.25*button_height)))
        self.screen.blit(name_game_2, (align_center,(200 + 0.25*button_height)))

        # Update the whole display
        pygame.display.update()





# Executing the Game (creating an instance of the ''Game'' class)
if __name__ == "__main__":
    theGame = Game(1000,500)
    theGame.on_execute()





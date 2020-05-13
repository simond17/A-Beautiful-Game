"""
Main module
Mainly used for controlling pygame events and dusplays
"""
# pygame doc: https://www.pygame.org/docs/
import pygame

# Pycharm runs an interactive session, therefore it must reach a pygame.quit statement
# Otherwise, pycharm freezes and closes the game window
# Therefore, needs a while loop listening for events, such as pygame.quit
# Taken from http://pygametutorials.wikidot.com/tutorials-basic

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
        pygame.display.set_caption("A Beautiful Game")
        self.display_stuff = pygame.display.set_mode(self.size)
        self.running = True

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False

    def on_loop(self):
        pass

    def on_render(self):
        pass

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self.running = False

        while(self.running):
            for event in pygame.event.get():
                self.on_event(event)

            self.on_loop()
            self.on_render()
        self.on_cleanup()

if __name__ == "__main__":
    theGame = Game(1000,500)
    theGame.on_execute()



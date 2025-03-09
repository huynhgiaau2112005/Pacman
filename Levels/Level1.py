from EntitiesManager import EntitiesManager as EM
from Config import Config
import pygame

class Level1:
    def __init__(self):
        pass

    def setup(self):
        print("setup")

    def execute(self):
        self.setup()
        
        clock = pygame.time.Clock()

        while Config.running:
            Config.screen.fill('black')
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Config.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        print("Phím Q được ấn")
                        Config.running = False
                    if event.key == pygame.K_ESCAPE:
                        return
            EM().maze.draw()
            EM().pacman.draw()
            pygame.display.flip()
            clock.tick(Config.fps)
            #Entity.Pacman.keyboardHandle()
            #for ghost in Entity.ghosts:
            #ghost.move()
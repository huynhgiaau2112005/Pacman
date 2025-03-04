from EntitiesManager import EntitiesManager as EM
from Config import Config
import pygame

class Level4:
  def __init__(self):
    pass

  def execute(self):
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

      EM().maze.draw()

      EM().pacman.draw()

      EM().redGhost.updatePos()
      EM().redGhost.draw()

      pygame.display.flip()
      clock.tick(Config.fps)
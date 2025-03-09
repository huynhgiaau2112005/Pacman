from EntitiesManager import EntitiesManager as EM
from Config import Config
import pygame

class Level4:
  def __init__(self):
    pass

  def execute(self):
    clock = pygame.time.Clock()

    countFrames = 0
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
      
      if countFrames % 15 == 0:
        EM().redGhost.updatePos()
      
      EM().redGhost.move()

      EM().maze.draw()
      EM().pacman.draw()
      EM().redGhost.draw()

      pygame.display.flip()
      clock.tick(Config.fps)
      countFrames += 1
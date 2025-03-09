from Entities.Entity import Entity
from EntitiesManager import EntitiesManager as EM
from Config import Config, Object
import pygame

class Level4:
  def __init__(self):
    pass

  def setup(self):
    Object.redGhostX = 15
    Object.redGhostY = 15
    (Object.realRedGhostX, Object.realRedGhostY) = Entity.getRealCoordinates((Object.redGhostX, Object.redGhostY), Object.RED_GHOST_SIZE)

  def execute(self):
    self.setup()

    clock = pygame.time.Clock()
    path, numOfExpendedNodes = EM().redGhost.getTargetPathInformation((Object.redGhostX, Object.redGhostY), (Object.pacmanX, Object.pacmanY))
    step = 0

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
      
      targetX, targetY = path[step]
      curX, curY = Object.redGhostX, Object.redGhostY

      if countFrames % 15 == 0:
        if (curX, curY) == (targetX, targetY):
          if step < len(path) - 1:
            step += 1
            targetX, targetY = path[step]

        if (curX, curY) != (targetX, targetY):
          newX, newY = curX, curY
          if targetX != curX:
            newX += (targetX - curX) // abs(targetX - curX) 
          if targetY != curY:
            newY += (targetY - curY) // abs(targetY - curY)
          Object.redGhostX = newX
          Object.redGhostY = newY
          
      
      EM().redGhost.move()

      EM().maze.draw()
      EM().pacman.draw()
      EM().redGhost.draw()

      pygame.display.flip()
      clock.tick(Config.fps)
      countFrames += 1
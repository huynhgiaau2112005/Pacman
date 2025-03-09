from EntitiesManager import EntitiesManager as EM
from Entities.Entity import Entity
from Config import Config, Object
import pygame

class Level3:
  def __init__(self):
    pass

  def setup(self):
    print("setup")
  
  def execute(self):
    self.setup()
    
    clock = pygame.time.Clock()
    path, numberofExpandnodes = EM().orangeghost.getTargetPathInformation((Object.orangeGhostX, Object.orangeGhostY), (Object.pacmanX, Object.pacmanY))
    node = 0 
    print(path, numberofExpandnodes)
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
      
      oldX, oldY = Object.orangeGhostX, Object.orangeGhostY
      if countFrames % 15 == 0:
        
        if (node >= len(path)):
          continue
        
        moveX, moveY = path[node]
        node += 1
        
        if (oldX, oldY) != (moveX, moveY):
            newX, newY = oldX, oldY
            if moveX != oldX:
                newX += 1 if moveX > oldX else -1 
            if moveY != oldY:
                newY += 1 if moveY > oldY else -1 
        
            Object.orangeGhostX = newX
            Object.orangeGhostY = newY
      
      EM().orangeghost.move()

      EM().maze.draw()
      EM().pacman.draw()
      EM().orangeghost.draw() 
      
      pygame.display.flip()
      clock.tick(Config.fps)
      countFrames += 1
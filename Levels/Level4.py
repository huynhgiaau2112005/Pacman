from Entities.Entity import Entity
from EntitiesManager import EntitiesManager as EM
from Config import Config, Object, Sounds
import pygame
import time
import psutil #de lay bo nho
import os

BoxWidth = 420
BoxHeight = 160

boxX = (Config.width - BoxWidth) / 2
boxY = 150

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class Level4:
  def __init__(self):
    pass

  def setup(self):
    #(Object.pinkGhostX, Object.pinkGhostY) = (16, 13) #(6, 2) (30, 27) (27, 3) (21, 3)
    #(Object.pacmanX, Object.pacmanY) = (24, 14) #(24, 26) (4, 2) (29, 27) (15, 21)
    Object.redGhostX = 15
    Object.redGhostY = 15
    (Object.realRedGhostX, Object.realRedGhostY) = Entity.getRealCoordinates((Object.redGhostX, Object.redGhostY), Object.RED_GHOST_SIZE)

  def execute(self):
    self.setup()
    Sounds.ghost_move_sound.play(loops=-1)

    clock = pygame.time.Clock()

    # Lấy bộ nhớ trước
    process = psutil.Process(os.getpid())
    before_mem = process.memory_info().rss / (1024 * 1024)  # MB

    start_time = time.time()  # Lấy thời gian bắt đầu
    path, numOfExpendedNodes = EM().redGhost.getTargetPathInformation((Object.redGhostX, Object.redGhostY), (Object.pacmanX, Object.pacmanY))
    end_time = time.time()    # Lấy thời gian kết thúc

    # Lấy bộ nhớ sau
    after_mem = process.memory_info().rss / (1024 * 1024)  # MB
    
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

      if (Object.redGhostX, Object.redGhostY) == (Object.pacmanX, Object.pacmanY):
        Sounds.ghost_move_sound.stop()
        break

    font = pygame.font.Font(None, 35)
    algorithm = font.render("Algorithm: A*", True, BLACK)
    search_time = font.render(f"Search time: {end_time - start_time:.6f} seconds", True, BLACK)
    memory_usage = font.render(f"Memory usage: {after_mem - before_mem:.6f} MB", True, BLACK)
    num_expanded_nodes = font.render(f"Number of expanded nodes : {numOfExpendedNodes}", True, BLACK)

    while Config.running:
        pygame.draw.rect(Config.screen, (255, 153, 51), (boxX, boxY, BoxWidth, BoxHeight), border_radius=15)
        Config.screen.blit(algorithm, (boxX + 24, boxY + 22))
        Config.screen.blit(search_time, (boxX + 24, boxY + 22 + 30))
        Config.screen.blit(memory_usage, (boxX + 24, boxY + 22 + 60))
        Config.screen.blit(num_expanded_nodes, (boxX + 24, boxY + 22 + 90))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Config.running = False
            if event.type == pygame.KEYDOWN:
                return
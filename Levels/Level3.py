from EntitiesManager import EntitiesManager as EM
from Entities.Entity import Entity
from Config import Config, Object, Sounds
import pygame
import time
import psutil #de lay bo nho
import os
import pygame

BoxWidth = 420
BoxHeight = 160

boxX = (Config.width - BoxWidth) / 2
boxY = 150

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class Level3:
  def __init__(self):
    pass

  def setup(self):
    #(Object.pinkGhostX, Object.pinkGhostY) = (16, 13) #(6, 2) (30, 27) (27, 3) (21, 3)
    #(Object.pacmanX, Object.pacmanY) = (24, 14) #(24, 26) (4, 2) (29, 27) (15, 21) # Setup tọa độ ma trận

    Object.orangeGhostX = 6
    Object.orangeGhostY = 2
    Object.pacmanX = 24
    Object.pacmanY = 26

    # Setup tọa độ thực
    (Object.realPacmanX, Object.realPacmanY) = Entity.getRealCoordinates((Object.pacmanX, Object.pacmanY), Object.PACMAN_SIZE)
    (Object.realOrangeGhostX, Object.realOrangeGhostY) = Entity.getRealCoordinates((Object.orangeGhostX, Object.orangeGhostY), Object.ORANGE_GHOST_SIZE)

    # Setup ma trận Coordinates 
    Board.coordinates[Object.orangeGhostX][Object.orangeGhostY] = Board.ORANGE_GHOST
    Board.coordinates[Object.pacmanX][Object.pacmanY] = Board.PACMAN 

    for i in range (len(Board.coordinates)): # Chỉ giữ lại giá trị Pacman, OrangeGhost trong ma trận Coordinates, các giá trị còn lại bỏ
      for j in range (len(Board.coordinates[0])):
        if Board.coordinates[i][j] not in (Board.PACMAN, Board.ORANGE_GHOST):
            Board.coordinates[i][j] = Board.BLANK
  
  def execute(self):
    self.setup()
    Sounds.ghost_move_sound.play(loops=-1)

    clock = pygame.time.Clock()

    # Lấy bộ nhớ trước
    process = psutil.Process(os.getpid())
    before_mem = process.memory_info().rss / (1024 * 1024)  # MB

    start_time = time.time()  # Lấy thời gian bắt đầu
    path, numberofExpandnodes = EM().orangeghost.getTargetPathInformation((Object.orangeGhostX, Object.orangeGhostY), (Object.pacmanX, Object.pacmanY))
    end_time = time.time()    # Lấy thời gian kết thúc

    # Lấy bộ nhớ sau
    after_mem = process.memory_info().rss / (1024 * 1024)  # MB

    node = 0 
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

      if (Object.orangeGhostX, Object.orangeGhostY) == (Object.pacmanX, Object.pacmanY):
        Sounds.ghost_move_sound.stop()
        break

    font = pygame.font.Font(None, 35)
    algorithm = font.render("Algorithm: UCS", True, BLACK)
    search_time = font.render(f"Search time: {end_time - start_time:.6f} seconds", True, BLACK)
    memory_usage = font.render(f"Memory usage: {after_mem - before_mem:.6f} MB", True, BLACK)
    num_expanded_nodes = font.render(f"Number of expanded nodes : {numberofExpandnodes}", True, BLACK)

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

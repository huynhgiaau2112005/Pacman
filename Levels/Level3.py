from EntitiesManager import EntitiesManager as EM
from Entities.Entity import Entity
from Config import Config, Object, Sounds, Board
from Levels.ExperimentBox import ExperimentBox
import pygame
import time
import psutil #de lay bo nho
import os
import math
import pygame

# testcases: (ghost, pacman)
testcases = [((16, 13), (24, 14)),
             ((6, 2), (24, 26)),
             ((30, 27), (4, 2)),
             ((27, 3), (29, 27)),
             #((15, 20), (15, 21))]
             ((21, 3), (15, 21))]
testcaseID = 0

quit = False
start = False

class Level3:
  def __init__(self):
    pass

  def setup(self):
    Object.orangeGhostX, Object.orangeGhostY = testcases[testcaseID][0]
    Object.pacmanX, Object.pacmanY = testcases[testcaseID][1]

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
  
  def get_volume(self, ghost_x, ghost_y, pac_x, pac_y, max_distance=15):
    distance = math.sqrt((ghost_x - pac_x) ** 2 + (ghost_y - pac_y) ** 2)  
    volume = max(0.0, 1 - (distance / max_distance))  # 0.1 là âm lượng nhỏ nhất, 1 là lớn nhất
    return min(1.0, max(0.0, volume))  # Giới hạn từ 0.0 đến 1.0
    
  def execute(self):
    global quit, start

    quit = False
    start = False

    while Config.running and not quit:
      self.setup()

      Sounds().dramatic_theme_music()
      ghost_move_sound = pygame.mixer.Sound("Assets/sounds/ghost_move.mp3")

      clock = pygame.time.Clock()
      countFrames = 0

      # Lấy bộ nhớ trước
      process = psutil.Process(os.getpid())
      before_mem = process.memory_info().rss / (1024 * 1024)  # MB

      start_time = time.time()  # Lấy thời gian bắt đầu
      path, numberofExpandnodes = EM().orangeGhost.getTargetPathInformation((Object.orangeGhostX, Object.orangeGhostY), (Object.pacmanX, Object.pacmanY))
      end_time = time.time()    # Lấy thời gian kết thúc

      # Lấy bộ nhớ sau
      after_mem = process.memory_info().rss / (1024 * 1024)  # MB

      node = 0
      while Config.running:
        Config.screen.fill('black')
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            ghost_move_sound.stop()
            Sounds.dramatic_theme_music_sound.stop()
            Config.running = False
            return
          elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
              ghost_move_sound.stop()
              Sounds.dramatic_theme_music_sound.stop()
              quit = True
              return
            if event.key == pygame.K_q:
              ghost_move_sound.stop()
              Sounds.dramatic_theme_music_sound.stop()
              Config.running = False
              return
            if event.key == pygame.K_SPACE:
              if not start:
                ghost_move_sound.play(loops=-1)  # Lặp vô hạn
              start = True
      
        EM().maze.draw()

        if start:
          if countFrames % 15 == 0:
            if (node >= len(path)):
              continue
            
            moveX, moveY = path[node]
            node += 1
            
            oldX, oldY = Object.orangeGhostX, Object.orangeGhostY
            if (oldX, oldY) != (moveX, moveY):
              newX, newY = oldX, oldY
              if moveX != oldX:
                newX += 1 if moveX > oldX else -1 
              if moveY != oldY:
                newY += 1 if moveY > oldY else -1 
          
              Object.orangeGhostX = newX
              Object.orangeGhostY = newY
        
          EM().orangeGhost.move()

        EM().pacman.draw()
        EM().orangeGhost.draw() 
        
        if not start:
          color = (255, 255, 255 - countFrames % 30 * 8)
          labelFont = pygame.font.Font(None, 30)
          space_to_start = labelFont.render("PRESS SPACE TO START", True, color)
          Config.screen.blit(space_to_start, (Config.width / 2 - 130, Config.height / 2 - 50))

        pygame.display.flip()
        clock.tick(Config.fps)
        countFrames += 1

        if (Object.orangeGhostX, Object.orangeGhostY) == (Object.pacmanX, Object.pacmanY):
          ghost_move_sound.stop()
          Sounds.dramatic_theme_music_sound.stop()
          break

      start = False

      algorithm = "BFS"
      search_time = end_time - start_time
      memory_usage = after_mem - before_mem
      num_expanded_nodes = numberofExpandnodes
          
      while Config.running:
        nextTestcase = ExperimentBox().showResultBoard(algorithm, search_time, memory_usage, num_expanded_nodes)
        if nextTestcase == -1:
          quit = True
          break
        elif nextTestcase != None:
          global testcaseID
          testcaseID = nextTestcase
          break
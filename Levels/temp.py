from Entities.Entity import Entity
from EntitiesManager import EntitiesManager as EM
from Config import Config, Object, Sounds, Board
from collections import deque
import threading
import time
import pygame

start = False

class Level6:
    def __init__(self):
        self.ghosts = [EM().blueGhost, EM().redGhost, EM().pinkGhost, EM().orangeGhost]
        self.threads = []
        self.running = threading.Event()

    def setup(self):
        # Setup tọa độ thực
        (Object.realPacmanX, Object.realPacmanY) = Entity.getRealCoordinates((Object.pacmanX, Object.pacmanY), Object.PACMAN_SIZE)
        (Object.realRedGhostX, Object.realRedGhostY) = Entity.getRealCoordinates((Object.redGhostX, Object.redGhostY), Object.RED_GHOST_SIZE)
        (Object.realOrangeGhostX, Object.realOrangeGhostY) = Entity.getRealCoordinates((Object.orangeGhostX, Object.orangeGhostY), Object.ORANGE_GHOST_SIZE)
        (Object.realPinkGhostX, Object.realPinkGhostY) = Entity.getRealCoordinates((Object.pinkGhostX, Object.pinkGhostY), Object.PINK_GHOST_SIZE)
        (Object.realBlueGhostX, Object.realBlueGhostY) = Entity.getRealCoordinates((Object.blueGhostX, Object.blueGhostY), Object.BLUE_GHOST_SIZE)

        # Setup ma trận Coordinates
        Board.coordinates[Object.blueGhostX][Object.blueGhostY] = Board.BLUE_GHOST
        Board.coordinates[Object.pinkGhostX][Object.pinkGhostY] = Board.PINK_GHOST
        Board.coordinates[Object.orangeGhostX][Object.orangeGhostY] = Board.ORANGE_GHOST
        Board.coordinates[Object.redGhostX][Object.redGhostY] = Board.RED_GHOST
        Board.coordinates[Object.pacmanX][Object.pacmanY] = Board.PACMAN 

        for i in range (len(Board.coordinates)): # Chỉ giữ lại giá trị Pacman, Red, Orange, Pink, BlueGhost trong ma trận Coordinates, các giá trị còn lại bỏ
            for j in range (len(Board.coordinates[0])):
                if Board.coordinates[i][j] not in (Board.PACMAN, Board.RED_GHOST) and \
                Board.coordinates[i][j] not in (Board.PACMAN, Board.ORANGE_GHOST) and \
                Board.coordinates[i][j] not in (Board.PACMAN, Board.PINK_GHOST) and \
                Board.coordinates[i][j] not in (Board.PACMAN, Board.BLUE_GHOST):
                    Board.coordinates[i][j] = Board.BLANK
    
    def isValidPos(self, x, y):
        if 0 <= x < Board.ROWS and 0 <= y < Board.COLS:
            if (Board.maze[x][y] < 3 or Board.maze[x][y] == 9) and Board.coordinates[x][y] in (Board.BLANK, Board.PACMAN):
                return True
        return False
    
    def move_ghost(self, ghost):
        clock = pygame.time.Clock()
        Sounds.ghost_move_sound.play(loops=-1)  # Lặp âm thanh ma di chuyển
        countFrames = 0
        
        while self.running.is_set():
            nx, ny = ghost.getTargetPos()
            if self.isValidPos(nx, ny):
                pass
            else:
                print(ghost.name())
            if countFrames % 15 == 0:
                if (nx, ny):
                    newPos = (nx, ny)
                    ghost.updatePosForEachLv(newPos)
                
                if ghost.getPos() == (Object.pacmanX, Object.pacmanY):
                    Sounds.ghost_move_sound.stop()
                    self.running.clear()
                    break
                
            ghost.move()
            clock.tick(Config.fps)
            countFrames += 1
        
    
    # def blueGhost(self):
    #     clock = pygame.time.Clock()
    #     Sounds.ghost_move_sound.play(loops=-1)  # Lặp vô hạn
    #     countFrames = 0

    #     while Config.running:
    #         for event in pygame.event.get():
    #             if event.type == pygame.QUIT:
    #                 Config.running = False
    #             elif event.type == pygame.KEYDOWN:
    #                 if event.key == pygame.K_ESCAPE:
    #                     return
            
    #         nx, ny = EM().blueGhost.getTargetPos((Object.blueGhostX, Object.blueGhostY), (Object.pacmanX, Object.pacmanY))
    #         if countFrames % 15 == 0:
    #             if (nx, ny):
    #                 newPos = (nx, ny)
    #                 EM().blueGhost.updatePosForEachLv(newPos)

    #         if (Object.blueGhostX, Object.blueGhostY) == (Object.pacmanX, Object.pacmanY):
    #             Sounds.ghost_move_sound.stop()
    #             break

    #         EM().blueGhost.move()
            
    #         clock.tick(Config.fps)
    #         countFrames += 1
            
    # def pinkGhost(self):
    #     clock = pygame.time.Clock()
    #     Sounds.ghost_move_sound.play(loops=-1)  # Lặp vô hạn
    #     countFrames = 0 # 0     
      
    #     while Config.running:
    #         for event in pygame.event.get():
    #             if event.type == pygame.QUIT:
    #                 Config.running = False
    #             elif event.type == pygame.KEYDOWN:
    #                 if event.key == pygame.K_q:
    #                     print("Phím Q được ấn")
    #                     Config.running = False
    #                 if event.key == pygame.K_ESCAPE:
    #                     Sounds.ghost_move_sound.stop()
    #                     return
            
    #         nx, ny = EM().pinkGhost.getTargetPos((Object.pinkGhostX, Object.pinkGhostY), (Object.pacmanX, Object.pacmanY))
    #         if countFrames % 15 == 0:
    #             if (nx, ny):
    #                 newPos = (nx, ny)
    #                 EM().pinkGhost.updatePosForEachLv(newPos)

    #         if (Object.pinkGhostX, Object.pinkGhostY) == (Object.pacmanX, Object.pacmanY):
    #             Sounds.ghost_move_sound.stop()
    #             break

    #         EM().pinkGhost.move()

    #         clock.tick(Config.fps)
    #         countFrames += 1
            
    # def orangeGhost(self):
    #     Sounds.ghost_move_sound.play(loops=-1)
    #     clock = pygame.time.Clock()
    #     countFrames = 0

    #     while Config.running:
    #         for event in pygame.event.get():
    #             if event.type == pygame.QUIT:
    #                 Config.running = False
    #             elif event.type == pygame.KEYDOWN:
    #                 if event.key == pygame.K_q:
    #                     print("Phím Q được ấn")
    #                     Config.running = False
    #                 if event.key == pygame.K_ESCAPE:
    #                     return
            
    #         oldX, oldY = Object.orangeGhostX, Object.orangeGhostY
    #         moveX, moveY = EM().orangeGhost.getTargetPos((Object.orangeGhostX, Object.orangeGhostY), (Object.pacmanX, Object.pacmanY))
             
    #         if countFrames % 15 == 0:        
                
    #             if (oldX, oldY) != (moveX, moveY):
    #                 newX, newY = oldX, oldY
    #                 if moveX != oldX:
    #                     newX += 1 if moveX > oldX else -1 
    #                 if moveY != oldY:
    #                     newY += 1 if moveY > oldY else -1 
                
    #                 Object.orangeGhostX = newX
    #                 Object.orangeGhostY = newY
            
    #         EM().orangeGhost.move()
    #         clock.tick(Config.fps)
    #         countFrames += 1

    #         if (Object.orangeGhostX, Object.orangeGhostY) == (Object.pacmanX, Object.pacmanY):
    #             Sounds.ghost_move_sound.stop()
    #             break
              
    # def redGhost(self):
    #     Sounds.ghost_move_sound.play(loops=-1)
    #     clock = pygame.time.Clock()   
    #     countFrames = 0

    #     while Config.running:

    #         #Config.screen.fill('black')

    #         for event in pygame.event.get():
    #             if event.type == pygame.QUIT:
    #                 Config.running = False
    #             elif event.type == pygame.KEYDOWN:
    #                 if event.key == pygame.K_q:
    #                     print("Phím Q được ấn")
    #                     Config.running = False
    #                 if event.key == pygame.K_ESCAPE:
    #                     return

    #         targetX, targetY = EM().redGhost.getTargetPos((Object.redGhostX, Object.redGhostY), (Object.pacmanX, Object.pacmanY))
    #         curX, curY = Object.redGhostX, Object.redGhostY
            
    #         if countFrames % 15 == 0:

    #             if (curX, curY) != (targetX, targetY):
    #                 newX, newY = curX, curY
    #                 if targetX != curX:
    #                     newX += (targetX - curX) // abs(targetX - curX) 
    #                 if targetY != curY:
    #                     newY += (targetY - curY) // abs(targetY - curY)
    #                 Object.redGhostX = newX
    #                 Object.redGhostY = newY
              
    #         EM().redGhost.move()
    #         clock.tick(Config.fps)
    #         countFrames += 1

    #         if (Object.redGhostX, Object.redGhostY) == (Object.pacmanX, Object.pacmanY):
    #             Sounds.ghost_move_sound.stop()
    #             break
    
    def pacman(self):
        clock = pygame.time.Clock()   
        countFrames = 0

        while self.running.is_set():
            
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                self.running.clear()
                break
            
            if countFrames % 15 == 0:
                EM().pacman.updatePos()
              
            EM().pacman.move()

            posGhost = [(Object.blueGhostX, Object.blueGhostY), (Object.pinkGhostX, Object.pinkGhostY), (Object.orangeGhostX, Object.orangeGhostY), (Object.redGhostX, Object.redGhostY)]
            if (Object.pacmanX, Object.pacmanY) in posGhost:
              Sounds.ghost_move_sound.stop()
              break
              
            clock.tick(Config.fps)
            countFrames += 1
    
    def draw(self):
        clock = pygame.time.Clock()

        while self.running.is_set():
            Config.screen.fill('black')

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running.clear()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        print("Phím Q được ấn")
                        self.running.clear()
                    if event.key == pygame.K_ESCAPE:
                        Sounds.ghost_move_sound.stop()
                        return

            EM().maze.draw()
            EM().pacman.draw()
            for ghost in self.ghosts:
                ghost.draw()

            pygame.display.flip()
            clock.tick(max(1, Config.fps - 30))
            
    def execute(self):
        global start
        self.setup()
        self.running.set()
        
        clock = pygame.time.Clock()
        Config.screen.fill('black')
        countFrames = 0
        waiting = True
        
        EM().maze.draw()
        EM().pacman.draw()
        EM().blueGhost.draw()
        EM().pinkGhost.draw()
        EM().orangeGhost.draw()
        EM().redGhost.draw()
        pygame.display.flip()

        # countFrames = 0
        # check = True
        while waiting:
          if not start:
            color = (255, 255, 255 - countFrames % 30 * 8)
            labelFont = pygame.font.Font(None, 30)
            space_to_start = labelFont.render("PRESS SPACE TO START", True, color)
            Config.screen.blit(space_to_start, (Config.width / 2 - 130, Config.height / 2 - 50))
            pygame.display.flip()
            clock.tick(Config.fps)
            countFrames += 1
            for event in pygame.event.get():
              if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                  start = True
                  waiting = False
        
        self.threads.append(threading.Thread(target=self.pacman))
        for ghost in self.ghosts:
            self.threads.append(threading.Thread(target=self.move_ghost, args=(ghost,)))

        for thread in self.threads:
            thread.start()

        self.draw()

        for thread in self.threads:
            thread.join()
        # Chạy 4 con ma đồng thời
        # thread0 = threading.Thread(target=self.pacman)
        # thread1 = threading.Thread(target=self.blueGhost)
        # thread2 = threading.Thread(target=self.pinkGhost)
        # thread3 = threading.Thread(target=self.orangeGhost)
        # thread4 = threading.Thread(target=self.redGhost)

        # thread0.start()
        # thread1.start()
        # thread2.start()
        # thread3.start()
        # thread4.start()

        # self.draw()

        # thread0.join()
        # thread1.join()  # Chờ thread1 kết thúc
        # thread2.join()  # Chờ thread2 kết thúc
        # thread3.join()
        # thread4.join()

from Entities.Entity import Entity
from EntitiesManager import EntitiesManager as EM
from Config import Config, Object, Sounds, Board
from collections import deque
import threading
import time
import pygame

start = False

class Level5:
    def __init__(self):
        pass

    def setup(self):
        # Setup tọa độ ma trận
        Object.blueGhostX = 6
        Object.blueGhostY = 2
        Object.pinkGhostX = 30
        Object.pinkGhostY = 27
        Object.orangeGhostX = 21#27
        Object.orangeGhostY = 4#3
        Object.redGhostX = 21
        Object.redGhostY = 3
        Object.pacmanX = 15
        Object.pacmanY = 21

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
        

    
    def blueGhost(self):
        clock = pygame.time.Clock()
        Sounds.ghost_move_sound.play(loops=-1)  # Lặp vô hạn
        countFrames = 0

        listPos = deque(EM().blueGhost.getTargetPathInformation((Object.blueGhostX, Object.blueGhostY), (Object.pacmanX, Object.pacmanY)))

        while Config.running:
            #Config.screen.fill('black')
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Config.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return
            if countFrames % 15 == 0:
                if listPos:
                    newPos = listPos.popleft()
                    EM().blueGhost.updatePosForEachLv(newPos)

            if (Object.blueGhostX, Object.blueGhostY) == (Object.pacmanX, Object.pacmanY):
                Sounds.ghost_move_sound.stop()
                break

            EM().blueGhost.move()

            # EM().maze.draw()
            # EM().pacman.draw()
            # EM().blueGhost.draw()
            
            # pygame.display.flip()
            clock.tick(Config.fps)
            countFrames += 1
    def pinkGhost(self):
        clock = pygame.time.Clock()
        Sounds.ghost_move_sound.play(loops=-1)  # Lặp vô hạn
        countFrames = 0 # 0     
        listPos = deque(EM().pinkGhost.getTargetPathInformation((Object.pinkGhostX, Object.pinkGhostY), (Object.pacmanX, Object.pacmanY)))   # Chạy thuật toán
        
        while Config.running:
           # Config.screen.fill('black')

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Config.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        print("Phím Q được ấn")
                        Config.running = False
                    if event.key == pygame.K_ESCAPE:
                        Sounds.ghost_move_sound.stop()
                        return
            
            if countFrames % 15 == 0:
                if listPos:
                    newPos = listPos.popleft()
                    EM().pinkGhost.updatePosForEachLv(newPos)

            if (Object.pinkGhostX, Object.pinkGhostY) == (Object.pacmanX, Object.pacmanY):
                Sounds.ghost_move_sound.stop()
                break

            EM().pinkGhost.move()

            # EM().maze.draw()
            # EM().pacman.draw()
            # EM().pinkGhost.draw()
            


            # pygame.display.flip()
            clock.tick(Config.fps)
            countFrames += 1
    def orangeGhost(self):
        Sounds.ghost_move_sound.play(loops=-1)
        clock = pygame.time.Clock()
        path, numberofExpandnodes = EM().orangeGhost.getTargetPathInformation((Object.orangeGhostX, Object.orangeGhostY), (Object.pacmanX, Object.pacmanY))
        node = 0 
        countFrames = 0

        while Config.running:
        
            #Config.screen.fill('black')
    
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
            
            EM().orangeGhost.move()

            # EM().maze.draw()
            # EM().pacman.draw()
            # EM().orangeghost.draw() 
            
            # pygame.display.flip()
            clock.tick(Config.fps)
            countFrames += 1

            if (Object.orangeGhostX, Object.orangeGhostY) == (Object.pacmanX, Object.pacmanY):
                Sounds.ghost_move_sound.stop()
                break
    def redGhost(self):
        Sounds.ghost_move_sound.play(loops=-1)
        clock = pygame.time.Clock()   
        path, numOfExpendedNodes = EM().redGhost.getTargetPathInformation((Object.redGhostX, Object.redGhostY), (Object.pacmanX, Object.pacmanY))
        step = 0
        countFrames = 0

        while Config.running:

            #Config.screen.fill('black')

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

            # EM().maze.draw()
            # EM().pacman.draw()
            # EM().redGhost.draw()

            # pygame.display.flip()
            clock.tick(Config.fps)
            countFrames += 1

            if (Object.redGhostX, Object.redGhostY) == (Object.pacmanX, Object.pacmanY):
                Sounds.ghost_move_sound.stop()
                break

    def draw(self):
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
                        Sounds.ghost_move_sound.stop()
                        return

            EM().maze.draw()
            EM().pacman.draw()
            EM().blueGhost.draw()
            EM().pinkGhost.draw()
            EM().orangeGhost.draw()
            EM().redGhost.draw()

            pygame.display.flip()
            clock.tick(Config.fps - 30)
    def execute(self):
        global start
        self.setup()
        clock = pygame.time.Clock()
        Config.screen.fill('black')
        EM().maze.draw()
        EM().pacman.draw()
        EM().blueGhost.draw()
        EM().pinkGhost.draw()
        EM().orangeGhost.draw()
        EM().redGhost.draw()
        pygame.display.flip()

        countFrames = 0
        check = True
        while check:
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
                  check = False

        # Chạy 4 con ma đồng thời
        thread1 = threading.Thread(target=self.blueGhost)
        thread2 = threading.Thread(target=self.pinkGhost)
        thread3 = threading.Thread(target=self.orangeGhost)
        thread4 = threading.Thread(target=self.redGhost)

        thread1.start()
        thread2.start()
        thread3.start()
        thread4.start()

        self.draw()

        thread1.join()  # Chờ thread1 kết thúc
        thread2.join()  # Chờ thread2 kết thúc
        thread3.join()
        thread4.join()

    

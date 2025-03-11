from EntitiesManager import EntitiesManager as EM
from Config import Config, Sounds, Object, Board
from collections import deque
from Entities.Entity import Entity
from Levels.ExperimentBox import ExperimentBox
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

class Level2:
    def __init__(self):
        pass

    def setup(self):
        #(Object.pinkGhostX, Object.pinkGhostY) = (16, 13) #(6, 2) (30, 27) (27, 3) (21, 3)
        #(Object.pacmanX, Object.pacmanY) = (24, 14) #(24, 26) (4, 2) (29, 27) (15, 21)
        
        # Setup tọa độ ma trận
        Object.pinkGhostX, Object.pinkGhostY = testcases[testcaseID][0]
        Object.pacmanX, Object.pacmanY = testcases[testcaseID][1]

        # Setup tọa độ thực
        (Object.realPacmanX, Object.realPacmanY) = Entity.getRealCoordinates((Object.pacmanX, Object.pacmanY), Object.PACMAN_SIZE)
        (Object.realPinkGhostX, Object.realPinkGhostY) = Entity.getRealCoordinates((Object.pinkGhostX, Object.pinkGhostY), Object.PINK_GHOST_SIZE)

        # Setup ma trận Coordinates 
        Board.coordinates[Object.pinkGhostX][Object.pinkGhostY] = Board.PINK_GHOST
        Board.coordinates[Object.pacmanX][Object.pacmanY] = Board.PACMAN 

        for i in range (len(Board.coordinates)): # Chỉ giữ lại giá trị Pacman, PinkGhost trong ma trận Coordinates, các giá trị còn lại bỏ
            for j in range (len(Board.coordinates[0])):
                if Board.coordinates[i][j] not in (Board.PACMAN, Board.PINK_GHOST):
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
            countFrames = 0 # 0

            # Lấy bộ nhớ trước
            process = psutil.Process(os.getpid())
            before_mem = process.memory_info().rss / (1024 * 1024)  # MB

            start_time = time.time()  # Lấy thời gian bắt đầu
            listPos, expanded_nodes = EM().pinkGhost.getTargetPathInformation((Object.pinkGhostX, Object.pinkGhostY), (Object.pacmanX, Object.pacmanY))   # Chạy thuật toán
            end_time = time.time()    # Lấy thời gian kết thúc

            # Lấy bộ nhớ sau
            after_mem = process.memory_info().rss / (1024 * 1024)  # MB

            listPos = deque(listPos)

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
                        if listPos:
                            newPos = listPos.popleft()
                            EM().pinkGhost.updatePosForEachLv(newPos)
                    volume = self.get_volume(Object.pinkGhostX, Object.pinkGhostY, Object.pacmanX, Object.pacmanY)
                    ghost_move_sound.set_volume(volume)
                    
                    EM().pinkGhost.move()

                EM().pacman.draw()
                EM().pinkGhost.draw()
                
                if not start:
                    color = (255, 255, 255 - countFrames % 30 * 8)
                    labelFont = pygame.font.Font(None, 30)
                    space_to_start = labelFont.render("PRESS SPACE TO START", True, color)
                    Config.screen.blit(space_to_start, (Config.width / 2 - 130, Config.height / 2 - 50))

                if not listPos:
                    ghost_move_sound.stop()
                    Sounds.dramatic_theme_music_sound.stop()
                    break

                pygame.display.flip()
                clock.tick(Config.fps)
                countFrames += 1
                
            start = False

            algorithm = "IDS"
            search_time = end_time - start_time
            memory_usage = after_mem - before_mem
            num_expanded_nodes = expanded_nodes
                
            while Config.running:
                nextTestcase = ExperimentBox().showResultBoard(algorithm, search_time, memory_usage, num_expanded_nodes)
                if nextTestcase == -1:
                    quit = True
                    break
                elif nextTestcase != None:
                    global testcaseID
                    testcaseID = nextTestcase
                    break

from EntitiesManager import EntitiesManager as EM
from Config import Config, Sounds, Object, Board
from collections import deque
from Entities.Entity import Entity
from Levels.ExperimentBox import ExperimentBox
import time
import tracemalloc #de lay bo nho
import os
import pygame
import math

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

class Level1:
    def __init__(self):
        pass

    def setup(self):
        # Setup tọa độ ma trận
        Object.blueGhostX, Object.blueGhostY = testcases[testcaseID][0]
        Object.pacmanX, Object.pacmanY = testcases[testcaseID][1]

        # Setup tọa độ thực
        (Object.realPacmanX, Object.realPacmanY) = Entity.getRealCoordinates((Object.pacmanX, Object.pacmanY), Object.PACMAN_SIZE)
        (Object.realBlueGhostX, Object.realBlueGhostY) = Entity.getRealCoordinates((Object.blueGhostX, Object.blueGhostY), Object.BLUE_GHOST_SIZE)

        # Setup ma trận Coordinates 
        Board.coordinates[Object.blueGhostX][Object.blueGhostY] = Board.BLUE_GHOST
        Board.coordinates[Object.pacmanX][Object.pacmanY] = Board.PACMAN 

        for i in range (len(Board.coordinates)): # Chỉ giữ lại giá trị Pacman, BlueGhost trong ma trận Coordinates, các giá trị còn lại bỏ
            for j in range (len(Board.coordinates[0])):
                if (i, j) not in ((Object.blueGhostX, Object.blueGhostY), (Object.pacmanX, Object.pacmanY)):
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

            # Bắt đầu đo bộ nhớ
            tracemalloc.start()

            start_time = time.time()  # Lấy thời gian bắt đầu
            listPos, expanded_nodes = EM().blueGhost.getTargetPathInformation((Object.blueGhostX, Object.blueGhostY), (Object.pacmanX, Object.pacmanY))   # Chạy thuật toán
            end_time = time.time()    # Lấy thời gian kết thúc

            # Lấy kết quả peak memory usage
            current, peak = tracemalloc.get_traced_memory()
            # Dừng đo
            tracemalloc.stop()

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
                            EM().blueGhost.updatePosForEachLv(newPos)
                    volume = self.get_volume(Object.blueGhostX, Object.blueGhostY, Object.pacmanX, Object.pacmanY)
                    ghost_move_sound.set_volume(volume)
                    
                    EM().blueGhost.move()

                EM().pacman.draw()
                EM().blueGhost.draw()
                
                if not start:
                    color = (255, 255, 255 - countFrames % 30 * 8)
                    labelFont = pygame.font.Font(None, 30)
                    space_to_start = labelFont.render("PRESS SPACE TO START", True, color)
                    Config.screen.blit(space_to_start, (Config.width / 2 - 130, Config.height / 2 - 50))

                if not listPos:
                    ghost_move_sound.stop()
                    Sounds.dramatic_theme_music_sound.stop()
                    # EM().blueGhost.move()

                    # EM().maze.draw()
                    # EM().pacman.draw()
                    # EM().blueGhost.draw()
                    # pygame.display.flip()
                    # #time.sleep(1)
                    break

                pygame.display.flip()
                clock.tick(Config.fps)
                countFrames += 1
            
            start = False

            algorithm = "BFS"
            search_time = end_time - start_time
            memory_usage = peak / (2 ** 20)
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


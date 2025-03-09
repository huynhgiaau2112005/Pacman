from EntitiesManager import EntitiesManager as EM
from Config import Config, Sounds, Object
from collections import deque
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

class Level1:
    def __init__(self):
        pass

    def setup(self):
        #(Object.pinkGhostX, Object.pinkGhostY) = (16, 13) #(6, 2) (30, 27) (27, 3) (21, 3)
        #(Object.pacmanX, Object.pacmanY) = (24, 14) #(24, 26) (4, 2) (29, 27) (15, 21)
        print("setup")

    def execute(self):
        self.setup()
        clock = pygame.time.Clock()
        Sounds.ghost_move_sound.play(loops=-1)  # Lặp vô hạn
        countFrames = 0

        # Lấy bộ nhớ trước
        process = psutil.Process(os.getpid())
        before_mem = process.memory_info().rss / (1024 * 1024)  # MB

        start_time = time.time()  # Lấy thời gian bắt đầu
        result = EM().blueGhost.getTargetPathInformation((Object.blueGhostX, Object.blueGhostY), (Object.pacmanX, Object.pacmanY))   # Chạy thuật toán
        end_time = time.time()    # Lấy thời gian kết thúc

        # Lấy bộ nhớ sau
        after_mem = process.memory_info().rss / (1024 * 1024)  # MB

        listPos = deque(EM().blueGhost.getTargetPathInformation((Object.blueGhostX, Object.blueGhostY), (Object.pacmanX, Object.pacmanY)))
        expanded_nodes = len(listPos)

        while Config.running:
            Config.screen.fill('black')
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
            EM().blueGhost.move()

            EM().maze.draw()
            EM().pacman.draw()
            EM().blueGhost.draw()
            

            if not listPos:
                Sounds.ghost_move_sound.stop()
                EM().blueGhost.move()

                EM().maze.draw()
                EM().pacman.draw()
                EM().blueGhost.draw()
                pygame.display.flip()
                #time.sleep(1)
                break

            pygame.display.flip()
            clock.tick(Config.fps)
            countFrames += 1

        font = pygame.font.Font(None, 35)
        algorithm = font.render("Algorithm: BFS", True, BLACK)
        search_time = font.render(f"Search time: {end_time - start_time:.6f} seconds", True, BLACK)
        memory_usage = font.render(f"Memory usage: {after_mem - before_mem:.6f} MB", True, BLACK)
        num_expanded_nodes = font.render(f"Number of expanded nodes : {expanded_nodes}", True, BLACK)
            
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
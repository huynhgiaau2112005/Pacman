from EntitiesManager import EntitiesManager as EM
from Config import Config, Object
from collections import deque
import pygame

class Level2:
    def __init__(self):
        pass

    def setup(self):
        print("setup")

    def execute(self):
        self.setup()
        clock = pygame.time.Clock()

        countFrames = 0 # 0
        #listPos = deque(EM().pinkGhost.pinkGhostForLv2((Object.pinkGhostX, Object.pinkGhostY), (Object.pacmanX, Object.pacmanY)))

        # path, depth = EM().pinkGhost.getTargetPos((Object.pinkGhostX, Object.pinkGhostY), (Object.pacmanX, Object.pacmanY))
        # index = 0
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
            
            if countFrames % 15 == 0:
                # if listPos:
                #     newPos = listPos.popleft()
                #     EM().pinkGhost.updatePosForLv2(newPos)
                EM().pinkGhost.updatePos()
                #print((Object.pinkGhostX, Object.pinkGhostY))
                # if index < len(path):
                #     (Object.pinkGhostX, Object.pinkGhostY) = path[index]
                #     index += 1
                #     print((index, depth))
            EM().pinkGhost.move()

            EM().maze.draw()
            EM().pacman.draw()
            EM().pinkGhost.draw()

            pygame.display.flip()
            clock.tick(Config.fps)
            countFrames += 1

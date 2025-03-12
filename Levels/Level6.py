from Entities.Entity import Entity
from EntitiesManager import EntitiesManager as EM
from Config import Config, Object, Sounds, Board
from collections import deque
import threading
import time
import pygame

start = False
PacmanGetCaught = False

class Level6:
    def __init__(self):
        pass

    def setup(self):
        global PacmanGetCaught, quit, start

        PacmanGetCaught = False
        quit = False
        start = False

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

        for i in range(len(Board.coordinates)):
            for j in range(len(Board.coordinates[i])):
                if (i, j) not in ((Object.blueGhostX, Object.blueGhostY), \
                                  (Object.pinkGhostX, Object.pinkGhostY), \
                                  (Object.orangeGhostX, Object.orangeGhostY), \
                                  (Object.redGhostX, Object.redGhostY), \
                                  (Object.pacmanX, Object.pacmanY)):
                    Board.coordinates[i][j] = Board.BLANK

    def isCaught(self):
        pacmanPos = (Object.pacmanX, Object.pacmanY)
        ghost = [(Object.blueGhostX, Object.blueGhostY), (Object.pinkGhostX, Object.pinkGhostY), (Object.redGhostX, Object.redGhostY), (Object.orangeGhostX, Object.orangeGhostY)]
        
        if pacmanPos == (Object.orangeGhostX, Object.orangeGhostY):
            print("Pacman is caught by Orange Ghost")
        
        if pacmanPos == (Object.redGhostX, Object.redGhostY):
            print("Pacman is caught by Red Ghost")
        
        if pacmanPos == (Object.pinkGhostX, Object.pinkGhostY):
            print("Pacman is caught by Pink Ghost")
        
        if pacmanPos == (Object.blueGhostX, Object.blueGhostY): 
            print("Pacman is caught by Blue Ghost")
        return pacmanPos in ghost

    def execute(self):
        global PacmanGetCaught, quit, start

        self.setup()
        clock = pygame.time.Clock()
        last_tick = pygame.time.get_ticks()
        countFrames = 0
        
        Sounds.dramatic_theme_music_sound.set_volume(0.1)
        Sounds.dramatic_theme_music_sound.play(loops=-1)

        while Config.running and not quit:
            Config.screen.fill('black')
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Sounds.ghost_move_sound.stop()
                    Sounds.dramatic_theme_music_sound.stop()
                    Config.running = False
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        Sounds.ghost_move_sound.stop()
                        Sounds.dramatic_theme_music_sound.stop()
                        quit = True
                        return
                    if event.key == pygame.K_q:
                        Sounds.ghost_move_sound.stop()
                        Sounds.dramatic_theme_music_sound.stop()
                        Config.running = False
                        return
                    if event.key == pygame.K_SPACE:
                        if not start:
                            Sounds.ghost_move_sound.play(loops=-1)  # Lặp vô hạn
                            start = True
            
            if Config.counter < 19:
                Config.counter += 1
                if Config.counter > 3:
                  Config.flicker = False
            else:
                Config.flicker = True
                Config.counter = 0
                
            EM().maze.draw()

            if not start:
                color = (255, 255, 255 - countFrames % 30 * 8)
                labelFont = pygame.font.Font(None, 30)
                space_to_start = labelFont.render("PRESS SPACE TO START", True, color)
                Config.screen.blit(space_to_start, (Config.width / 2 - 130, Config.height / 2 - 50))

            if start and not PacmanGetCaught:
                if countFrames % 15 == 0:
                    EM().orangeGhost.updatePos()
                    PacmanGetCaught = self.isCaught()
                    EM().blueGhost.updatePos()
                    PacmanGetCaught = self.isCaught()
                    EM().pinkGhost.updatePos()
                    PacmanGetCaught = self.isCaught()
                    EM().redGhost.updatePos()
                    PacmanGetCaught = self.isCaught()
                    EM().pacman.updatePos()
                EM().blueGhost.move()
                EM().pinkGhost.move()
                EM().orangeGhost.move()
                EM().redGhost.move()
                EM().pacman.move()

            EM().pacman.setupdrawdir()
            EM().blueGhost.draw()
            EM().pinkGhost.draw()
            EM().orangeGhost.draw()
            EM().redGhost.draw()
            EM().life.draw()
            EM().score.draw()

            pygame.display.flip()
            clock.tick(Config.fps)
            countFrames += 1

            if PacmanGetCaught:
                Sounds.ghost_move_sound.stop()
                Sounds.dramatic_theme_music_sound.stop()
                


        

    

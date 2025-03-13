from Entities.Entity import Entity
from EntitiesManager import EntitiesManager as EM
from Config import Config, Object, Sounds, Board, Mode
import time
import random
import pygame

start = False
PacmanGetCaught = False
quit = False

countFrames = 0

setUpCoordinates = {
    'blueGhost': (14, 12),
    'pinkGhost': (16, 12),
    'orangeGhost': (16, 17),
    'redGhost': (14, 17),
    'pacman': (24, 14)
}
availableNodes = [(21, 16), (27, 4), (27, 13), (14, 13), (2, 2), (6, 2), (15, 14), (16, 13), (18, 10), (18, 19), (30, 2), (14, 15), (9, 10), (9, 19), (24, 10), (15, 7), (24, 19), (15, 16), (6, 13), (16, 15), (21, 2), (14, 17), (30, 13), (15, 0), (16, 17), (2, 27), (12, 13), (6, 27), (27, 22), (30, 27), (12, 15), (14, 12), (21, 27), (9, 7), (9, 16), (24, 7), (24, 16), (15, 13), (2, 13), (16, 12), (24, 25), (2, 22), (6, 22), (14, 14), (16, 14), (21, 13), (12, 10), (21, 22), (9, 2), (12, 19), (14, 16), (27, 10), (24, 2), (27, 19), (16, 16), (15, 29), (24, 4), (6, 10), (15, 22), (6, 19), (12, 14), (9, 27), (15, 15), (21, 10), (24, 27), (21, 19), (12, 16), (27, 7), (27, 16), (27, 25), (15, 17), (9, 13), (27, 27), (2, 7), (9, 22), (2, 16), (24, 13), (15, 10), (6, 7), (24, 22), (15, 19), (6, 16), (27, 2), (30, 16), (15, 12), (21, 7)]
TargetPosInPowerUp = {
    'blueGhost': (6, 2),
    'pinkGhost': (30, 2),
    'orangeGhost': (30, 27),
    'redGhost': (2, 27),
}

def isHit(pos1, pos2):
    dx = abs(pos1[0] - pos2[0])
    dy = abs(pos1[1] - pos2[1])
    return dx < Config.p_width and dy < Config.p_height

class Level6:
    def __init__(self):
        pass

    def setup(self):
        global PacmanGetCaught, quit, start, countFrames
        global BlueGhostStatus, PinkGhostStatus, OrangeGhostStatus, RedGhostStatus

        countFrames = 0
        PacmanGetCaught = False
        quit = False
        start = False

        Config.KeyMovePacman = None

        # Setup mode
        Mode.mode = Mode.CHASING
        Mode.powerupTime = 0
        Mode.BlueGhost = Mode.CHASING
        Mode.PinkGhost = Mode.CHASING
        Mode.OrangeGhost = Mode.CHASING
        Mode.RedGhost = Mode.CHASING

        # Setup tọa độ ma trận
        Object.pacmanX, Object.pacmanY = setUpCoordinates["pacman"]
        Object.blueGhostX, Object.blueGhostY = setUpCoordinates["blueGhost"]
        Object.pinkGhostX, Object.pinkGhostY = setUpCoordinates["pinkGhost"]
        Object.orangeGhostX, Object.orangeGhostY = setUpCoordinates["orangeGhost"]
        Object.redGhostX, Object.redGhostY = setUpCoordinates["redGhost"]
        
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
        ghostPos = [(Object.blueGhostX, Object.blueGhostY), (Object.pinkGhostX, Object.pinkGhostY), (Object.redGhostX, Object.redGhostY), (Object.orangeGhostX, Object.orangeGhostY)]
        ghostMode = [Mode.BlueGhost, Mode.PinkGhost, Mode.RedGhost, Mode.OrangeGhost]

        for i in range(len(ghostPos)):
            pos = ghostPos[i]
            mode = ghostMode[i]
            if mode == Mode.CHASING and pos == pacmanPos:
                Config.life -= 1
                return True

        return False
    
    def setTargetPosPowerUp(self):
        global TargetPosInPowerUp
        curCoordinates = {"blueGhost": (Object.blueGhostX, Object.blueGhostY), 
                          "pinkGhost": (Object.realPacmanX, Object.pinkGhostY),
                          "redGhost": (Object.redGhostX, Object.redGhostY), 
                          "orangeGhost": (Object.orangeGhostX, Object.orangeGhostY)}
        
        newBlueGhostPos = TargetPosInPowerUp["blueGhost"]
        while newBlueGhostPos in set(TargetPosInPowerUp.values()) | set(curCoordinates.values()):
            newBlueGhostPos = random.choice(availableNodes)
        TargetPosInPowerUp["blueGhost"] = newBlueGhostPos

        newPinkGhostPos = TargetPosInPowerUp["pinkGhost"]
        while newPinkGhostPos in set(TargetPosInPowerUp.values()) | set(curCoordinates.values()):
            newPinkGhostPos = random.choice(availableNodes)
        TargetPosInPowerUp["pinkGhost"] = newPinkGhostPos

        newOrangeGhostPos = TargetPosInPowerUp["orangeGhost"]
        while newOrangeGhostPos in set(TargetPosInPowerUp.values()) | set(curCoordinates.values()):
            newOrangeGhostPos = random.choice(availableNodes)
        TargetPosInPowerUp["orangeGhost"] = newOrangeGhostPos

        newRedGhostPos = TargetPosInPowerUp["redGhost"]
        while newRedGhostPos in set(TargetPosInPowerUp.values()) | set(curCoordinates.values()):
            newRedGhostPos = random.choice(availableNodes)
        TargetPosInPowerUp["redGhost"] = newRedGhostPos

    def ghostChasingMode(self):
        global start, PacmanGetCaught, countFrames
        if start and not PacmanGetCaught:
            if countFrames % 15 == 0:
                if Mode.BlueGhost == Mode.CHASING:
                    EM().blueGhost.updatePos()
                if Mode.PinkGhost == Mode.CHASING and countFrames > 60 * 5:
                    EM().pinkGhost.updatePos()
                if Mode.OrangeGhost == Mode.CHASING and countFrames > 60 * 10:
                    EM().orangeGhost.updatePos()
                if Mode.RedGhost == Mode.CHASING and countFrames > 60 * 15:
                    EM().redGhost.updatePos()
                PacmanGetCaught = self.isCaught()

            if Mode.BlueGhost == Mode.CHASING:   
                EM().blueGhost.move()
            if Mode.PinkGhost == Mode.CHASING:
                EM().pinkGhost.move()
            if Mode.OrangeGhost == Mode.CHASING:
                EM().orangeGhost.move()
            if Mode.RedGhost == Mode.CHASING:
                EM().redGhost.move()
    
    def powerupMode(self):
        global PacmanGetCaught, random_node, countFrames
        if start and not PacmanGetCaught:
            if countFrames % 60 * 2 == 0:
                self.setTargetPosPowerUp()
            if countFrames % 15 == 0:
                if Mode.PinkGhost == Mode.POWER_UP:
                    EM().pinkGhost.updatePosPowerUp(TargetPosInPowerUp["pinkGhost"])
                if Mode.OrangeGhost == Mode.POWER_UP and countFrames > 60 * 5:
                    EM().orangeGhost.updatePosPowerUp(TargetPosInPowerUp["orangeGhost"])
                if Mode.BlueGhost == Mode.POWER_UP and countFrames > 60 * 10:
                    EM().blueGhost.updatePosPowerUp(TargetPosInPowerUp["blueGhost"])
                if Mode.RedGhost == Mode.POWER_UP and countFrames > 60 * 15:
                    EM().redGhost.updatePosPowerUp(TargetPosInPowerUp["redGhost"])

                pacmanPos = (Object.realPacmanX, Object.realPacmanY)
                pinkGhostPos = (Object.realPinkGhostX, Object.realPinkGhostY)
                blueGhostPos = (Object.realBlueGhostX, Object.realBlueGhostY)
                orangeGhostPos = (Object.realOrangeGhostX, Object.realOrangeGhostY)
                redGhostPos = (Object.realRedGhostX, Object.realRedGhostY)

                if isHit(pinkGhostPos, pacmanPos):
                    (Object.realPinkGhostX, Object.realPinkGhostY) = Entity.getRealCoordinates((Object.pinkGhostX, Object.pinkGhostY), Object.PINK_GHOST_SIZE)
                    Mode.PinkGhost = Mode.DEAD
                if isHit(blueGhostPos, pacmanPos):
                    (Object.realBlueGhostX, Object.realBlueGhostY) = Entity.getRealCoordinates((Object.blueGhostX, Object.blueGhostY), Object.BLUE_GHOST_SIZE)
                    Mode.BlueGhost = Mode.DEAD
                if isHit(orangeGhostPos, pacmanPos):
                    (Object.realOrangeGhostX, Object.realOrangeGhostY) = Entity.getRealCoordinates((Object.orangeGhostX, Object.orangeGhostY), Object.ORANGE_GHOST_SIZE)
                    Mode.OrangeGhost = Mode.DEAD
                if isHit(redGhostPos, pacmanPos):
                    (Object.realRedGhostX, Object.realRedGhostY) = Entity.getRealCoordinates((Object.redGhostX, Object.redGhostY), Object.RED_GHOST_SIZE)
                    Mode.RedGhost = Mode.DEAD

            if Mode.BlueGhost == Mode.POWER_UP:   
                EM().blueGhost.move()
            if Mode.PinkGhost == Mode.POWER_UP:
                EM().pinkGhost.move()
            if Mode.OrangeGhost == Mode.POWER_UP:
                EM().orangeGhost.move()
            if Mode.RedGhost == Mode.POWER_UP:
                EM().redGhost.move()
    
    def deadGhostRelives(self):
        if countFrames % 10 == 0:
            if (Mode.BlueGhost == Mode.DEAD):
                if (Object.blueGhostX, Object.blueGhostY) == setUpCoordinates["blueGhost"]:
                    Mode.BlueGhost = Mode.CHASING
                else:
                    EM().blueGhost.updatePosRelive(setUpCoordinates["blueGhost"])
            if (Mode.PinkGhost == Mode.DEAD):
                if (Object.pinkGhostX, Object.pinkGhostY) == setUpCoordinates["pinkGhost"]:
                    Mode.PinkGhost = Mode.CHASING
                else:
                    EM().pinkGhost.updatePosRelive(setUpCoordinates["pinkGhost"])
            if (Mode.OrangeGhost == Mode.DEAD):
                if (Object.orangeGhostX, Object.orangeGhostY) == setUpCoordinates["orangeGhost"]:
                    Mode.OrangeGhost = Mode.CHASING
                else:
                    EM().orangeGhost.updatePosRelive(setUpCoordinates["orangeGhost"])
            if (Mode.RedGhost == Mode.DEAD):
                if (Object.redGhostX, Object.redGhostY) == setUpCoordinates["redGhost"]:
                    Mode.RedGhost = Mode.CHASING
                else:
                    EM().redGhost.updatePosRelive(setUpCoordinates["redGhost"])
        
        if Mode.BlueGhost == Mode.DEAD:   
            EM().blueGhost.moveRelive()
        if Mode.PinkGhost == Mode.DEAD:
            EM().pinkGhost.moveRelive()
        if Mode.OrangeGhost == Mode.DEAD:
            EM().orangeGhost.moveRelive()
        if Mode.RedGhost == Mode.DEAD:
            EM().redGhost.moveRelive()

    def execute(self):
        global PacmanGetCaught, quit, start, countFrames

        self.setup()
        clock = pygame.time.Clock()
        last_tick = pygame.time.get_ticks()
        
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
                    if event.key == pygame.K_UP:
                        Config.KeyMovePacman = pygame.K_UP
                    if event.key == pygame.K_DOWN:
                        Config.KeyMovePacman = pygame.K_DOWN
                    if event.key == pygame.K_LEFT:
                        Config.KeyMovePacman = pygame.K_LEFT
                    if event.key == pygame.K_RIGHT:
                        Config.KeyMovePacman = pygame.K_RIGHT
            
            if Config.counter < 19:
                Config.counter += 1
                if Config.counter > 3:
                  Config.flicker = False
            else:
                Config.flicker = True
                Config.counter = 0
                
            EM().maze.draw()
            EM().pacman.setupdrawdir()
            EM().blueGhost.draw()
            EM().pinkGhost.draw()
            EM().orangeGhost.draw()
            EM().redGhost.draw()
            EM().life.draw()
            EM().score.draw()

            if not start:
                overlay = pygame.Surface((Config.width, Config.height))
                overlay.set_alpha(180)  # Độ trong suốt (0: trong suốt hoàn toàn, 255: không trong suốt)
                overlay.fill((0, 0, 0))  # Màu đen
                Config.screen.blit(overlay, (0, 0))
                
                color = (255, 255, 255 - countFrames % 30 * 8)
                labelFont = pygame.font.Font(None, 30)
                space_to_start = labelFont.render("PRESS SPACE TO START", True, color)
                Config.screen.blit(space_to_start, (Config.width / 2 - 130, Config.height / 2 - 50))

            if Mode.powerupTime == 0:
                Mode.mode = Mode.CHASING
                Mode.BlueGhost = Mode.CHASING if Mode.BlueGhost != Mode.DEAD else Mode.DEAD
                Mode.PinkGhost = Mode.CHASING if Mode.PinkGhost != Mode.DEAD else Mode.DEAD
                Mode.OrangeGhost = Mode.CHASING if Mode.OrangeGhost != Mode.DEAD else Mode.DEAD
                Mode.RedGhost = Mode.CHASING if Mode.RedGhost != Mode.DEAD else Mode.DEAD

            self.ghostChasingMode()
            self.powerupMode()

            if start and countFrames % 15 == 0:
                EM().pacman.updatePos()
            EM().pacman.move()

            self.deadGhostRelives()

            pygame.display.flip()
            clock.tick(Config.fps)
            if start:
                countFrames += 1
                Mode.powerupTime -= 1 if Mode.powerupTime > 0 else 0
                
            if PacmanGetCaught:
                #Sounds.dramatic_theme_music_sound.stop()
                Sounds.ghost_move_sound.stop()
                #Sounds.pacman_death()
                time.sleep(1.5)
                self.setup()
                continue
        Sounds.dramatic_theme_music_sound.stop()

                


        

    

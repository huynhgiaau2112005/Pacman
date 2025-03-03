from abc import ABC, abstractmethod
from .MovingEntity import MovingEntity
import pygame
from Config import Config

class GhostStrategy(ABC):
  @abstractmethod
  def getTargetPos(self, ghost, pacman):
      pass
  def move(self, position: tuple):
    pass

class Ghost(MovingEntity):
    def __init__(self, xPos, yPos, sprite, time):
        super().__init__(xPos, yPos, 32, 2, sprite, 0.3, 2)

        # self.ghost_eaten_sprite = pygame.image.load('Pacman_Python_PTITHCM-master/res/img/ghost_eaten.png')
        # self.ghost_frightened_1 = pygame.image.load('Pacman_Python_PTITHCM-master/res/img/ghost_frightened.png')
        # self.ghost_frightened_2 = pygame.image.load('Pacman_Python_PTITHCM-master/res/img/ghost_frightened_2.png')

        # MODE
        # self.chaseMode = ChaseMode(self)
        # self.scatterMode = ScatterMode(self)
        # self.frightenedMode = FrightenedMode(self)
        # self.eatenMode = EatenMode(self)
        # self.houseMode = HouseMode(self)
        # self.state = self.houseMode
        # self.strategy = GhostStrategy()

        # self.modeTimer = 0
        # self.frightenedTimer = 0
        # self.isChasing = False
        # self.time = time
        # self.count = 0

    def getChasePos(self):
        pass

    def getScatterPos(self):
        pass

    def draw(self):
        pass
    
    def switchFrightenedMode(self):
        pass

    def switchScatterMode(self):
        pass
    
    def switchHouseMode(self):
        pass

    def switchEatenMode(self):
        pass

    def switchChaseModeOrScatterMode(self):
        pass

    def switchChaseMode(self):
        pass

    def getState(self):
        return self.getState()

    def update(self):
        pass

    def reset(self):
        super().reset()
        self.state = self.houseMode

class GhostState():

    def __init__(self, ghost: Ghost):
        self.ghost = ghost

    def superPacGumEaten(self):
        pass

    def timeModeOver(self):
        pass

    def timeFrightenModeOver(self):
        pass

    def eaten(self):
        pass

    def outsideHouse(self):
        pass

    def insideHouse(self):
        pass

    def getTargetPos(self):
        pass

    def computeNextDir(self):
        pass
    
class ChaseMode(GhostState):
    pass

class ScatterMode(GhostState):
    pass

class FrightenedMode(GhostState):
    pass

class EatenMode(GhostState):
    pass

class HouseMode(GhostState):
    pass

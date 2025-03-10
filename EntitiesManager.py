import pygame
from Entities import *

class EntitiesManager:
    def __init__(self):
        self.maze = Maze()
        self.pacman = Pacman()
        self.orangeGhost = OrangeGhost()
        self.redGhost = RedGhost()
        self.pinkGhost = PinkGhost()
        self.blueGhost = BlueGhost()
        #self.ghosts = [BlueGhost, RedGhost, PinkGhost, OrangeGhost]
    
    def reset(self):
        self.pacman.reset()
        self.maze.reset()
        self.redGhost.reset()
        # for ghost in self.ghosts:
        # ghost.reset()

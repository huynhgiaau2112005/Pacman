import pygame
from Entities import *

class EntitiesManager:
    def __init__(self):
        self.maze = Maze()
        self.pacman = Pacman()
        #self.ghosts = [BlueGhost, RedGhost, PinkGhost, OrangeGhost]
    
    def reset(self):
        self.pacman.reset()
        self.maze.reset()
        # for ghost in self.ghosts:
        #     ghost.reset()

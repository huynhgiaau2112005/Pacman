class Config:
  running = True
  score = 0

from Entities.BlueGhost import BlueGhost
from Entities.RedGhost import RedGhost
from Entities.PinkGhost import PinkGhost
from Entities.OrangeGhost import OrangeGhost
from Entities.Pacman import Pacman
from Entities.Maze import Maze

class Entity:
  Pacman
  Maze
  
  ghosts = [
    BlueGhost,
    RedGhost,
    PinkGhost,
    OrangeGhost 
  ]
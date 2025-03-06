from .Entity import Entity
from Config import Config, Material, Object
import pygame

class Pacman(Entity):
  def draw(self):
    realX = Object.realPacmanX
    realY = Object.realPacmanY

    Config.screen.blit(Material.Pacman1Image, (realY, realX))

  def keyboardHandle():
    print('Press nút nào di chuyển nút đó, ...')
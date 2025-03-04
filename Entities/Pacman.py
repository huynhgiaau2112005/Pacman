from .Entity import Entity
from Config import Config, Material
import pygame

class Pacman(Entity):
  def draw(self):
    realX = Config.pacmanX * Config.p_height #+ (0.5 * Config.p_height)
    realY = Config.pacmanY * Config.p_width #+ (0.5 * Config.p_width)

    Config.screen.blit(Material.Pacman1Image, (realY, realX))

  def keyboardHandle():
    print('Press nút nào di chuyển nút đó, ...')
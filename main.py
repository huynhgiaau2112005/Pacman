from Levels import *
from Config import Config, setup
from Menu import Menu
import pygame

def mainBusiness():
  setup()
  pygame.init()
  # Level4().execute()
  # Level3().execute()
  # Level2().execute()
  # Level4().excute()
  # Level5().excute()
  # Level6().excute()
  menu = Menu()
  menu.execute()
  print('nothing')  

def main():
  mainBusiness()

if __name__ == "__main__":
  main()
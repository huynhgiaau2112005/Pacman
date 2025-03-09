from Levels import *
from Config import setup
from Menu import Menu
import pygame

def mainBusiness():
  setup()
  pygame.init()
  # Level4().execute()
  # Level3().execute()
  # Level2().execute()
  # Level4().execute()
  # Level5().execute()
  # Level6().execute()
  menu = Menu()
  menu.execute()
  print('nothing')  
def main():
  mainBusiness()

if __name__ == "__main__":
  main()
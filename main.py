from Levels import *
from Config import setup
from Menu import Menu
import pygame

def mainBusiness():
  setup()
  pygame.init()
  menu = Menu()
  menu.execute()
  
def main():
  mainBusiness()

if __name__ == "__main__":
  main()  
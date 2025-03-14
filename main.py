from Levels import *
from Config import setup, Sounds
from Menu import Menu
import pygame

def mainBusiness():
  Sounds.beginning_game_sound.play()
  setup()
  pygame.init()
  menu = Menu()
  menu.execute()
  
def main():
  mainBusiness()

if __name__ == "__main__":
  main()  
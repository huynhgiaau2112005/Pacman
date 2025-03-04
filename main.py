from Levels import *
import Config
import pygame

def mainBusiness():
  Config.setup()
  pygame.init()
  Level4().execute()
  #Levels.Level2().excute()
  #Levels.Level3().excute()
  #Levels.Level4().excute()
  #Levels.Level5().excute()
  #Levels.Level6().excute()
  print('nothing')

def main():
  mainBusiness()

if __name__ == "__main__":
  main()
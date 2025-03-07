import pygame

class Config:
  flicker = False
  running = True
  score = 0
  width = 900
  height = 900
  p_width = 900//30 
  p_height = 850//32
  screen = pygame.display.set_mode([width, height])
  fps = 60 #600

class Object:
  PACMAN_SIZE = 42
  BLUE_GHOST_SIZE = 42
  PINK_GHOST_SIZE = 42
  RED_GHOST_SIZE = 42
  ORANGE_GHOST_SIZE = 42

  pacmanX = 24
  pacmanY = 14
  blueGhostX = 15
  blueGhostY = 13
  pinkGhostX = 16
  pinkGhostY = 13
  redGhostX = 15
  redGhostY = 15
  orangeGhostX = 16
  orangeGhostY = 15

  realPacmanX = 0
  realPacmanY = 0
  realBlueGhostX = 0
  realBlueGhostY = 0
  realPinkGhostX = 0
  realPinkGhostY = 0
  realRedGhostX = 0
  realRedGhostY = 0
  realOrangeGhostX = 0
  realOrangeGhostY = 0

  
class Color:
  color_wall = 'blue'
  color_food = 'white'
  color_bg = 'black'
  color_fence = 'white'

class Material:
  BlueGhostImage = pygame.transform.scale(pygame.image.load("Pacman/Assets/ghost_images/blue.png"), (Object.BLUE_GHOST_SIZE, Object.BLUE_GHOST_SIZE))
  RedGhostImage = pygame.transform.scale(pygame.image.load("Pacman/Assets/ghost_images/red.png"), (Object.RED_GHOST_SIZE, Object.RED_GHOST_SIZE))
  PinkGhostImage = pygame.transform.scale(pygame.image.load("Pacman/Assets/ghost_images/pink.png"), (Object.PINK_GHOST_SIZE, Object.PINK_GHOST_SIZE))
  OrangeGhostImage = pygame.transform.scale(pygame.image.load("Pacman/Assets/ghost_images/orange.png"), (Object.ORANGE_GHOST_SIZE, Object.ORANGE_GHOST_SIZE))
  DeadGhostImage = pygame.transform.scale(pygame.image.load("Pacman/Assets/ghost_images/dead.png"), (Config.p_height, Config.p_width))
  PowerupImage = pygame.transform.scale(pygame.image.load("Pacman/Assets/ghost_images/powerup.png"), (Config.p_height, Config.p_width))
  Pacman1Image = pygame.transform.scale(pygame.image.load("Pacman/Assets/player_images/1.png"), (Object.PACMAN_SIZE, Object.PACMAN_SIZE))
  Pacman2Image = pygame.transform.scale(pygame.image.load("Pacman/Assets/player_images/2.png"), (Object.PACMAN_SIZE, Object.PACMAN_SIZE))
  Pacman3Image = pygame.transform.scale(pygame.image.load("Pacman/Assets/player_images/3.png"), (Object.PACMAN_SIZE, Object.PACMAN_SIZE))
  Pacman4Image = pygame.transform.scale(pygame.image.load("Pacman/Assets/player_images/4.png"), (Object.PACMAN_SIZE, Object.PACMAN_SIZE))
  
class Board:
# 0 = empty black rectangle, 1 = dot, 2 = big dot, 3 = vertical line,
# 4 = horizontal line, 5 = top right, 6 = top left, 7 = bot left, 8 = bot right
# 9 = gate
  PACMAN = 50
  BLUE_GHOST = 60
  PINK_GHOST = 61
  RED_GHOST = 62
  ORANGE_GHOST = 63

  ROWS = 33
  COLS = 30
  BLANK = 0
  maze = [
[6, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5],
[3, 6, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 6, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 3],
[3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3],
[3, 3, 1, 6, 4, 4, 5, 1, 6, 4, 4, 4, 5, 1, 3, 3, 1, 6, 4, 4, 4, 5, 1, 6, 4, 4, 5, 1, 3, 3],
[3, 3, 2, 3, 0, 0, 3, 1, 3, 0, 0, 0, 3, 1, 3, 3, 1, 3, 0, 0, 0, 3, 1, 3, 0, 0, 3, 2, 3, 3],
[3, 3, 1, 7, 4, 4, 8, 1, 7, 4, 4, 4, 8, 1, 7, 8, 1, 7, 4, 4, 4, 8, 1, 7, 4, 4, 8, 1, 3, 3],
[3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3],
[3, 3, 1, 6, 4, 4, 5, 1, 6, 5, 1, 6, 4, 4, 4, 4, 4, 4, 5, 1, 6, 5, 1, 6, 4, 4, 5, 1, 3, 3],
[3, 3, 1, 7, 4, 4, 8, 1, 3, 3, 1, 7, 4, 4, 5, 6, 4, 4, 8, 1, 3, 3, 1, 7, 4, 4, 8, 1, 3, 3],
[3, 3, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 1, 1, 3, 3],
[3, 7, 4, 4, 4, 4, 5, 1, 3, 7, 4, 4, 5, 0, 3, 3, 0, 6, 4, 4, 8, 3, 1, 6, 4, 4, 4, 4, 8, 3],
[3, 0, 0, 0, 0, 0, 3, 1, 3, 6, 4, 4, 8, 0, 7, 8, 0, 7, 4, 4, 5, 3, 1, 3, 0, 0, 0, 0, 0, 3],
[3, 0, 0, 0, 0, 0, 3, 1, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 1, 3, 0, 0, 0, 0, 0, 3],
[8, 0, 0, 0, 0, 0, 3, 1, 3, 3, 0, 6, 4, 4, 9, 9, 4, 4, 5, 0, 3, 3, 1, 3, 0, 0, 0, 0, 0, 7],
[4, 4, 4, 4, 4, 4, 8, 1, 7, 8, 0, 3, 0, 0, 0, 0, 0, 0, 3, 0, 7, 8, 1, 7, 4, 4, 4, 4, 4, 4],
[0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
[4, 4, 4, 4, 4, 4, 5, 1, 6, 5, 0, 3, 0, 0, 0, 0, 0, 0, 3, 0, 6, 5, 1, 6, 4, 4, 4, 4, 4, 4],
[5, 0, 0, 0, 0, 0, 3, 1, 3, 3, 0, 7, 4, 4, 4, 4, 4, 4, 8, 0, 3, 3, 1, 3, 0, 0, 0, 0, 0, 6],
[3, 0, 0, 0, 0, 0, 3, 1, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 1, 3, 0, 0, 0, 0, 0, 3],
[3, 0, 0, 0, 0, 0, 3, 1, 3, 3, 0, 6, 4, 4, 4, 4, 4, 4, 5, 0, 3, 3, 1, 3, 0, 0, 0, 0, 0, 3],
[3, 6, 4, 4, 4, 4, 8, 1, 7, 8, 0, 7, 4, 4, 5, 6, 4, 4, 8, 0, 7, 8, 1, 7, 4, 4, 4, 4, 5, 3],
[3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3],
[3, 3, 1, 6, 4, 4, 5, 1, 6, 4, 4, 4, 5, 1, 3, 3, 1, 6, 4, 4, 4, 5, 1, 6, 4, 4, 5, 1, 3, 3],
[3, 3, 1, 7, 4, 5, 3, 1, 7, 4, 4, 4, 8, 1, 7, 8, 1, 7, 4, 4, 4, 8, 1, 3, 6, 4, 8, 1, 3, 3],
[3, 3, 2, 1, 1, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1, 2, 3, 3],
[3, 7, 4, 5, 1, 3, 3, 1, 6, 5, 1, 6, 4, 4, 4, 4, 4, 4, 5, 1, 6, 5, 1, 3, 3, 1, 6, 4, 8, 3],
[3, 6, 4, 8, 1, 7, 8, 1, 3, 3, 1, 7, 4, 4, 5, 6, 4, 4, 8, 1, 3, 3, 1, 7, 8, 1, 7, 4, 5, 3],
[3, 3, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 1, 1, 3, 3],
[3, 3, 1, 6, 4, 4, 4, 4, 8, 7, 4, 4, 5, 1, 3, 3, 1, 6, 4, 4, 8, 7, 4, 4, 4, 4, 5, 1, 3, 3],
[3, 3, 1, 7, 4, 4, 4, 4, 4, 4, 4, 4, 8, 1, 7, 8, 1, 7, 4, 4, 4, 4, 4, 4, 4, 4, 8, 1, 3, 3],
[3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3],
[3, 7, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 8, 3],
[7, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 8]
]  
  coordinates = []

def setup():
  # set up coordinates
  Board.coordinates = [[Board.BLANK for _ in range(Board.COLS)] for _ in range(Board.ROWS)] # tạo ma trận cols x rows với các ô có giá trị 0

  Board.coordinates[Object.pacmanX][Object.pacmanY] = Board.PACMAN
  Board.coordinates[Object.blueGhostX][Object.blueGhostY] = Board.BLUE_GHOST
  Board.coordinates[Object.pinkGhostX][Object.pinkGhostY] = Board.PINK_GHOST
  Board.coordinates[Object.redGhostX][Object.redGhostY] = Board.RED_GHOST
  Board.coordinates[Object.orangeGhostX][Object.orangeGhostY] = Board.ORANGE_GHOST

  Object.realPacmanX = Object.pacmanX * Config.p_height + Config.p_height * 0.5 - Object.PACMAN_SIZE * 0.5 
  Object.realPacmanY = Object.pacmanY * Config.p_width + Config.p_width * 0.5 - Object.PACMAN_SIZE * 0.5
  Object.realBlueGhostX = Object.blueGhostX * Config.p_height + Config.p_height * 0.5 - Object.BLUE_GHOST_SIZE * 0.5 
  Object.realBlueGhostY = Object.blueGhostY * Config.p_width + Config.p_width * 0.5 - Object.BLUE_GHOST_SIZE * 0.5
  Object.realPinkGhostX = Object.pinkGhostX * Config.p_height + Config.p_height * 0.5 - Object.PINK_GHOST_SIZE * 0.5 
  Object.realPinkGhostY = Object.pinkGhostY * Config.p_width + Config.p_width * 0.5 - Object.PINK_GHOST_SIZE * 0.5
  Object.realRedGhostX = Object.redGhostX * Config.p_height + Config.p_height * 0.5 - Object.RED_GHOST_SIZE * 0.5 
  Object.realRedGhostY = Object.redGhostY * Config.p_width + Config.p_width * 0.5 - Object.RED_GHOST_SIZE * 0.5
  Object.realOrangeGhostX = Object.orangeGhostX * Config.p_height + Config.p_height * 0.5 - Object.ORANGE_GHOST_SIZE * 0.5 
  Object.realOrangeGhostY = Object.orangeGhostY * Config.p_width + Config.p_width * 0.5 - Object.ORANGE_GHOST_SIZE * 0.5
  
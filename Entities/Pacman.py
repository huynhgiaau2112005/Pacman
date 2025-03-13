from .Entity import Entity
from Config import Config, Material, Object, Board
import pygame

class Pacman(Entity):
  def __init__(self):
    self.PacmanImages = [Material.Pacman1Image, Material.Pacman2Image, Material.Pacman3Image, Material.Pacman4Image]
  
  def draw(self):
    realX = Object.realPacmanX
    realY = Object.realPacmanY
    Config.screen.blit(Material.Pacman1Image, (realY, realX))

  def picperdir(self, picture, direction, realX, realY):
    if direction == (0, 1) or direction == (0, 0):
          Config.screen.blit(picture, (realY, realX))
    elif direction == (0, -1):
        Config.screen.blit(pygame.transform.flip(picture, True, False), (realY, realX))  
    elif direction == (-1, 0):
        Config.screen.blit(pygame.transform.rotate(picture, 90),(realY, realX))
    elif direction == (1, 0):
        Config.screen.blit(pygame.transform.rotate(picture, 270), (realY, realX))
        
  def drawdir(self, direction):
    realX = Object.realPacmanX
    realY = Object.realPacmanY
    if (Board.maze[Object.pacmanX][Object.pacmanY] != 0):
      self.picperdir(self.PacmanImages[Config.counter // 5], direction, realX, realY)
    else:
      self.picperdir(Material.Pacman2Image, direction, realX, realY)    
        
  def setupdrawdir(self):
    direction = Object.PACMAN_DIRX, Object.PACMAN_DIRY

    if direction != (0, 0):
        Object.PACMAN_DRAWX, Object.PACMAN_DRAWY = direction
        self.drawdir(direction)
    else:
      direction = Object.PACMAN_DRAWX, Object.PACMAN_DRAWY
      self.drawdir(direction)
        
  def keyboardHandle(self):
    keys = pygame.key.get_pressed() # Kiểm tra giá trị keys

    if keys is None:  
      return (0, 0)
    elif keys[pygame.K_UP]:
      return (-1, 0)
    elif keys[pygame.K_DOWN]:
      return (1, 0)
    elif keys[pygame.K_LEFT]:
      return (0, -1)
    elif keys[pygame.K_RIGHT]:
      return (0, 1)
  
    return (0, 0)
  
  def isValidPos(self, x, y):
      if 0 <= x < Board.ROWS and 0 <= y < Board.COLS:
          if (Board.maze[x][y] < 3 or Board.maze[x][y] == 9) and Board.coordinates[x][y] in (Board.BLANK, Board.PACMAN):
              return True
      return False
    
  def getTargetPos(self):
    dx, dy = self.keyboardHandle()
    oldx, oldy = Object.pacmanX + Object.PACMAN_DIRX, Object.pacmanY + Object.PACMAN_DIRY
    
    if (dx, dy) != (0, 0):
      newx, newy = Object.pacmanX + dx, Object.pacmanY + dy
      
      if self.isValidPos(newx, newy):
        Object.PACMAN_DIRX, Object.PACMAN_DIRY = (dx, dy)
        return (newx, newy)
      
    if self.isValidPos(oldx, oldy):
        return (oldx, oldy)
    else:
        return (Object.pacmanX, Object.pacmanY)
    
    
  def move(self):
    x, y = Object.pacmanX, Object.pacmanY
    targetX, targetY = Entity.getRealCoordinates((x, y), Object.PACMAN_SIZE) 
    realX, realY = Object.realPacmanX, Object.realPacmanY

    dx, dy = (targetX - realX), (targetY - realY)
    sX = Config.p_height / 15
    sY = Config.p_width / 15
  
    if abs(dx) >= sX:
      realX = realX + dx / abs(dx) * sX
    else:
      realX = targetX
    
    if (abs(dy)) == 728:
      realY = 0
      realX = 15 * Config.p_height + Config.p_height * 0.5 - Object.PACMAN_SIZE * 0.5
    elif abs(dy) >= sY:
      realY = realY + dy / abs(dy) * sY
    else:
      realY = targetY

    Object.realPacmanX = realX
    Object.realPacmanY = realY
  
  def updatePos(self):
    oldX, oldY = Object.pacmanX, Object.pacmanY
    if (oldX, oldY) == (15, 0):
      Board.coordinates[oldX][oldY] = Board.BLANK
      Board.coordinates[15][28] = Board.PACMAN
      Object.pacmanX, Object.pacmanY = 15,28
      return
    elif (oldX, oldY) == (15, 29):
      Board.coordinates[oldX][oldY] = Board.BLANK
      Board.coordinates[15][1] = Board.PACMAN
      Object.pacmanX, Object.pacmanY = 15, 1
      return
    else:
      if Board.maze[oldX][oldY] == 1:
        Board.maze[oldX][oldY] = 0
        Config.score += 10
      if Board.maze[oldX][oldY] == 2:
        Board.maze[oldX][oldY] = 0
        Config.score += 100
        
      targetPos = self.getTargetPos()
      
      if targetPos:
          targetX, targetY = targetPos
          newX, newY = oldX, oldY
          
          if targetX != oldX:
              newX += 1 if targetX > oldX else -1 
          if targetY != oldY:
              newY += 1 if targetY > oldY else -1 


          Board.coordinates[oldX][oldY] = Board.BLANK
          Board.coordinates[newX][newY] = Board.PACMAN
          Object.pacmanX, Object.pacmanY = newX, newY

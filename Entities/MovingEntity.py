import pygame
from Config import Config

class Entity:

    def __init__(self, xPos, yPos, size):
        self.xPos = xPos
        self.yPos = yPos
        self.size = size
        self.dead = False

    def draw(self):
        pass

    def update(self):
        pass

    def getRect(self):
        pass

    def getSize(self):
        return self.size

    def isDead(self):
        return self.dead

    def getXPos(self):
        return self.xPos

    def getYPos(self):
        return self.yPos

    def setDead(self):
        self.xPos = -32
        self.yPos = -32
        self.dead = True
        
class MovingEntity(Entity):
    def __init__(self, xPos, yPos, size, speed, spriteName, imgSpeed, imgPerCycle):
        super().__init__(xPos, yPos, size)

        self.speed = speed
        self.sprite = pygame.image.load(spriteName)
        self.imgSpeed = imgSpeed
        self.imgPerCycle = imgPerCycle
        self.direction = 0
        self.xSpeed = 0
        self.ySpeed = 0
        self.subImg = 0
        self.x_start = xPos
        self.y_start = yPos

    def draw(self):
        Config.screen.blit(
            self.sprite.subsurface(self.direction * self.imgPerCycle * self.size + self.size * int(self.subImg), 0,
                                   self.size, self.size), (self.xPos, self.yPos))

    def update(self):
        self.updatePos()

    def onTheGrid(self):
        return self.xPos % 8 == 0 and self.yPos % 8 == 0

    def onTheGamePlay(self):
        return 0 < self.xPos < Config.width and 0 < self.yPos < Config.height

    def updatePos(self):
        # ghost, x y nhân jđược từ thuật toán
        # pacman, x y nhận được từ bàn phim
        pass

    def getRect(self):
        pass

    def getDir(self):
        pass

    def reset(self):
        self.xPos = self.x_start
        self.yPos = self.y_start
        self.direction = 0
        self.xSpeed = 0
        self.ySpeed = 0
        self.subImg = 0
    
    
    

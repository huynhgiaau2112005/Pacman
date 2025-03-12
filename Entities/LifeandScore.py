from Config import Color, Config
from math import pi
import copy
import pygame

pygame.init()

class Life:
    def __init__(self):
        self.font = pygame.font.Font(None, 36)
        
    def draw(self):
        text = self.font.render("Lives: " + str(Config.life), 1, Color.color_text)
        Config.screen.blit(text, (150, 760))
        
    def decrease(self):
        Config.life -= 1
        
    def getLife(self):
        return Config.life

class Score:
    def __init__(self):
        self.font = pygame.font.Font(None, 36)
        
    def draw(self):
        text = self.font.render("Score: " + str(Config.score), 1, Color.color_text)
        Config.screen.blit(text, (20, 760))
        
    def increase(self, amount):
        Config.score += amount
        
    def getScore(self):
        return Config.score

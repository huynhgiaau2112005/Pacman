# A*

# Tham khảo BlueGhost.py

from .GhostInterface import GhostStrategy

class RedGhost(GhostStrategy):
    def move(self, position):
        print("Code Here")
    
    def getTargetPos(self, ghost, pacman):
        print("A*")
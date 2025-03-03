# A*

# Tham khảo BlueGhost.py

from .GhostInterface import GhostInterface

class RedGhost(GhostInterface):
    def move(self, position):
        print("Code Here")
    
    def getTargetPos(self, ghost, pacman):
        print("A*")
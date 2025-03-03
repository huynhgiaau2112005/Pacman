from .GhostInterface import GhostStrategy

class PinkGhost(GhostStrategy):
    def move(self, position):
        print("Code Here")
    
    def getTargetPos(self, ghost, pacman):
        print("UCS")
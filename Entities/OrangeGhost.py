from .GhostInterface import GhostStrategy

class OrangeGhost(GhostStrategy):
    def move(self, position):
        print("Code Here")
    
    def getTargetPos(self, ghost, pacman):
        print("DFS")
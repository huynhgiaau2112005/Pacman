from .GhostInterface import GhostInterface

class OrangeGhost(GhostInterface):
    def move(self, position):
        print("Code Here")
    
    def getTargetPos(self, ghost, pacman):
        print("DFS")
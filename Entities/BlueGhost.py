# # BFS
from .GhostInterface import GhostStrategy

class BlueGhost(GhostStrategy):
    def move(self, position):
        print("Code Here")

    def getTargetPos(self, ghost, pacman):
        print("BFS")
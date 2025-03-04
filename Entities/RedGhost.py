# A*

# Tham khảo BlueGhost.py

from .GhostInterface import GhostInterface
from Config import Config, Material, Board
import heapq

class RedGhost(GhostInterface):
    def draw(self):
        realX = Config.redGhostX * Config.p_height #+ (0.5 * Config.p_height)
        realY = Config.redGhostY * Config.p_width #+ (0.5 * Config.p_width)

        Config.screen.blit(Material.RedGhostImage, (realY, realX))
        
    def move(self, position):
        print("Code Here")
    
    def heuristic(self, ghostX, ghostY):
        return abs(ghostX - Config.pacmanX) + abs(ghostY - Config.pacmanY)
    
    def getTargetPos(self, ghost, pacman): # A*
        (posX, posY) = ghost
        f = 0
        h = f + self.heuristic(posX, posY)
        
        heap = [(f, h, posX, posY, [])] # f(x), heuristic curX, curY, path
        heapq.heapify(heap)
        
        visited = set([(posX, posY)])
        
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        PATH_LIMIT = 100

        while heap:
            (f, h, x, y, path) = heapq.heappop(heap)
            
            if Board.coordinates[x][y] == Board.PACMAN or len(path) == PATH_LIMIT:
                return path[0]

            for dx, dy in DIRECTIONS:
                nx = x + dx
                ny = y + dy

                if 0 <= nx < Board.ROWS and 0 <= ny < Board.COLS and (nx, ny) not in visited:
                    if Board.maze[nx][ny] < 3 or Board.maze[nx][ny] == 9 or Board.coordinates[nx][ny] == Board.PACMAN:
                        nh = self.heuristic(nx, ny)
                        nf = f + 1 - h + nh
                        heapq.heappush(heap, (nf, nh, nx, ny, path + [(nx, ny)]))
                        visited.add((nx, ny))
        
        return []
    
    def updatePos(self):
        oldX, oldY = Config.redGhostX, Config.redGhostY
        newPos = self.getTargetPos((oldX, oldY), (Config.pacmanX, Config.pacmanY))
        
        if newPos:
            newX, newY = newPos

            Board.coordinates[oldX][oldY] = Board.BLANK
            Board.coordinates[newX][newY] = Board.RED_GHOST

            Config.redGhostX = newX
            Config.redGhostY = newY


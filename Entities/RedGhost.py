# A*

# Tham khảo BlueGhost.py

from .Entity import Entity
from .GhostInterface import GhostInterface
from Config import Config, Material, Board, Object
import heapq

class RedGhost(GhostInterface):
    def draw(self):
        realX = Object.realRedGhostX
        realY = Object.realRedGhostY
        Config.screen.blit(Material.RedGhostImage, (realY, realX))
        
    def move(self):
        x, y = Object.redGhostX, Object.redGhostY

        targetX, targetY = Entity.getRealCoordinates((x, y), Object.RED_GHOST_SIZE) # tọa độ thực muốn đi đến
        realX, realY = Object.realRedGhostX, Object.realRedGhostY # tọa độ thực hiện tại

        dx, dy = (targetX - realX), (targetY - realY)
        sX = Config.p_height / 15
        sY = Config.p_width / 15
        if abs(dx) >= sX:
            realX = realX + dx / abs(dx) * sX
        else:
            realX = targetX
        
        if abs(dy) >= sY:
            realY = realY + dy / abs(dy) * sY
        else:
            realY = targetY

        Object.realRedGhostX = realX
        Object.realRedGhostY = realY
    
    def isValidPos(self, x, y):
        if 0 <= x < Board.ROWS and 0 <= y < Board.COLS:
            if (Board.maze[x][y] < 3 or Board.maze[x][y] == 9) and Board.coordinates[x][y] in (Board.BLANK, Board.PACMAN):
                return True
        return False
    
    def heuristic(self, ghostX, ghostY):
        return abs(ghostX - Object.pacmanX) + abs(ghostY - Object.pacmanY)
    
    def getTargetPos(self, ghost, pacman): # A*
        (posX, posY) = ghost
        f = 0
        h = f + self.heuristic(posX, posY)
        
        heap = [(f, h, posX, posY, [])] # f(x), heuristic curX, curY, path
        heapq.heapify(heap)
        
        visited = set([(posX, posY)])
        
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)] # lên, xuống, phải, trái

        PATH_LIMIT = 100

        while heap:
            (f, h, x, y, path) = heapq.heappop(heap)
            
            if Board.coordinates[x][y] == Board.PACMAN or len(path) == PATH_LIMIT:
                return path[0]

            for dx, dy in DIRECTIONS:
                nx = x + dx
                ny = y + dy
                if not self.isValidPos(nx, ny):
                    continue
                while (nx, ny) not in Board.nodes and (nx, ny) != (Object.pacmanX, Object.pacmanY):
                    nx += dx
                    ny += dy
                    if not self.isValidPos(nx, ny):
                        break

                if (nx, ny) not in visited and self.isValidPos(nx, ny):
                    nh = self.heuristic(nx, ny)
                    nf = f - h + nh + abs(nx - x) + abs(ny - y)
                    heapq.heappush(heap, (nf, nh, nx, ny, path + [(nx, ny)]))
                    visited.add((nx, ny))
        
        return None
    
    def getTargetPathInformation(self, ghost, pacman):
        (posX, posY) = ghost
        f = 0
        h = f + self.heuristic(posX, posY)
        
        heap = [(f, h, posX, posY, [])] # f(x), heuristic curX, curY, path
        heapq.heapify(heap)
        
        visited = set([])
        
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)] # lên, xuống, phải, trái

        PATH_LIMIT = 100

        while heap:
            (f, h, x, y, path) = heapq.heappop(heap)
            visited.add((x, y))

            if Board.coordinates[x][y] == Board.PACMAN or len(path) == PATH_LIMIT:
                return path, len(visited)

            for dx, dy in DIRECTIONS:
                nx = x + dx
                ny = y + dy
                if not self.isValidPos(nx, ny):
                    continue
                while (nx, ny) not in Board.nodes and (nx, ny) != (Object.pacmanX, Object.pacmanY):
                    nx += dx
                    ny += dy
                    if not self.isValidPos(nx, ny):
                        break

                if (nx, ny) not in visited and self.isValidPos(nx, ny):
                    nh = self.heuristic(nx, ny)
                    nf = f - h + nh + abs(nx - x) + abs(ny - y)
                    heapq.heappush(heap, (nf, nh, nx, ny, path + [(nx, ny)]))
        
        return None, len(visited)

    def updatePos(self):
        oldX, oldY = Object.redGhostX, Object.redGhostY
        targetPos = self.getTargetPos((oldX, oldY), (Object.pacmanX, Object.pacmanY))

        if targetPos:
            targetX, targetY = targetPos

            newX, newY = oldX, oldY
            if targetX != oldX:
                newX += (targetX - oldX) // abs(targetX - oldX) 
            if targetY != oldY:
                newY += (targetY - oldY) // abs(targetY - oldY)

            Board.coordinates[oldX][oldY] = Board.BLANK
            Board.coordinates[newX][newY] = Board.RED_GHOST

            Object.redGhostX = newX
            Object.redGhostY = newY


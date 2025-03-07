# # DFS
import heapq
from .Entity import Entity
from .GhostInterface import GhostInterface
from Config import Config, Material, Board, Object

class OrangeGhost(GhostInterface):
    def draw(self):
        realX = Object.realOrangeGhostX
        realY = Object.realOrangeGhostY
        Config.screen.blit(Material.OrangeGhostImage, (realY, realX))

    def move(self):
        x, y = Object.orangeGhostX, Object.orangeGhostY

        targetX, targetY = Entity.getRealCoordinates((x, y), Object.ORANGE_GHOST_SIZE) # tọa độ thực muốn đi đến
        realX, realY = Object.realOrangeGhostX, Object.realOrangeGhostY # tọa độ thực hiện tại

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

        Object.realOrangeGhostX = realX
        Object.realOrangeGhostY = realY

    # Anh em chỉ cần viết thuật toán vào hàm này, các hàm còn lại Âu đã viết 
    def getTargetPos(self, ghost, pacman):
        (ghostX, ghostY) = ghost
        f = 0
        heap = [(f, ghostX, ghostY, [])]
        visited = set([(ghostX, ghostY)])
        
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        PATH_LIMIT = 100
        
        while heap:
            
            (f, x, y, path) = heapq.heappop(heap)
    
            if Board.coordinates[x][y] == Board.PACMAN or len(path) == PATH_LIMIT:
                return path[0]
            
            for dx, dy in DIRECTIONS:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < Board.ROWS and 0 <= ny < Board.COLS and (nx, ny) not in visited:
                    if Board.maze[nx][ny] < 3 or Board.maze[nx][ny] == 9 or Board.coordinates[nx][ny] == Board.PACMAN:
                        visited.add((nx, ny))
                        heapq.heappush(heap, (f + 1, nx, ny, path + [(nx, ny)]))
        
        return None
                
    def updatePos(self):
        oldX, oldY = Object.orangeGhostX, Object.orangeGhostY
        newPos = self.getTargetPos((oldX, oldY), (Object.pacmanX, Object.pacmanY))
        
        if newPos:
            newX, newY = newPos

            Board.coordinates[oldX][oldY] = Board.BLANK
            Board.coordinates[newX][newY] = Board.ORANGE_GHOST

            Object.orangeGhostX = newX
            Object.orangeGhostY = newY
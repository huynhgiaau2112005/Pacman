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

    def isValidPos(self, x, y):
        if 0 <= x < Board.ROWS and 0 <= y < Board.COLS:
            if (Board.maze[x][y] < 3 or Board.maze[x][y] == 9) and Board.coordinates[x][y] in (Board.BLANK, Board.PACMAN):
                return True
        return False
    
    # Anh em chỉ cần viết thuật toán vào hàm này, các hàm còn lại Âu đã viết 
   
    def getTargetPos(self, ghost, pacman): # UCS*
        (posX, posY) = ghost
        f = 0
        heap = [(f, posX, posY, [])] 
        heapq.heapify(heap)
        visited = set([])
        
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)] # lên, xuống, phải, trái
        PATH_LIMIT = 100

        while heap:
            (f, x, y, path) = heapq.heappop(heap)
            visited.add((x, y))
            
            #print(Board.coordinates[int(x)][int(y)])
            if Board.coordinates[int(x)][int(y)] == Board.PACMAN or len(path) == PATH_LIMIT:
                return path[0]   
            
            for dx, dy in DIRECTIONS:
                
                nx = x + dx
                ny = y + dy
                
                while self.isValidPos(nx, ny) and (nx, ny) not in Board.nodes and (nx, ny) != (Object.pacmanX, Object.pacmanY):
                    nx += dx
                    ny += dy          
                    
                if (nx, ny) not in visited and self.isValidPos(nx, ny)\
                    and Board.coordinates[nx][ny] != Board.PINK_GHOST \
                    and Board.coordinates[nx][ny] != Board.BLUE_GHOST \
                    and Board.coordinates[nx][ny] != Board.RED_GHOST: #check collision::
                    heapq.heappush(heap, (f + abs(nx - x) + abs(ny - y), nx, ny, path + [(nx, ny)]))
                
        return None
    
    
    def getTargetPathInformation(self, ghost, pacman):
        if ghost == pacman:
            return None, 0
        
        (ghostX, ghostY) = ghost
        f = 0
        heap = [(f, ghostX, ghostY, [])]
        visited = set([])
        
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        PATH_LIMIT = 100
        
        while heap:
            
            (f, x, y, path) = heapq.heappop(heap)
            visited.add((x, y))
            
            if Board.coordinates[int(x)][int(y)] == Board.PACMAN or len(path) == PATH_LIMIT:
                return path, len(visited)    
            
            for dx, dy in DIRECTIONS:
                
                nx = x + dx
                ny = y + dy
                subpath = [(nx, ny)]
                
                while self.isValidPos(nx, ny) and (nx, ny) not in Board.nodes and (nx, ny) != (Object.pacmanX, Object.pacmanY):
                    nx += dx
                    ny += dy
                    subpath.append((nx, ny))          
                
                if (nx, ny) == (Object.pacmanX, Object.pacmanY):
                    return path + subpath, len(visited)
                    
                if (nx, ny) not in visited and self.isValidPos(nx, ny)\
                    and Board.coordinates[nx][ny] != Board.PINK_GHOST \
                    and Board.coordinates[nx][ny] != Board.BLUE_GHOST \
                    and Board.coordinates[nx][ny] != Board.RED_GHOST: #check collision::
                    heapq.heappush(heap, (f + abs(nx - x) + abs(ny - y), nx, ny, path + subpath))
                
        return None, len(visited)
    
    def updatePos(self):
        oldX, oldY = Object.orangeGhostX, Object.orangeGhostY
        targetPos = self.getTargetPos((oldX, oldY), (Object.pacmanX, Object.pacmanY))
        if targetPos:
            targetX, targetY = targetPos

            newX, newY = oldX, oldY
            if targetX != oldX:
                newX += (targetX - oldX) // abs(targetX - oldX) 
            if targetY != oldY:
                newY += (targetY - oldY) // abs(targetY - oldY)

            Board.coordinates[oldX][oldY] = Board.BLANK
            Board.coordinates[newX][newY] = Board.ORANGE_GHOST

            Object.orangeGhostX = newX
            Object.orangeGhostY = newY
    
    def isValidPosPowerUp(self, x, y):
        if 0 <= x < Board.ROWS and 0 <= y < Board.COLS:
            if (Board.maze[x][y] < 3 or Board.maze[x][y] == 9) and Board.coordinates[x][y] == Board.BLANK:
                return True
        return False
    
    def getTargetPosPowerUp(self, ghost, target): # UCS*
        (posX, posY) = ghost
        f = 0
        heap = [(f, posX, posY, [])] 
        heapq.heapify(heap)
        visited = set([(posX, posY)])
        
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)] # lên, xuống, phải, trái
        PATH_LIMIT = 100

        while heap:
            (f, x, y, path) = heapq.heappop(heap)
            
            if (x, y) == target or len(path) == PATH_LIMIT:
                return path[0] if len(path) > 0 else None

            for dx, dy in DIRECTIONS:
                nx = x + dx
                ny = y + dy
                
                if not self.isValidPosPowerUp(nx, ny):
                    continue
                while (nx, ny) not in Board.nodes and (nx, ny) != target:
                    nx += dx
                    ny += dy
                    if not self.isValidPosPowerUp(nx, ny):
                        break

                if (nx, ny) not in visited and self.isValidPosPowerUp(nx, ny)\
                    and (nx, ny) != (Object.pinkGhostX, Object.pinkGhostY) \
                    and (nx, ny) != (Object.blueGhostX, Object.blueGhostY) \
                    and (nx, ny) != (Object.redGhostX, Object.redGhostY) \
                    and (nx, ny) != (Object.pacmanX, Object.pacmanY): #check collision:
                    nf = f + abs(nx - x) + abs(ny - y)
                    heapq.heappush(heap, (nf, nx, ny, path + [(nx, ny)]))
                    visited.add((nx, ny))
        
        return None
    
    def updatePosPowerUp(self, target):
        oldX, oldY = Object.orangeGhostX, Object.orangeGhostY
        targetPos = self.getTargetPosPowerUp((oldX, oldY), target)

        if targetPos:
            targetX, targetY = targetPos

            newX, newY = oldX, oldY
            if targetX != oldX:
                newX += (targetX - oldX) // abs(targetX - oldX) 
            if targetY != oldY:
                newY += (targetY - oldY) // abs(targetY - oldY)

            Board.coordinates[oldX][oldY] = Board.BLANK
            Board.coordinates[newX][newY] = Board.ORANGE_GHOST

            Object.orangeGhostX = newX
            Object.orangeGhostY = newY
    
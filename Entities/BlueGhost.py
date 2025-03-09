# # BFS
from .Entity import Entity
from .GhostInterface import GhostInterface
from Config import Config, Material, Board, Object
from collections import deque

class BlueGhost(GhostInterface):
    def draw(self):
        realX = Object.realBlueGhostX
        realY = Object.realBlueGhostY
        Config.screen.blit(Material.BlueGhostImage, (realY, realX))

    def move(self):
        x, y = Object.blueGhostX, Object.blueGhostY

        targetX, targetY = Entity.getRealCoordinates((x, y), Object.BLUE_GHOST_SIZE) # tọa độ thực muốn đi đến
        realX, realY = Object.realBlueGhostX, Object.realBlueGhostY # tọa độ thực hiện tại

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

        Object.realBlueGhostX = realX
        Object.realBlueGhostY = realY

    # Anh em chỉ cần viết thuật toán vào hàm này, các hàm còn lại Âu đã viết 
    def getTargetPos(self, ghost, pacman):
        bfs_direction = [(0, -1), (0, 1), (-1, 0), (1, 0)] #trai, phai, tren, duoi
        queue = deque([ghost])
        visited = set([ghost])
        parent = {ghost : None} # con : cha

        if ghost == pacman: return None

        while queue:
            ghost_x, ghost_y = queue.popleft()

            #Neu gap pacman
            if (ghost_x, ghost_y) == pacman:     
                path = [] #list path
                while (ghost_x, ghost_y) != ghost:
                    path.append((ghost_x, ghost_y))
                    (ghost_x, ghost_y) = parent[(ghost_x, ghost_y)]
                #path.append((ghost_x, ghost_y))
                path = path[::-1]
                return path[0]

            #Duyet BFS
            for x, y in bfs_direction:
                go_x = ghost_x + x
                go_y = ghost_y + y
                if 0 <= go_x < Board.ROWS and 0 <= go_y < Board.COLS:
                    if (0 <= Board.maze[go_x][go_y] <= 2 or Board.maze[go_x][go_y] == 9) and (go_x, go_y) not in visited:
                        queue.append((go_x, go_y))
                        visited.add((go_x, go_y))
                        parent[(go_x, go_y)] = (ghost_x, ghost_y)                        
        return None
    
    def getTargetPathInformation(self, ghost, pacman):
        bfs_direction = [(0, -1), (0, 1), (-1, 0), (1, 0)] #trai, phai, tren, duoi
        queue = deque([ghost])
        visited = set([ghost])
        parent = {ghost : None} # con : cha

        if ghost == pacman: return None

        while queue:
            ghost_x, ghost_y = queue.popleft()

            #Neu gap pacman
            if (ghost_x, ghost_y) == pacman:     
                path = [] #list path
                while (ghost_x, ghost_y) != ghost:
                    path.append((ghost_x, ghost_y))
                    (ghost_x, ghost_y) = parent[(ghost_x, ghost_y)]
                #path.append((ghost_x, ghost_y))
                path = path[::-1]
                return path

            #Duyet BFS
            for x, y in bfs_direction:
                go_x = ghost_x + x
                go_y = ghost_y + y
                if 0 <= go_x < Board.ROWS and 0 <= go_y < Board.COLS:
                    if (0 <= Board.maze[go_x][go_y] <= 2 or Board.maze[go_x][go_y] == 9) and (go_x, go_y) not in visited:
                        queue.append((go_x, go_y))
                        visited.add((go_x, go_y))
                        parent[(go_x, go_y)] = (ghost_x, ghost_y)                        
        return None
    def updatePos(self):
        oldX, oldY = Object.blueGhostX, Object.blueGhostY
        newPos = self.getTargetPos((oldX, oldY), (Object.pacmanX, Object.pacmanY))
        
        if newPos:
            newX, newY = newPos

            Board.coordinates[oldX][oldY] = Board.BLANK
            Board.coordinates[newX][newY] = Board.BLUE_GHOST

            Object.blueGhostX = newX
            Object.blueGhostY = newY

    def updatePosForEachLv(self, newPos):
        oldX, oldY = Object.blueGhostX, Object.blueGhostY        
        if newPos:
            newX, newY = newPos

            Board.coordinates[oldX][oldY] = Board.BLANK
            Board.coordinates[newX][newY] = Board.BLUE_GHOST

            Object.blueGhostX = newX
            Object.blueGhostY = newY
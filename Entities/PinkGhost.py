# # DFS
from .Entity import Entity
from .GhostInterface import GhostInterface
from Config import Config, Material, Board, Object
from collections import deque

class PinkGhost(GhostInterface):
    def draw(self):
        realX = Object.realPinkGhostX
        realY = Object.realPinkGhostY
        Config.screen.blit(Material.PinkGhostImage, (realY, realX))

    def move(self):
        x, y = Object.pinkGhostX, Object.pinkGhostY

        targetX, targetY = Entity.getRealCoordinates((x, y), Object.PINK_GHOST_SIZE) # tọa độ thực muốn đi đến
        realX, realY = Object.realPinkGhostX, Object.realPinkGhostY # tọa độ thực hiện tại

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

        Object.realPinkGhostX = realX
        Object.realPinkGhostY = realY

    # Anh em chỉ cần viết thuật toán vào hàm này, các hàm còn lại Âu đã viết 
    def getTargetPos(self, ghost, pacman):
        # dfs_directions = [(1, 0), (-1, 0), (0, -1), (0, 1)] # Xuống, Lên, Trái, Phải
        # stack = deque([ghost])
        # visited = set([ghost])
        # parent = {ghost : None}

        # while stack:
        #     (ghost_x, ghost_y) = stack.pop()

        #     #Neu gap pacman
        #     if (ghost_x, ghost_y) == pacman:
        #         path = [] #list path
        #         while (ghost_x, ghost_y) != ghost:
        #             path.append((ghost_x, ghost_y))
        #             (ghost_x, ghost_y) = parent[(ghost_x, ghost_y)]
        #         path = path[::-1]
        #         for i in path:
        #             print(i)
        #         print("\n\n---------------------------------")
        #         return path[0]

        #     found_next = False  # Biến kiểm tra có tìm được đường đi hợp lệ không
        #     for x, y in dfs_directions:
                
        #         go_x = ghost_x + x
        #         go_y = ghost_y + y

        #         if 0 <= go_x < Board.ROWS and 0 <= go_y < Board.COLS and (go_x, go_y) not in visited:
        #             if 0 <= Board.maze[go_x][go_y] <= 2 or Board.maze[go_x][go_y] == 9:
        #                 stack.append((go_x, go_y))
        #                 visited.add((go_x, go_y))
        #                 parent[(go_x, go_y)] = (ghost_x, ghost_y)
        #                 found_next = True
        #                 #break
        #     # Nếu không tìm được hướng đi hợp lệ nào, quay lui
        #     if not found_next and parent[(ghost_x, ghost_y)] is not None:
        #         stack.append(parent[(ghost_x, ghost_y)])
        # return None
        
        #Neu ban dau da o pacman
        if (ghost) == pacman:
            return None 
            
        ids_direction = [(1, 0), (-1, 0), (0, -1), (0, 1)] # Xuống, Lên, Trái, Phải
        max_depth_limit = 100
        depth_limit = 1
        while depth_limit <= max_depth_limit:
            stack = deque([(ghost)])
            visited = set([ghost])
            depths = {ghost: 0}  
            parent = {ghost : None}

            while stack:# is not None or count_depth == depth_limit:
                (ghost_x, ghost_y) = stack.pop()
                depth = depths[(ghost_x, ghost_y)]
                #print((depth_limit, (ghost_x, ghost_y), depth))

                if depth < depth_limit:
                    for x, y in ids_direction:
                        go_x = ghost_x + x
                        go_y = ghost_y + y

                        if 0 <= go_x < Board.ROWS and 0 <= go_y < Board.COLS and ((go_x, go_y) not in visited or depth + 1 < depths[(go_x, go_y)]):
                            if 0 <= Board.maze[go_x][go_y] <= 2 or Board.maze[go_x][go_y] == 9:
                                stack.append((go_x, go_y))
                                visited.add((go_x, go_y))
                                depths[(go_x, go_y)] = depth + 1
                                parent[(go_x, go_y)] = (ghost_x, ghost_y)

                                #Neu gap pacman
                                if (go_x, go_y) == pacman:      #Early stop
                                    ghost_x, ghost_y = pacman
                                    path = [] #list path
                                    while (ghost_x, ghost_y) != ghost:
                                        path.append((ghost_x, ghost_y))
                                        (ghost_x, ghost_y) = parent[(ghost_x, ghost_y)]
                                    #path.append((ghost_x, ghost_y))
                                    path = path[::-1]
                                    return path[0]    
                else: visited.discard((ghost_x, ghost_y))
            depth_limit += 1
                    

        
    
    def updatePos(self):
        oldX, oldY = Object.pinkGhostX, Object.pinkGhostY
        newPos = self.getTargetPos((oldX, oldY), (Object.pacmanX, Object.pacmanY))
        # print("Gia tri lay ra: ", end="")
        # print(newPos, end='\n\n=======================')

        if newPos:
            newX, newY = newPos

            Board.coordinates[oldX][oldY] = Board.BLANK
            Board.coordinates[newX][newY] = Board.PINK_GHOST

            Object.pinkGhostX = newX
            Object.pinkGhostY = newY

    def pinkGhostForLv2(self, ghost, pacman):
        dfs_directions = [(1, 0), (-1, 0), (0, -1), (0, 1)] # Xuống, Lên, Trái, Phải
        stack = deque([ghost])
        visited = set([ghost])
        parent = {ghost : None}

        while stack:
            (ghost_x, ghost_y) = stack.pop()

            #Neu gap pacman
            if (ghost_x, ghost_y) == pacman:
                path = [] #list path
                while (ghost_x, ghost_y) != ghost:
                    path.append((ghost_x, ghost_y))
                    (ghost_x, ghost_y) = parent[(ghost_x, ghost_y)]
                path = path[::-1]
                #for i in path:
                #    print(i)
               # print("\n\n---------------------------------")
                return path

            found_next = False  # Biến kiểm tra có tìm được đường đi hợp lệ không
            for x, y in dfs_directions:
                
                go_x = ghost_x + x
                go_y = ghost_y + y

                if 0 <= go_x < Board.ROWS and 0 <= go_y < Board.COLS and (go_x, go_y) not in visited:
                    if 0 <= Board.maze[go_x][go_y] <= 2 or Board.maze[go_x][go_y] == 9:
                        stack.append((go_x, go_y))
                        visited.add((go_x, go_y))
                        parent[(go_x, go_y)] = (ghost_x, ghost_y)
                        found_next = True
                        break
            # Nếu không tìm được hướng đi hợp lệ nào, quay lui
            if not found_next and parent[(ghost_x, ghost_y)] is not None:
                stack.append(parent[(ghost_x, ghost_y)])
        return None
    def updatePosForLv2(self, newPos):
        oldX, oldY = Object.pinkGhostX, Object.pinkGhostY
        #print("Gia tri lay ra: ", end="")
        #print(newPos, end='\n\n=======================')
    

        if newPos:
            newX, newY = newPos

            Board.coordinates[oldX][oldY] = Board.BLANK
            Board.coordinates[newX][newY] = Board.PINK_GHOST

            Object.pinkGhostX = newX
            Object.pinkGhostY = newY

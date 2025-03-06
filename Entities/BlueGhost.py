# # BFS
from .Entity import Entity
from .GhostInterface import GhostInterface
from Config import Config, Material, Board, Object

class BlueGhost(GhostInterface):
    def draw(self):
        realX = Object.realBlueGhostX
        realY = Object.realBlueGhostY
        Config.screen.blit(Material.blueGhostImage, (realY, realX))

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
        print("BFS")
    
    def updatePos(self):
        oldX, oldY = Object.blueGhostX, Object.blueGhostY
        newPos = self.getTargetPos((oldX, oldY), (Object.pacmanX, Object.pacmanY))
        
        if newPos:
            newX, newY = newPos

            Board.coordinates[oldX][oldY] = Board.BLANK
            Board.coordinates[newX][newY] = Board.BLUE_GHOST

            Object.blueGhostX = newX
            Object.blueGhostY = newY
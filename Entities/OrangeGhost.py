# # DFS
from .Entity import Entity
from .GhostInterface import GhostInterface
from Config import Config, Material, Board, Object

class OrangeGhost(GhostInterface):
    def draw(self):
        realX = Object.realOrangeGhostX
        realY = Object.realOrangeGhostY
        Config.screen.blit(Material.orangeGhostImage, (realY, realX))

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
        print("DFS")
    
    def updatePos(self):
        oldX, oldY = Object.orangeGhostX, Object.orangeGhostY
        newPos = self.getTargetPos((oldX, oldY), (Object.pacmanX, Object.pacmanY))
        
        if newPos:
            newX, newY = newPos

            Board.coordinates[oldX][oldY] = Board.BLANK
            Board.coordinates[newX][newY] = Board.ORANGE_GHOST

            Object.orangeGhostX = newX
            Object.orangeGhostY = newY
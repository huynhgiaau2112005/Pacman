# # UCS
from .Entity import Entity
from .GhostInterface import GhostInterface
from Config import Config, Material, Board, Object

class PinkGhost(GhostInterface):
    def draw(self):
        realX = Object.realPinkGhostX
        realY = Object.realPinkGhostY
        Config.screen.blit(Material.pinkGhostImage, (realY, realX))

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
        print("UCS")
    
    def updatePos(self):
        oldX, oldY = Object.pinkGhostX, Object.pinkGhostY
        newPos = self.getTargetPos((oldX, oldY), (Object.pacmanX, Object.pacmanY))
        
        if newPos:
            newX, newY = newPos

            Board.coordinates[oldX][oldY] = Board.BLANK
            Board.coordinates[newX][newY] = Board.PINK_GHOST

            Object.pinkGhostX = newX
            Object.pinkGhostY = newY
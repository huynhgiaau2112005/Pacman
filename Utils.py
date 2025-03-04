class Utils:
  @staticmethod
  def getCoordinates(board, rows, cols, value):
    for x in range (rows):
      for y in range (cols):
        if board[x][y] == value:
          return x, y
    return None
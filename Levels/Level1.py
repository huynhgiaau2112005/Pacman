class Level1:
  def execute():
    print('Code Here')

    # init procedure: FPS, ...

    while running:
      # clear screen
      Maze.drawing()
      Pacman.keyboardHandle()
      for ghost in ghosts:
        ghost.move()
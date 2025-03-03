from ..entitiesmanager import Config, Entity

class Level2:
  def execute():
    print('Code Here')

    # init procedure: FPS, ...

    while Config.running:
      # clear screen
      Entity.Maze.drawing()
      #Entity.Pacman.keyboardHandle()
      #for ghost in Entity.ghosts:
        #ghost.move()
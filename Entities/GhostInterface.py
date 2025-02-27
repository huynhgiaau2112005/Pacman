from abc import ABC, abstractmethod

class GhostInterface(ABC):
  @abstractmethod
  def move(self, position: tuple):
    pass
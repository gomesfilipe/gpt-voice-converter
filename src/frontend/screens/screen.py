from abc import ABC, abstractmethod

class Screen(ABC):
  @abstractmethod
  def render(self) -> None:
    pass
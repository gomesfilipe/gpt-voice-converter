from abc import ABC, abstractmethod

class GPT(ABC):
  @abstractmethod
  def send(self, text: str) -> str:
    pass

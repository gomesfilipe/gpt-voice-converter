from abc import ABC, abstractmethod

class GptApi(ABC):
  def __init__(self, api_key: str):
    self._api_key = api_key

  @abstractmethod
  def send(self, text: str) -> str:
    pass

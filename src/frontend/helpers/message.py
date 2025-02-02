from src.enums.side import Side

class Message():
  def __init__(
      self,
      content: str,
      audio_filename: str,
      max_width: int,
      side: Side,
    ):
    self.__content = content
    self.__audio_filename = audio_filename
    self.__max_width = max_width
    self.__side = side
  
  @property
  def content(self) -> str:
    return self.__content
  
  @property
  def audio_filename(self) -> str:
    return self.__audio_filename
  
  @property
  def max_width(self) -> int:
    return self.__max_width
  
  @property
  def side(self) -> Side:
    return self.__side

from abc import ABC, abstractmethod
from src.enums.language import Language

class AudioTextConverter(ABC):
  @abstractmethod
  def save_audio_from_text(self, text: str, audio_filename: str, language: Language) -> None:
    pass

  @abstractmethod
  def generate_text_from_audio_file(self, audio_filename: str) -> str:
    """
      Raises:
        UnknownAudioException
        ConnetionFailedException
    """

  @abstractmethod
  def save_audio_from_voice(self, audio_filename: str) -> None:
    """
      Raises:
        UnknownAudioException
        ConnetionFailedException
    """

  @abstractmethod
  def run_audio_from_file(self, audio_filename: str) -> None:
    pass

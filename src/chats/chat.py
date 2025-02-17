from src.audio_text_converters.audio_text_converter import AudioTextConverter
from src.gpts.gpt import GPT
import os
from typing import List
from src.enums.color import Color
import time
from src.enums.language import Language
from src.exceptions.audio_exceptions import UnknownAudioException, ConnetionFailedException

class Chat():
  def __init__(self, audio_text_converter: AudioTextConverter, gpt: GPT):
    self.__audio_text_converter = audio_text_converter
    self.__gpt = gpt
    self.__audios_path = 'audios'
    os.makedirs(self.__audios_path, exist_ok = True)
    self.__index: int = 0

  def __delete_audio_files(self) -> None:
    files: List[str] = os.listdir(self.__audios_path)

    for file in files:
      file_path: str = os.path.join(self.__audios_path, file)
      if os.path.isfile(file_path):
        os.remove(file_path)

  def __get_audio_input_from_user(self) -> str:
    user_audio_filename = os.path.join(self.__audios_path, f'user_{self.__index}.wav')
    text = None

    while True:
      try:
        self.__audio_text_converter.save_audio_from_voice(user_audio_filename)
        Color.BLUE.print('[APP] Processando voz...')
        text =  self.__audio_text_converter.generate_text_from_audio_file(user_audio_filename)
        Color.GREEN.print(f'[USER] {text}')

      except UnknownAudioException:
        Color.RED.print('[APP] Fala não foi reconhecida, por favor repita.')
      except ConnetionFailedException:
        Color.RED.print('[APP] Houve um erro ao capturar sua voz, por favor repita.')
      finally:
        if text is not None:
          return text

  def __display_audio_answer_from_gpt(self, text: str) -> None:
    gpt_audio_filename = os.path.join(self.__audios_path, f'gpt_{self.__index}.wav')
    gpt_text = None

    for _ in range(3):
      try:
        gpt_text = self.__gpt.send(text)
        break
      except ConnetionFailedException:
        continue

    if gpt_text is None:
      Color.RED.print('[APP] Houve um erro ao se conectar com o GPT. Tente novamente.')
      return

    Color.GREEN.print(f'[GPT] {gpt_text}')

    self.__audio_text_converter.save_audio_from_text(gpt_text, gpt_audio_filename, Language.PORTUGUESE)
    self.__audio_text_converter.run_audio_from_file(gpt_audio_filename)

  def __chat(self) -> None:
    while True:
      Color.YELLOW.print('[APP] Diga alguma coisa...')
      user_text = self.__get_audio_input_from_user()

      Color.YELLOW.print('[APP] Enviando mensagem para o GPT...')
      self.__display_audio_answer_from_gpt(user_text)
      self.__index += 1

  def run_chat(self) -> None:
    self.__delete_audio_files()

    try:
      self.__chat()
    except KeyboardInterrupt as exception:
      Color.YELLOW.print('\n[APP] Encerrando Chat...')
      time.sleep(0.5)
      Color.GREEN.print('[APP] Chat encerrado com sucesso!')

    self.__delete_audio_files()

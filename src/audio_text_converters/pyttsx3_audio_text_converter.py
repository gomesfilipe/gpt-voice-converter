from src.audio_text_converters.audio_text_converter import AudioTextConverter
from src.enums.language import Language
from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
from src.exceptions.audio_exceptions import UnknownAudioException, ConnetionFailedException
from src.enums.color import Color
import contextlib
import noisereduce as nr
import scipy.io.wavfile as wav
import tempfile
import os

# Estava aparecendo muitos warnings na execução que nao eram relevantes
@contextlib.contextmanager
def suppress_stderr():
    # Salva o descritor original do stderr
    original_stderr_fd = os.dup(2)
    # Abre /dev/null para escrita
    devnull_fd = os.open(os.devnull, os.O_WRONLY)
    try:
        # Redireciona o stderr para /dev/null
        os.dup2(devnull_fd, 2)
        yield
    finally:
        # Restaura o stderr original
        os.dup2(original_stderr_fd, 2)
        os.close(devnull_fd)

class Pyttsx3AudioTextConverter(AudioTextConverter):
    def __init__(self):
        self.__recognizer = sr.Recognizer()

    def save_audio_from_text(self, text: str, audio_filename: str, language: Language) -> None:
        tts = gTTS(text, lang=language.value)
        tts.save(audio_filename)

    def preprocess_audio(self, audio_filename: str) -> str:
        """
        Carrega o áudio do arquivo, aplica redução de ruído e salva em um arquivo temporário.
        Retorna o caminho do arquivo processado.
        """

        with suppress_stderr():
          # Carrega o áudio (taxa de amostragem e dados)
          rate, data = wav.read(audio_filename)
          # Aplica a redução de ruído usando noisereduce
          reduced_noise = nr.reduce_noise(y=data, sr=rate)
          # Cria um arquivo temporário para salvar o áudio processado
          tmp_file = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
          tmp_filename = tmp_file.name
          tmp_file.close()
          wav.write(tmp_filename, rate, reduced_noise)
          return tmp_filename

    def generate_text_from_audio_file(self, audio_filename: str) -> str:
        with suppress_stderr():
          # Pré-processa o áudio para redução de ruído
          tmp_filename = self.preprocess_audio(audio_filename)
          try:
              # Utiliza o arquivo processado para o reconhecimento
              with sr.AudioFile(tmp_filename) as source:
                  # Ajusta com base no ruído ambiente (duração em segundos)
                  self.__recognizer.adjust_for_ambient_noise(source, duration=1)
                  audio = self.__recognizer.record(source)
              # Realiza o reconhecimento de fala usando o Google
              result = self.__recognizer.recognize_google(audio, language='pt-BR')
              return result
          except sr.UnknownValueError:
              raise UnknownAudioException()
          except sr.RequestError:
              raise ConnetionFailedException()
          finally:
              # Remove o arquivo temporário
              os.remove(tmp_filename)

    def run_audio_from_file(self, audio_filename: str):
        playsound(audio_filename)

    def save_audio_from_voice(self, audio_filename: str):
        with suppress_stderr():
          try:
              with sr.Microphone() as source:
                  Color.YELLOW.print('[APP] Ajustando ruídos do ambiente...')
                  self.__recognizer.adjust_for_ambient_noise(source, duration=1)
                  Color.YELLOW.print('[APP] Ruídos ajustados!')
                  # Define timeout e limite para captação da fala
                  audio = self.__recognizer.listen(source, timeout=5, phrase_time_limit=10)
              with open(audio_filename, "wb") as f:
                  f.write(audio.get_wav_data())
          except sr.UnknownValueError:
              raise UnknownAudioException()
          except sr.RequestError:
              raise ConnetionFailedException()

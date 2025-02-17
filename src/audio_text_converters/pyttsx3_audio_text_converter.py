from src.audio_text_converters.audio_text_converter import AudioTextConverter
from src.enums.language import Language
from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
from src.exceptions.audio_exceptions import UnknownAudioException, ConnetionFailedException
import sounddevice
from src.enums.color import Color

class Pyttsx3AudioTextConverter(AudioTextConverter):
  def __init__(self):
    self.__recognizer = sr.Recognizer()

  def save_audio_from_text(self, text: str, audio_filename: str, language: Language) -> None:
    tts = gTTS(text, lang = language.value)
    tts.save(audio_filename)

  def generate_text_from_audio_file(self, audio_filename: str) -> str:    
    try:
      with sr.AudioFile(audio_filename) as source:
        self.__recognizer.adjust_for_ambient_noise(source)
        audio = self.__recognizer.record(source)

      return self.__recognizer.recognize_google(audio, language = 'pt-BR')
    except sr.UnknownValueError:
      raise UnknownAudioException()
    except sr.RequestError:
      raise ConnetionFailedException()
  
  def run_audio_from_file(self, audio_filename: str):
    playsound(audio_filename)

  def save_audio_from_voice(self, audio_filename: str):
    try:
      with sr.Microphone() as source:
        Color.YELLOW.print('[APP] Ajustando ruídos do ambiente...')
        self.__recognizer.adjust_for_ambient_noise(source)
        Color.YELLOW.print('[APP] Ruídos ajustados!')
        audio = self.__recognizer.listen(source)

      with open(audio_filename, "wb") as f:
        f.write(audio.get_wav_data())
    except sr.UnknownValueError:
      raise UnknownAudioException()
    except sr.RequestError:
      raise ConnetionFailedException()

from src.audio_text_converters.audio_text_converter import AudioTextConverter
from src.enums.language import Language
from gtts import gTTS
from playsound import playsound
import speech_recognition as sr

class Pyttsx3AudioTextConverter(AudioTextConverter):
  def __init__(self):
    self.__recognizer = sr.Recognizer()

  def save_audio_from_text(self, text: str, audio_filename: str, language: Language) -> None:
    tts = gTTS(text, lang = language.value)
    tts.save(audio_filename)

  def generate_text_from_audio_file(self, audio_filename: str) -> str:
    return 'test'
  
  def run_audio_from_file(self, audio_filename: str):
    playsound(audio_filename)

  def save_audio_from_voice(self, audio_filename: str):
    with sr.Microphone() as source:
      print("Ajustando o ruído ambiente...")
      self.__recognizer.adjust_for_ambient_noise(source)
      print("Fale agora...")
      audio = self.__recognizer.listen(source)

    with open(audio_filename, "wb") as f:
      f.write(audio.get_wav_data())
      print("Áudio salvo como 'audio.wav'")

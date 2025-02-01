from src.audio_text_converters.pyttsx3_audio_text_converter import Pyttsx3AudioTextConverter
from playsound import playsound

filename = 'teste.mp3'
text = 'o rato roeu a roupa do rei de roma'
converter = Pyttsx3AudioTextConverter()
converter.save_audio_from_text(text, filename)
converter.run_audio_from_file(filename)

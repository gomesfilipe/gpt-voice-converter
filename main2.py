from src.audio_text_converters.pyttsx3_audio_text_converter import Pyttsx3AudioTextConverter

c = Pyttsx3AudioTextConverter()

c.save_audio_from_voice('hello.wav')

# import speech_recognition as sr

# # Cria um objeto de reconhecimento
# recognizer = sr.Recognizer()

# # Captura o áudio do microfone
# with sr.Microphone() as source:
#     print("Ajustando o ruído ambiente...")
#     recognizer.adjust_for_ambient_noise(source)
#     print("Fale agora...")
#     audio = recognizer.listen(source)

# try:
#     # Usa o Google Web Speech API para reconhecer o texto
#     print("Você disse: " + recognizer.recognize_google(audio, language='pt-BR'))
# except sr.UnknownValueError:
#     print("Não consegui entender o áudio")
# except sr.RequestError:
#     print("Erro ao se conectar ao serviço de reconhecimento")

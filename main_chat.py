from src.chats.chat import Chat
from src.audio_text_converters.pyttsx3_audio_text_converter import Pyttsx3AudioTextConverter
from src.gpts.chat_gpt import ChatGPT

chat = Chat(
  Pyttsx3AudioTextConverter(),
  ChatGPT(),
)

chat.run_chat()

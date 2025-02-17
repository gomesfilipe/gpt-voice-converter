from src.chats.chat import Chat
from config import AUDIO_TEXT_CONVERTER, GPT_API

Chat(AUDIO_TEXT_CONVERTER, GPT_API).run_chat()

from dotenv import load_dotenv
import os
from src.audio_text_converters.audio_text_converter import AudioTextConverter
from src.audio_text_converters.pyttsx3_audio_text_converter import Pyttsx3AudioTextConverter
from src.gpt_apis.gpt_api import GptApi
from src.gpt_apis.gemini_api import GeminiApi

load_dotenv()

MAX_CALLS_GPT_API: int = 3
AUDIOS_DIR: str = 'audios'
USER_SUFFIX_AUDIO_FILENAME = 'user'
GPT_SUFFIX_AUDIO_FILENAME = 'gpt'
GPT_API_KEY = os.getenv('GPT_API_KEY')

# TODO Descomentar quando integrar com a API do ChatGPT 
if GPT_API_KEY is None:
    raise Exception('GPT_API_KEY is missing in .env file.')

AUDIO_TEXT_CONVERTER: AudioTextConverter = Pyttsx3AudioTextConverter()
GPT_API: GptApi = GeminiApi(GPT_API_KEY)

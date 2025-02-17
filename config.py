from dotenv import load_dotenv
import os

load_dotenv()

MAX_CALLS_GPT_API: int = 3
AUDIOS_DIR: str = 'audios'
USER_SUFFIX_AUDIO_FILENAME = 'user'
GPT_SUFFIX_AUDIO_FILENAME = 'gpt'
GPT_API_KEY = os.getenv('GPT_API_KEY')

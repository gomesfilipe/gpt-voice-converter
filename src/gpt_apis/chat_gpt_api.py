from src.gpt_apis.gpt_api import GptApi

class ChatGptApi(GptApi):
  def send(self, text: str):
    return 'MENSAGEM CHAT GPT'

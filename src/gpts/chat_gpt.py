from src.gpts.gpt import GPT
from config import GPT_API_KEY

class ChatGPT(GPT):
  def __init__(self):
    self.__api_key = GPT_API_KEY

    # TODO Descomentar quando integrar com a API do ChatGPT 
    # if self.__api_key is None:
    #   raise Exception('Add GPT_API_KEY in your .env file.')

  def send(self, text):
    return 'MENSAGEM CHAT GPT'

from src.gpt_apis.gpt_api import GptApi
from google import genai

import os

class GeminiApi(GptApi):
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.client = genai.Client(api_key=api_key)

    def send(self, text: str) -> str:
        try:
            if not hasattr(self, "prompt"):
                self.prompt = "Responda apenas ao ultimo texto após a última tag [HUMAN] como uma conversa entre humanos, considere o restante como o contexto da conversa, não utilize emojis, ignore tudo que está entre colchetes. Seu nome é Cassandra, aja como uma mulher divorciada em busca de um homem solteiro. Não responda citando seu nome, responda como se estivesse em uma conversa casual. "
            self.prompt += "[HUMAN]:\n" + text + "\n"

            response = self.client.models.generate_content(
                model="gemini-2.0-flash",
                contents=self.prompt
            )

            resposta_api = response.text

            resposta_api = resposta_api.replace("[HUMAN]", "")
            resposta_api = resposta_api.replace("[ROBOT]", "")
            resposta_api = resposta_api.replace("Cassandra:", "")

            self.prompt += "[ROBOT] " + response.text + "\n"

            return response.text
        except Exception as e:
            return f"Erro na chamada da API: {str(e)}"

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
                self.prompt = "Responda como uma conversa entre humanos, não utilize emojis: "
            self.prompt += text

            response = self.client.models.generate_content(
                model="gemini-2.0-flash",
                contents=self.prompt
            )

            return response.text
        except Exception as e:
            return f"Erro na chamada da API: {str(e)}"

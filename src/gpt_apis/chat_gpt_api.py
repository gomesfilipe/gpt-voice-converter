from src.gpt_apis.gpt_api import GptApi
from dotenv import load_dotenv
from google import genai

import os

# Diretório raiz do projeto
root_path = os.getcwd()
env_path = os.path.join(root_path, ".env")

load_dotenv(dotenv_path=env_path)

api_key = os.getenv("GEMINI_API_KEY")

if api_key is None:
    raise ValueError("GEMINI_API_KEY não configurada")

client = genai.Client(api_key=api_key)

class GeminiApi(GptApi):
  def send(self, text: str) -> str:
        try:
            if not hasattr(self, "prompt"):
                self.prompt = "Responda como uma conversa entre humanos, não utilize emojis: "
            self.prompt += text

            response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=self.prompt
            )

            return response.text
        except Exception as e:
            return f"Erro na chamada da API: {str(e)}"

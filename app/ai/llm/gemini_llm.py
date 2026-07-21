from google import genai

from app.ai.llm.base_llm import BaseLLM
from app.ai.llm.config import GEMINI_API_KEY


class GeminiLLM(BaseLLM):

    def __init__(self):
        self.client = genai.Client(api_key=GEMINI_API_KEY)

    def generate_response(self, prompt: str) -> str:

        response = self.client.models.generate_content(
            model="models/gemini-3.6-flash",
            contents=prompt,
        )

        return response.text
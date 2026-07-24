from groq import Groq

from app.core.config import settings


class LLMService:
    """
    Handles communication with the Groq API.
    """

    def __init__(self):

        if not settings.GROQ_API_KEY:
            raise ValueError(
                "GROQ_API_KEY not found in environment variables."
            )

        self.client = Groq(
            api_key=settings.GROQ_API_KEY
        )

    def generate_response(self, prompt: str) -> str:

        try:

            response = self.client.chat.completions.create(
                model=settings.LLM_MODEL,
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.3,
                max_tokens=2048
            )

            return response.choices[0].message.content

        except Exception as e:

            raise RuntimeError(
                f"Groq API Error: {str(e)}"
            ) from e
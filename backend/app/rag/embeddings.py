import os

from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings

from app.core.config import settings



load_dotenv()


class EmbeddingModel:
    """
    Initializes the Gemini embedding model.
    """

    def __init__(self):

        api_key = os.getenv("GEMINI_API_KEY")

        if not settings.GEMINI_API_KEY:
            raise ValueError(
                "GEMINI_API_KEY not found in environment variables."
            )

        self.embeddings = GoogleGenerativeAIEmbeddings(
        model=settings.EMBEDDING_MODEL,
        google_api_key=settings.GEMINI_API_KEY
        )

    def get_embeddings(self):
        """
        Returns the initialized embedding model.
        """
        return self.embeddings
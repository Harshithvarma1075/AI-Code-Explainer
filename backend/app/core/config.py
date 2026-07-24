import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    """
    Centralized configuration for the application.
    """

    # Gemini
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

    EMBEDDING_MODEL = os.getenv(
    "EMBEDDING_MODEL",
    "models/gemini-embedding-001"
    )

    GROQ_API_KEY = os.getenv("GROQ_API_KEY")

    LLM_MODEL = os.getenv(
        "LLM_MODEL",
        "llama-3.3-70b-versatile"
    )


    # RAG
    CHUNK_SIZE = 800
    CHUNK_OVERLAP = 150

    # ChromaDB
    COLLECTION_NAME = "python_knowledge_base"
    CHROMA_DB_PATH = "app/database/chroma_db"

    # Retrieval
    TOP_K = 5


settings = Settings()
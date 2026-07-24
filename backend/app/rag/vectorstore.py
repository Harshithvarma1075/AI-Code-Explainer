from langchain_chroma import Chroma

from app.core.config import settings
from app.rag.embeddings import EmbeddingModel


class VectorStore:
    """
    Manages the ChromaDB vector database.
    """

    def __init__(self):

        embedding_function = EmbeddingModel().get_embeddings()

        self.vector_store = Chroma(
            collection_name=settings.COLLECTION_NAME,
            embedding_function=embedding_function,
            persist_directory=settings.CHROMA_DB_PATH,
        )

    def get_vector_store(self):
        """
        Returns the initialized ChromaDB vector store.
        """
        return self.vector_store
    
    def reset_collection(self):
        """
        Deletes all documents from the collection while keeping
        the collection itself.
        """

        ids = self.vector_store.get()["ids"]

        if ids:
            self.vector_store.delete(ids=ids)
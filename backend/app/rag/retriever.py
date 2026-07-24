from app.core.config import settings
from app.rag.vectorstore import VectorStore


class Retriever:
    """
    Retrieves relevant and diverse documents from the vector database.
    """

    def __init__(self):
        self.vector_store = VectorStore().get_vector_store()

        self.retriever = self.vector_store.as_retriever(
            search_type="mmr",
            search_kwargs={
                "k": settings.TOP_K,
                "fetch_k": 10,
                "lambda_mult": 0.5,
            },
        )

    def retrieve(self, query: str):
        """
        Returns unique documents based on their source file.
        """

        docs = self.retriever.invoke(query)

        unique_docs = []
        seen_sources = set()

        for doc in docs:
            source = doc.metadata.get("source", "unknown")

            if source not in seen_sources:
                seen_sources.add(source)
                unique_docs.append(doc)

        return unique_docs
import math
import time

from langchain_google_genai._common import GoogleGenerativeAIError

from app.rag.loader import DocumentLoader
from app.rag.splitter import DocumentSplitter
from app.rag.vectorstore import VectorStore


# Configuration
BATCH_SIZE = 10
MAX_RETRIES = 3
RETRY_DELAY = 60  # seconds


class DocumentIngestor:
    """
    Handles the complete RAG ingestion pipeline.
    """

    def __init__(self):

        self.loader = DocumentLoader()
        self.splitter = DocumentSplitter()
        self.vector_store = VectorStore()

    def ingest(self):

        print("\nLoading documents...")

        documents = self.loader.load_documents()

        print(f"Loaded {len(documents)} documents.")

        print("\nSplitting documents...")

        chunks = self.splitter.split_documents(documents)

        print(f"Generated {len(chunks)} chunks.")

        print("\nResetting ChromaDB collection...")

        self.vector_store.reset_collection()

        print("Collection cleared.")

        vectorstore = self.vector_store.get_vector_store()

        total_batches = math.ceil(len(chunks) / BATCH_SIZE)

        print(f"\nAdding {len(chunks)} chunks in {total_batches} batches...\n")

        for batch_num in range(total_batches):

            start = batch_num * BATCH_SIZE
            end = start + BATCH_SIZE
            batch = chunks[start:end]

            retry_count = 0

            while retry_count < MAX_RETRIES:

                try:

                    print(
                        f"Batch {batch_num + 1}/{total_batches} "
                        f"({len(batch)} chunks)..."
                    )

                    vectorstore.add_documents(batch)

                    print("Batch completed successfully.\n")

                    break

                except GoogleGenerativeAIError as e:

                    retry_count += 1

                    if "RESOURCE_EXHAUSTED" in str(e):

                        print(
                            f"Rate limit reached."
                            f"\nWaiting {RETRY_DELAY} seconds before retry "
                            f"({retry_count}/{MAX_RETRIES})...\n"
                        )

                        time.sleep(RETRY_DELAY)

                    else:
                        raise

            else:
                raise RuntimeError(
                    f"Failed to ingest batch {batch_num + 1} "
                    f"after {MAX_RETRIES} retries."
                )

        print(
            f"\nSuccessfully indexed {len(chunks)} chunks."
        )

        print("\nKnowledge base ingestion completed successfully!")


if __name__ == "__main__":

    ingestor = DocumentIngestor()

    ingestor.ingest()
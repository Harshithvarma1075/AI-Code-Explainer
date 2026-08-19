import hashlib
from pathlib import Path

from langchain_text_splitters import RecursiveCharacterTextSplitter


from app.core.config import settings


class DocumentSplitter:
    def __init__(
        self,
        chunk_size: int = settings.CHUNK_SIZE,
        chunk_overlap: int = settings.CHUNK_OVERLAP
    ):

        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            separators=[
                "\n## ",
                "\n# ",
                "\n\n",
                "\n",
                " ",
                ""
            ]
        )

    def split_documents(self, documents):

        chunks = self.text_splitter.split_documents(documents)

        source_positions = {}

        for index, chunk in enumerate(chunks):

            source = chunk.metadata.get("source", "")

            source = source.replace("\\", "/")

            source_path = Path(source)
            filename = source_path.name
            category = source_path.parent.name
            source_key = f"{category}/{filename}"
            chunk_index = source_positions.get(source_key, 0)
            source_positions[source_key] = chunk_index + 1

            # A content-derived identifier stays meaningful across a full
            # re-ingestion, unlike the old collection-wide numeric index.
            chunk_id = hashlib.sha256(
                f"{source_key}:{chunk.page_content.strip()}".encode("utf-8")
            ).hexdigest()[:12]

            chunk.metadata.update(
                {
                    "chunk_id": chunk_id,
                    "chunk_index": chunk_index,
                    "filename": filename,
                    "category": category,
                    "source_key": source_key,
                    "citation_id": f"src-{chunk_id}",
                }
            )

        return chunks

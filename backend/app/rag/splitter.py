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

        for index, chunk in enumerate(chunks):

            source = chunk.metadata.get("source", "")

            source = source.replace("\\", "/")

            filename = source.split("/")[-1]

            category = source.split("/")[-2]

            chunk.metadata.update(
                {
                    "chunk_id": index,
                    "filename": filename,
                    "category": category
                }
            )

        return chunks
from pathlib import Path

from langchain_community.document_loaders import DirectoryLoader
from langchain_community.document_loaders import TextLoader


class DocumentLoader:
    """
    Loads all markdown documents from the knowledge base.
    """

    def __init__(self):

        self.documents_path = (
            Path(__file__)
            .resolve()
            .parent.parent.parent
            / "documents"
        )

    def load_documents(self):

        from langchain_community.document_loaders import DirectoryLoader, TextLoader

        loader = DirectoryLoader(
            self.documents_path,
            glob="**/*.md",
            loader_cls=TextLoader,
            loader_kwargs={"encoding": "utf-8"}
        )

        documents = loader.load()

        return documents
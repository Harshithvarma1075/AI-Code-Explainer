from typing import List, Optional

from pydantic import BaseModel, Field


class SourceReference(BaseModel):
    citation_id: str
    filename: str
    category: str
    chunk_id: str
    excerpt: str


class ChatResponse(BaseModel):

    answer: str

    sources: List[str]
    # Kept additive so current clients that consume ``sources`` keep working.
    source_details: List[SourceReference] = Field(default_factory=list)


class ConversationResponse(ChatResponse):
    session_id: str

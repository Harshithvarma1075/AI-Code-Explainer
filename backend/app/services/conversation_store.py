"""Small bounded in-memory store for optional follow-up conversations."""

from collections import deque
from threading import Lock
from uuid import uuid4


class ConversationStore:
    def __init__(self, max_turns: int = 8):
        self.max_turns = max_turns
        self._conversations = {}
        self._lock = Lock()

    def ensure_session(self, session_id: str | None) -> str:
        session_id = session_id or str(uuid4())
        with self._lock:
            self._conversations.setdefault(session_id, deque(maxlen=self.max_turns))
        return session_id

    def history(self, session_id: str) -> str:
        with self._lock:
            turns = list(self._conversations.get(session_id, ()))
        return "\n\n".join(f"{role.title()}: {content}" for role, content in turns)

    def append(self, session_id: str, role: str, content: str) -> None:
        with self._lock:
            self._conversations.setdefault(session_id, deque(maxlen=self.max_turns)).append(
                (role, content)
            )


conversation_store = ConversationStore()

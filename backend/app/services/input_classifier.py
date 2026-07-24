import re
from enum import Enum


class InputType(Enum):
    QUESTION = "question"
    CODE = "code"


class InputClassifier:

    PYTHON_KEYWORDS = (
        "def ",
        "class ",
        "import ",
        "from ",
        "return ",
        "for ",
        "while ",
        "if ",
        "elif ",
        "else:",
        "try:",
        "except",
        "finally:",
        "with ",
    )

    TRACEBACK_PATTERNS = (
        "Traceback (most recent call last):",
        "SyntaxError",
        "IndentationError",
        "NameError",
        "TypeError",
        "ValueError",
        "ZeroDivisionError",
        "IndexError",
        "KeyError",
        "AttributeError",
        "ImportError",
        "ModuleNotFoundError",
        "RuntimeError",
    )

    @classmethod
    def classify(cls, text: str) -> InputType:

        text = text.strip()

        # Markdown code blocks
        if "```" in text:
            return InputType.CODE

        # Tracebacks / Exceptions
        if any(pattern in text for pattern in cls.TRACEBACK_PATTERNS):
            return InputType.CODE

        # Common Python keywords
        if any(keyword in text for keyword in cls.PYTHON_KEYWORDS):
            return InputType.CODE

        # Indented code
        if re.search(r"^\s{2,}\S+", text, re.MULTILINE):
            return InputType.CODE

        return InputType.QUESTION
from app.services.input_classifier import InputType


class PromptManager:
    """
    Builds prompts for the LLM based on the detected input type.
    """

    @staticmethod
    def build_prompt(
        input_type: InputType,
        user_input: str,
        context: str,
    ) -> str:

        if input_type == InputType.CODE:
            return PromptManager._build_code_prompt(
                user_input,
                context,
            )

        return PromptManager._build_knowledge_prompt(
            user_input,
            context,
        )

    @staticmethod
    def _build_knowledge_prompt(
        question: str,
        context: str,
    ) -> str:

        return f"""
You are an expert Python Software Engineer and Programming Mentor.

Answer the user's question using the retrieved context as the primary source.

Instructions:

1. Use the retrieved context whenever possible.
2. If the context is incomplete, supplement it with correct Python knowledge.
3. Never invent information about the retrieved documents.
4. Explain concepts clearly.
5. Use Markdown formatting.
6. Include examples when appropriate.

==========================
Retrieved Context
==========================

{context}

==========================
User Question
==========================

{question}
"""

    @staticmethod
    def _build_code_prompt(
        code: str,
        context: str,
    ) -> str:

        return f"""
You are a Senior Python Software Engineer, Code Reviewer, and Debugging Expert.

Analyze the user's Python code.

Use the retrieved context whenever it is relevant, but focus primarily on the submitted code.

Provide your response using the following structure:

# Code Summary

Briefly explain what the code is trying to accomplish.

# Line-by-Line Explanation

Explain the important parts of the code.

# Bugs / Issues

Identify:

- Syntax errors
- Runtime errors
- Logical errors
- Edge cases

If no issues exist, clearly state that.

# Suggested Fixes

Provide corrected code if necessary.

# Time Complexity

Analyze the algorithm.

# Space Complexity

Analyze memory usage.

# Best Practices

Suggest improvements following Python best practices and PEP 8.

# Optimized Version

Only provide an optimized version if meaningful improvements exist.

==========================
Retrieved Context
==========================

{context}

==========================
User Code
==========================

{code}
"""
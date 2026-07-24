from fastapi import APIRouter, HTTPException

from app.models.request_models import ChatRequest
from app.models.response_models import ChatResponse

from app.rag.retriever import Retriever
from app.rag.context_builder import ContextBuilder
from app.core.prompt_manager import PromptManager
from app.services.llm_service import LLMService
from app.services.input_classifier import InputClassifier

from app.core.logger import logger


router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    question = request.question

    logger.info(
        f"Received input: {question}"
    )

    try:

        # Classify the user input
        input_type = InputClassifier.classify(question)

        logger.info(
            f"Detected input type: {input_type.value}"
        )

        # Retrieve relevant documents
        documents = Retriever().retrieve(question)

        sources = []

        for doc in documents:

            source = doc.metadata.get(
                "source",
                "Unknown"
            )

            filename = source.replace("\\", "/").split("/")[-1]

            if filename not in sources:
                sources.append(filename)

        logger.info(
            f"Retrieved {len(documents)} documents."
        )

        # Build context
        context = ContextBuilder().build_context(documents)

        logger.info(
            "Building prompt."
        )

        # Build prompt based on detected input type
        prompt = PromptManager.build_prompt(
            input_type=input_type,
            user_input=question,
            context=context
        )

        logger.info(
            "Sending prompt to LLM."
        )

        answer = LLMService().generate_response(prompt)

        logger.info(
            "Response generated successfully."
        )

        return ChatResponse(
            answer=answer,
            sources=sources
        )

    except RuntimeError as e:

        logger.exception(
            "LLM service error."
        )

        raise HTTPException(
            status_code=503,
            detail="The AI service is temporarily unavailable. Please try again shortly."
        ) from e

    except Exception as e:

        logger.exception(
            "Unexpected server error."
        )

        raise HTTPException(
            status_code=500,
            detail="Internal server error."
        ) from e
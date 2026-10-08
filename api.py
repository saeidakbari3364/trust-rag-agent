from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from src.trust_rag_agent.agent import TrustRAGAgent


load_dotenv()


app = FastAPI(
    title="TrustRAG-Agent API",
    description=(
        "A trustworthy and adaptive agent "
        "for evidence-based question answering."
    ),
    version="0.1.0",
)


class QuestionRequest(BaseModel):
    question: str


class QuestionResponse(BaseModel):
    question: str
    answer: str | None


@app.get("/")
def root():
    return {
        "name": "TrustRAG-Agent API",
        "version": "0.1.0",
        "status": "running",
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.post("/ask", response_model=QuestionResponse)
def ask(request: QuestionRequest):

    if not request.question.strip():
        raise HTTPException(
            status_code=400,
            detail="Question cannot be empty.",
        )

    try:

        agent = TrustRAGAgent()

        answer = agent.run(
            request.question
        )

        return QuestionResponse(
            question=request.question,
            answer=answer,
        )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )
from typing import List, Optional

from fastapi import FastAPI
from pydantic import BaseModel, Field


app = FastAPI(title="Lumiere GPT-like Backend", version="0.1.0")


class ChatMessage(BaseModel):
    role: str = Field(pattern="^(system|user|assistant)$")
    content: str


class ChatCompletionRequest(BaseModel):
    model: str = "lumiere-gpt"
    messages: List[ChatMessage]
    temperature: Optional[float] = 0.7


class ChatCompletionChoice(BaseModel):
    index: int
    message: ChatMessage
    finish_reason: str = "stop"


class ChatCompletionResponse(BaseModel):
    id: str
    object: str = "chat.completion"
    model: str
    choices: List[ChatCompletionChoice]


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.post("/v1/chat/completions", response_model=ChatCompletionResponse)
def chat_completions(payload: ChatCompletionRequest) -> ChatCompletionResponse:
    user_messages = [m.content for m in payload.messages if m.role == "user" and m.content.strip()]
    prompt = user_messages[-1] if user_messages else "Hello"
    content = (
        "I am a GPT-like assistant running on Lumiere. "
        f"You said: {prompt}"
    )
    return ChatCompletionResponse(
        id="chatcmpl-lumiere-1",
        model=payload.model,
        choices=[
            ChatCompletionChoice(
                index=0,
                message=ChatMessage(role="assistant", content=content),
            )
        ],
    )

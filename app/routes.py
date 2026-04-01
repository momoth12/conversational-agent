from datetime import datetime, timezone
from fastapi import APIRouter
from app.models import ChatRequest, ChatResponse
from app.services import mistral_client, MODEL, conversations

router = APIRouter()

SYSTEM_PROMPT = {
    "role": "system",
    "content": "You are a chatbot that gives really short answers in maximum 2 sentences.",
}


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    # 1. Load past messages from MongoDB for this session
    history = conversations.find(
        {"session_id": request.session_id},
        {"_id": 0, "role": 1, "content": 1},
    ).sort("timestamp", 1)

    messages = [SYSTEM_PROMPT] + list(history) + [{"role": "user", "content": request.message}]

    # 2. Call Mistral
    response = mistral_client.chat.complete(messages=messages, model=MODEL)
    answer = response.choices[0].message.content

    # 3. Save user message + assistant reply to MongoDB
    now = datetime.now(timezone.utc)
    conversations.insert_many([
        {"session_id": request.session_id, "role": "user", "content": request.message, "timestamp": now},
        {"session_id": request.session_id, "role": "assistant", "content": answer, "timestamp": now},
    ])

    return ChatResponse(response=answer)

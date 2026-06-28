from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from services.chat import get_answer

app = FastAPI(title="FAQ Chatbot")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    question: str
    history: List[Message] = []

@app.get("/")
async def root():
    return {
        "message": "FAQ Chatbot API is running 🚀"
    }

@app.post("/api/chat")
async def chat(req: ChatRequest):
    history = [{"role": m.role, "content": m.content} for m in req.history]
    answer = await get_answer(req.question, history)
    return {"answer": answer}

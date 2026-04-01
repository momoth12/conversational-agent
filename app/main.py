from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="Chatbot API")

app.include_router(router)

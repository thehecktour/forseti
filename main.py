from fastapi import FastAPI
from src.router import router

app = FastAPI(title="Forseti - Add XP to UX")

app.include_router(router, prefix="/api")

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.db import engine, Base
from app.routers import forms, questions

# Opcional: gera tabelas automaticamente (útil em dev, mas use migrations em prod)
# Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API de Formulários Dinâmicos",
    version="0.1.0",
    description="CRUD de formulários e perguntas usando FastAPI + SQLAlchemy"
)

# CORS (ajuste origens conforme necessidade)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(forms.router)
app.include_router(questions.router)

@app.get("/health", tags=["health"])
def health_check():
    return {"status": "ok"}

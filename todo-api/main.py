from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import engine, Base
from routers import tarefas

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Todo API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://todo-aplicacao-mauve.vercel.app", "http://localhost:4200"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(tarefas.router)


@app.get("/health", tags=["infra"])
def health():
    return {"status": "ok"}

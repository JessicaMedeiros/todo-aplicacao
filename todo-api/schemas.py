from pydantic import BaseModel

# o que a API espera receber quando criamos uma tarefa
class TarefaCreate(BaseModel):
    titulo: str
    prioridade: int
    observacao: str | None = None

# o que a API devolve como resposta
class TarefaResponse(BaseModel):
    id: int
    titulo: str
    concluida: bool
    prioridade: int
    observacao: str | None = None

    class Config:
        from_attributes = True  # permite converter direto do objeto do banco
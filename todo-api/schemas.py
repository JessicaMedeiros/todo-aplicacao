from pydantic import BaseModel, ConfigDict


class TarefaCreate(BaseModel):
    titulo: str
    prioridade: int = 0
    observacao: str | None = None


class TarefaResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    titulo: str
    concluida: bool
    prioridade: int
    observacao: str | None = None

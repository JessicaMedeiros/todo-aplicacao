from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
import schemas
import services.tarefas as service

router = APIRouter(prefix="/tarefas", tags=["tarefas"])


@router.post("", response_model=schemas.TarefaResponse, status_code=201)
def criar(dados: schemas.TarefaCreate, db: Session = Depends(get_db)):
    return service.criar_tarefa(db, dados)


@router.get("", response_model=list[schemas.TarefaResponse])
def listar(db: Session = Depends(get_db)):
    return service.listar_tarefas(db)


@router.get("/{tarefa_id}", response_model=schemas.TarefaResponse)
def buscar(tarefa_id: int, db: Session = Depends(get_db)):
    return service.buscar_tarefa(db, tarefa_id)


@router.put("/{tarefa_id}", response_model=schemas.TarefaResponse)
def atualizar(tarefa_id: int, dados: schemas.TarefaCreate, db: Session = Depends(get_db)):
    return service.atualizar_tarefa(db, tarefa_id, dados)


@router.patch("/{tarefa_id}/concluir", response_model=schemas.TarefaResponse)
def concluir(tarefa_id: int, db: Session = Depends(get_db)):
    return service.concluir_tarefa(db, tarefa_id)


@router.delete("/{tarefa_id}", status_code=204)
def deletar(tarefa_id: int, db: Session = Depends(get_db)):
    service.deletar_tarefa(db, tarefa_id)

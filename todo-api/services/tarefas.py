from sqlalchemy.orm import Session
from fastapi import HTTPException

import models
import schemas


def criar_tarefa(db: Session, dados: schemas.TarefaCreate) -> models.Tarefa:
    nova = models.Tarefa(
        titulo=dados.titulo,
        prioridade=dados.prioridade,
        observacao=dados.observacao,
    )
    db.add(nova)
    db.commit()
    db.refresh(nova)
    return nova


def listar_tarefas(db: Session) -> list[models.Tarefa]:
    return db.query(models.Tarefa).all()


def buscar_tarefa(db: Session, tarefa_id: int) -> models.Tarefa:
    tarefa = db.query(models.Tarefa).filter(models.Tarefa.id == tarefa_id).first()
    if not tarefa:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return tarefa


def atualizar_tarefa(db: Session, tarefa_id: int, dados: schemas.TarefaCreate) -> models.Tarefa:
    tarefa = buscar_tarefa(db, tarefa_id)
    tarefa.titulo = dados.titulo
    tarefa.prioridade = dados.prioridade
    tarefa.observacao = dados.observacao
    db.commit()
    db.refresh(tarefa)
    return tarefa


def concluir_tarefa(db: Session, tarefa_id: int) -> models.Tarefa:
    tarefa = buscar_tarefa(db, tarefa_id)
    tarefa.concluida = True
    db.commit()
    db.refresh(tarefa)
    return tarefa


def deletar_tarefa(db: Session, tarefa_id: int) -> None:
    tarefa = buscar_tarefa(db, tarefa_id)
    db.delete(tarefa)
    db.commit()

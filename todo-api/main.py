from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import engine, get_db, Base
import models, schemas

# cria as tabelas no banco (se ainda não existirem)
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# criar uma tarefa
@app.post("/tarefas", response_model=schemas.TarefaResponse)
def criar(tarefa: schemas.TarefaCreate, db: Session = Depends(get_db)):
    nova = models.Tarefa(titulo=tarefa.titulo, prioridade = tarefa.prioridade, observacao = tarefa.observacao)
    db.add(nova)
    db.commit()
    db.refresh(nova)
    return nova

# listar todas as tarefas
@app.get("/tarefas", response_model=list[schemas.TarefaResponse])
def listar(db: Session = Depends(get_db)):
    return db.query(models.Tarefa).all()

# marcar uma tarefa como concluída
@app.patch("/tarefas/{id}/concluir", response_model=schemas.TarefaResponse)
def concluir(id: int, db: Session = Depends(get_db)):
    tarefa = db.query(models.Tarefa).filter(models.Tarefa.id == id).first()
    if not tarefa:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    tarefa.concluida = True
    db.commit()
    return tarefa

# deletar uma tarefa
@app.delete("/tarefas/{id}")
def deletar(id: int, db: Session = Depends(get_db)):
    tarefa = db.query(models.Tarefa).filter(models.Tarefa.id == id).first()
    if not tarefa:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    db.delete(tarefa)
    db.commit()
    return {"ok": True}

@app.get("/tarefas/{id}", response_model=schemas.TarefaResponse)
def buscar(id: int, db: Session = Depends(get_db)):
    tarefa = db.query(models.Tarefa).filter(models.Tarefa.id == id).first()
    if not tarefa:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return tarefa

@app.put("/tarefas/{id}", response_model=schemas.TarefaResponse)
def atualizar(id: int, dados: schemas.TarefaCreate, db: Session = Depends(get_db)):
    tarefa = db.query(models.Tarefa).filter(models.Tarefa.id == id).first()
    if not tarefa:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    tarefa.titulo = dados.titulo
    tarefa.prioridade = dados.prioridade
    tarefa.observacao = dados.observacao
    db.commit()
    db.refresh(tarefa)
    return tarefa
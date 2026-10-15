from sqlalchemy import Column, Integer, String, Boolean
from database import Base

class Tarefa(Base):
    __tablename__ = "tarefas"  # nome da tabela no banco

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, nullable=False)
    concluida = Column(Boolean, default=False)
    prioridade = Column(Integer, default=0)
    observacao = Column(String, nullable=True)
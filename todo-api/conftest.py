import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from database import Base, get_db
from main import app

# banco de testes: SQLite em memória — existe só durante a execução dos testes
engine_teste = create_engine(
    "sqlite:///:memory:",
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,  # garante que todas as conexões usem o mesmo banco em memória
)
SessionTeste = sessionmaker(bind=engine_teste)

def get_db_teste():
    db = SessionTeste()
    try:
        yield db
    finally:
        db.close()

# troca a dependência real (get_db) pela versão de teste, só durante os testes
app.dependency_overrides[get_db] = get_db_teste

@pytest.fixture
def client():
    Base.metadata.create_all(bind=engine_teste)  # cria as tabelas do zero
    yield TestClient(app)                         # entrega o client pro teste usar
    Base.metadata.drop_all(bind=engine_teste)      # limpa tudo depois
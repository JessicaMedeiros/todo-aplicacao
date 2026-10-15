from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# cria um banco SQLite chamado "todo.db" — um arquivo único, sem precisar instalar servidor de banco
engine = create_engine("sqlite:///todo.db", connect_args={"check_same_thread": False})

# SessionLocal é a "porta de entrada" pra fazer operações no banco
SessionLocal = sessionmaker(bind=engine)

# Base é a classe que todos os nossos modelos (tabelas) vão herdar
Base = declarative_base()

# função que abre uma conexão, entrega pra quem precisar, e fecha no final
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
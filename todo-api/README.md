# Todo API

API REST para gerenciamento de tarefas, construída com **FastAPI**, **SQLAlchemy** e **Alembic**.

## Tecnologias

- **Python 3.13**
- **FastAPI** — framework web assíncrono
- **SQLAlchemy** — ORM
- **Alembic** — migrations de banco de dados
- **Pydantic Settings** — configuração via variáveis de ambiente
- **Pytest** — testes automatizados

## Estrutura do projeto

```
todo-api/
├── routers/
│   └── tarefas.py      # rotas HTTP
├── services/
│   └── tarefas.py      # regras de negócio
├── models.py           # modelos do banco (SQLAlchemy)
├── schemas.py          # contratos da API (Pydantic)
├── database.py         # conexão com o banco
├── config.py           # variáveis de ambiente
├── main.py             # inicialização do app
└── test/
    └── test_tarefas.py # testes de integração
```

## Como rodar localmente

**1. Clone o repositório e entre na pasta:**

```bash
cd todo-api
```

**2. Crie e ative um ambiente virtual:**

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

**3. Instale as dependências:**

```bash
pip install -r requirements.txt
```

**4. Configure as variáveis de ambiente:**

```bash
cp .env.example .env
# edite o .env se necessário
```

**5. Suba o servidor:**

```bash
uvicorn main:app --reload
```

A API estará disponível em `http://localhost:8000`.  
Documentação interativa: `http://localhost:8000/docs`

## Rodando os testes

```bash
pytest -v
```

## Endpoints

| Método   | Rota                        | Descrição              |
|----------|-----------------------------|------------------------|
| `POST`   | `/tarefas`                  | Criar tarefa           |
| `GET`    | `/tarefas`                  | Listar todas           |
| `GET`    | `/tarefas/{id}`             | Buscar por ID          |
| `PUT`    | `/tarefas/{id}`             | Atualizar tarefa       |
| `PATCH`  | `/tarefas/{id}/concluir`    | Marcar como concluída  |
| `DELETE` | `/tarefas/{id}`             | Deletar tarefa         |
| `GET`    | `/health`                   | Health check           |

## Deploy

O backend está hospedado no **Render** e o frontend no **Vercel**.  
A variável `DATABASE_URL` é configurada diretamente no painel do Render.

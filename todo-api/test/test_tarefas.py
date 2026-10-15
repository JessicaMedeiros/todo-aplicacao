def test_criar_tarefa(client):
    resposta = client.post("/tarefas", json={"titulo": "Estudar pytest"})

    assert resposta.status_code == 200
    dados = resposta.json()
    assert dados["titulo"] == "Estudar pytest"
    assert dados["concluida"] is False
    assert "id" in dados


def test_listar_tarefas_vazia(client):
    resposta = client.get("/tarefas")

    assert resposta.status_code == 200
    assert resposta.json() == []


def test_listar_tarefas_apos_criar(client):
    client.post("/tarefas", json={"titulo": "Tarefa 1"})
    client.post("/tarefas", json={"titulo": "Tarefa 2"})

    resposta = client.get("/tarefas")

    assert resposta.status_code == 200
    assert len(resposta.json()) == 2


def test_concluir_tarefa(client):
    criada = client.post("/tarefas", json={"titulo": "Tarefa a concluir"}).json()

    resposta = client.patch(f"/tarefas/{criada['id']}/concluir")

    assert resposta.status_code == 200
    assert resposta.json()["concluida"] is True


def test_concluir_tarefa_inexistente(client):
    resposta = client.patch("/tarefas/999/concluir")

    assert resposta.status_code == 404


def test_deletar_tarefa(client):
    criada = client.post("/tarefas", json={"titulo": "Tarefa a deletar"}).json()

    resposta = client.delete(f"/tarefas/{criada['id']}")
    assert resposta.status_code == 200

    resposta_lista = client.get("/tarefas")
    assert resposta_lista.json() == []


def test_deletar_tarefa_inexistente(client):
    resposta = client.delete("/tarefas/999")
    assert resposta.status_code == 404
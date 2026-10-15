def test_criar_tarefa(client):
    resposta = client.post("/tarefas", json={"titulo": "Estudar pytest"})

    assert resposta.status_code == 201
    dados = resposta.json()
    assert dados["titulo"] == "Estudar pytest"
    assert dados["concluida"] is False
    assert dados["prioridade"] == 0
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
    assert resposta.status_code == 204

    resposta_lista = client.get("/tarefas")
    assert resposta_lista.json() == []


def test_deletar_tarefa_inexistente(client):
    resposta = client.delete("/tarefas/999")
    assert resposta.status_code == 404


def test_atualizar_tarefa(client):
    criada = client.post("/tarefas", json={"titulo": "Original"}).json()

    resposta = client.put(
        f"/tarefas/{criada['id']}",
        json={"titulo": "Atualizada", "prioridade": 2},
    )

    assert resposta.status_code == 200
    dados = resposta.json()
    assert dados["titulo"] == "Atualizada"
    assert dados["prioridade"] == 2


def test_buscar_tarefa(client):
    criada = client.post("/tarefas", json={"titulo": "Buscar isso"}).json()

    resposta = client.get(f"/tarefas/{criada['id']}")

    assert resposta.status_code == 200
    assert resposta.json()["titulo"] == "Buscar isso"


def test_buscar_tarefa_inexistente(client):
    resposta = client.get("/tarefas/999")

    assert resposta.status_code == 404

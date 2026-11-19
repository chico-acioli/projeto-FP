# Tarefas e orçamento

tarefas = []

def gerar_id():
    maior = 0
    for t in tarefas:
        if t["id"] > maior:
            maior = t["id"]
    return maior + 1

def buscar_tarefa(id_tarefa, id_evento):
    for t in tarefas:
        if t["id"] == id_tarefa and t["id_evento"] ==  id_evento:
            return t

    return None

def ler_custo(texto):
    texto = texto.replace(",",".")
    try:
        custo = float(texto)
    except ValueError:
        print("ERRO: digite um numero valido!")
        return None
    if custo < 0:
        print("ERRO: o custo não pode ser negativo!")
        return None
    return custo

def cadastrar_tarefa(id_evento):
    nome = input("Nome da tarefa: ").strip()
    if nome == "":
        print("ERRO: nome não pode ficar vazio!")
        return
    if ";" in nome:
        print("Erro: não use ; no nome!")
        return

    custo = ler_custo(input("custo da tarefa (R$): "))

    if custo is None:
        return

    tarefa = {
        "id": gerar_id(),
        "id_evento": id_evento,
        "nome": nome,
        "custo": custo
    }
    tarefas.append(tarefa)
    print("tarefa cadastrada com sucesso!")

def listar_tarefas(id_evento):
    achou = False
    print("\n--- Tarefas do evento ---")

    for t in tarefas:
        if t["id_evento"] == id_evento:
            print(f"ID {t['id']} | {t['nome']} | R$ {t['custo']:.2f}")
            achou = True

        if not achou:
            print("Nenhuma tarefa cadastrada")

def editar_tarefa(id_evento):
    try:
        id_tarefa = int(input("ID da tarfa que quer editar: "))


    except ValueError:
        print("ERRO: o ID tem que ser um numero!")
        return

    tarefa = buscar_tarefa(id_tarefa, id_evento)

    if tarefa is None:
        print("Tarefa não encontrada!")
        return

    novo_nome = input(f"Novo nome {tarefa['nome']}").strip()

    if ";" in novo_nome:
        print("ERRO: não use ; no nome!")
        return

    novo_custo = input(f"Novo custo [{tarefa['custo']:.2f}]").strip()

    if novo_custo != "":
        custo = ler_custo(novo_custo)
        if custo is None:
            return
        tarefa["custo"] = custo

    if novo_nome != "":
        tarefa["nome"] = novo_nome

    print("Tarefa editada co suceso!")


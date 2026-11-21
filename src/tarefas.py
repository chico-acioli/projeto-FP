# Tarefas e orçamento
try:
    from src import eventos
except ImportError:
    eventos = None

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
        id_tarefa = int(input("ID da tarefa que quer editar: "))


    except ValueError:
        print("ERRO: o ID tem que ser um numero!")
        return

    tarefa = buscar_tarefa(id_tarefa, id_evento)

    if tarefa is None:
        print("Tarefa não encontrada!")
        return

    novo_nome = input(f"Novo nome [{tarefa['nome']}]: ").strip()

    if ";" in novo_nome:
        print("ERRO: não use ; no nome!")
        return

    novo_custo = input(f"Novo custo [{tarefa['custo']:.2f}]: ").strip()

    if novo_custo != "":
        custo = ler_custo(novo_custo)
        if custo is None:
            return
        tarefa["custo"] = custo

    if novo_nome != "":
        tarefa["nome"] = novo_nome

    print("Tarefa editada com sucesso!")

def remover_tarefa(id_evento):
    try:
        id_tarefa = int(input("ID da tarefa que quer remover: "))

    except ValueError:
        print("ERRO: o ID tem que ser um numero!")
        return

    tarefa = buscar_tarefa(id_tarefa, id_evento)
    if tarefa is None:
        print("tarefa não encontrada!")
        return

    tarefas.remove(tarefa)
    print("tarefa removida!")

def remover_tarefas_evento(id_evento):
    for t in tarefas[:]:
        if t["id_evento"] == id_evento:
            tarefas.remove(t)

def total_gasto(id_evento):
    total = 0
    for t in tarefas:
        if t["id_evento"] == id_evento:
            total += t["custo"]
    return total

def orcamento_restante(id_evento, orcamento_total):
    return orcamento_total - total_gasto(id_evento)

def mostrar_orcamento(evento_id, orcamento_total):
    gasto = total_gasto(evento_id)
    restante = orcamento_restante(evento_id, orcamento_total)
    print("\n--- Orçamento ---")
    print(f"Orçamento total: R$ {orcamento_total:.2f}")
    print(f"Total gasto: R$ {gasto:.2f}")
    print(f"Orçamento restante: R$ {restante:.2f}")
    if restante < 0:
        print("ATENÇÃO: o orçamento estourou!")


def obter_todas():
    return tarefas


def carregar(lista):
    # troca as tarefas pelas que vieram do arquivo
    tarefas.clear()
    for t in lista:
        tarefas.append(t)


def escolher_evento():
    # pergunta qual evento e devolve (id, orçamento) ou (None, None)
    if eventos is None:
        print("Módulo de eventos não encontrado.")
        return None, None

    lista = eventos.carregar_eventos()
    if len(lista) == 0:
        print("Nenhum evento cadastrado. Cadastre um evento primeiro.")
        return None, None

    print("\n--- Eventos ---")
    for e in lista:
        print(f"ID {e['id']} | {e['nome']}")

    try:
        id_evento = int(input("Digite o ID do evento: "))
    except ValueError:
        print("ERRO: o ID tem que ser um numero!")
        return None, None

    for e in lista:
        # no eventos.py o id e o orçamento são guardados como texto
        if int(e["id"]) == id_evento:
            return id_evento, float(e["orcamento"])

    print("Evento não encontrado!")
    return None, None


def menu_tarefas(evento_id=None, orcamento_total=None):
    # o main.py chama essa função sem argumentos, aí ela pergunta o evento
    if evento_id is None:
        evento_id, orcamento_total = escolher_evento()
        if evento_id is None:
            return

    opcao = ""
    while opcao != "0":
        print("\n=== TAREFAS ===")
        print("1 - Cadastrar tarefa")
        print("2 - Listar tarefas")
        print("3 - Editar tarefa")
        print("4 - Remover tarefa")
        print("5 - Ver orçamento")
        print("0 - Voltar")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_tarefa(evento_id)
            if orcamento_restante(evento_id, orcamento_total) < 0:
                print("ATENÇÃO: o orçamento estourou!")
        elif opcao == "2":
            listar_tarefas(evento_id)
        elif opcao == "3":
            editar_tarefa(evento_id)
        elif opcao == "4":
            remover_tarefa(evento_id)
        elif opcao == "5":
            mostrar_orcamento(evento_id, orcamento_total)
        elif opcao == "0":
            print("Voltando...")
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu_tarefas(1, 1000)  

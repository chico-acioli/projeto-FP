import os
from src import arquivos
from src import tarefas

ARQUIVO_CONVIDADOS = os.path.join(arquivos.PASTA_DADOS,"convidados.csv")

CABECALHO  = "id;id_evento;nome;status"

STATUS_VALIDOS = ("pendente", "confirmado", "recusou")

def salvar_convidados(lista):
    #Vai gravar todos os convidados do arquivo csv e reescreve-lo por inteiro
    linhas = []
    for c in lista:
        linhas.append(f"{c['id']};{c['id_evento']};{c['nome']};{c['status']}")
    return arquivos.salvar_registros(ARQUIVO_CONVIDADOS, CABECALHO, linhas, False)


def carregar_convidados():
    #vai ler os convidados do arquivo csv ou devolver uma lista vazia
    lista = []
    try:
        with open(ARQUIVO_CONVIDADOS, "r", newline="", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()

        for linha in linhas[1:]:
            dados = linha.strip().split(";")
            if len(dados) != 4 or dados[3] not in STATUS_VALIDOS:
                continue
            try:
                lista.append({
                    "id": int(dados[0]),
                    "id_evento": int(dados[1]),
                    "nome": dados[2],
                    "status": dados[3]
                })
            except ValueError:
                continue
    except FileNotFoundError:
        pass
    except (OSError, UnicodeDecodeError) as erro:
        print(f"\nErro ao carregar convidados: {erro}")

    return lista

def gerar_id(lista):
    #vai devolver o próximo id que estiver livre
    maior = 0
    for c in lista:
        if c["id"] > maior:
            maior = c["id"]
    return maior + 1


def buscar_convidado(lista, id_convidado, id_evento):
    #irá procurar o convidado pelo id do evento
    for c in lista:
        if c["id"] == id_convidado and c["id_evento"] == id_evento:
            return c
    return None

def existem_convidados(lista, id_evento):
    #ela vai dizer se o evento tem ao menos um convidado
    for c in lista:
        if c["id_evento"] == id_evento:
            return True
    return False

def ler_id(texto):
    #vai pedir um número para o usuário que se ele for inválido vai sair None
    try:
        return int(input(texto))
    except ValueError:
        print("ERRO: o ID tem que ser um número válido!")
        return None

def cadastrar_convidado(lista, id_evento):
    nome = input("Nome do convidado: ").strip()
    if nome == "":
        print("ERRO: o nome não pode ficar vazio!")
        return
    if ";" in nome:
        print("ERRO: não use ; no nome!")
        return

    convidado = {
        "id": gerar_id(lista),
        "id_evento": id_evento,
        "nome": nome,
        "status": "pendente"
    }
    lista.append(convidado)
    print(f"Convidado cadastrado com ID {convidado['id']} (status: pendente)!")


def listar_convidados(lista, id_evento):
    achou = False
    print("\n--- Convidados do evento ---")
    for c in lista:
        if c["id_evento"] == id_evento:
            print(f"ID {c['id']} | {c['nome']} | {c['status']}")
            achou = True

    if not achou:
        print("Nenhum convidado cadastrado.")


def alterar_status(lista, id_evento):
    if not existem_convidados(lista, id_evento):
        print("Nenhum convidado cadastrado.")
        return

    listar_convidados(lista, id_evento)

    id_convidado = ler_id("ID do convidado: ")
    if id_convidado is None:
        return

    convidado = buscar_convidado(lista, id_convidado, id_evento)
    if convidado is None:
        print("Convidado não encontrado!")
        return

    print("1 - Confirmado")
    print("2 - Recusou")
    print("3 - Pendente")
    opcao = input("Novo status: ").strip()

    if opcao == "1":
        convidado["status"] = "confirmado"
    elif opcao == "2":
        convidado["status"] = "recusou"
    elif opcao == "3":
        convidado["status"] = "pendente"
    else:
        print("Opção inválida!")
        return

    print("Status atualizado!")


def remover_convidado(lista, id_evento):
    if not existem_convidados(lista, id_evento):
        print("Nenhum convidado cadastrado.")
        return

    listar_convidados(lista, id_evento)

    id_convidado = ler_id("ID do convidado que quer remover: ")
    if id_convidado is None:
        return

    convidado = buscar_convidado(lista, id_convidado, id_evento)
    if convidado is None:
        print("Convidado não encontrado!")
        return

    lista.remove(convidado)
    print("Convidado removido!")

def mostrar_resumo(lista, id_evento, orcamento_total):
    confirmados = 0
    pendentes = 0
    recusaram = 0

    for c in lista:
        if c["id_evento"] == id_evento:
            if c["status"] == "confirmado":
                confirmados += 1
            elif c["status"] == "recusou":
                recusaram += 1
            else:
                pendentes += 1

    gasto = tarefas.total_gasto(id_evento)

    print("\n--- Resumo de presença ---")
    print(f"Confirmados: {confirmados}")
    print(f"Pendentes: {pendentes}")
    print(f"Recusaram: {recusaram}")
    print(f"Total gasto até agora: R$ {gasto:.2f}")

    if confirmados == 0:
        print("Nenhum convidado confirmado ainda, não dá para calcular o custo por pessoa.")
    else:
        print(f"Custo por convidado confirmado: R$ {gasto / confirmados:.2f}")
        print(f"Orçamento por convidado confirmado: R$ {orcamento_total / confirmados:.2f}")

def remover_convidados_evento(id_evento):
    lista = carregar_convidados()
    restantes = []
    for c in lista:
        if c["id_evento"] != id_evento:
            restantes.append(c)
    salvar_convidados(restantes)

def menu_convidados():
    id_evento, orcamento_total = tarefas.escolher_evento()
    if id_evento is None:
        return

    lista = carregar_convidados()

    opcao = ""
    while opcao != "0":
        print("\n=== CONVIDADOS ===")
        print("1 - Cadastrar convidado")
        print("2 - Listar convidados")
        print("3 - Alterar status de presença")
        print("4 - Remover convidado")
        print("5 - Ver resumo e custo por pessoa")
        print("0 - Voltar")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_convidado(lista, id_evento)
            salvar_convidados(lista)
        elif opcao == "2":
            listar_convidados(lista, id_evento)
        elif opcao == "3":
            alterar_status(lista, id_evento)
            salvar_convidados(lista)
        elif opcao == "4":
            remover_convidado(lista, id_evento)
            salvar_convidados(lista)
        elif opcao == "5":
            mostrar_resumo(lista, id_evento, orcamento_total)
        elif opcao == "0":
            print("Voltando...")
        else:
            print("Opção inválida!")
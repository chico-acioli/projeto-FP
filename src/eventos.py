# Gerenciamento de eventos
from datetime import datetime


def cadastrar_evento():
    nome = input("Digite o nome do evento: ").strip().lower()
    tipo = input("Digite o tipo do evento: ").strip().lower()
    data = input("Digite a data do evento (DD/MM/AAAA): ").strip()
    local = input("Digite o local do evento: ").strip().lower()
    orcamento = input("Digite o orçamento do evento: ").strip()

    if nome == "" or tipo == "" or data == "" or local == "" or orcamento == "":
        print("Preencha todos os campos!")
        return 

    try:
        datetime.strptime(data, "%d/%m/%Y")
    except ValueError:
        print("Data Inválida. Use esse formato (DD/MM/AAAA).")
        return

    try:
        valor = float(orcamento.replace(",", "."))
    except ValueError:
        print("Orçamento Inválido.")
        return

    if valor < 0: 
        print("O orçamento não pode ser negativo.")
        return 

    eventos = carregar_eventos()

    if len(eventos) == 0:
        novo_id = 1 
    else:
        maior_id = 0 
        
        for evento in eventos:
            if int(evento["id"]) > maior_id:
                maior_id = int(evento["id"])

        novo_id = maior_id + 1 

    evento = {
        "id": str(novo_id),
        "nome": nome,
        "tipo": tipo,
        "data": data,
        "local": local,
        "orcamento": str(valor)
    }

    eventos.append(evento)

    salvar_evento(eventos)

def carregar_eventos():
    eventos = []

    try:
        with open("eventos.csv", "r", newline= "", encoding= "utf-8") as arquivo:
            
            for linha in arquivo:
                dados = linha.strip().split(";")
                if len(dados) == 6:
                    evento = {
                        "id": dados[0],
                        "nome": dados[1],
                        "tipo": dados[2],
                        "data": dados[3],
                        "local": dados[4],
                        "orcamento": dados[5]
                    }
                    eventos.append(evento)

    except FileNotFoundError:
        return eventos 

    return eventos 

def salvar_evento(eventos):
    
    with open("eventos.csv", "w", newline= "", encoding= "utf-8") as arquivo:
            
        for evento in eventos:
            linha = (
            evento["id"] + ";" +
            evento["nome"] + ";" +
            evento["tipo"] + ";" +
            evento["data"] + ";" +
            evento["local"] + ";" +
            evento["orcamento"] + "\n"
        )
        
            arquivo.write(linha)

def listar_eventos():
    eventos = carregar_eventos()

    if len(eventos) > 0: 
        print("Eventos: \n")
        for evento in eventos:
            print("ID:", evento["id"])
            print("Nome:", evento["nome"])
            print("Tipo:", evento["tipo"])
            print("Data:", evento["data"])
            print("Local:", evento["local"])
            print("Orcamento: R$", evento["orcamento"])
            print("\n")
    else:
        print("Nenhum evento cadastrado.")

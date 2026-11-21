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

def excluir_evento():
    eventos = carregar_eventos()

    if len(eventos) > 0:
        id = input("Digite o ID do evento que deseja excluir: ")
        
        evento_encontrado_flag = False

        for evento in eventos:
            if evento["id"] == id:
                evento_encontrado_flag = True 
                evento_encontrado = evento
                break
        if evento_encontrado_flag == False:
            print("Nenhum evento com esse ID foi encontrado.")
        else:
            print("Evento encontrado:")
            print("ID:", evento_encontrado["id"])
            print("Nome:", evento_encontrado["nome"])
            print("Tipo:", evento_encontrado["tipo"])
            print("Data:", evento_encontrado["data"])
            print("Local:", evento_encontrado["local"])
            print("Orçamento: R$", evento_encontrado["orcamento"])
            
            confirmacao = input("Deseja excluir este evento (S/N): ").strip().lower()
            
            if confirmacao == "s":
                eventos.remove(evento_encontrado)
                salvar_evento(eventos)
                print("Evento excluído com sucesso!")
            else:
                print("Exclusão cancelada!")

    else:
        print("Nenhum evento cadastrado.")

def editar_evento():
    eventos = carregar_eventos()
    
    if len(eventos) > 0:
        id = input("Digite o ID do evento que deseja editar: ")
            
        evento_encontrado_flag = False

        for evento in eventos:
            if evento["id"] == id:
                evento_encontrado_flag = True 
                evento_encontrado = evento
                break
        if evento_encontrado_flag == False:
            print("Nenhum evento com esse ID foi encontrado.")
        else:
            print("Evento encontrado:")
            print("ID:", evento_encontrado["id"])
            print("Nome:", evento_encontrado["nome"])
            print("Tipo:", evento_encontrado["tipo"])
            print("Data:", evento_encontrado["data"])
            print("Local:", evento_encontrado["local"])
            print("Orçamento: R$", evento_encontrado["orcamento"])
            
            while True:
               
                menu_exibir()
                opcao = input("Escolha uma opção: ").strip()

                if opcao == "6":
                    break
                    
                elif opcao == "1":
                    novo_nome = input("Digite o novo nome do evento: ").strip().lower()
                    if novo_nome == "":
                        print("Nome inválido.")
                    else:
                        evento_encontrado["nome"] = novo_nome
                        break
                    
                elif opcao == "2":
                    novo_tipo = input("Digite o novo tipo de evento: ").strip().lower()
                    if novo_tipo == "":
                        print("Tipo inválido.")
                    else:
                        evento_encontrado["tipo"] = novo_tipo
                        break
                    
                elif opcao == "3":
                    nova_data = input("Digite a nova data (DD/MM/AAAA): ").strip()
                    try:
                        datetime.strptime(nova_data, "%d/%m/%Y")
                        evento_encontrado["data"] = nova_data
                        break
                    except ValueError:
                        print("Data inválida.")
                        
                elif opcao == "4":
                    novo_local = input("Digite o novo local do evento: ").strip().lower()
                    if novo_local == "":
                        print("Local inválido.")
                    else:
                        evento_encontrado["local"] = novo_local
                        break
                    
                elif opcao == "5":
                    novo_orcamento = input("Digite o novo orçamento: ").strip()
                    try:
                        valor = float(novo_orcamento.replace(",", "."))
                        if valor < 0:
                            print("O orçamento não pode ser negativo.")
                            continue
                        evento_encontrado["orcamento"] = str(valor)
                        break
                    except ValueError:
                        print("Orçamento inválido.")
                        
                else:
                    print("Opção Inválida. Escolha uma opção válida.")

            if opcao != "6":
                print("Evento editado com  sucesso!")
                print("ID:", evento_encontrado["id"])
                print("Nome:", evento_encontrado["nome"])
                print("Tipo:", evento_encontrado["tipo"])
                print("Data:", evento_encontrado["data"])
                print("Local:", evento_encontrado["local"])
                print("Orçamento: R$", evento_encontrado["orcamento"])
                
                salvar_evento(eventos)
    
    else:
        print("Nenhum evento cadastrado.")

def menu_exibir():
    print("1- Nome")
    print("2- Tipo")
    print("3- Data")
    print("4- Local")
    print("5- Orçamento")
    print("6- Cancelar")


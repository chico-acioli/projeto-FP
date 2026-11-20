# Manipulação e armazenamento dos dados

def salvar_tarefas(tarefas):

    with open("dados/tarefas.csv", "a", encoding="utf-8") as arquivo:

        for tarefa in tarefas:
            linha = (f"{tarefa['id']};"
                f"{tarefa['id_evento']};"
                f"{tarefa['nome']};"
                f"{tarefa['custo']}\n")
            
            arquivo.write(linha)

def carregar_tarefas():

    tarefas = []

    try:
        with open("dados/tarefas.csv", "r", encoding="utf-8") as arquivo:

            linhas = arquivo.readlines()

            for linha in linhas[1:]:
                dados = linha.strip().split(";")

                if len(dados) == 4:
                    tarefa = {
                        "id": int(dados[0]),
                        "id_evento": int(dados[1]),
                        "nome": dados[2],
                        "custo": float(dados[3])
                    }

                    tarefas.append(tarefa)

    except FileNotFoundError:
        print("\nArquivo de tarefas não encontrado.")

    return tarefas
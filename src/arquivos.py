import os

PASTA_PROJETO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))    
PASTA_DADOS = os.path.join(PASTA_PROJETO, "dados")    
ARQUIVO_TAREFAS = os.path.join(PASTA_DADOS, "tarefas.csv")   
ARQUIVO_EVENTOS = os.path.join(PASTA_DADOS, "eventos.csv")   


def preparar_pasta_dados():
    """Cria a pasta de dados se ela ainda não existir."""
    try:
        os.makedirs(PASTA_DADOS, exist_ok=True)
    except OSError as erro:
        print(f"Erro ao preparar a pasta de dados: {erro}")


def salvar_registros(caminho, cabecalho, linhas, acrescentar):
    """Acrescenta linhas novas ou regrava o arquivo completo."""
    
    preparar_pasta_dados()

    try:
        modo = "a" if acrescentar else "w"
        with open(caminho, modo, newline="", encoding="utf-8") as arquivo:
            if not acrescentar or os.path.getsize(caminho) == 0:
                arquivo.write(cabecalho + "\n")

            for linha in linhas:
                arquivo.write(linha + "\n")

        return True
    except OSError as erro:
        print(f"\nErro ao salvar arquivo: {erro}")
        return False


def salvar_tarefas(tarefas, acrescentar=False):
    try:
        linhas = [f"{tarefa.get('id', '')};"
            f"{tarefa.get('id_evento', '')};"
            f"{tarefa.get('nome', '')};"
            f"{tarefa.get('custo', '')}"
            for tarefa in tarefas]
        
    except AttributeError as erro:
        print("\nErro ao salvar tarefas:", erro)
        return False

    return salvar_registros(ARQUIVO_TAREFAS, "id;id_evento;nome;custo", linhas, acrescentar)


def carregar_tarefas():
    tarefas = []

    try:
        with open(ARQUIVO_TAREFAS, "r", newline="", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()

        for linha in linhas[1:]:
            dados = linha.strip().split(";")
            if len(dados) != 4:
                continue

            try:
                tarefas.append({"id": int(dados[0]), "id_evento": int(dados[1]), "nome": dados[2], "custo": float(dados[3].replace(",", "."))})
            
            except ValueError:
                continue
    except FileNotFoundError:
        preparar_pasta_dados()
    except (OSError, UnicodeDecodeError) as erro:
        print(f"\nErro ao carregar tarefas: {erro}")

    return tarefas


def salvar_eventos(eventos, acrescentar=False):
    try:
        linhas = [f"{evento.get('id', '')};"
            f"{evento.get('nome', '')};"
            f"{evento.get('tipo', '')};"
            f"{evento.get('data', '')};"
            f"{evento.get('local', '')};"
            f"{evento.get('orcamento', '')}"
            for evento in eventos]
        
    except AttributeError as erro:
        print(f"\nErro ao salvar eventos: {erro}")
        return False

    return salvar_registros(ARQUIVO_EVENTOS, "id;nome;tipo;data;local;orcamento", linhas, acrescentar)

def carregar_eventos():
    """Lê os eventos do CSV ou retorna uma lista vazia."""

    eventos = []

    try:
        with open(ARQUIVO_EVENTOS, "r", newline="", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()

        for linha in linhas[1:]:
            dados = linha.strip().split(";")
            if len(dados) != 6:
                continue

            eventos.append({"id": dados[0],
            "nome": dados[1], "tipo": dados[2], "data": dados[3], "local": dados[4], "orcamento": dados[5]})
    
    except FileNotFoundError:
        preparar_pasta_dados()
    except (OSError, UnicodeDecodeError) as erro:
        print(f"\nErro ao carregar eventos: {erro}")

    return eventos

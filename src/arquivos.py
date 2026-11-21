import os

# Localiza os dados a partir da pasta do projeto.
PASTA_PROJETO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PASTA_DADOS = os.path.join(PASTA_PROJETO, "dados")
ARQUIVO_TAREFAS = os.path.join(PASTA_DADOS, "tarefas.csv")


def preparar_pasta_dados():
    """Cria a pasta de dados se ela ainda não existir."""
    try:
        # exist_ok evita erro quando a pasta já está criada.
        os.makedirs(PASTA_DADOS, exist_ok=True)
    except OSError as erro:
        print(f"Erro ao preparar a pasta de dados: {erro}")


def salvar_registros(caminho, cabecalho, linhas, acrescentar):
    """Acrescenta linhas novas ou regrava o arquivo completo."""
    
    preparar_pasta_dados()

    try:
        # "a" mantém os dados existentes; "w" substitui a lista inteira.
        modo = "a" if acrescentar else "w"
        with open(caminho, modo, newline="", encoding="utf-8") as arquivo:
            # O cabeçalho é escrito ao regravar ou criar um arquivo vazio.
            if not acrescentar or os.path.getsize(caminho) == 0:
                arquivo.write(cabecalho + "\n")

            # Cada tarefa é gravada em uma linha do CSV.
            for linha in linhas:
                arquivo.write(linha + "\n")

        return True
    except OSError as erro:
        print(f"\nErro ao salvar arquivo: {erro}")
        return False


def salvar_tarefas(tarefas, acrescentar=False):
    """Salva tarefas; para acrescentar, envie somente as tarefas novas."""
    try:
        # Organiza os campos na mesma ordem do cabeçalho do CSV.
        linhas = [f"{tarefa.get('id', '')};"
            f"{tarefa.get('id_evento', '')};"
            f"{tarefa.get('nome', '')};"
            f"{tarefa.get('custo', '')}"
            for tarefa in tarefas]
        
    except AttributeError as erro:
        print("\nErro ao salvar tarefas:", erro)
        return False

    # Para editar ou excluir, envie a lista completa sem ativar acrescentar.
    return salvar_registros(ARQUIVO_TAREFAS, "id;id_evento;nome;custo", linhas, acrescentar)


def carregar_tarefas():
    """Lê as tarefas do CSV ou retorna uma lista vazia."""
    tarefas = []

    try:
        with open(ARQUIVO_TAREFAS, "r", newline="", encoding="utf-8") as arquivo:
            # Lê as linhas; a primeira é o cabeçalho.
            linhas = arquivo.readlines()

        # Separa os campos e ignora linhas com quantidade incorreta de colunas.
        for linha in linhas[1:]:
            dados = linha.strip().split(";")
            if len(dados) != 4:
                continue

            try:
                # Converte os IDs e o custo para os tipos usados pelo programa.
                tarefas.append({"id": int(dados[0]), "id_evento": int(dados[1]), "nome": dados[2], "custo": float(dados[3].replace(",", "."))})
            
            except ValueError:
                continue
    except FileNotFoundError:
        # Permite iniciar sem tarefas cadastradas.
        preparar_pasta_dados()
    except (OSError, UnicodeDecodeError) as erro:
        print(f"\nErro ao carregar tarefas: {erro}")

    return tarefas
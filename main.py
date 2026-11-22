import os

try:
    from src import arquivos
except ImportError:
    arquivos = None
try:
    from src import eventos
except ImportError:
    eventos = None

try:
    from src import tarefas
except ImportError:
    tarefas = None

try:
    from src import sugestoes
except ImportError:
    sugestoes = None

try:
    from src import convidados
except ImportError:
    convidados = None

def limpar_tela():
    """Essa função limpa o terminal. Para Windows, usa 'cls', para Linux ou Mac, usa 'clear'"""
    os.system("cls" if os.name == "nt" else "clear")

def menu_exibir():
    print("=" * 36) #pra fazer aquelas linhas decorativa supimpa
    print("          ORGANIZA FESTA")
    print("=" * 36)
    print("1 - Eventos")
    print("2 - Tarefas")
    print("3 - Sugestões")
    print("4 - Convidados")
    print("5 - Sair")
    print("-" * 36)

def chamar_funcao(modulo, funcao_nome):
    if modulo is None or not hasattr(modulo, funcao_nome): #hasattr é pra perguntar se um objeto tem algo com determinado nome, e vai responder True ou False
        print("\nFuncionalidade em desenvolvimento, tente novamente posteriormente")
        return
    getattr(modulo, funcao_nome)() #vai buscar a função pelo nome em texto e os "()" é pra executar dps

def pausar():
    input("\nPara voltar ao menu, pressione 'enter' ")

def carregar_dados():
    #ela vai carregar os dados salvos nos arquivos e iniciar o programa
    if arquivos is None or tarefas is None:
        return
    tarefas.carregar(arquivos.carregar_tarefas())

def salvar_dados():
    #meio auto explicativo
    if arquivos is None or tarefas is None:
        return
    arquivos.salvar_tarefas(tarefas.obter_todas())

def main():
    carregar_dados()          #ela vai rodar uma vez antes do menu aparecer
    while True:
        limpar_tela()
        menu_exibir()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            chamar_funcao(eventos, "menu_eventos")
        elif opcao == "2":
            chamar_funcao(tarefas, "menu_tarefas")
        elif opcao == "3":
            chamar_funcao(sugestoes, "menu_sugestoes")
        elif opcao == "4":
            chamar_funcao(convidados, "menu_convidados")
        elif opcao == "5":
            print("\nTe espero na próxima festinha!")
            break
        else:
            print("\nOpção inválida, tente novamente com um número do menu.")

        salvar_dados()        #ela vai salvar depois de cada ação
        pausar()


if __name__ == "__main__":  #'só rode isso se este arquivo foi executado diretamente', é isso que significa essa linha
    try:
        main()
    except (KeyboardInterrupt, EOFError): #KeyboardInterrupt acontece quando o cara aperta Ctrl+C, e o EOFError acontece quando a entrada é fechada de repente (Ctrl+D/Ctrl+Z)
        print("\n\nPrograma encerrado.")

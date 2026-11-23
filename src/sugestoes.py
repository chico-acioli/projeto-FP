from datetime import datetime

def calcular_dias_restantes(data_evento):
    data_evento = datetime.strptime(data_evento, "%d/%m/%Y").date()
    
    hoje = datetime.now().date()

    diferenca = data_evento - hoje

    return diferenca.days



def exibir_sugestoes(tipo_evento, convidados):

    print("\n========== SUGESTÕES PARA O EVENTO ==========")

    if tipo_evento == "aniversario" or tipo_evento == "aniversário":

        if convidados <= 20:
            print("Fornecedor: encomendar salgadinhos e bolo.")
            print("Decoração: usar balões e enfeites simples.")
            print("Cardápio: bolo, salgadinhos e refrigerantes.")
            print("Atividades: brincadeiras e música.")

        elif convidados <= 50:
            print("Fornecedor: contratar um buffet pequeno.")
            print("Decoração: usar painel tematico e balões.")
            print("Cardápio: salgadinhos, doces e bolo.")
            print("Atividades: contratar um animador ou um DJ.")

        else:
            print("Fornecedor: contratar um buffet profissional.")
            print("Decoração: investir em decoração temática.")
            print("Cardápio: oferecer um buffet variado.")
            print("Atividades: contratar DJ e organizar uma pista de dança.")

    elif tipo_evento == "casamento":

        if convidados <= 20:
            print("Fornecedor: contratar um buffet intimista.")
            print("Decoração: utilizar flores e velas.")
            print("Cardápio: jantar especial.")
            print("Atividades: música ao vivo em formato acustico.")

        elif convidados <= 50:
            print("Fornecedor: contratar buffet e fótografo.")
            print("Decoração: utilizar arranjos florais.")
            print("Cardápio: jantar com sobremesas.")
            print("Atividades: música ao vivo.")

        else:
            print("Fornecedor: contratar um buffet completo e equipe de fotografia.")
            print("Decoração: investir em decoracão floral e iluminação.")
            print("Cardápio: buffet completo com sobremesas.")
            print("Atividades: contratar banda ou DJ.")

    elif tipo_evento == "reuniao" or tipo_evento == "reunião":

        if convidados <= 20:
            print("Fornecedor: organizar um coffee break simples.")
            print("Decoração: utilizar uma decoração discreta.")
            print("Cardápio: café, sucos e biscoitos.")
            print("Atividades: debates e apresentações.")

        elif convidados <= 50:
            print("Fornecedor: contratar servico de coffee break.")
            print("Decoração: organizar mesas e cadeiras.")
            print("Cardápio: salgados, bebidas e frutas.")
            print("Atividades: utilizar projetor e microfone.")

        else:
            print("Fornecedor: contratar buffet para eventos corporativos.")
            print("Decoração: organizar um auditório.")
            print("Cardápio: coffee break completo.")
            print("Atividades: palestras e apresentações.")

    else:
        print("Tipo de evento não reconhecido.")
        print("Sugestão: organize fornecedores e atividades de acordo com o perfil dos convidados.")


def menu_sugestoes():

    print("\n========== CONTAGEM REGRESSIVA E SUGESTÕES ==========")

    tipo_evento = input("Digite o tipo do evento (aniversário, casamento ou reunião): ").strip().lower()

    while True:
        try:
            convidados = int(input("Digite a quantidade de convidados: "))

            if convidados <= 0:
                print("A quantidade deve ser maior que zero.")
            else:
                break

        except ValueError:
            print("Digite uma quantidade válida de convidados.")

    while True:
        data_evento = input("Digite a data do evento (DD/MM/AAAA): ")


        try:
            dias = calcular_dias_restantes(data_evento)
            break

        except ValueError:
            print("Data inválida! Digite novamente no formato DD/MM/AAAA.")


    print("\n========== CONTAGEM REGRESSIVA ==========")

    if dias > 0:
        print(f"Faltam {dias} dias para o evento!")

    elif dias == 0:
        print("O evento acontece hoje!")

    else:
        print(f"Este evento já aconteceu há {abs(dias)} dias.")

    exibir_sugestoes(tipo_evento, convidados)



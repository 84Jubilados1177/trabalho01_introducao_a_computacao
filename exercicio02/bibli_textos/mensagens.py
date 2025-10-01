def Linha():
    print("-" * 30)

def Instrucoes():
    Linha()
    print("Seja bem-vindo ao conversor para decimal!")
    print("Para executar os testes digite a opção")
    print("desejada:")
    print("0 - Teste automatizado")
    print("1 - Teste independente")
    print("2 - Sair")

def Sentenca():
    print("--------Conversor para Decimal:----------")


def Saida():
    Linha()
    print("saindo ...")
    Linha()

def Erro(Num_erro):
    if(Num_erro == 1):
        print("-" * 30)
        print(("-" * 10) + "Eu acho que isso não é um binário :(" + ("-" + 10))

    elif(Num_erro == 2):
        print("Entrada inválida, responda com (S/N) ")
        Linha()

    elif(Num_erro == 3):
        Linha()
        print("Entrada inválida, responda com (0, 1 ou 2)")
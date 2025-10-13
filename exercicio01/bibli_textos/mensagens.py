def Linha():
    print("-" * 50)

def Instrucoes():
    Linha()
    print("Seja bem-vindo ao conversor para binário!")
    print("Para executar os testes digite a opção desejada:")
    print("0 - Teste automatizado")
    print("1 - Teste independente")
    print("2 - Sair")

def Sentenca():
    print(("-" * 12) + " Conversor para Binário: " + ("-" * 13))


def Saida():
    Linha()
    print("saindo ...")
    Linha()

def Erro(Num_erro):
    if(Num_erro == 1):
        print("-" * 50)
        print("Eu acho que isso não é um número inteiro :(")
        Linha()

    elif(Num_erro == 2):
        print("Entrada inválida, responda com (S/N) ")
        Linha()

    elif(Num_erro == 3):
        Linha()
        print("Entrada inválida, responda com (0, 1 ou 2)")

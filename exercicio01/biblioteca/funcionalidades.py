def Instrucoes():
    print("-----------------------------------------")
    print("Seja bem vindo ao conversor para binario!")
    print("Para executar os testes digite a opção")
    print("desejada:")
    print("0 - Teste automatizado")
    print("1 - Teste independente")
    print("2 - Sair")

def Algarismo(numero):
    algarismo = numero%2
    return int (algarismo)

#Apagar se não for usado futuramente
def Completa_zeros(numero):
    num = numero
    zeros = ""
    binario = ""

    while num != 0:
        alg = Algarismo(num)
        binario = str(alg) + binario
        num = int(num/2)

    for i in range(7-len(binario)):
        zeros += "0"

    return zeros

def Em_binario(numero):
    binario = ""
    num = numero

    if(num == 0):
        binario = "0"

    while num != 0:
        alg = Algarismo(num)
        binario = str(alg) + binario
        num = int(num/2)
    
    if(numero >= 0):
        return (binario)
    else:
        return ("-" + binario)

def Em_bin_numero_positivo_par():
    assert Em_binario(8) == "1000"
def Em_bin_numero_positivo_impar():
    assert Em_binario(13) == "1101"
def Em_bin_numero_negativo_par():
    assert Em_binario(-8) == "-1000"
def Em_bin_numero_negativo_impar():
    assert Em_binario(-13) == "-1101"
def Em_bin_numero_nulo():
    assert Em_binario(0) == "0"

def Testes():
    print("-----------Teste automatizado------------")
    print("Teste 1: {}".format(Em_bin_numero_positivo_par()))
    print("Teste 2: {}".format(Em_bin_numero_positivo_impar()))
    print("Teste 3: {}".format(Em_bin_numero_negativo_par()))
    print("Teste 4: {}".format(Em_bin_numero_negativo_impar()))
    print("Teste 5: {}".format(Em_bin_numero_nulo()))

    
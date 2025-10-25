def Algarismo(numero):
    return numero%2

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

def Confere_decimal(numero):
    try:
        int(numero)
        return True
    except ValueError:
        return False

def Eh_numero_inteiro(variavel):
    try:
        int(variavel)
        return True
    except ValueError:
        return False

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

def Teste1():
    assert Em_binario(8) == "1000"
def Teste2():
    assert Em_binario(0) == "0"
def Teste3():
    assert Em_binario(-8) == "-1000"

def Testes():
    print(("-" * 15) + " Teste automatizado " + ("-" * 15))
    print("Decimal -> Binário")
    print("Inteiro 13 para String \"1101\": {}".format(Teste1()))
    print("Inteiro 0 para String \"0\": {}".format(Teste2()))
    print("Inteiro 0 para String \"-1000\": {}".format(Teste3()))

    
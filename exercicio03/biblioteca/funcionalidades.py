def Algarismo(numero):
    algarismo = numero%8
    return int (algarismo)

def Confere_decimal(numero):
    try:
        int(numero)
        return True
    except ValueError:
        return False

def Em_decimal(numero, base):
    negativo = False
    dec = 0
    cont = 0

    if(numero < 0):
        negativo = True  
        numero *= -1
    
    num = int(numero)
    

    while(num != 0):
        alg = Algarismo(num)
        num -= alg
        num //= 8
        dec += alg*pow(base, cont)
        cont += 1
    
    if(negativo):
        return ("-" + str(dec))
    else:
        return str(dec)

def Teste1():
    assert Em_decimal(93, 10) == "135"
def Teste2():
    assert Em_decimal(-64, 10) == "-100"
def Teste3():
    assert Em_decimal(0, 10) == "0"

def Testes():
    print(("-" * 16) + "Teste automatizado" + ("-" * 16))
    print("Decimal -> Octal")
    print("Inteiro 93 para String \"135\": {}".format(Teste1()))
    print("Inteiro -64 para String \"-100\": {}".format(Teste2()))
    print("Inteiro 0 para String \"0\": {}".format(Teste3()))

Testes()
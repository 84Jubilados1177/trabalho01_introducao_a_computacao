def Algarismo(numero):
    algarismo = numero%10
    return int (algarismo)

def Confere_binario(numero):
    for i in numero:
        if(i != '0' and i != '1' and i != '-'):
            return False
    return True

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

    if(numero[0] == "-"):
        numero = numero[1:] 
        negativo = True  
    
    num = int(numero)
    

    while(num != 0):
        alg = Algarismo(num)
        num -= alg
        num //= 10
        dec += alg*pow(base, cont)
        cont += 1
    
    if(negativo):
        return (dec*-1)
    else:
        return dec

def Teste1():
    assert Em_decimal("1101", 2) == 13
def Teste2():
    assert Em_decimal("-1000", 2) == -8
def Teste3():
    assert Em_decimal("0", 2) == 0

def Testes():
    print(("-" * 16) + "Teste automatizado" + ("-" * 16))
    print("Binário -> Decimal")
    print("String \"1101\" para o Inteiro 13: {}".format(Teste1()))
    print("String \"-1000\" para o Inteiro -8: {}".format(Teste2()))
    print("String \"0\" para o Inteiro 0: {}".format(Teste3()))

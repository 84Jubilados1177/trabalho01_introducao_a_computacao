def Instrucoes():
    print("-----------------------------------------")
    print("Seja bem vindo ao conversor para binario!")
    print("Para executar os testes digite a opção")
    print("desejada:")
    print("0 - Teste automatizado")
    print("1 - Teste independente")
    print("2 - Sair")

def Algarismo(numero):
    algarismo = numero%10
    return int (algarismo)

def Em_decimal(numero, base):
    negativo = 0
    if(numero[0] == "-"):
        for i in numero:
            numero[i] = numero[i+1]
        negativo = True

    num = int(numero)
    dec = 0
    cont = 0

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


print("Teste 1: {}".format(Em_decimal("-1000")))
print("Teste 1: {}".format(Em_decimal("-1101")))

def Em_dec_numero_positivo_par():
    assert Em_decimal("1000", 2) == 8
def Em_dec_numero_positivo_impar():
    assert Em_decimal("1101", 2) == 13
def Em_dec_numero_negativo_par():
    assert Em_decimal("-1000", 2) == -8
def Em_dec_numero_negativo_impar():
    assert Em_decimal("-1101", 2) == -13
def Em_dec_numero_nulo():
    assert Em_decimal("0", 2) == 0

def Testes():
    print("-----------Teste automatizado------------")
    print("Teste 1: {}".format(Em_dec_numero_positivo_par()))
    print("Teste 2: {}".format(Em_dec_numero_positivo_impar()))
    print("Teste 3: {}".format(Em_dec_numero_negativo_par()))
    print("Teste 4: {}".format(Em_dec_numero_negativo_impar()))
    print("Teste 5: {}".format(Em_dec_numero_nulo()))

def Algarismo(numero):
    algarismo = numero%10
    return int (algarismo)

def Confere_binario(numero):
    for i in numero:
        if(i != '0' and i != '1' and i != '-'):
            return False
    return True

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
    print("Teste com o numero 8: {}".format(Em_dec_numero_positivo_par()))
    print("Teste com o numero 13: {}".format(Em_dec_numero_positivo_impar()))
    print("Teste com o numero -8: {}".format(Em_dec_numero_negativo_par()))
    print("Teste com o numero -13: {}".format(Em_dec_numero_negativo_impar()))
    print("Teste com o numero 0: {}".format(Em_dec_numero_nulo()))

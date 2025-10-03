def Algarismo(numero):
    algarismo = numero%10
    return int (algarismo)

def Confere_octal(numero):
    caracteres = ['0', '1', '2', '3', '4', '5', '6', '7', '-']
    num = str(numero)
    octal = True
    for i in num:
        if not(i in caracteres):
            octal = False
    return octal

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
        num //= 10
        dec += alg*pow(base, cont)
        cont += 1
    
    if(negativo):
        return ("-" + str(dec))
    else:
        return str(dec)

def Em_dec_numero_positivo_par():
    assert Em_decimal(10, 8) == "8"
def Em_dec_numero_positivo_impar():
    assert Em_decimal(15, 8) == "13"
def Em_dec_numero_negativo_par():
    assert Em_decimal(-10, 8) == "-8"
def Em_dec_numero_negativo_impar():
    assert Em_decimal(-15, 8) == "-13"
def Em_dec_numero_nulo():
    assert Em_decimal(0, 8) == "0"

def Testes():
    print("-----------Teste automatizado------------")
    print("Teste com o numero 8: {}".format(Em_dec_numero_positivo_par()))
    print("Teste com o numero 13: {}".format(Em_dec_numero_positivo_impar()))
    print("Teste com o numero -8: {}".format(Em_dec_numero_negativo_par()))
    print("Teste com o numero -13: {}".format(Em_dec_numero_negativo_impar()))
    print("Teste com o numero 0: {}".format(Em_dec_numero_nulo()))

def Algarismo(numero):
    algarismo = numero%10
    return int (algarismo)

def Confere_decimal(numero):
    caracteres = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-']
    num = numero
    octal = True
    for i in num:
        if not(i in caracteres):
            octal = False
    return octal

def Cria_quociente(numero):
    quociente = numero 
    quociente //= 8
    return quociente

def Acha_resto(numero):
    resto = numero % 8
    return resto

def Para_octal(numero):
    negativo = False

    if (numero[0] == "-"):
        numero = numero[1:]
        negativo = True

    quociente = int(numero)
    octal = 0
    cont = 1
    while quociente != 0:
        resto = Acha_resto(quociente)
        quociente = Cria_quociente(quociente)
        octal += resto * cont
        cont *= 10

    if (negativo == True):
        octal *= -1
    return octal

print("{}".format(Para_octal("100")))

def Em_dec_numero_positivo_par():
    assert Para_octal("8") == 10
def Em_dec_numero_positivo_impar():
    assert Para_octal("13") == 15
def Em_dec_numero_negativo_par():
    assert Para_octal("-8") == -10
def Em_dec_numero_negativo_impar():
    assert Para_octal("-13") == -15
def Em_dec_numero_nulo():
    assert Para_octal("0") == 0

def Testes():
    print("-----------Teste automatizado------------")
    print("Teste com o numero 8: {}".format(Em_dec_numero_positivo_par()))
    print("Teste com o numero 13: {}".format(Em_dec_numero_positivo_impar()))
    print("Teste com o numero -8: {}".format(Em_dec_numero_negativo_par()))
    print("Teste com o numero -13: {}".format(Em_dec_numero_negativo_impar()))
    print("Teste com o numero 0: {}".format(Em_dec_numero_nulo()))

def Algarismo(numero):
    algarismo = numero%10
    return int (algarismo)

def Confere_decimal(numero):
    try:
        int(numero)
        return True
    except ValueError:
        return False

def Quociente(numero):
    quociente = numero
    quociente //= 16
    return quociente

def Resto(numero):
    resto = numero
    resto %= 16
    return resto

def Mapeamento(resto):
    if (resto < 10):
        return str(resto)
    elif (resto == 10):
        return 'A'
    elif (resto == 11):
        return 'B'
    elif (resto == 12):
        return 'C'
    elif (resto == 13):
        return 'D'
    elif (resto == 14):
        return 'E'
    elif (resto == 15):
        return 'F'


def Para_hexadecimal(numero):
    negativo = False
    resto = 0
    quociente = numero     
    hexadecimal = "" 
    
    if (numero < 0):
        negativo = True
        quociente *= -1

    if (quociente == 0):
        hexadecimal = "0"

    while quociente != 0:
        resto = Resto(quociente)
        quociente = Quociente(quociente) 
        hexadecimal = Mapeamento(resto) + hexadecimal

    if (negativo == True):
        return ("-" + hexadecimal)
    return hexadecimal


def Em_dec_numero_positivo_par():
    assert Para_hexadecimal(254) == "FE"
def Em_dec_numero_positivo_impar():
    assert Para_hexadecimal(785) == "311"
def Em_dec_numero_negativo_par():
    assert Para_hexadecimal(-254) == "-FE"
def Em_dec_numero_negativo_impar():
    assert Para_hexadecimal(-785) == "-311"
def Em_dec_numero_nulo():
    assert Para_hexadecimal(0) == "0"

def Testes():
    print(("-" * 15) + "Teste automatizado" + ("-" * 15))
    print("Teste com o numero 254: {}".format(Em_dec_numero_positivo_par()))
    print("Teste com o numero 785: {}".format(Em_dec_numero_positivo_impar()))
    print("Teste com o numero -254: {}".format(Em_dec_numero_negativo_par()))
    print("Teste com o numero -785: {}".format(Em_dec_numero_negativo_impar()))
    print("Teste com o numero 0: {}".format(Em_dec_numero_nulo()))

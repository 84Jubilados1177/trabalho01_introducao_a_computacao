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


def Teste1():
    assert Para_hexadecimal(255) == "FF"
def Teste2():
    assert Para_hexadecimal(4095) == "FFF"
def Teste3():
    assert Para_hexadecimal(-26) == "-1A"
def Teste4():
    assert Para_hexadecimal(0) == "0"

def Testes():
    print(("-" * 15) + " Teste automatizado " + ("-" * 15))
    print("Decimal -> Hexadecimal")
    print("Inteiro 255 para String \"FF\": {}".format(Teste1()))
    print("Inteiro 4095 para String \"FFF\": {}".format(Teste2()))
    print("Inteiro -26 para String \"-1A\": {}".format(Teste3()))
    print("Inteiro 0 para String \"0\": {}".format(Teste4()))

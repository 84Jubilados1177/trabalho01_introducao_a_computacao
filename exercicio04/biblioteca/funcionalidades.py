def Algarismo(numero):
    algarismo = numero%10
    return int (algarismo)

def Confere_octal_str(numero):
    caracteres = ['0', '1', '2', '3', '4', '5', '6', '7', '-']
    num = numero
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

def Confere_decimal_str(numero):
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

def Para_decimal(numero):
    negativo = False

    if (numero[0] == "-"):
        numero = numero[1:]
        negativo = True

    decimal = 0
    cont = len(numero) - 1 

    for digito in numero:
        decimal += int(digito) * (8 ** cont)
        cont -= 1

    if (negativo == True):
        decimal *= -1
    return decimal

def Teste1():
    assert Para_decimal("135") == 93
def Teste2():
    assert Para_decimal("-100") == -64
def Teste3():
    assert Para_decimal("0") == 0

def Testes():
    print(("-" * 16) + "Teste automatizado" + ("-" * 16))
    print("Octal -> Decimal")
    print("String \"135\" para o inteiro 93: {}".format(Teste1()))
    print("String \"-100\" para o inteiro -64: {}".format(Teste2()))
    print("String \"0\" para o inteiro 0: {}".format(Teste3()))
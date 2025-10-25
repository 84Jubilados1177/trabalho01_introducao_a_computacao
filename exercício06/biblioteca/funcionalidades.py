def Algarismo(numero):
    algarismo = numero%10
    return int (algarismo)

def Confere_decimal(numero):
    try:
        int(numero)
        return True
    except ValueError:
        return False

def Confere_hexadecimal(numero):
    caracteres = ['0', '1', '2', '3', '4', '5', '6', '7', 
                  '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 
                  'a', 'b', 'c', 'd', 'e', 'f', '-']
    num = numero
    octal = True
    for i in num:
        if not(i in caracteres):
            octal = False
    return octal

def Quociente(numero):
    quociente = numero
    quociente //= 16
    return quociente

def Resto(numero):
    resto = numero
    resto %= 16
    return resto

def Tamanho(numero):
    tamanho = 0
    for i in numero:
        tamanho += 1
    return tamanho

def Mapeamento(resto):
    if (resto == 'A' or resto == 'a'):
        return 10
    elif (resto == 'B' or resto == 'b'):
        return 11
    elif (resto == 'C' or resto == 'c'):
        return 12
    elif (resto == 'D' or resto == 'd'):
        return 13
    elif (resto == 'E' or resto == 'e'):
        return 14
    elif (resto == 'F' or resto == 'f'):
        return 15
    else:
        return int(resto)

def Conversor(numero, tamanho):
    algarismo = numero[0];
    total = Mapeamento(algarismo) * (16 ** tamanho)
    
    return total


def Para_decimal(numero):
    negativo = False
    decimal = 0
    
    if(numero[0] == '-'):
        numero = numero[1:]    
        negativo = True

    tamanho = Tamanho(numero) - 1

    while numero != "":
        decimal += Conversor(numero, tamanho);
        numero = numero[1:]
        tamanho -= 1

    if (negativo == True):
        return (decimal*-1)
    
    return decimal

def Teste1():
    assert Para_decimal("FF") == 255
def Teste2():
    assert Para_decimal("fff") == 4095
def Teste3():
    assert Para_decimal("-1A") == -26
def Teste4():
    assert Para_decimal("0") == 0

def Testes():
    print(("-" * 15) + " Teste automatizado " + ("-" * 15))
    print("Hexadecimal -> Decimal")
    print("String \"FF\" para o Inteiro 255: {}".format(Teste1()))
    print("String \"fff\" para o Inteiro 4095: {}".format(Teste2()))
    print("String \"-1A\" para o Inteiro -26: {}".format(Teste3()))
    print("String \"0\" para o Inteiro 0: {}".format(Teste4()))
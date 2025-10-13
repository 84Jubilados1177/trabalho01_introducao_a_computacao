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

def Tamanho(numero):
    tamanho = 0
    for i in numero:
        tamanho += 1
    return tamanho

def Mapeamento(resto):
    if (resto == 'A'):
        return 10
    elif (resto == 'B'):
        return 11
    elif (resto == 'C'):
        return 12
    elif (resto == 'D'):
        return 13
    elif (resto == 'E'):
        return 14
    elif (resto == 'F'):
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

def Em_dec_numero_positivo_par():
    assert Para_decimal("FE") == 254
def Em_dec_numero_positivo_impar():
    assert Para_decimal("311") == 785
def Em_dec_numero_negativo_par():
    assert Para_decimal("-FE") == -254
def Em_dec_numero_negativo_impar():
    assert Para_decimal("-311") == -785
def Em_dec_numero_nulo():
    assert Para_decimal("0") == 0

def Testes():
    print(("-" * 15) + "Teste automatizado" + ("-" * 15))
    print("Teste com a string FE: {}".format(Em_dec_numero_positivo_par()))
    print("Teste com a string 311: {}".format(Em_dec_numero_positivo_impar()))
    print("Teste com a string -FE: {}".format(Em_dec_numero_negativo_par()))
    print("Teste com a string -311: {}".format(Em_dec_numero_negativo_impar()))
    print("Teste com a string 0: {}".format(Em_dec_numero_nulo()))

Testes()
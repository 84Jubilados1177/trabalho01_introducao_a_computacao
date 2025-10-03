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

def Conversor(numero, contador, tam):
    algarismo = numero[0];
    total = Mapeamento(algarismo) * (16 ** (tam - contador))
    
    print("".format(Para_decimal("A11")))
    return total

def Para_decimal(numero):
    negativo = False
    resto = 0
    decimal = 0
    cont = 0
    
    if(numero[0] == '-'):
        numero = numero[1:]    
        negativo = True


    while numero != "":
        tam = Tamanho(numero)
        decimal += Conversor(numero, cont, tam);
        numero = numero[1:]
        print(numero)
        cont += 1

    if (negativo == True):
        return ("-" + decimal)
    
    return decimal


print("{}".format(Para_decimal("A11")))

def Em_dec_numero_positivo_par():
    assert Para_decimal(254) == "FE"
def Em_dec_numero_positivo_impar():
    assert Para_decimal(785) == "311"
def Em_dec_numero_negativo_par():
    assert Para_decimal(-254) == "-FE"
def Em_dec_numero_negativo_impar():
    assert Para_decimal(-785) == "-311"
def Em_dec_numero_nulo():
    assert Para_decimal(0) == "0"

def Testes():
    print("-----------Teste automatizado------------")
    print("Teste com o numero 254: {}".format(Em_dec_numero_positivo_par()))
    print("Teste com o numero 785: {}".format(Em_dec_numero_positivo_impar()))
    print("Teste com o numero -254: {}".format(Em_dec_numero_negativo_par()))
    print("Teste com o numero -785: {}".format(Em_dec_numero_negativo_impar()))
    print("Teste com o numero 0: {}".format(Em_dec_numero_nulo()))

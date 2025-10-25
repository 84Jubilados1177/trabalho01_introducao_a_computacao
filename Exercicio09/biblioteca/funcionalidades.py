def Confere_numero(numero):
    try:
        float(numero)
        return True
    except ValueError:
        return False
    
def Confere_binario_flutuante(numero):
    caracteres = ['0', '1', '.', '-']
    num = numero
    octal = True
    for i in num:
        if not(i in caracteres):
            octal = False
    return octal

def binfrac_to_dec(b):
    negativo = False

    if (b[0] == '-'):
        negativo = True
        b = b[1:]

    if '.' in b:
        parte_inteira, parte_fracionaria = b.split('.')
    else:
        parte_inteira, parte_fracionaria = b, ""

    for c in parte_inteira + parte_fracionaria:
        if c not in "01":
            return None

    val_int = 0
    pot = 0
    for i in range(len(parte_inteira) - 1, -1, -1):
        if parte_inteira[i] == '1':
            val_int += 2 ** pot
        pot += 1

    val_frac = 0
    pot = -1
    for c in parte_fracionaria:
        if c == '1':
            val_frac += 2 ** pot
        pot -= 1

    resultado = val_int + val_frac

    if negativo:
        resultado *= -1

    return resultado

def Teste1():
    assert binfrac_to_dec("1010.101") == 10.625
def Teste2():
    assert binfrac_to_dec("-0.01") == -0.25
def Teste3():
    assert binfrac_to_dec("1101") == 13
def Teste4():
    assert binfrac_to_dec("0") == 0

def Testes():
    print(("-" * 15) + "Teste automatizado" + ("-" * 15))
    print("Binário -> Decimal")
    print("String \"1010.101\" para Real 10.625: {}".format(Teste1()))
    print("String \"-0.01\" para Real -0.25: {}".format(Teste2()))
    print("String \"13\" para Real 1101: {}".format(Teste3()))
    print("String \"0\" para Real 0: {}".format(Teste4()))
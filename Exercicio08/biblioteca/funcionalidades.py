def Confere_numero(numero):
    try:
        float(numero)
        return True
    except ValueError:
        return False

def Algarismo(numero):
    return numero % 2

def Em_binario(numero):
    binario = ""
    num = abs(int(numero))

    if num == 0:
        binario = "0"

    while num > 0:
        binario = str(int(Algarismo(num))) + binario
        num //= 2

    if numero < 0:
        binario = "-" + binario

    return binario

def Ponto_flutuante_binario(numero, max_frac_bits = 16):
    parte_inteira = int(numero)
    parte_fracionaria = abs(numero - parte_inteira)
    binario_inteiro = Em_binario(parte_inteira)

    binario_fracionaria = ""
    contador = 0

    while parte_fracionaria != 0 and contador < max_frac_bits:
        parte_fracionaria *= 2
        alg = int(parte_fracionaria)
        binario_fracionaria += str(alg)
        parte_fracionaria -= alg
        contador += 1

    if binario_fracionaria == "":
        return str(binario_inteiro)
    else:
        return f"{binario_inteiro}.{binario_fracionaria}"

def Teste1():
    assert Ponto_flutuante_binario(13) == "1101"
def Teste2():
    assert Ponto_flutuante_binario(10.625, 8) == "1010.101"
def Teste3():
    r = Ponto_flutuante_binario(0.1, 10)
    assert r.startswith("0.") and len(r.split(".")[1]) == 10
def Teste4():
    assert Ponto_flutuante_binario(0) == "0"

def Testes():
    print(("-" * 15) + " Teste automatizado " + ("-" * 15))
    print("Decimal fracionário -> Binário fracionário")
    print("Real 13 para String \"1101\" : {}".format(Teste1()))
    print("Real 10.625 para String \"1010.101\" : {}".format(Teste2()))
    print("Real 0.1 para String truncada 10 bits: {}".format(Teste3()))
    print("Real 0 para String \"0\" : {}".format(Teste4()))

Testes()
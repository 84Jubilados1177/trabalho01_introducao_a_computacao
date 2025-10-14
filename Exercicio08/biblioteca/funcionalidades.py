#from bibli_banco.banco_de_dados import Mapeamento, Mapeamento_inverso

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

def Ponto_flutuante_binario(numero):
    parte_inteira = int(numero)
    parte_fracionaria = abs(numero - parte_inteira) 
    
    # Converte parte inteira
    binario_inteiro = Em_binario(parte_inteira)
    
    # Converte parte fracionária
    binario_fracionaria = ""
    contador = 0

    while parte_fracionaria != 0 and contador < 16:
        parte_fracionaria *= 2
        alg = int(parte_fracionaria)
        binario_fracionaria += str(alg)
        parte_fracionaria -= alg
        contador += 1

    if binario_fracionaria == "":
        return str(binario_inteiro)
    else:
        return f"{binario_inteiro}.{binario_fracionaria}"

def Em_dec_numero_positivo_par():
    assert Ponto_flutuante_binario(13) == "1101"
def Em_dec_numero_positivo_impar():
    assert Ponto_flutuante_binario(14.625) == "1110.101"
def Em_dec_numero_negativo_par():
    assert Ponto_flutuante_binario(-13) == "-1101"
def Em_dec_numero_negativo_impar():
    assert Ponto_flutuante_binario(-14.625) == "-1110.101"
def Em_dec_numero_nulo():
    assert Ponto_flutuante_binario(0) == "0"

def Testes():
    print(("-" * 15) + "Teste automatizado" + ("-" * 15))
    print("Teste com a string FE: {}".format(Em_dec_numero_positivo_par()))
    print("Teste com a string 311: {}".format(Em_dec_numero_positivo_impar()))
    print("Teste com a string -FE: {}".format(Em_dec_numero_negativo_par()))
    print("Teste com a string -311: {}".format(Em_dec_numero_negativo_impar()))
    print("Teste com a string 0: {}".format(Em_dec_numero_nulo()))

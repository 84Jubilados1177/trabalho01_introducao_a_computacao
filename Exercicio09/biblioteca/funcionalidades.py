#from bibli_banco.banco_de_dados import Mapeamento, Mapeamento_inverso

def Confere_numero(numero):
    try:
        float(numero)
        return True
    except ValueError:
        return False

def Binario_flutuante_para_decimal(numero):
    negativo = False

    # Verifica sinal
    if numero[0] == '-':
        negativo = True
        numero = numero[1:]

    # Separa parte inteira e fracionária
    if '.' in numero:
        parte_inteira, parte_fracionaria = numero.split('.')
    else:
        parte_inteira, parte_fracionaria = numero, ""

    # Validação básica
    for c in parte_inteira + parte_fracionaria:
        if c not in "01":
            return None

    # Parte inteira
    val_int = 0
    pot = 0
    for i in range(len(parte_inteira) - 1, -1, -1):
        val_int += (parte_inteira[i] == '1') * (2 ** pot)
        pot += 1

    # Parte fracionária
    val_frac = 0
    pot = -1
    for c in parte_fracionaria:
        val_frac += (c == '1') * (2 ** pot)
        pot -= 1

    if(negativo):
        return  ((val_int + val_frac)*-1)
    
    return (val_int + val_frac)

def Em_dec_numero_positivo_par():
    assert Binario_flutuante_para_decimal(13) == "1101"
def Em_dec_numero_positivo_impar():
    assert Binario_flutuante_para_decimal(14.625) == "1110.101"
def Em_dec_numero_negativo_par():
    assert Binario_flutuante_para_decimal(-13) == "-1101"
def Em_dec_numero_negativo_impar():
    assert Binario_flutuante_para_decimal(-14.625) == "-1110.101"
def Em_dec_numero_nulo():
    assert Binario_flutuante_para_decimal(0) == "0"

def Testes():
    print(("-" * 15) + "Teste automatizado" + ("-" * 15))
    print("Teste com a string FE: {}".format(Em_dec_numero_positivo_par()))
    print("Teste com a string 311: {}".format(Em_dec_numero_positivo_impar()))
    print("Teste com a string -FE: {}".format(Em_dec_numero_negativo_par()))
    print("Teste com a string -311: {}".format(Em_dec_numero_negativo_impar()))
    print("Teste com a string 0: {}".format(Em_dec_numero_nulo()))
    
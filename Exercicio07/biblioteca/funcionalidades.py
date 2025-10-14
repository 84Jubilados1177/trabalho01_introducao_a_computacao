from bibli_banco.banco_de_dados import Mapeamento, Mapeamento_inverso

def Confere_decimal(numero):
    try:
        int(numero)
        return True
    except ValueError:
        return False

def Transforma_em_decimal(base, numero):
    negativo = False
    if(numero[0] == "-"):
        numero = numero[1:]
        negativo = True
    num_decimal = 0
    cont = len(numero)-1

    for i in numero:
        num_decimal += Mapeamento(i) * pow(base, cont)
        cont -= 1
    
    if(negativo):
        num_decimal*= -1

    return num_decimal

def Resto_divisao_inteira(numero, base):
    return (numero % base)

def Divisao_inteira(numero, base):
    return (numero // base)

def Transforma_bases(numero, base_ini, base_fin):
    num = Transforma_em_decimal(base_ini, numero)
    num_final = ""
    negativo = 0

    if numero[0] == '-':
        negativo = True
        num *= -1

    if num == 0:
        num_final = Mapeamento_inverso(num)

    while num != 0:
        num_final = Mapeamento_inverso(Resto_divisao_inteira(num, base_fin)) + num_final
        num -= Resto_divisao_inteira(num, base_fin)
        num //= base_fin
    
    if(negativo):
        num_final = "-" + num_final

    return num_final 


def Em_dec_numero_positivo_par():
    assert Transforma_bases("1101", 2, 16) == "D"
def Em_dec_numero_positivo_impar():
    assert Transforma_bases("-7B", 16, 8) == "-173"
def Em_dec_numero_negativo_par():
    assert Transforma_bases("zzz", 36, 10) == "46655"
def Em_dec_numero_negativo_impar():
    assert Transforma_bases("-zzz", 36, 10) == "-46655"
def Em_dec_numero_nulo():
    assert Transforma_bases("0", 15, 10) == "0"

def Testes():
    print(("-" * 15) + "Teste automatizado" + ("-" * 15))
    print("Teste com a string FE: {}".format(Em_dec_numero_positivo_par()))
    print("Teste com a string 311: {}".format(Em_dec_numero_positivo_impar()))
    print("Teste com a string -FE: {}".format(Em_dec_numero_negativo_par()))
    print("Teste com a string -311: {}".format(Em_dec_numero_negativo_impar()))
    print("Teste com a string 0: {}".format(Em_dec_numero_nulo()))

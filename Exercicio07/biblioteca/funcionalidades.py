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


def Teste1():
    assert Transforma_bases("1101", 2, 16) == "D"
def Teste2():
    assert Transforma_bases("-7B", 16, 8) == "-173"
def Teste3():
    assert Transforma_bases("zzz", 36, 10) == "46655"
def Teste4():
    assert Transforma_bases("0", 20, 10) == "0"

def Testes():
    print(("-" * 15) + " Teste automatizado " + ("-" * 15))
    print("Base (2-36) -> Base (2-36)")
    print("String \"1101\" de base 2 para String \"D\" de base 16: {}".format(Teste1()))
    print("String \"-7B\" de base 16 para String \"-173\" de base 8: {}".format(Teste2()))
    print("String \"zzz\" de base 36 para String \"46655\" de base 10: {}".format(Teste3()))
    print("String \"0\" de base 20 para String \"0\" de base 10: {}".format(Teste4()))
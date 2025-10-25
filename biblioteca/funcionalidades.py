from banco_de_dados.data_base import Mapeamento, Mapeamento_inverso, Mapeamento16, MapeamentoInverso16

# ------------------ ALGARISMOS ---------------------

# Exclusivo para conversão em binário
def Algarismo2(numero):
    return numero%2

# Exclusivo para conversão em octal
def Algarismo8(numero):
    return numero%8

# Exclusivo para conversão em decimal
def Algarismo10(numero):
    return numero%10

def Algarismo16(numero):
    return numero%16

# ---------------- CONFERÊNCIAS --------------------

def Confere_numero(numero):
    try:
        float(numero)
        return True
    except ValueError:
        return False

def Tamanho(numero):
    tamanho = 0
    for i in numero:
        tamanho += 1
    return tamanho

def Confere_binario_inteiro_str(numero):
    for i in numero:
        if(i != '0' and i != '1' and i != '-'):
            return False
    return True

def Confere_binario_flutuante_str(numero):
    caracteres = ['0', '1', '.', '-']
    num = numero
    octal = True
    for i in num:
        if not(i in caracteres):
            octal = False
    return octal


def Confere_octal_str(numero):
    caracteres = ['0', '1', '2', '3', '4', '5', '6', '7', '-']
    num = numero
    octal = True
    for i in num:
        if not(i in caracteres):
            octal = False
    return octal

#Confere se o número é um número decimal inteiro
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

# --------------- QUOCIENTE ------------------------

def Quociente16(numero):
    quociente = numero
    quociente //= 16
    return quociente

# --------------- AUXILIARES -----------------------

def Conversor(numero, tamanho):
    algarismo = numero[0];
    total = MapeamentoInverso16(algarismo) * (16 ** tamanho)
    return total

def Resto_divisao_inteira(numero, base):
    return (numero % base)

def Divisao_inteira(numero, base):
    return (numero // base)

# --------------- CONVERSÕES -----------------------

# Converte um número inteiro em uma String Binária
def Em_binario(numero):
    binario = ""
    num = abs(int(numero))

    if num == 0:
        binario = "0"

    while num > 0:
        binario = str(int(Algarismo2(num))) + binario
        num //= 2

    if numero < 0:
        binario = "-" + binario

    return binario

# Converte um um inteiro (decimal) uma string octal
def Em_octal_str(numero, base):
    negativo = False
    dec = 0
    cont = 0

    if(numero < 0):
        negativo = True  
        numero *= -1
    
    num = int(numero)
    

    while(num != 0):
        alg = Algarismo8(num)
        num -= alg
        num //= 8
        dec += alg*pow(base, cont)
        cont += 1
    
    if(negativo):
        return ("-" + str(dec))
    else:
        return str(dec)

def Para_decimal_base_8(numero):
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

def Para_decimal_base_16(numero):
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

def Para_hexadecimal(numero):
    negativo = False
    resto = 0
    quociente = numero     
    hexadecimal = "" 
    
    if (numero < 0):
        negativo = True
        quociente *= -1

    if (quociente == 0):
        hexadecimal = "0"

    while quociente != 0:
        resto = Algarismo16(quociente)
        quociente = Quociente16(quociente) 
        hexadecimal = Mapeamento16(resto) + hexadecimal

    if (negativo == True):
        return ("-" + hexadecimal)
    return hexadecimal


# Converte uma String binária em um inteiro decimal
def Em_decimal(numero, base):
    negativo = False
    dec = 0
    cont = 0

    if(numero[0] == "-"):
        numero = numero[1:] 
        negativo = True  
    
    num = int(numero)
    

    while(num != 0):
        alg = Algarismo10(num)
        num -= alg
        num //= 10
        dec += alg*pow(base, cont)
        cont += 1
    
    if(negativo):
        return (dec*-1)
    else:
        return dec
    
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

    decimal = val_int + val_frac

    if negativo:
        decimal *= -1

    return decimal

    
# -------------------- TESTES -----------------------

def Teste1_1():
    assert Em_binario(8) == "1000"
def Teste1_2():
    assert Em_binario(0) == "0"
def Teste1_3():
    assert Em_binario(-8) == "-1000"

def TestesQ1():
    print(("-" * 15) + " Teste automatizado " + ("-" * 15))
    print("Decimal -> Binário")
    print("Inteiro 13 para String \"1101\": {}".format(Teste1_1()))
    print("Inteiro 0 para String \"0\": {}".format(Teste1_2()))
    print("Inteiro -8 para String \"-1000\": {}".format(Teste1_3()))

def Teste2_1():
    assert Em_decimal("1101", 2) == 13
def Teste2_2():
    assert Em_decimal("-1000", 2) == -8
def Teste2_3():
    assert Em_decimal("0", 2) == 0

def TestesQ2():
    print(("-" * 16) + "Teste automatizado" + ("-" * 16))
    print("Binário -> Decimal")
    print("String \"1101\" para o Inteiro 13: {}".format(Teste2_1()))
    print("String \"-1000\" para o Inteiro -8: {}".format(Teste2_2()))
    print("String \"0\" para o Inteiro 0: {}".format(Teste2_3()))

def Teste3_1():
    assert Em_octal_str(93, 10) == "135"
def Teste3_2():
    assert Em_octal_str(-64, 10) == "-100"
def Teste3_3():
    assert Em_octal_str(0, 10) == "0"

def TestesQ3():
    print(("-" * 16) + "Teste automatizado" + ("-" * 16))
    print("Decimal -> Octal")
    print("Inteiro 93 para String \"135\": {}".format(Teste3_1()))
    print("Inteiro -64 para String \"-100\": {}".format(Teste3_2()))
    print("Inteiro 0 para String \"0\": {}".format(Teste3_3()))


def Teste4_1():
    assert Para_decimal_base_8("135") == 93
def Teste4_2():
    assert Para_decimal_base_8("-100") == -64
def Teste4_3():
    assert Para_decimal_base_8("0") == 0

def TestesQ4():
    print(("-" * 16) + "Teste automatizado" + ("-" * 16))
    print("Octal -> Decimal")
    print("String \"135\" para o inteiro 93: {}".format(Teste4_1()))
    print("String \"-100\" para o inteiro -64: {}".format(Teste4_2()))
    print("String \"0\" para o inteiro 0: {}".format(Teste4_3()))

def Teste5_1():
    assert Para_hexadecimal(255) == "FF"
def Teste5_2():
    assert Para_hexadecimal(4095) == "FFF"
def Teste5_3():
    assert Para_hexadecimal(-26) == "-1A"
def Teste5_4():
    assert Para_hexadecimal(0) == "0"

def TestesQ5():
    print(("-" * 15) + " Teste automatizado " + ("-" * 15))
    print("Decimal -> Hexadecimal")
    print("Inteiro 255 para String \"FF\": {}".format(Teste5_1()))
    print("Inteiro 4095 para String \"FFF\": {}".format(Teste5_2()))
    print("Inteiro -26 para String \"-1A\": {}".format(Teste5_3()))
    print("Inteiro 0 para String \"0\": {}".format(Teste5_4()))

def Teste6_1():
    assert Para_decimal_base_16("FF") == 255
def Teste6_2():
    assert Para_decimal_base_16("fff") == 4095
def Teste6_3():
    assert Para_decimal_base_16("-1A") == -26
def Teste6_4():
    assert Para_decimal_base_16("0") == 0

def TestesQ6():
    print(("-" * 15) + " Teste automatizado " + ("-" * 15))
    print("Hexadecimal -> Decimal")
    print("String \"FF\" para o Inteiro 255: {}".format(Teste6_1()))
    print("String \"fff\" para o Inteiro 4095: {}".format(Teste6_2()))
    print("String \"-1A\" para o Inteiro -26: {}".format(Teste6_3()))
    print("String \"0\" para o Inteiro 0: {}".format(Teste6_4()))

def Teste7_1():
    assert Transforma_bases("1101", 2, 16) == "D"
def Teste7_2():
    assert Transforma_bases("-7B", 16, 8) == "-173"
def Teste7_3():
    assert Transforma_bases("zzz", 36, 10) == "46655"
def Teste7_4():
    assert Transforma_bases("0", 20, 10) == "0"

def TestesQ7():
    print(("-" * 15) + " Teste automatizado " + ("-" * 15))
    print("Base (2-36) -> Base (2-36)")
    print("String \"1101\" de base 2 para String \"D\" de base 16: {}".format(Teste7_1()))
    print("String \"-7B\" de base 16 para String \"-173\" de base 8: {}".format(Teste7_2()))
    print("String \"zzz\" de base 36 para String \"46655\" de base 10: {}".format(Teste7_3()))
    print("String \"0\" de base 20 para String \"0\" de base 10: {}".format(Teste7_4()))

def Teste8_1():
    assert Ponto_flutuante_binario(13) == "1101"
def Teste8_2():
    assert Ponto_flutuante_binario(10.625, 8) == "1010.101"
def Teste8_3():
    r = Ponto_flutuante_binario(0.1, 10)
    assert r.startswith("0.") and len(r.split(".")[1]) == 10
def Teste8_4():
    assert Ponto_flutuante_binario(0) == "0"

def TestesQ8():
    print(("-" * 15) + " Teste automatizado " + ("-" * 15))
    print("Decimal fracionário -> Binário fracionário")
    print("Real 13 para String \"1101\" : {}".format(Teste8_1()))
    print("Real 10.625 para String \"1010.101\" : {}".format(Teste8_2()))
    print("Real 0.1 para String truncada 10 bits: {}".format(Teste8_3()))
    print("Real 0 para String \"0\" : {}".format(Teste8_4()))
    
def Teste9_1():
    assert binfrac_to_dec("1010.101") == 10.625
def Teste9_2():
    assert binfrac_to_dec("-0.01") == -0.25
def Teste9_3():
    assert binfrac_to_dec("1101") == 13
def Teste9_4():
    assert binfrac_to_dec("0") == 0

def TestesQ9():
    print(("-" * 15) + "Teste automatizado" + ("-" * 15))
    print("Binário -> Decimal")
    print("String \"1010.101\" para Real 10.625: {}".format(Teste9_1()))
    print("String \"-0.01\" para Real -0.25: {}".format(Teste9_2()))
    print("String \"13\" para Real 1101: {}".format(Teste9_3()))
    print("String \"0\" para Real 0: {}".format(Teste9_4()))

# ------------------------ TEXTOS ------------------------------

## Gerais ------------------------------------------------------

def Linha():
    print("-" * 50)

def Saida():
    Linha()
    print("Saindo ...")
    Linha()

## Especícifos -------------------------------------------------

# Intruções

def InstrucoesQ1():
    Linha()
    print("Seja bem-vindo ao conversor para binário!")
    print("Para executar os testes digite a opção desejada:")
    print("0 - Teste automatizado")
    print("1 - Teste independente")
    print("2 - Sair")

def InstrucoesQ2():
    Linha()
    print("Seja bem-vindo ao conversor para decimal!")
    print("Para executar os testes digite a opção desejada:")
    print("0 - Teste automatizado")
    print("1 - Teste independente")
    print("2 - Sair")

def InstrucoesQ3():
    Linha()
    print("Seja bem-vindo ao conversor para octal!")
    print("Para executar os testes digite a opção")
    print("desejada:")
    print("0 - Teste automatizado")
    print("1 - Teste independente")
    print("2 - Sair")

def InstrucoesQ4():
    Linha()
    print("Seja bem-vindo ao conversor para decimal!")
    print("Para executar os testes digite a opção")
    print("desejada:")
    print("0 - Teste automatizado")
    print("1 - Teste independente")
    print("2 - Sair")

def InstrucoesQ5():
    Linha()
    print("Seja bem-vindo ao conversor para Hexadecimal!")
    print("Para executar os testes digite a opção")
    print("desejada:")
    print("0 - Teste automatizado")
    print("1 - Teste independente")
    print("2 - Sair")

def InstrucoesQ6():
    Linha()
    print("Seja bem-vindo ao conversor para decimal!")
    print("Para executar os testes digite a opção")
    print("desejada:")
    print("0 - Teste automatizado")
    print("1 - Teste independente")
    print("2 - Sair")

def InstrucoesQ7():
    Linha()
    print("Seja bem-vindo ao conversor para Hexadecimal!")
    print("Para executar os testes digite a opção")
    print("desejada:")
    print("0 - Teste automatizado")
    print("1 - Teste independente")
    print("2 - Sair")

def InstrucoesQ8():
    Linha()
    print("Seja bem-vindo ao conversor para binário!")
    print("Para executar os testes digite a opção")
    print("desejada:")
    print("0 - Teste automatizado")
    print("1 - Teste independente")
    print("2 - Sair")

def InstrucoesQ9():
    Linha()
    print("Seja bem-vindo ao conversor para decimal!")
    print("Para executar os testes digite a opção")
    print("desejada:")
    print("0 - Teste automatizado")
    print("1 - Teste independente")
    print("2 - Sair")

# Sentenças

def SentencaQ1():
    print(("-" * 12) + " Conversor para Binário: " + ("-" * 13))

def SentencaQ2():
    print(("-" * 12) + " Conversor para Decimal: " + ("-" * 13))

def SentencaQ3():
    print(("-" * 14) + " Conversor para Octal: " + ("-" * 14))

def SentencaQ4():
    print(("-" * 12) + " Conversor para Decimal: " + ("-" * 13))

def SentencaQ5():
    print((10 * "-") + " Conversor para Hexadecimal: " + ("-" * 11))

def SentencaQ6():
    print(("-" * 12) + " Conversor para Decimal: " + ("-" * 13))

def SentencaQ7():
    print((10 * "-") + " Conversor de Base para Base: " + ("-" * 11))
    
def SentencaQ8():
    print("--------- Conversor para Binário Real: -----------")

def SentencaQ9():
    print("----------- Conversor para Decimal: -------------")


# Mensagens de Erro

def MensagemDeErroQ1(Num_erro):
    if(Num_erro == 1):
        print("-" * 50)
        print("Eu acho que isso não é um número inteiro :(")
        Linha()

    elif(Num_erro == 2):
        print("Entrada inválida, responda com (S/N) ")
        Linha()

    elif(Num_erro == 3):
        Linha()
        print("Entrada inválida, responda com (0, 1 ou 2)")

def MensagemDeErroQ2(Num_erro):
    if(Num_erro == 1):
        print("-" * 50)
        print("Eu acho que isso não é um binário :(")

    elif(Num_erro == 2):
        print("Entrada inválida, responda com (S/N)")
        Linha()

    elif(Num_erro == 3):
        Linha()
        print("Entrada inválida, responda com (0, 1 ou 2)")

def MensagemDeErroQ3(Num_erro):
    if(Num_erro == 1):
        print("-" * 50)
        print("Eu acho que isso não é um decimal :(")

    elif(Num_erro == 2):
        print("Entrada inválida, responda com (S/N)")
        Linha()

    elif(Num_erro == 3):
        Linha()
        print("Entrada inválida, responda com (0, 1 ou 2)")

def MensagemDeErroQ4(Num_erro):
    if(Num_erro == 1):
        Linha()
        print("Eu acho que isso não é um octal :(")
        Linha()

    elif(Num_erro == 2):
        print("Entrada inválida, responda com (S/N) ")
        Linha()

    elif(Num_erro == 3):
        Linha()
        print("Entrada inválida, responda com (0, 1 ou 2)")
        
def MensagemDeErroQ5(Num_erro):
    if(Num_erro == 1):
        print("-" * 50)
        print("Eu acho que isso não é um decimal :(")

    elif(Num_erro == 2):
        print("Entrada inválida, responda com (S/N) ")
        Linha()

    elif(Num_erro == 3):
        Linha()
        print("Entrada inválida, responda com (0, 1 ou 2)")

def MensagemDeErroQ6(Num_erro):
    if(Num_erro == 1):
        Linha()
        print("Eu acho que isso não é um hexadecimal :(")

    elif(Num_erro == 2):
        print("Entrada inválida, responda com (S/N) ")
        Linha()

    elif(Num_erro == 3):
        Linha()
        print("Entrada inválida, responda com (0, 1 ou 2)")

def MensagemDeErroQ7(Num_erro):
    if(Num_erro == 1):
        print("-" * 50)
        print("Eu acho que isso não é um decimal :(")

    elif(Num_erro == 2):
        print("Entrada inválida, responda com (S/N) ")
        Linha()

    elif(Num_erro == 3):
        Linha()
        print("Entrada inválida, responda com (0, 1 ou 2)")

def MensagemDeErroQ8(Num_erro):
    if(Num_erro == 1):
        print("-" * 50)
        print("Eu acho que isso não é um decimal :(")

    elif(Num_erro == 2):
        print("Entrada inválida, responda com (S/N) ")
        Linha()

    elif(Num_erro == 3):
        Linha()
        print("Entrada inválida, responda com (0, 1 ou 2)")
    
def MensagemDeErroQ9(Num_erro):
    if(Num_erro == 1):
        Linha()
        print("Eu acho que isso não é um binário :(")

    elif(Num_erro == 2):
        print("Entrada inválida, responda com (S/N) ")
        Linha()

    elif(Num_erro == 3):
        Linha()
        print("Entrada inválida, responda com (0, 1 ou 2)")
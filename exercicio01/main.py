from biblioteca import *

def Algarismo(numero):
    algarismo = numero%2
    return int (algarismo)

def Completa_zeros(numero):
    num = numero
    zeros = ""
    binario = ""

    while num != 0:
        alg = Algarismo(num)
        binario = str(alg) + binario
        num = int(num/2)

    for i in range(7-len(binario)):
        zeros += "0"

    return zeros

def Em_binario(numero):
    binario = ""
    if numero < 0:
        binario = "1"
    else:
        binario = "0"

    num = numero
    binario = binario +Completa_zeros(num)

    while num != 0:
        alg = Algarismo(num)
        binario = binario + str(alg) 
        num = int(num/2)
        
    return binario

print("\n{}\n".format(Em_binario(-13)))


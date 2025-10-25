from banco_de_dados import Nomes_bases
from biblioteca import *

opcao = 1

while (opcao != 2):
    InstrucoesQ6()
    auxiliar = input().strip()
    
    if(Confere_decimal(auxiliar)):
        opcao = int(auxiliar)
    else:
        opcao = 3 # erro

    if opcao == 0:
        TestesQ6()
    elif opcao == 1:
        continuar = 'S'
        while(continuar != 'N' and continuar != 'n'):
            invalido = True
            while (invalido):
                SentencaQ6()
                numero = input("Digite um número em hexadecimal: ")
                if(Confere_hexadecimal(numero)):
                    print("{} em decimal: {}".format(numero, Para_decimal_base_16(numero)))
                    invalido = False
                    Linha()
                else:
                    MensagemDeErroQ6(1)
                    
            invalido = True
            while(invalido):
                continuar = input("Deseja testar outro número? (S/N) ")
                if(continuar == 'S' or continuar == 's' or continuar == 'N' or continuar == 'n'):
                    invalido = False
                    print(continuar)
                elif(continuar != 'N' or continuar != 'n'):
                    MensagemDeErroQ6(2)

    elif opcao == 2: # Sai do codigo
        Saida()
        continue
    else:
        MensagemDeErroQ6(3)
    

        





from banco_de_dados import Nomes_bases
from biblioteca import *

opcao = 1

while (opcao != 2):
    InstrucoesQ3()
    auxiliar = input().strip()
    
    if(Confere_decimal(auxiliar)):
        opcao = int(auxiliar)
    else:
        opcao = 3 # Erro
    
    if opcao == 0:
        TestesQ3()
    elif opcao == 1:
        continuar = 'S'
        while(continuar != 'N' and continuar != 'n'):
            invalido = True
            while (invalido):
                SentencaQ3()
                numero = input("Digite um número em decimal: ")
                if(Confere_decimal(numero)):
                    print("{} em octal: {}".format(numero, Em_octal_str(int(numero), 10)))
                    invalido = False
                    Linha()
                else:
                    MensagemDeErroQ3(1)
                    
            invalido = True
            while(invalido):
                continuar = input("Deseja testar outro número? (S/N) ")
                if(continuar == 'S' or continuar == 's' or continuar == 'N' or continuar == 'n'):
                    invalido = False
                    print(continuar)
                elif(continuar != 'N' or continuar != 'n'):
                    MensagemDeErroQ3(2)

    elif opcao == 2: # Sai do codigo
        Saida()
        continue
    else:
        MensagemDeErroQ3(3)
    

        





from biblioteca import *
from bibli_textos import *

opcao = 1

while (opcao != 2):
    Instrucoes()
    opcao = int(input().strip())
    
    if opcao == 0:
        Testes()
    elif opcao == 1:
        continuar = 'S'
        while(continuar != 'N' and continuar != 'n'):
            invalido = True
            while (invalido):
                Sentenca()
                numero = input("Digite um número em octal: ")
                if(Confere_octal(numero)):
                    print("{} em Decimal: {}".format(numero, Em_decimal(int(numero), 8)))
                    invalido = False
                    Linha()
                else:
                    Erro(1)
                    
            invalido = True
            while(invalido):
                continuar = input("Deseja testar outro número? (S/N) ")
                if(continuar == 'S' or continuar == 's' or continuar == 'N' or continuar == 'n'):
                    invalido = False
                    print(continuar)
                elif(continuar != 'N' or continuar != 'n'):
                    Erro(2)

    elif opcao == 2: # Sai do codigo
        Saida()
        continue
    else:
        Erro(3)
    

        





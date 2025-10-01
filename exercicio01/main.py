from biblioteca import *
from bibli_textos import *

opcao = 1

while (opcao != 2):
    Instrucoes()
    opcao = int(input())
    
    if opcao == 0:
        Testes()
    elif opcao == 1:
        continuar = 'S'
        while(continuar != 'N' and continuar != 'n'):
            invalido = True
            Sentenca()

            while(invalido):
                numero = input("Digite um número inteiro: ")
                if(Eh_numero_inteiro(numero)):
                    print("{} em binário: {}".format(numero, Em_binario(numero)))
                    Linha()
                    invalido = False
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

        





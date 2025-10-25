from bibli_banco import *
from biblioteca import *
from bibli_textos import *

opcao = -1

while (opcao != 2):
    Instrucoes()
    auxiliar = input().strip()
    
    if(Confere_numero(auxiliar)):
        opcao = int(auxiliar)
    else:
        opcao = 3 # erro

    if opcao == 0:
        Testes()
    elif opcao == 1:
        continuar = 'S'
        while(continuar != 'N' and continuar != 'n'):
            invalido = True
            while (invalido):
                Sentenca()
                numero = input("Digite um número binário real: ")
                if(Confere_binario_flutuante(numero)):
                    print("{} em decimal: {}".format(numero , binfrac_to_dec(numero)))
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
    

        





from bibli_banco import *
from biblioteca import *
from bibli_textos import *

opcao = 1

while (opcao != 2):
    Instrucoes()
    auxiliar = input().strip()
    
    if(Confere_decimal(auxiliar)):
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
                numero = input("Digite um número em qualquer base\nentre 2 e 16: ")
                base_original = int(input("Digite o valor da base do numero que\nacabou de digitar: "))
                base_final = int(input("Digite o valor o da base final para a conversão: "))
                if(numero):
                    print("{} na base {}: {}".format(numero, Nomes_bases(base_final),Transforma_bases(numero, base_original, base_final)))
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
    

        





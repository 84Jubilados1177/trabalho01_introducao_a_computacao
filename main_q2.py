from banco_de_dados import Nomes_bases
from biblioteca import *

opcao = 1

while (opcao != 2):
    InstrucoesQ2()
    auxiliar = input().strip()
    
    if(Confere_decimal(auxiliar)):
        opcao = int(auxiliar)
    else:
        opcao = 3 # erro
    
    if opcao == 0:
        TestesQ2()
    elif opcao == 1:
        continuar = 'S'
        while(continuar != 'N' and continuar != 'n'):
            invalido = True
            while (invalido):
                SentencaQ2()
                numero = input("Digite um número em binário: ")
                if(Confere_binario_inteiro_str(numero)):
                    print("{} em Decimal: {}".format(numero, Em_decimal(numero, 2)))
                    invalido = False
                    Linha()
                else:
                    MensagemDeErroQ2(1)
                    
            invalido = True
            while(invalido):
                continuar = input("Deseja testar outro número? (S/N) ")
                if(continuar == 'S' or continuar == 's' or continuar == 'N' or continuar == 'n'):
                    invalido = False
                    print(continuar)
                elif(continuar != 'N' or continuar != 'n'):
                    MensagemDeErroQ2(2)

    elif opcao == 2: # Sai do codigo
        Saida()
        continue
    else:
        MensagemDeErroQ2(3)
    

        





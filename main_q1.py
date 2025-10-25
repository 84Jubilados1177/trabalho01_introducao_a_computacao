from banco_de_dados import *
from biblioteca import *

opcao = 1

while (opcao != 2):
    InstrucoesQ1()
    auxiliar = input().strip()
    
    if(Confere_decimal(auxiliar)):
        opcao = int(auxiliar)
    else:
        opcao = 3 # erro
    
    if opcao == 0:
        TestesQ1()
    elif opcao == 1:
        continuar = 'S'
        while(continuar != 'N' and continuar != 'n'):
            invalido = True
            SentencaQ1()
            while(invalido):
                numero = input("Digite um número inteiro: ")
                if(Confere_decimal(numero)):
                    print("{} em binário: {}".format(numero, Em_binario(int(numero))))
                    Linha()
                    invalido = False
                else:
                    MensagemDeErroQ1(1)
            invalido = True 
            while(invalido):
                continuar = input("Deseja testar outro número? (S/N)")
                if(continuar == 'S' or continuar == 's' or continuar == 'N' or continuar == 'n'):
                    invalido = False
                    print(continuar)
                elif(continuar != 'N' or continuar != 'n'):
                    MensagemDeErroQ1(2)

    elif opcao == 2: # Sai do codigo
        Saida()
        continue
    else:
        MensagemDeErroQ1(3)

        





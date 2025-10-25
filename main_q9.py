from banco_de_dados import Nomes_bases
from biblioteca import *

opcao = -1

while (opcao != 2):
    InstrucoesQ9()
    auxiliar = input().strip()
    
    if(Confere_numero(auxiliar)):
        opcao = int(auxiliar)
    else:
        opcao = 3 # erro

    if opcao == 0:
        TestesQ9()
    elif opcao == 1:
        continuar = 'S'
        while(continuar != 'N' and continuar != 'n'):
            invalido = True
            while (invalido):
                SentencaQ9()
                numero = input("Digite um número binário real: ")
                if(Confere_binario_flutuante_str(numero)):
                    print("{} em decimal: {}".format(numero , binfrac_to_dec(numero)))
                    invalido = False
                    Linha()
                else:
                    MensagemDeErroQ9(1)
            invalido = True
            while(invalido):
                continuar = input("Deseja testar outro número? (S/N) ")
                if(continuar == 'S' or continuar == 's' or continuar == 'N' or continuar == 'n'):
                    invalido = False
                    print(continuar)
                elif(continuar != 'N' or continuar != 'n'):
                    MensagemDeErroQ9(2)

    elif opcao == 2: # Sai do codigo
        Saida()
        continue
    else:
        MensagemDeErroQ9(3)
    

        





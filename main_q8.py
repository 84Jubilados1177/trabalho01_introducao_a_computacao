from banco_de_dados import Nomes_bases
from biblioteca import *
opcao = 1

while (opcao != 2):
    InstrucoesQ8()
    auxiliar = input().strip()
    
    if(Confere_numero(auxiliar)):
        opcao = int(auxiliar)
    else:
        opcao = 3 # Erro

    if opcao == 0:
        TestesQ8()
    elif opcao == 1:
        continuar = 'S'
        while(continuar != 'N' and continuar != 'n'):
            invalido = True
            while (invalido):
                SentencaQ8()
                numero = input("Digite um número decimal real: ")
                if(Confere_numero(numero)):
                    print("{} em binário: {}".format(numero , Ponto_flutuante_binario(float(numero))))
                    invalido = False
                    Linha()
                else:
                    MensagemDeErroQ8(1)
                    
            invalido = True
            while(invalido):
                continuar = input("Deseja testar outro número? (S/N) ")
                if(continuar == 'S' or continuar == 's' or continuar == 'N' or continuar == 'n'):
                    invalido = False
                    print(continuar)
                elif(continuar != 'N' or continuar != 'n'):
                    MensagemDeErroQ8(2)

    elif opcao == 2: # Sai do codigo
        Saida()
        continue
    else:
        MensagemDeErroQ8(3)
    

        





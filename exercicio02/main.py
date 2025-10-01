from biblioteca import *

opcao = 1

while (opcao != 2):
    Instrucoes()
    opcao = int(input())
    
    if opcao == 0:
        Testes()
    if opcao == 1:
        continuar = 'S'
        while(continuar != 'N' and continuar != 'n'):
            invalido = True
            print("--------Conversor para Decimal:----------")
            numero = int(input("Digite um número em binário: "))
            print("{} em Decimal: {}".format(numero, Em_decimal(numero, 2)))
            print("-----------------------------------------")

            while(invalido):
                continuar = input("Deseja testar outro número? (S/N) ")
                if(continuar == 'S' or continuar == 's' or continuar == 'N' or continuar == 'n'):
                    invalido = False
                    print(continuar)
                elif(continuar != 'N' or continuar != 'n'):
                    print("Entrada inválida, responda com (S/N) ")
                    print("-----------------------------------------")

    elif opcao == 2: # Sai do codigo
        print("-----------------------------------------")
        print("saindo ...")
        print("-----------------------------------------")
        continue
    else:
        print("-----------------------------------------")
        print("Entrada inválida, responda com (0, 1 ou 2)")

        





# trabalho01_introducao_a_computacao
### Dados dos integrantes:
**Alunos:** 
> Isabel Valadares Pessoa

> Pablo dos Santos Martins

**Semestre:** 2025/2

**Turma:** 10A - Bacharelado em Ciência da Computação

**Disciplina:** Introdução à Computação

****
**Versão do Python:** 3.13.7

Para testar cada um dos códigos referentes às suas respectivas questões, compilar o arquivo main.py na própria pasta em que ele se localiza e seguir as instruções que aparecerem no terminal.
A seguir, um exemplo sobre como seguir tais instruções:

## Menu:
    --------------------------------------------------
    Seja bem-vindo ao conversor para binário!
    Para executar os testes digite a opção desejada:
    0 - Teste automatizado
    1 - Teste independente
    2 - Sair

Nesse caso o usuário deve escolher uma opção, sendo ela:

0. Um teste automatizado rápido com entradas diversas predefinidas pelo próprio professor para agilizar a verificação do requerido na atividade.
1. Um teste personalizado podendo ser utilizado para testar com mais precisão possíveis entradas que não estejam preciamente explicitadas no enunciado da atividade.
2. Encerra o código logo apos a mensagem "Saindo ..."

## Caso 0:
Será impresso na tela o descrito na opção 0 do menu:

    --------------- Teste automatizado ---------------
    Inteiro 13 para String "1101": None
    Inteiro 0 para String "0": None
    Inteiro 0 para String "-1000": None

A informação "None" encontrada logo após cada um dos testes, singnifica que não houve nenhum erro durante a execução utilizando as entradas indicadas.

Imediatamente após o teste, o menu será reimpresso para que o usuário possa continuar explorando o programa.

## Caso 1:
Será impresso na tela um enunciado solicitando um valor ao usuário:

    ------------ Conversor para Binário: -------------
    Digite um número inteiro:

Esse valor pode ter base decimal, binária, exadecimal ou qualquer base entre 0 e 36 dependendo do código avaliado. O enunciado de cada código também é diferente diante da base exigida pelo exercício.

    ------------ Conversor para Binário: -------------
    Digite um número inteiro: 13  
    13 em binário: 1101
    --------------------------------------------------
    Deseja testar outro número? (S/N)

Após enviar o solicitado para o programa, será imediatamente impresso na tela o seu correspondente na base explicitada pelo enunciado.

Além disso será questionado ao usuário se este deseja testar outro número.

1. caso o usuário responda "s" ou "S" a função de conversão para a base do exercício será reativada.
2. caso o usuário responda "n" ou "N" o usuário será redirecionado ao menu.

## Caso 2:
O programa será encerrado após a seguinte mensagem:

    --------------------------------------------------
    saindo ...
    --------------------------------------------------

****

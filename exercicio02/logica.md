## Exercício 2 — 
### Binário → Decimal inteiro (método posicional) (3 pts)
**Tarefa:** 
Implemente (que converte uma string binária (com opcional-) para inteiro decimal)
> bin_to_dec(b: str) -> int 

**Regras:**
1. Valide que b contenha apenas 0 e 1 (ignorando um -    inicial).
2. Use potências de 2 e soma posicional (nada de int(b, 2)).

    Exemplos:
    > bin_to_dec("1101") → 13
    
    > bin_to_dec("-1000") → -8
    
    > bin_to_dec("0") → 0

**Critérios (3 pts):**
- Validação (1), 
- algoritmo posicional (1), 
- cobertura de sinal/zero (1).
**** 
**Variáveis:**
> int inteiro_decimal, algarismo[n];


**Fórmula:**
> algarismo(N) = Resto(numero/2);

> numero = (numero/2);

. 

> algasrismo(N-1) = Resto(numrero/2);

> numero = (numero/2)

.

> algasrismo(N-2) = Resto(numrero/2);

> numero = (numero/2)

.
.
.

> algarismo(3) = Resto(numero/2);

> numero = (numero/2);

.

> algasrismo(2) = Resto(numrero/2);

> numero = (numero/2)

.

> algasrismo(1) = Resto(numrero/2);

> numero = (numero/2)

**Observações:** Talvez o ideal seja criar uma função para calcular e outra para concatenar os algarismos calculados separadamente.
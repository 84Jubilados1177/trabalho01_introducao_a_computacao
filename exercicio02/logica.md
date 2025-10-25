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
> decimal = 0;

> potência = 1; // começa valendo 2^0

.

> algarismo(último) = binario[posição final];

> decimal = decimal + (algarismo * potência);

> potência = potência * 2;

.

> algarismo(último - 1) = binario[posição final - 1];

> decimal = decimal + (algarismo * potência);

> potência = potência * 2;

.

> algarismo(último - 2) = binario[posição final - 2];

> decimal = decimal + (algarismo * potência);

> potência = potência * 2;

.
.
.

> algarismo(2) = binario[1];

> decimal = decimal + (algarismo * potência);

> potência = potência * 2;

.

> algarismo(1) = binario[0];

> decimal = decimal + (algarismo * potência);

> potência = potência * 2;

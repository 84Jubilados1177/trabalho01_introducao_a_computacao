## Exercício 4 — 
### Octal → Decimal inteiro (2 pts)
**Tarefa:** Implemente oct_to_dec(o: str) -> int usando soma posicional em base 8.

**Validação:** 
1. caracteres válidos: 0–7
2. -inicial.

    Exemplos:
> oct_to_dec("135") → 93

> oct_to_dec("-100") → -64

**Critérios (2 pts):**
- Correção + validação (2).

**** 

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
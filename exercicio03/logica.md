## Exercício 3 — 
### Decimal inteiro → Octal (3 pts)

**Tarefa:** Implemente dec_to_oct(n: int) -> str via divisões sucessivas por 8.

Exemplos:
> dec_to_oct(93) → "135"

> dec_to_oct(-64) → "-100"

**Critérios (3 pts):**
- Correção (2), 
- negativos/zero (1).

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
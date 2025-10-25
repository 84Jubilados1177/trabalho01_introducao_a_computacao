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
> octal = 0;

> multiplicador = 1; // representa a posição do dígito (1, 10, 100, …)

.

> resto = decimal % 8;

> decimal = decimal // 8;

> octal = octal + resto * multiplicador;

> multiplicador = multiplicador * 10;

.

> resto = decimal % 8;

> decimal = decimal // 8;

> octal = octal + resto * multiplicador;

> multiplicador = multiplicador * 10;

.

> resto = decimal % 8;

> decimal = decimal // 8;

> octal = octal + resto * multiplicador;

> multiplicador = multiplicador * 10;

.
.
.

> resto = decimal % 8;

> decimal = decimal // 8;

> octal = octal + resto * multiplicador;

> multiplicador = multiplicador * 10;
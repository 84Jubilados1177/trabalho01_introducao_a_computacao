
## Exercício 5 — 
### Decimal inteiro → Hexadecimal (com letras maiúsculas) (3 pts)
**Tarefa:** Implemente: (Use dígitos 0–9 e A–F.)
> dec_to_hex(n: int) -> str via divisões por 16. 

Exemplos:
>  dec_to_hex(255) → "FF"

> dec_to_hex(4095) → "FFF"


> dec_to_hex(-26) → "-1A"

**Critérios (3 pts):**
- Correção (2), 
- mapeamento 10→A … 15→F (1).
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
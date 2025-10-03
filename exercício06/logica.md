## Exercício 6 — 
### Hexadecimal → Decimal inteiro (3 pts)
**Tarefa:** Implemente: (Aceite letras maiúsculas ou minúsculas normalizando internamente.)
> hex_to_dec(h: str) -> int. 

**Validação:** 
- caracteres válidos: 0–9, A–F/a–f, 
- -inicial.

Exemplos:
> hex_to_dec("FF") → 255

> hex_to_dec("fff") → 4095

> hex_to_dec("-1A") → -26

**Critérios (3 pts):**
- Correção (2), 
- case-insensitive + validação (1).

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
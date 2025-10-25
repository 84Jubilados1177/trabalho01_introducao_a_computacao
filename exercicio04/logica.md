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

> decimal = 0;

> valorPosicional = 1; // representa 8^0

.

> algarismo(último) = octal[posição final];

> decimal = decimal + (algarismo * valorPosicional);

> valorPosicional = valorPosicional * 8;

.

> algarismo(último - 1) = octal[posição final - 1];

> decimal = decimal + (algarismo * valorPosicional);

> valorPosicional = valorPosicional * 8;

.

> algarismo(último - 2) = octal[posição final - 2];

> decimal = decimal + (algarismo * valorPosicional);

> valorPosicional = valorPosicional * 8;

.
.
.

> algarismo(2) = octal[1];

> decimal = decimal + (algarismo * valorPosicional);

> valorPosicional = valorPosicional * 8;

.

> algarismo(1) = octal[0];

> decimal = decimal + (algarismo * valorPosicional);

> valorPosicional = valorPosicional * 8;
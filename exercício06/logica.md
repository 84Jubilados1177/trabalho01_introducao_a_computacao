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
> decimal = 0

> negativo = False

.

> se hexadecimal[0] == '-':

> .    hexadecimal = hexadecimal[1:]

> .    negativo = True

.

> tamanho = comprimento(hexadecimal) - 1 // expoente da > potência mais à esquerda

.

> algarismo(1) = hexadecimal[0]

> valor = mapear(algarismo) * (16^tamanho)

> decimal = decimal + valor

> tamanho -= 1

.

> algarismo(2) = hexadecimal[1]

> valor = mapear(algarismo) * (16^tamanho)

> decimal = decimal + valor

> tamanho -= 1

.

> algarismo(3) = hexadecimal[2]

> valor = mapear(algarismo) * (16^tamanho)

> decimal = decimal + valor

> tamanho -= 1

.

.

.

> algarismo(n) = hexadecimal[n-1]

> valor = mapear(algarismo) * (16^tamanho)

> decimal = decimal + valor

> tamanho -= 1

(se o numero for negativo multiplicamos por -1)
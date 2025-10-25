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
> hexadecimal = ""
> negativo = False

.

> se decimal < 0:
>.    decimal *= -1
>.    negativo = True

.

> quociente = decimal

.

> resto = quociente % 16
> quociente = quociente // 16
> algarismo = mapear(resto) // 0–9 ou A–F
> hexadecimal = algarismo + hexadecimal

.

> resto = quociente % 16
> quociente = quociente // 16
> algarismo = mapear(resto)
> hexadecimal = algarismo + hexadecimal

.

> resto = quociente % 16
> quociente = quociente // 16
> algarismo = mapear(resto)
> hexadecimal = algarismo + hexadecimal

.
.
.

(repetir até quociente = 0)
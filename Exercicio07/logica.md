## Exercício 7 —
# Conversão geral base N → base M (sem passar por int(x, base)) (5 pts)
**Tarefa:** Implemente: (que converte números inteiros entre bases de 2 a 36.)
> convert_base(num: str, base_from: int, base_to: int) -> str 

1. Alfabeto: dígitos 0–9 e letras A–Z (ou a–z, trate sem diferença de maiúsculas/minúsculas).
2. Saída sempre com letras maiúsculas.

**Estratégia sugerida:**
1. Converter num para decimal manualmente (algoritmo posicional).
2. Converter do decimal para base_to (divisões sucessivas).
3. Preservar o sinal -.
    
    Exemplos:
> convert_base("1101", 2, 16) → "D"

> convert_base("-7B", 16, 8) → "-173"

> convert_base("zzz", 36, 10) → "46655"

**Validação:**
1. 2 ≤ base_from, base_to ≤ 36
2. caracteres do num devem pertencer ao alfabeto da base_from.

**Critérios (5 pts):**
- Correção geral (3), 
- validação robusta (1), 
- organização/código limpo (1).

**** 

> decimal = 0

> negativo = False

.

> se num[0] == '-':

> .    num = num[1:]

> .    negativo = True

.

> expoente = comprimento(num) - 1 // posição mais à esquerda

.

> algarismo(1) = num[0]

> valor = mapear(algarismo) * (base_from ^ expoente)

> decimal = decimal + valor

> expoente -= 1

.

> algarismo(2) = num[1]

> valor = mapear(algarismo) * (base_from ^ expoente)

> decimal = decimal + valor

> expoente -= 1

.

> algarismo(3) = num[2]

> valor = mapear(algarismo) * (base_from ^ expoente)

> decimal = decimal + valor

> expoente -= 1

.

.

.

(repetir para todos os algarismos do número original)

### Para decimal:

> Conversão de Decimal → base_to (divisões sucessivas)

> resultado = ""

> multiplicador = 1 // opcional, dependendo de como concatenar

.

> resto = decimal % base_to

> decimal = decimal // base_to

> algarismo = mapear_inverso(resto)

> resultado = algarismo + resultado

.

> resto = decimal % base_to

> decimal = decimal // base_to

> algarismo = mapear_inverso(resto)

> resultado = algarismo + resultado

.

.

.

(repetir até decimal = 0)
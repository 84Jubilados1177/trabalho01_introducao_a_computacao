## Exercício 9 — 
### Binário fracionário → Decimal fracionário (3 pts)
**Tarefa:** Implemente:
> binfrac_to_dec(b: str) -> float.

Aceite strings como "1010.101", "0.0001100110", com - opcional. Calcule a soma posicional:
- parte inteira: potências de 2 positivas;
- parte fracionária: potências de 2 negativas (½, ¼, ⅛, …).

Exemplos:
> binfrac_to_dec("1010.101") → 10.625

> binfrac_to_dec("-0.01") → -0.25

**Critérios (3 pts):**
- Correção (2), 
- validação (1).

**** 

> decimal = 0

.

> parte_inteira = antes do ponto

> parte_fracionaria = depois do ponto

.

> expoente_inteiro = 0

(começa do último algarismo da parte inteira e vai aumentando)

> valor_inteiro(N) = algarismo(N) * (2^expoente_inteiro);

> decimal = decimal + valor_inteiro(N);

> expoente_inteiro = expoente_inteiro + 1;

.

> valor_inteiro(N-1) = algarismo(N-1) * (2^expoente_inteiro);

> decimal = decimal + valor_inteiro(N-1);

> expoente_inteiro = expoente_inteiro + 1;

.

.

.

> valor_inteiro(1) = algarismo(1) * (2^expoente_inteiro);

> decimal = decimal + valor_inteiro(1);

> expoente_inteiro = expoente_inteiro + 1;

> expoente_fracionario = -1

(começa do primeiro algarismo depois do ponto e vai diminuindo)

> valor_frac(1) = algarismo(1) * (2^expoente_fracionario);

> decimal = decimal + valor_frac(1);

> expoente_fracionario = expoente_fracionario - 1;

.

> valor_frac(2) = algarismo(2) * (2^expoente_fracionario);

> decimal = decimal + valor_frac(2);

> expoente_fracionario = expoente_fracionario - 1;

.

.

.

> valor_frac(K) = algarismo(K) * (2^expoente_fracionario);

> decimal = decimal + valor_frac(K);

> expoente_fracionario = expoente_fracionario - 1;

> Caso tenha sinal:

se começar com '-':
> decimal = decimal * (-1)
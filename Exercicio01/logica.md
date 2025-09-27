## Exercício 1 —
#### Decimal inteiro → Binário (método das divisões sucessivas) (4 pts)
**Tarefa:** Implemente (que converte um inteiro decimal (positivo, zero ou negativo) para binário sem usar bin().)
> dec_to_bin(n: int) -> str 

**Regras/Detalhes:**

1. Use o método das divisões por 2, acumulando restos.
2.  Preserve o sinal: -13 → -1101.
3. Casos especiais: 0 deve retornar "0".

    Exemplos:
    > dec_to_bin(13) → "1101"

    > dec_to_bin(0) → "0"

    > dec_to_bin(-8) → "-1000"

**Critérios (4 pts):**

- Correção (2), 
- negativos/zero (1), 
- código claro e testável (1).
**** 
**Variáveis:**
> int inteiro_decimal;

**Fórmula:**
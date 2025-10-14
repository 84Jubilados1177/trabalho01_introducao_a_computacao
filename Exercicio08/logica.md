## Exercício 8 — 
### Partes fracionárias: Decimal fracionário → Binário fracionário (4 pts)
**Tarefa:** Implemente:
> decfrac_to_bin(x: float, max_frac_bits: int = 16) -> str.

Converta a parte inteira por divisões por 2 e a parte fracionária pelo método das multiplicações por 2, gerando até max_frac_bits bits após o ponto. 

Arredonde por truncamento (não arredonde para cima).

Exemplos:
> decfrac_to_bin(10.625, max_frac_bits=8) → "1010.101"

> decfrac_to_bin(0.1, max_frac_bits=10) → retorna algo como "0.0001100110" (binário periódico truncado)

**Observações:**
1. Para negativos, 
2. trate o sinal e converta o módulo: -10.5 → "-1010.1".

**Critérios (4 pts):**
- Correção inteiro+fração (2), 
- controle de precisão (1), 
- negativos (1).

**** 


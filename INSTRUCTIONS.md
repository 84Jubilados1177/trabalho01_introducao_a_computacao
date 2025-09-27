# trabalho01_introducao_a_computacao
## Lista de Exercícios — Conversão entre Bases em Python
#### Disciplina: Introdução à Computação
#### Valor total: 30 pontos (+ até 5 pontos bônus opcionais)
#### Entrega: arquivo .py único (ou um pacote com arquivos organizados), seguindo as instruções ao fim.
#### Regras gerais:
1. Salvo onde for explicitamente permitido, não use as funções prontas bin(), oct(), hex() nem int(x, base) para fazer a conversão principal. Você pode usá-las apenas para criar tests de verificação (quando o exercício permitir) e nunca para gerar a saída final exigida no enunciado.
2. Trate entradas inválidas (caracteres fora do alfabeto da base, sinais em posições erradas etc.) com mensagens claras de erro.
3. Onde aplicável, aceite números negativos (base 10) e preserve o sinal - na conversão.
4. Onde houver fração (parte decimal), use ponto como separador (ex.: 10.625).
5. Escreva funções puras (sem input() dentro delas). Se desejar, crie um main() que demonstra o uso.

## Exercício 1 —
#### Decimal inteiro → Binário (método das divisões sucessivas) (4 pts)
**Tarefa:** Implemente (que converte um inteiro decimal (positivo, zero ou negativo) para binário sem usar bin()):
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

## Exercício 2 — 
### Binário → Decimal inteiro (método posicional) (3 pts)
**Tarefa:** 
Implemente (que converte uma string binária (com opcional-) para inteiro decimal)
> bin_to_dec(b: str) -> int 

**Regras:**
1. Valide que b contenha apenas 0 e 1 (ignorando um -    inicial).
2. Use potências de 2 e soma posicional (nada de int(b, 2)).

    Exemplos:
    > bin_to_dec("1101") → 13
    
    > bin_to_dec("-1000") → -8
    
    > bin_to_dec("0") → 0

**Critérios (3 pts):**
- Validação (1), 
- algoritmo posicional (1), 
- cobertura de sinal/zero (1).

## Exercício 3 — 
### Decimal inteiro → Octal (3 pts)

**Tarefa:** Implemente dec_to_oct(n: int) -> str via divisões sucessivas por 8.

Exemplos:
> dec_to_oct(93) → "135"

> dec_to_oct(-64) → "-100"

**Critérios (3 pts):**
- Correção (2), 
- negativos/zero (1).


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

## Exercício 10 — 
### Formatação e largura fixa (ex.: bytes e IPv4) (0–? → 0 pts obrigatórios / tarefa de prática recomendada)
**Tarefa (prática, sem pontuação obrigatória):**
1. Escreva:
    > to_fixed_width_bin(n: int, bits: int) -> str 
    
    que retorna o binário preenchido com zeros à esquerda (ex.: to_fixed_width_bin(5, 8) → "00000101").
2. Construa:
    > ipv4_to_bin(ip: str) -> str 
    
    que recebe "192.168.0.1" e devolve quatro blocos de 8 bits separados por ponto: "11000000.10101000.00000000.00000001".
3. O inverso 
    > bin_to_ipv4(bits: str) -> str.

Use isso para testes e aplicações com os exercícios anteriores.
(Sem pontuação fixa — recomendo como base para desafios bônus abaixo.)

### Desafios Bônus (até +5 pts)
#### B1 (até 2 pts): 
Suporte a bases fracionárias na função geral (Ex. aceitar ponto em num e converter entre bases diferentes com fração, mantendo limite de dígitos fracionários).
#### B2 (até 2 pts): 
Implementar complemento de dois para representar inteiros negativos em largura fixa:
> to_twos_complement(n: int, bits: int) -> str 

> from_twos_complement(b: str) -> int.

#### B3 (1 pt): 
Criar uma CLI simples (python main.py --from 2 --to 16 --num 1101) que chama convert_base.

Entregue um pequeno arquivo README.md explicando como rodar e exemplos.

### Dicas algorítmicas (resumo para os alunos)
- Inteiro → base: dividir por base, guardar resto, repetir com o quociente até zero, inverter os restos.
- Base → inteiro: ler da direita para a esquerda somando dígito * (base^posição).
- Frações:
    - Decimal → base 2: parte fracionária × 2; bit = parte inteira; repita com a nova fração.
    - Base 2 → decimal: somar bit * 2^{-posição} após o ponto.
- Mapeamento de dígitos: 0–9 e A–Z ↔ 0–35.
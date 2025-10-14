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

// --- Etapa 1: Montar uma tabela de conversão ---

Defina tabela_simbolos como:

    '0'→0, '1'→1, '2'→2, '3'→3, '4'→4, '5'→5, '6'→6, '7'→7, '8'→8, '9'→9,
    'A'→10, 'B'→11, 'C'→12, 'D'→13, 'E'→14, 'F'→15,
    'G'→16, 'H'→17, ..., 'Z'→35

// --- Etapa 2: Converter da base de origem para decimal ---

valor_decimal ← 0

para cada caractere c em numero_texto:

    valor_c ← tabela_simbolos[c]       // Ex: 'A' → 10
    valor_decimal ← valor_decimal * base_origem + valor_c

// Agora "valor_decimal" contém o número equivalente em base 10

// --- Etapa 3: Converter do decimal para base de destino ---

se valor_decimal = 0 então

    resultado ← "0"

senão

    restos ← lista vazia
    enquanto valor_decimal > 0 faça
        resto ← valor_decimal MOD base_destino
        valor_decimal ← (valor_decimal - resto) / base_destino
        adicionar resto ao final da lista "restos"
    fim_enquanto

    inverter a lista "restos"

// --- Etapa 4: Converter cada resto para símbolo correspondente ---

    resultado ← texto vazio

    para cada valor em "restos":
        se valor < 10 então
            símbolo ← caractere correspondente a ('0' + valor)
        senão
            símbolo ← caractere correspondente a ('A' + (valor - 10))
        fim_se
        concatenar símbolo ao final de "resultado"
    fim_para
    fim_se

// --- Saída ---

    Escreva "Número convertido:", resultado

FimAlgoritmo

**Observações:** Talvez o ideal seja criar uma função para calcular e outra para concatenar os algarismos calculados separadamente.
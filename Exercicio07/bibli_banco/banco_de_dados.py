def Mapeamento(algarismo):
    if algarismo == '0':
        return 0
    elif algarismo == '1':
        return 1
    elif algarismo == '2':
        return 2
    elif algarismo == '3':
        return 3
    elif algarismo == '4':
        return 4
    elif algarismo == '5':
        return 5
    elif algarismo == '6':
        return 6
    elif algarismo == '7':
        return 7
    elif algarismo == '8':
        return 8
    elif algarismo == '9':
        return 9
    elif algarismo == 'A' or algarismo == 'a':
        return 10
    elif algarismo == 'B' or algarismo == 'b':
        return 11
    elif algarismo == 'C' or algarismo == 'c':
        return 12
    elif algarismo == 'D' or algarismo == 'd':
        return 13
    elif algarismo == 'E' or algarismo == 'e':
        return 14
    elif algarismo == 'F' or algarismo == 'f':
        return 15
    elif algarismo == 'G' or algarismo == 'g':
        return 16
    elif algarismo == 'H' or algarismo == 'h':
        return 17
    elif algarismo == 'I' or algarismo == 'i':
        return 18
    elif algarismo == 'J' or algarismo == 'j':
        return 19
    elif algarismo == 'K' or algarismo == 'k':
        return 20
    elif algarismo == 'L' or algarismo == 'l':
        return 21
    elif algarismo == 'M' or algarismo == 'm':
        return 22
    elif algarismo == 'N' or algarismo == 'n':
        return 23
    elif algarismo == 'O' or algarismo == 'o':
        return 24
    elif algarismo == 'P' or algarismo == 'p':
        return 25
    elif algarismo == 'Q' or algarismo == 'q':
        return 26
    elif algarismo == 'R' or algarismo == 'r':
        return 27
    elif algarismo == 'S' or algarismo == 's':
        return 28
    elif algarismo == 'T' or algarismo == 't':
        return 29
    elif algarismo == 'U' or algarismo == 'u':
        return 30
    elif algarismo == 'V' or algarismo == 'v':
        return 31
    elif algarismo == 'W' or algarismo == 'w':
        return 32
    elif algarismo == 'X' or algarismo == 'x':
        return 33
    elif algarismo == 'Y' or algarismo == 'y':
        return 34
    elif algarismo == 'Z' or algarismo == 'z':
        return 35

def Mapeamento_inverso(algarismo):
    if algarismo == 0:
        return '0'
    elif algarismo == 1:
        return '1'
    elif algarismo == 2:
        return '2'
    elif algarismo == 3:
        return '3'
    elif algarismo == 4:
        return '4'
    elif algarismo == 5:
        return '5'
    elif algarismo == 6:
        return '6'
    elif algarismo == 7:
        return '7'
    elif algarismo == 8:
        return '8'
    elif algarismo == 9:
        return '9'
    elif algarismo == 10:
        return 'A'
    elif algarismo == 11:
        return 'B'
    elif algarismo == 12:
        return 'C'
    elif algarismo == 13:
        return 'D'
    elif algarismo == 14:
        return 'E'
    elif algarismo == 15:
        return 'F'
    elif algarismo == 16:
        return 'G'
    elif algarismo == 17:
        return 'H'
    elif algarismo == 18:
        return 'I'
    elif algarismo == 19:
        return 'J'
    elif algarismo == 20:
        return 'K'
    elif algarismo == 21:
        return 'L'
    elif algarismo == 22:
        return 'M'
    elif algarismo == 23:
        return 'N'
    elif algarismo == 24:
        return 'O'
    elif algarismo == 25:
        return 'P'
    elif algarismo == 26:
        return 'Q'
    elif algarismo == 27:
        return 'R'
    elif algarismo == 28:
        return 'S'
    elif algarismo == 29:
        return 'T'
    elif algarismo == 30:
        return 'U'
    elif algarismo == 31:
        return 'V'
    elif algarismo == 32:
        return 'W'
    elif algarismo == 33:
        return 'X'
    elif algarismo == 34:
        return 'Y'
    elif algarismo == 35:
        return 'Z'
    
def Nomes_bases(base):
    if base == 2:
        return "binário"
    elif base == 3:
        return "ternário"
    elif base == 4:
        return "quaternário"
    elif base == 5:
        return "quinário"
    elif base == 6:
        return "senário"
    elif base == 7:
        return "septenário"
    elif base == 8:
        return "octal"
    elif base == 9:
        return "novenário"
    elif base == 10:
        return "decimal"
    elif base == 11:
        return "unodecimal"
    elif base == 12:
        return "duodecimal"
    elif base == 13:
        return "tridecimal"
    elif base == 14:
        return "tetradecimal"
    elif base == 15:
        return "pentadecimal"
    elif base == 17:
        return "heptadecimal"
    elif base == 18:
        return "octadecimal"
    elif base == 19:
        return "enneadecimal"
    elif base == 20:
        return "vigesimal"
    elif base > 20 and base < 24:
        return str(base)
    elif base == 24:
        return "vigesimal"
    elif base > 24 and base < 30:
        return str(base)
    elif base == 30:
        return "trigesimal"
    elif base > 30 and base < 36:
        return str(base)
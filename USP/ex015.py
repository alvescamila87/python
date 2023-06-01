#repetições encaixadas (while dentro de outro while) - exercício de tabuada

linha = 1
coluna = 1

while linha <= 10:
    while coluna <= 10:
        print(linha * coluna, end = "\t")
        coluna = coluna + 1
    linha = linha + 1
    print()
    coluna = 1
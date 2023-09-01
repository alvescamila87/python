# Criando colunas com CSV - Opção 1:

with open('ArquivosAulas/aula04_cities.csv', 'r', encoding='windows 1252') as file:
    for line in file:
        row = line.rstrip().split(",")
        print(f"{row[0]}-{row[1]}")
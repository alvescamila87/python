# Criando colunas com CSV - Op��o 2:

with open("ArquivosAulas/aula04_cities.csv", 'r', encoding='windows 1252') as file:
    for line in file:
        state, city = line.rstrip().split(",")
        print(f"{state}-{city}")
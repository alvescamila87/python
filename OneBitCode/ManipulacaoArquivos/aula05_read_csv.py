# Ordenar valores na leitura de arquivo CSV

cities = []

with open("ArquivosAulas/aula04_cities.csv", 'r', encoding='windows 1252') as file:
    for line in file:
        state, city = line.rstrip().split(",")
        cities.append(f"{state}-{city}")

for city in sorted(cities):
    print(city)

# Sorted: DESC
# for city in sorted(cities, reverse=True):
#     print(city)
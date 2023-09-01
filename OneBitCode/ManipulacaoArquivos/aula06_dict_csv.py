# Transformando dados de um CSV em um Dicionário

cidades = []

with open("ArquivosAulas/aula04_cities.csv", "r", encoding="windows 1252") as file:
    for line in file:
        estado, cidade = line.rstrip().split(",")
        cidade_sc = {}
        cidade_sc['estado'] = estado
        cidade_sc['cidade'] = cidade
        cidades.append(cidade_sc)

print(cidades)

for cidade in cidades:
    print(f"{cidade['estado']}{cidade['cidade']}")
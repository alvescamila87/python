# Ordenar valores em dicionário CSV utilizando expressão Lambda

cidades = []

with open("ArquivosAulas/aula07_cities_desc.csv", "r", encoding="windows 1252") as file:
    for line in file:
        estado, cidade = line.rstrip().split(",")
        cidade_uf = dict()
        cidade_uf['estado'] = estado
        cidade_uf['cidade'] = cidade
        cidades.append(cidade_uf)

print(cidades)

def get_estado(cidade_uf):
    return cidade_uf['estado']

def get_cidade(cidade_uf):
    return cidade_uf['cidade']


# for cidade in sorted(cidades, key=get_cidade):
for cidade in sorted(cidades, key=lambda cidade : cidade_uf['cidade']):
    print(f"{cidade['estado']}{cidade['cidade']}")


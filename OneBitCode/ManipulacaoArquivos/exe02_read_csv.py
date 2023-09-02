carros = []

with open("ArquivosAulas/aula10_cars2.csv", "r", encoding="windows 1252") as file:
    for line in file:
        marca, modelo = line.rstrip().split(",")
        veiculos = dict()
        veiculos['marca'] = marca
        veiculos['modelo'] = modelo
        carros.append(veiculos)

print(veiculos)

def get_marca(veiculos):
    return veiculos['marca']

def get_modelo(veiculos):
    return veiculos['modelo']

for carro in sorted(carros, key=get_modelo):
    print(f"{carro['marca']} {carro['modelo']}")


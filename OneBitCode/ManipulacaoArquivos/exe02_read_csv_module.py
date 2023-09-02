import csv

carros = []

with open("ArquivosAulas/aula10_cars2.csv", "r", encoding="windows 1252") as file:
    reader = csv.DictReader(file)
    for row in reader:
        carros.append(dict(marca=row["marca"], modelo=row["modelo"]))

print(carros)

for carro in sorted(carros, key=lambda carros: row["modelo"]):
    print(f"{carro['marca']} {carro['modelo']}")
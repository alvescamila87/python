# Escrevendo Dados em CSV

import csv

marca = str(input("Informe a marca do carro: "))
modelo = str(input(f"Informe o modelo do veículo da {marca}: "))

with open("ArquivosAulas/aula10_cars.csv", "a", encoding="UTF-8") as file:
    writer = csv.writer(file, lineterminator="\n")
    writer.writerow([marca, modelo])
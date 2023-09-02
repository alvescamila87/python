# Leitura de dados em CSV utilizando o Módulo CSV

import csv

cidades = []

# 1) Colocar o nome das rows no arquivo raiz "Estado" e "Município" no "aula09.csv"

with open("ArquivosAulas/aula09.csv", "r", encoding="windows 1252") as file:
    reader = csv.DictReader(file)
    for row in reader:
        # print(row)
        # 1.1) Colocar o nome das rows conforme readers do arquivo raiz "Estado" e "Município" no "aula09.csv"
        cidades.append(dict(Estado=row["Estado"], Município=row["Município"]))
print(cidades)

# 2) Ordenar

# 2.1) Colocar o nome da key lambda exatamente como a key do append do dicionário
for cidade in sorted(cidades, key=lambda cidade: cidade["Município"]):
    print(f"{cidade['Estado']}-{cidade['Município']}")
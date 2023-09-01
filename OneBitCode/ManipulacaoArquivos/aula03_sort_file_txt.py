# Colocar os dados em uma lista
names = []

with open("ArquivosAulas/aula02_names.txt", 'r', encoding='windows 1252') as file:
    for line in file:
        names.append(line.rstrip())

print(names)

# Remover os dados da lista e apresentar linha-a-linha os registros de forma ordenada
for name in sorted(names):
    print(name)
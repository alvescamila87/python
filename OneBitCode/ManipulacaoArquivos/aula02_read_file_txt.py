with open('ArquivosAulas/aula02_names.txt', 'r', encoding='windows 1252') as file:
    for line in file:
        print(f"{line.rstrip()}")

# rs.strip() remover quebradas
# encoding='utf-8'

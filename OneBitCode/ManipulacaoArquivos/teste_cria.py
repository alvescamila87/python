


while True:
    name = str(input("Informe um nome: [0 para parar] ")).capitalize().strip()
    with open('ArquivosAulas/aula02_names.txt', 'a') as file:
        file.write(f"{name}\n")
        file.close()
    if name == 0:
        break


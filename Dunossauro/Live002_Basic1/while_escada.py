
resposta = str(input("Montar uma escada no console? [s/n]"))

n = 1

while resposta != 'n':
    resposta = input(f"*{'*' * n} [s/n]")
    n += 1

print(f"Escada montada :D ")
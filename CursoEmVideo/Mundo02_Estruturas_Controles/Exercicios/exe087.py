#Parte 2: Estruturas compostas -> Mais sobre Matriz em Python 

matriz = [[0,0,0], [0,0,0], [0,0,0]]

soma_pares = 0
maior_valor = 0
soma_coluna = 0

for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f"Digite um valor para {l, c}:"))
print("-="*30)

for l in range(0,3):
    for c in range(0,3):
        print(f"[{matriz[l][c]:^5}]", end="")
        # Verifica todos os valores pares da matriz:
        if matriz[l][c] % 2 == 0:
            soma_pares = soma_pares + matriz[l][c]
    print()
print("-="*30)

print(f"A soma dos valores pares é: {soma_pares}")

for l in range(0,3):
    soma_coluna = soma_coluna + matriz[l][2]
print(f"A soma dos valores da terceira coluna é: {soma_coluna}")

for c in range(0,3):
    if c == 0:
        maior_valor = matriz[1][c]
    elif matriz[1][c] > maior_valor:
        maior_valor = matriz[1][c]
print(f"O maior valor da segunda linha é: {maior_valor}")


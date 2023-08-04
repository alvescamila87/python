#Parte 2: Estruturas compostas -> Matriz em Python 

# Dimensão da matriz 3x3

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# FOR de alimentação, o FOR que coloca os valores na matriz
for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f"Digite um valor para a posição {linha, coluna}: "))

print("-="*30)
# print(matriz)

# Os FORs abaixo são de estruturas de repetição para mostrar a estrutura tela
for linha in range(0,3):
    for coluna in range(0,3):
        print(f"[{matriz[linha][coluna]:^5}]", end="")
    # Print abaixo para quebrar a linha quando finalizar o FOR de coluna
    print()




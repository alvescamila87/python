#Dado um número inteiro n >= 0, calcular n! (fatorial).

n = int(input('informe o valor de "n": '))
i = 1
n_fat = 1

while i <= n:
    n_fat = n_fat * i
    i = i + 1

print("Cálculo do fatorial de {} é {}". format(n, n_fat))
#Dados números inteiros n e k, com k >= 0, calcular n elevado a k. Por exemplo, dados os números 3 e 4 o seu programa deve escrever o número 81.

n = int(input('informe o valor de "n": '))
k = int(input('informe o valor de "k": '))

pot = 1
i = 0

while i < k:
    pot = pot * n
    i = i + 1
print("O valor de {} elevado a {} é {}".format(n, k, pot))
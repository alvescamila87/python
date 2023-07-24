#estrutura de repetição:cálculo de fatorial

#opção 1
import math
num = int(input("Digite um número para calcular seu Fatorial: "))
print("O fatorial de {} é {}.".format(num, math.factorial(num)))

#opção 2
n = int(input("Digite um número para calcular seu Fatorial: "))
c = n
f = 1
print("Calculando {}! = ".format(n), end="")
while c > 0:
    print("{}".format(c), end="")
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print("{}.".format(f))


for f in range(1,n):
    numero = int(input("Digite um número para calcular seu Fatorial: "))
    print(f)

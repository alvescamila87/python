#Dados dois inteiros positivos calcular o máximo divisor comum entre eles usando o algoritmo de Euclides.

n = int(input("Digite o valor de n (n > 0): "))
m = int(input("Digite o valor de m (m > 0): "))

mdc = n

while n % mdc != 0 or m % mdc != 0:
    mdc = mdc -1

print('MDC({}, {}) = {}'.format(n, m, mdc))

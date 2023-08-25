import random

# Exe02
lista_numeros = random.sample(range(1, 100), 20)
par = list()
impar = list()

for numero in lista_numeros:
    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)


print("Lista ORIGINAL: ", lista_numeros)
print("Lista PAR: ", par)
print("Lista ÍMPAR: ", impar)

# Opção 2 list comprehension python

vetor = random.sample(range(100), 20)
lista_par = [x for x in vetor if x % 2 == 0]
lista_impar = [x for x in vetor if x % 2 == 1]

print("OPÇÃO2 - Lista ORIGINAL: ", vetor)
print("OPÇÃO2 - Lista PAR: ", lista_par)
print("OPÇÃO2 - Lista ÍMPAR: ", lista_impar)

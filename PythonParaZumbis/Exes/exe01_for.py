import random

# Exe01
lista = random.sample(range(100), 10)

maior = menor = lista[0]

for numero in lista[:]:
    if numero > maior:
        maior = numero
    elif numero < menor:
        menor = numero

print(lista)
print("O maior número da lista sorteada é: ", maior)
print("O menor número da lista sorteada é: ", menor)


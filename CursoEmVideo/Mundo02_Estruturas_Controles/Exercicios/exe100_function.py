# Função: EXERCÍCIO: Funções para sortear e somar

# Opção Camila
from random import randint

def sortear(lista):
    print("-=" *30)
    contador = 0
    while contador < 5:
        lista_valores.append(randint(1,11))
        contador += 1
    print(f"Sorteando {contador} valores da lista: {lista_valores}. Pronto, números sorteados!!!.")


lista_valores = list()
sortear(lista_valores)

def somar_par(lista):
    soma = 0
    for i in lista_valores:
        if i % 2 == 0:
            soma += i
    print(f"Somando os valores PARES de {lista_valores}, temos: {soma}.")
    print("-=" *30)


somar_par(lista_valores)


# Opção Guanabara

from time import sleep

def sorteia(lista):
    print(f"Sorteando 5 valores da lista: ", end="")
    for cont in range(0,5):
        n = randint(1,10)
        lista.append(n)
        print(f"{n} ", end="", flush=True)
        sleep(0.3)
    print("PRONTO!")

def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
        print(f"Somando os valores pares da {lista}, temos {soma}")

números = list()
sorteia(números)
somar_par(números)
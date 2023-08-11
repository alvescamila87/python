#Parte 2: Estruturas compostas -> Palpites mega sena

from random import randint
from time import sleep

lista = list()
jogos = list()

print("-="*30)
print("      JOGA NA MEGA SENA       ")
print("-="*30)
qtd_jogos = int(input("Quantos jogos você quer que eu sorteie? "))
total = 1
while total <= qtd_jogos:
    contador = 0

    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            contador += 1
        if contador >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1

print("-=" *3, f" SORTEANDO {qtd_jogos} JOGOS ", "-=" *3)
for indice, l in enumerate(jogos):
    print(f"Jogo {indice+1}: {l}")
    sleep(1)
print("-="*5, '< BOA SORTE! >', "-="*5)

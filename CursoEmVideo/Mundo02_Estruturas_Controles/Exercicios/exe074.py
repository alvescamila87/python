#estruturas compostas: maior e menor valor em Tupla

from random import randint, random

numeros = (randint(1, 10), 
     randint(1, 10), 
     randint(1, 10), 
     randint(1, 10), 
     randint(1, 10))

#opção de print 1
print(f"Os valores sorteados foram: {numeros}")

#opção de print 2
for n in numeros:
    print(f"{n} ", end='')


# maior e menor valor sorteados
print(f"\nO maior valor sorteado foi {max(numeros)}.")
print(f"O menor valor sorteado foi {min(numeros)}.")

#maior e menor valor sorteados - opção 2
maior_valor = 0
menor_valor = 0

for x in numeros:
    if x > maior_valor:
        maior_valor = x
        print(f"MAIOR valor: '{maior_valor}'")
    if x < menor_valor:
        menor_valor = x
        print(f"MENOR valor: '{menor_valor}'")


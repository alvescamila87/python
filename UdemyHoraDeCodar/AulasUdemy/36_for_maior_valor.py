#for para checar maior valor

lista = [1000,85, 999, 105, 33, 66, 5000, 8888]

maior_valor = 0

for n in lista:
    if n > maior_valor:
        maior_valor = n

print(maior_valor)


#for para checar menor valor

menor_valor = lista[0]

for x in lista:
    if x < menor_valor:
        menor_valor = x

print(menor_valor)
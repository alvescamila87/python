#encontrando o menor valor da lista com for in

lista = [99, 2, 66,3, 5, 4, -5, 7]

menor_valor = lista[0]

for x in lista:
    if x < menor_valor:
        menor_valor = x

print(menor_valor)
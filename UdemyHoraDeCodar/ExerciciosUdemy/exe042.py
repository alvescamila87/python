#lista com loop e remove 4º elemento, não o 4º índice

lista = [1,2,3,4,5,6,7,8,9,10]

x = 0

while x < len(lista):
    if lista[x] == 4:
        del lista[x]
    x = x + 1

print(lista)

#segunda opção de resolução:

lista_a = []

i = 0

while i <= 10: #preencher a lista_a vazia, incrementando os números de 0 a 10
    lista_a.append(i)
    i = i + 1

print(lista_a)

j = 0 

while j < len(lista_a):
    if lista_a[j] == 4:
        del lista_a[j]
    j = j + 1

print(lista_a)


#lista

lista_a = [1,2,3,4,5]

lista_b = ["Camila", "Maria", "Helena", "Lorena", "Beatriz"]

lista_c = (lista_a[:] + lista_b[:])

print(lista_c)

#solução 2

lista_1 = [9,8,7,6,5]

lista_2 = [0,1,2,3,4]

lista_3 = []

x = 0

while x < len(lista_1):
    lista_3.append(lista_1[x])
    x = x + 1

y = 0

while y < len(lista_2):
    lista_3.append(lista_2[y])
    y = y + 1

print(lista_3)
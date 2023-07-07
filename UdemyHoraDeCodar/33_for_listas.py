#for com listas

lista =[1,2,3,4,5,6,7,8,9,10]
print(lista)

for x in lista:
    print(x)


#hipótese 2, de obter o mesmo resultado, porém com while

n = 0

while n < len(lista):
    print(lista[n])
    n = n + 1
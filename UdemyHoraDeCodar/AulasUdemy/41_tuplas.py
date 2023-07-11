#tuplas

tupla = (1,2,3)

print(tupla)
print(type(tupla))
print(tupla[0])

#não suporta atribição/assignment
#tupla[0] = 10

#iterar tuplas com for

#iteracao tipo 1
for x in tupla:
    print(x)


#iteracao tipo 2
i = 0

while i < len(tupla):
    print(tupla[i])
    i = i + 1
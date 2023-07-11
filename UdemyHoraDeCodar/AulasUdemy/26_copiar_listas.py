#copiar listas

lista = ["Camila", "Isabel", "Karoline"]

nova_lista = lista[:] #utilizar sempre essa sintaxe especial

print(lista)
print(nova_lista)

#alteração na lista filha

nova_lista[0] = "Maria"

print(nova_lista)
print(lista)
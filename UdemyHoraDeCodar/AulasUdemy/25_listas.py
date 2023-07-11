#listas


#fazer lista
lista = [ 1,2,3,4,5]
print(lista)


#acessar itens da lista

nomes = ["João", "Karoline", "Paulo", "Isabel"]

print(nomes[2])

#modificar itens da lista
nomes[0] = "Camila"
print(nomes)

print("O meu nome é %s" %nomes[0])

nome = nomes[0]
print(nome)

#percorrer itens da lista

frutas = ["Maça", "Banana", "Mamão", "Goiaba", "Uva"]

i = 0

while i < 5:
    print(frutas[i])
    i = i + 1
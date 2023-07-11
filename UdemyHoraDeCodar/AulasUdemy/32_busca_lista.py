#busca lista

lista = ['AC', 'TV', 'Controle', 'Som']

i = 0

while i < len(lista):
    if lista[i] == 'Controle':
        print('Encontramos o controle!')
    i = i + 1

print(lista)

#procurando um item dinâmico

lista_1 = ["Fusca", "Audi", "Gol", "Polo"]

x = 0

item_procurado = str(input("Informe o veículo que está procurando: "))

while x < len(lista_1):
    if lista_1[x] == item_procurado:
        print('Encontramos o %s!' %item_procurado)
    else:
        print("O veículo %s não foi encontrado na lista" %item_procurado)
    x = x + 1

print(lista_1)
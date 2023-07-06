#lista valores zerados

lista = [0,0,0,0,0]

i = 0

while i < 5:
    novo_valor = int(input("Informe um número %d: " %i))
    lista[i] = novo_valor
    i = i + 1

print(lista)


#Parte 2: Estruturas compostas -> Listas com pares e ímpares

# Opção 1 - Camila

numeros = [[], []]
valor = 0

for c in range(1,8):
    valor = int(input(f"Informe o {c}º número: "))
    if valor % 2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)

print("-="*30)
print(f"Os valores pares digitados foram: {sorted(numeros[0])}.")
print(f"Os valores ímpares digitados foram: {sorted(numeros[1])}")
# outra opção de print ordenado:
# numeros[0.sorted()]
# numeros[0.sorted()]




# Opção 2 - Guanabara
lista_numeros = list()
pares = list()
impares = list()

for num in range(1,8):
    valor = int(input(f"Digite o {num}º número: "))
    lista_numeros.append(valor)
    if valor % 2 == 0:
        pares.append(lista_numeros[:])
        lista_numeros.clear()
    else:
        impares.append(lista_numeros[:])
        lista_numeros.clear()

print(f"Os valores pares digitados foram: {sorted(pares)}.")
print(f"Os valores ímpares digitados foram: {sorted(impares)}.")


    
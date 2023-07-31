#estruturas compostas: Dividindo valores em válias listas

lista_numeros = list()
pares = list()
impares = list()

while True:
    num = int(input("Digite um número: "))
    lista_numeros.append(num)
    continuar = " "
    while continuar not in "SN":
        continuar = str(input("Quer continuar? [S/N]")).strip().upper()[0]
    if continuar == "N":
        break

print(f"A lista completa é: {lista_numeros}.")

for par in lista_numeros:
    if par % 2 == 0:
       pares.append(par)
print(f"A lista de PARES é: {pares}.")

for impar in lista_numeros:
    if impar % 2 != 0:
        impares.append(impar)
print(f"A lista de ÍMPARES é: {impares}.")


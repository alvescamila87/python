#estruturas compostas: Extraindo dados de uma Lista

lista_numeros = list()

# contador = 0

while True:
    num = int(input("Digite um valor: "))
    lista_numeros.append(num)
    # contador += 1
    continuar = " "
    while continuar not in "SN":
        continuar = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if continuar == "N":
        break
    
# print(f"Você digitou {contador} elementos.")
print(f"Você digitou {len(lista_numeros)} elementos.")
lista_numeros.sort(reverse=True)
print(f"Os valores em ordem descrescente são: {lista_numeros}")
# if num == 5 in lista_numeros:
if 5 in lista_numeros:
        print("O valor '5' faz parte da lista.")
else:
    print("O valor '5' não foi encontrado na lista.")



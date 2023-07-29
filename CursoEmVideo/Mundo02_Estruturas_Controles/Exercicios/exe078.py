#estruturas compostas: Maior e menor valores na Lista

lista_numeros = []

maior_valor = 0
menor_valor = 0

for n in range(0,5):
    lista_numeros.append(int(input(f"Digite um valor para a {n}ª posição: ")))
    if n == 0:
        maior_valor = menor_valor = lista_numeros[n]
    else:
        if lista_numeros[n] > maior_valor:
            maior_valor = lista_numeros[n]
        if lista_numeros[n] < menor_valor:
            menor_valor = lista_numeros[n]
print("-="*30)
print(f"Você digitou os valores: {lista_numeros}")
print(f"O MAIOR valor digitado foi {maior_valor} nas posições: ", end="")
for chave, v in enumerate(lista_numeros):
    if v == maior_valor:
        print(f"{chave}... ", end="")
print()
print(f"O MENOR valor digitado foi {menor_valor} nas posições: ", end="")
for chave, v in enumerate(lista_numeros):
    if v == menor_valor:
        print(f"{chave}... ", end="")
print()

#estruturas compostas: Lista ordenada sem repetições

lista_numeros = list()

for contador in range(1,6):
    num = int(input(f"Digite o {contador}º valor: "))
    if contador == 1 or num > lista_numeros[-1]:
        lista_numeros.append(num)
    else:
        posicao = 0
        while posicao < len(lista_numeros):
            if num <= lista_numeros[posicao]:
                lista_numeros.insert(posicao, num)
                break
            posicao += 1
    print(f"Número adicionado...")
print("-="*30)
print(f"Os valores digitador em ordem foram: {lista_numeros}")
    
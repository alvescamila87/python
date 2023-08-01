#Parte 2: Estruturas compostas -> Lista composta e análise de dados

temporario = list()
pessoas = list()
maior_peso = 0
menor_peso = 0


while True: 
    # Iterar lista temporária
    temporario.append(str(input("Nome: ")))
    temporario.append(float(input("Peso: ")))

    # Verificar maior e menor peso das pessoas da lista temporária
    if len(pessoas) == 0:
        maior_peso = temporario[1]
        menor_peso = temporario[1]
    
    # Verificar maior e menor peso das pessoas da lista temporária
    else:
        if temporario[1] > maior_peso:
            maior_peso = temporario[1]
            
        if temporario[1] < menor_peso:
            menor_peso = temporario[1]
    
    # Cria cópia da lista temporária e apaga ao final a lista temp
    pessoas.append(temporario[:]) 
    temporario.clear()

    # Verifica se usuário quer continuar incluindo pessoas na lista
    continuar = " "
    while continuar not in "SN":
        continuar = str(input("Quer continuar? [S/N]")).strip().upper()[0]
    if continuar == "N":
        break

print(f"Dados de pessoas: {pessoas}")
print(f"Ao todo, você cadastrou {len(pessoas)} pessoas.")
print(f"O maior peso foi de {maior_peso}kg. Peso de: ", end="")
for p in pessoas:
    if p[1] == maior_peso:
        print(f"{p[0]} ", end="")

print()
print(f"O menor peso foi de {menor_peso}kg. Peso de: ", end="")
for p in pessoas:
    if p[1] == menor_peso:
        print(f"{p[0]} ", end="")


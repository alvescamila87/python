#estruturas compostas: Valores únicos em uma Lista

lista_numeros = list()

while True:
    num = int(input("Digite um número: "))
    if num not in lista_numeros:
        lista_numeros.append(num)
        print("Número adicionado com sucesso!")
    else:
        print("Número duplicado!!! Não adicionado.")      
    continuar = " "
    while continuar not in "SN":
        continuar = str(input("Quer continuar? [S/N] ")).strip().upper()[0]  
    if continuar == "N":
        break
print(f"Você digitou os valores: {sorted(lista_numeros)}")
#Parte 2: Estruturas compostas -> Lista composta e análise de dados

pessoas = list()

while True: 
    nome = str(input("Nome: "))
    peso = float(input("Peso: "))
    pessoas.append(nome)
    pessoas.append(peso)
    continuar = " "
    while continuar not in "SN":
        continuar = str(input("Quer continuar? [S/N]")).strip().upper()[0]
    if continuar == "N":
        break

print(pessoas)

#estrutura de repetição: análise de dados do grupo

contador = 0
total_homens = 0
total_mulheres = 0

while True: 
    print("-"*30)
    print("CADASTRE UMA PESSOA")    
    print("-"*30)
    idade = int(input("Idade: "))
    sexo = ' '
    while sexo not in "FM":
        sexo = str(input("Sexo: [M/F] ")).strip().upper()[0]
    if idade >= 18:
            contador += 1
    if sexo in "M":  
            total_homens += 1
    if sexo in "F" and idade <= 20:
            total_mulheres += 1  
    continuar = ' '
    while continuar not in "SN":
        print("-"*30)
        continuar = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
        print("-"*30)
    if continuar == "N":
        break
print("Acabou!")
print(f"Total de pessoas com mais de 18 anos: {contador}")
print(f"Total de HOMENS cadastrados: {total_homens}")
print(f"Total de MULHERES com menos de 20 anos cadastradas: {total_mulheres}")
        

        
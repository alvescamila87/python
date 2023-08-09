#Estruturas compostas: Dicionários {} - EXERCÍCIO: Unindo dicionários e listas

dados = dict()
pessoas = list()

while True:
     dados["nome"] = str(input("Nome: "))
     sexo = str(input("Sexo: [M/F] ")).strip().upper()[0]
     while sexo not in "MF":
          sexo = str(input("ERRO! Repita apenas M ou F. \nSexo: [M/F] ")).strip().upper()[0]
     dados["sexo"] = sexo
     dados["idade"] = int(input("Idade: "))
     pessoas.append(dados.copy())
     continuar = str(input("Quer continuar? [S/N]")).strip().upper()[0]
     while continuar not in "SN":
          continuar = str(input("ERRO! Repita apenas M ou F. \nQuer continuar? [S/N]")).strip().upper()[0]
     if continuar == "N":
          break 

print("LISTA: ", pessoas)
print("DICIONADO: ", dados)

print(f"Ao todo temos {len(pessoas)} pessoas cadastradas.")
for pessoa in pessoas:
     for v in pessoa.values():
          print(f'{v}')
     print()
#print(f"A média de idade é de {media} anos")
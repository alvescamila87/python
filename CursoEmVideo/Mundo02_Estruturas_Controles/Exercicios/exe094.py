#Estruturas compostas: Dicionários {} - EXERCÍCIO: Unindo dicionários e listas

dados = dict()
pessoas = list()
soma = 0
media = 0

while True:
     dados["nome"] = str(input("Nome: "))
     sexo = str(input("Sexo: [M/F] ")).strip().upper()[0]
     while sexo not in "MF":
          sexo = str(input("ERRO! Repita apenas M ou F. \nSexo: [M/F] ")).strip().upper()[0]
     dados["sexo"] = sexo
     dados["idade"] = int(input("Idade: "))
     soma += dados["idade"]
     pessoas.append(dados.copy())
     continuar = str(input("Quer continuar? [S/N]")).strip().upper()[0]
     while continuar not in "SN":
          continuar = str(input("ERRO! Repita apenas M ou F. \nQuer continuar? [S/N]")).strip().upper()[0]
     if continuar == "N":
          break 

print("LISTA: ", pessoas)
print("DICIONADO: ", dados)

print(f"A) Ao todo temos {len(pessoas)} pessoas cadastradas.")
media = soma / len(pessoas)
print(f"B) A média de idade é de {media:5.2f} anos.")
print(f"C) A mulheres cadastradas foram ", end="")
for p in pessoas:
     if p['sexo'] == 'F':
          print(f"{p['nome']} ", end="")
print()
print("D) Lista das pessoas que estão acima da média: ")
for p in pessoas:
     if p['idade'] >= media:
          print('    ', end="")
          for k, v in p.items():
               print(f"{k} = {v}; ", end="")
          print()
print('<< ENCERRADO >>')


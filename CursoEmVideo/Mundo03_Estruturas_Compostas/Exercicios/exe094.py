#Estruturas compostas: Dicionários {} - EXERCÍCIO: Unindo dicionários e listas

# Opção Camila 

dados = dict()
pessoas = list()
soma = 0
media = 0

while True:
     dados["nome"] = str(input("Nome: ")).strip().capitalize()
     sexo = str(input("Sexo: [M/F] ")).strip().upper()[0]
     while sexo not in "MF":
          sexo = str(input("ERRO! Repita apenas M ou F. \nSexo: [M/F] ")).strip().upper()[0]
     dados["sexo"] = sexo
     dados["idade"] = int(input("Idade: "))
     soma += dados["idade"]
     pessoas.append(dados.copy())
     continuar = str(input("Quer continuar? [S/N]")).strip().upper()[0]
     while continuar not in "SN":
          continuar = str(input("ERRO! Repita apenas M ou F. \nQuer continuar? [S/N] ")).strip().upper()[0]
     if continuar == "N":
          break 

print("LISTA: ", pessoas)
print("DICIONADO: ", dados)

print(f"A) Ao todo temos {len(pessoas)} pessoas cadastradas.")
media = soma / len(pessoas)
print(f"B) A média de idade é de {media:5.2f} anos.")
print(f"C) A mulheres cadastradas foram: ", end="")
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

# Opção Guanabara

galera = list() 
pessoas = dict()
soma = media = 0

while True:
     pessoas.clear()
     pessoas['nome'] = str(input("Nome: "))
     while True:
          pessoas['sexo'] = str(input("Sexo: [M/F] ")).upper()[0]
          if pessoas['sexo'] in "MF":
               break 
          print("ERRO! Por favor, digite apenas M ou F.")
     pessoas['idade'] = int(input("Idade: "))
     soma += pessoas['idade']
     galera.append(pessoas.copy())
     while True:
          resp = str(input("Quer continuar? [S/N] ")).upper()[0]
          if resp in "SN":
               break
          print("ERRO! Responda S ou N.")
     if resp == "N":
          break
print('-='*30)
print(f"A) Ao todo temos {len(galera)} pessoas cadastradas.")
media = soma / len(galera)
print(f"B) A média de idade é de {media:5.2f} anos.")
print(f"C) A mulheres cadastradas foram: ", end="")
for p in galera:
     if p['sexo'] == 'Ff':
          print(f"{p['nome']} ", end="")
print()
print("D) Lista das pessoas que estão acima da média: ")
for p in galera:
     if p['idade'] >= media:
          print('    ', end="")
          for k, v in p.items():
               print(f"{k} = {v}; ", end="")
          print()
print('<< ENCERRADO >>')

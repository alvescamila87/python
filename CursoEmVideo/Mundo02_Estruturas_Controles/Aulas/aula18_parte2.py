# Estruturas compostas: variáveis compostas: Foco em LISTAS[] - Parte 2
# Listas são mutáveis
# Listas dentro de listas
# Estrutura = nome da lista

dados = list()
dados.append("Pedro")
dados.append(25)
dados.append("Camila")
dados.append(35)
dados.append("Maria")
dados.append(19)
print(dados)

pessoas = list()
pessoas.append(dados[:])
print(pessoas)

# Acessar conteúdo por índice / Posicionamento de elementos dentro de estruturas compostas
print(pessoas[0][0]) #joão
print(pessoas[1][1]) #35
print(pessoas[2][0]) #Maria
print(pessoas[1])    #['Maria', 19]

galera = [["Camila", 35], ["Karoline", 36], ["Isabel", 61], ["Paulo", 63]]
print(galera)
print(galera[1][0])

# Criar listas
for p in galera:
    print(p) # Estrutura completa

for p in galera:
    print(p[0]) # Somente nomes

for p in galera:
    print(p[1]) # Somente idades

for p in galera:
    print(f"{p[0]} tem {p[1]} anos de idade.")


# Criar lista que pega dados temporariamente

pessoas = list()
dados = list()
for c in range(0,3):
    dados.append(str(input("Nome: ")))
    dados.append(int(input("Idade: ")))
    pessoas.append(dados[:])
    dados.clear()

print(pessoas)

# Mostrar pessoas com condicionais
total_maior = 0
total_menor = 0

for p in pessoas:
    if p[1] >= 21:
        print(f"{p[0]} é maior de idade.") 
        total_maior += 1
    else:
        print(f"{p[0]} é menor de idade.")
        total_menor += 1
print(f"Temos {total_maior} pessoas maiores de idade e {total_menor} menores de idade.")
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
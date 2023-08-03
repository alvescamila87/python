# Estruturas compostas: variáveis compostas: Foco em LISTAS[] - Parte 1
# Listas são mutáveis

lanche = ["hambúrguer", "suco", "pizza", "pudim"]
print(lanche)

# Alterar item da lista
lanche[3] = "picolé"
print(lanche)

# Incluir item na lista (adiciona ao FINAL da lista)
lanche.append("cookie")
print(lanche)

# Incluir item na lista (adiciona no local 'customizado' da lista)
lanche.insert(0,"cachorro-quente")
print(lanche)

# Deletar um item da lista pela CHAVE
del lanche[3]
print(lanche)

# Deletar um item da lista pela CHAVE (deleta o ÚLTIMO item da lista, mas pode passar por parâmetro qual quer eliminar)
lanche.pop() 
lanche.pop(1) 
print(lanche)

# Deletar item da lista pelo CONTEÚDO
lanche.remove("cachorro-quente")
print(lanche)

# Verificar item para poder remover
if "cookie" in lanche:
    lanche.remove("cookie")
else:
    print('Item não está na lista.')
print(lanche)

# Criar listas com RANGE
valores = list(range(4,11))
print(valores)

# Colocar a lista em ordem
numeros = [8,2,3,6,5,1,9,7,4]
print(numeros)
numeros.sort()
print(numeros)

# Colocar a lista em ordem - IVNERSA
num = [9,6,1,2,3,4,5]
print(num)
num.sort(reverse=True)
print(num)

# Tamanho da lista, quantidade de ELEMENTOS e não de índice
print(len(num))

# Criar lista nas formas:
nome = []
nome = list()

# Criando lista
lista_numeros = []
lista_numeros.append(14)
lista_numeros.append(13)
lista_numeros.append(20)
lista_numeros.append(29)

for n in lista_numeros:
    print(f"{n}...", end="")

# Se quiser as chaves e os valores:
for chave, n in enumerate(lista_numeros):
    print(f"Na posição {chave}, o número '{n}' foi adicionado.")

# Ler valores pelo teclado e colocar na lista[]:
lista_valores = []

for contador in range(0,5):
    lista_valores.append(int(input("Digite um valor: ")))

for chave, x in enumerate(lista_valores):
    print(f"Na posição {chave}, o número '{x}' foi adicionado.")

# Ligação de lista (NÃO É CÓPIA)
a = [2,3,4,7]
b = a
b[2] = 8 # Alterará as duas listas, pois estão INTERLIGADAS / IGUALADAS
print(f"Lista A: {a}")
print(f"Lista B: {b}")

# Criar uam CÓPIA da lista 
c = [9,6,5,4]
d = c[:] # CÓPIA
d[2] = 8 # Alterará SOMENTE a lista D, pois NÃO estão  INTERLIGADAS / IGUALADAS
print(f"Lista C: {c}")
print(f"Lista D: {d}")
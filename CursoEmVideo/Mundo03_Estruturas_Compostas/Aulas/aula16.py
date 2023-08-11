# Estruturas compostas: variáveis compostas (), [], {}
# tuplas(), listas[] e dicionários{}
# Foco em TUPLAS(), o python novo permite criar tupla sem parênteses
# Tuplas são ÍMUTÁVEIS

# Tuplas são imutáveis
lanche = ("Hambúrguer", "Suco", "Pizza", "Pudim")
print(lanche)
print(lanche[0])
print(lanche[-1])
print(lanche[1:3])
print(lanche[:2])
print(lanche[1:])
print(len(lanche))

# Tuplas são imutáveis
# lanche[1] = "Refrigerante"

# For in - Opção 1
for comida in lanche:
    print(f"{comida}")


# Lenght - Opção 2
print(len(lanche))

for contador in range(0, len(lanche)):
    print(lanche[contador])

# Se precisar de posição, segue opções:
veiculos = ("Carro", "Moto", "Bicleta", "Patinete elétrico")
print(veiculos)

# Opção 1
for transporte in veiculos:
    print(f"[OPÇÃO EXEMPLO 1]: Vou de: {transporte}")

# Opção 2
for transporte in range(0, len(veiculos)):
    print(f"[OPÇÃO EXEMPLO 2]: Eu vou de {veiculos[transporte]}, na posição {transporte}")

# Opção 3
for posicao, transporte in enumerate(veiculos):
    print(f"[OPÇÃO EXEMPLO 3]: Irei de: {transporte} na posição {posicao}")

# Mostrar na ORDEM sorted():
nomes = ("Paulo", "Isabel", "Karoline", "Camila", "Ana", "Maria", "João", "Lorenzo")

print(nomes)
print(sorted(nomes))

# Criação de Tuplas com: +
a = (5, 2, 4)
b = (10, 2, 5, 3, 7, 8)
c = a + b
print(c)

d = b + a
print(d) #diferente de c, pois mudou a ordem

#lenght
print(len(c))

#count: quantas vezes aparece o '5' na tupla 'c'
print(c.count(5))

#index com deslocamento: qual a posição de segundo '2' na tupla 'c'
# informar a partir de que posição deseja visualizar o segundo valor
print(c.index(3))
print(c.index(2, 2))

# no python, a tupla aceita dados string, int, boolean
pessoa = ("Camila", 35, "F", 58.0)
print(pessoa)

#apagar tupla
del(pessoa)
print(pessoa)
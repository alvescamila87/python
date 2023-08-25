import random

# 1) Randint:
print(random.randint(1, 100))
print(random.randint(1, 100))
print(random.randint(1, 100))

# 2) Lista de nomes:

nomes = "camila paulo isabel karoline".split()
print(nomes)

# escolher nome da lista:
print(random.choice(nomes))
print(random.choice(nomes))

# misturar nomes da lista:
random.shuffle(nomes)
print(nomes)

# 3) Gerar números aleatórios em range:
print(random.sample(range(500), 10))

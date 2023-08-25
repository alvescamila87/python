import random

# Exe03

vetor1 = random.sample(range(1, 100), 10)
vetor2 = random.sample(range(1, 100), 10)
vetor3 = list()

for x in vetor1:
    vetor3.append(x)

for x in vetor2:
    vetor3.append(x)

print("VETOR 1: ", vetor1)
print("VETOR 2: ", vetor2)
print("VETOR 3: ", vetor3)

# Opção 2:

v1 = []
v2 = []
v3 = []

for k in range(10):
    x = random.randint(1, 100)
    v1.append(x)
    v3.append(x)
    x = random.randint(1, 100)
    v2.append(x)
    v3.append(x)

print("OPÇÃO 2 - VETOR 1: ", v1)
print("OPÇÃO 2 - VETOR 2: ", v2)
print("OPÇÃO 2 - VETOR 3: ", v3)

# Opção 3: ZIP

vet1 = random.sample(range(100), 10)
vet2 = random.sample(range(100), 10)
vet3 = []

for x in zip(vet1, vet2):
    vet3.extend(list(x))

print("OPÇÃO 3 - VETOR 1: ", vet1)
print("OPÇÃO 3 - VETOR 2: ", vet2)
print("OPÇÃO 3 - VETOR 3: ", vet3)
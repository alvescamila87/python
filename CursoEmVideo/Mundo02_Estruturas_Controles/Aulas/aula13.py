#Estruturas de repetição for: laço de repetição ou lado de iteração
#Laço com variável de controle (c) no intervalo de (0,10)

for c in range(0,10):
    print(c, "C")

#contar para trás (-1)
for x in range(6, 0, -1):
    print(x)
print("FIM X")


#contar pulando 2 casas
for z in range(0, 7, 2):
    print(z)
print("FIM Z")


#iteração

n = int(input("Digite um número: "))
for y in range(0, n + 1):
    print(y)
print("FIM Y")

#iteracao i, f, p

i = int(input("Início: "))
f = int(input("Fim: "))
p = int(input("Passo: "))

for b in range(i, f+1, p):
    print(b, "B")
print("FIM B")
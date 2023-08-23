
# 1) Imprimir de 1 até um número lido

x = 1
fim = int(input("Digite um número: "))

while x <= fim:
    print(x)
    x = x + 1

# 2) Imprimir números pares

x = 0
fim = int(input("Digite um número: "))
while x <= fim:
    print(x)
    x = x + 2

# 3) Somar 10 números lidos

n = 1
soma = 0
while n <= 10:
    x = int(input(f"Informe o {n} número: "))
    soma = soma + x
    n = n + 1
print(f"A soma é: {soma}.")

# 4) Somar 10 números lidos e calcular a média

n = 1
soma = 0
while n <= 10:
    x = int(input(f"Informe o {n} número: "))
    soma = soma + x
    n = n + 1

print(f"A soma é: {soma} e a média da soma é: {soma / n:.2f}")

# 5) FAT!

k = 1
fat = 1
while k <= 10:
    fat = fat * k
    k = k + 1
print(f"fat(10)! = {fat}")

# 6) FAT! de um número lido

k = 1
fat = 1
fim = int(input(("Número fatoral: ")))
while k <= fim:
    fat = fat * k
    k = k + 1
print(f"fat{fim}! = {fat}")

# 7) Loop até a pessoa digitar '0'

soma = 0
while True:
    n = int(input("Informe um número: [0 para parar] "))
    if n == 0:
        break
    soma = soma + n
print(soma)


# 8) Loop até a pessoa digitar '0' e calcular a média

soma = 0
c = 0
while True:
    n = int(input("Informe um número: [0 para parar] "))
    if n == 0:
       break
    else:
        c = c + 1
    soma = soma + n
print("A média é: ", soma / c)


# Lista de exercícios III - EXE 01

nota = float(input("Digite uma nota: "))
while nota < 0 or nota > 10:
    nota = float(input("Inválido. Tente novamente. Digite uma nota: "))
print(nota)

# Lista de exercícios III - EXE 02

usuario = str(input("Informe nome de usuário: "))
senha = str(input("Informe uma senha: "))
while usuario == senha:
    print("A 'senha informada' precisa ser DIFERENTE do 'nome de usuário'! Tente novamente...")
    senha = str(input("Informe uma senha: "))

print(f"usuário: '{usuario}', senha: '{senha}'")

# Lista de exercícios III - EXE 03 (população igualar ou ultrapassar a outra)

a = 80000
b = 100000
anos = 0
while a <= b:
    a = a + a * 0.03
    b = b + b * 0.015
    anos = anos + 1

print(anos)

# Lista de exercícios III - EXE 04 (Fibonacci)

n = int(input("Digite o valor de n: "))

a, b = 1, 1
k = 1

while k <= n-2:
    a, b = b, a + b
    k = k + 1

print(b)

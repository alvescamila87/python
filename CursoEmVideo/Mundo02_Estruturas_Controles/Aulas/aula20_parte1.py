# Funções: DEFs Python
# Rotina: atividade que faz constantemente

# 0) Parâmetros reais e parâmetros formais

# Parâmetros formais:
def contador(i, f, p):
    print(i, f, p)

# Parâmetros reais:
contador(2,10,2)

# 1) Função SEM parâmetro
def mostraLinha():
    print('-' * 40)

# Chamar sem função:
mostraLinha()
print('         SISTEMA DE ALUNOS           ')
mostraLinha()
print('         CAMILA ALVES           ')
mostraLinha()
print('         PYTHON           ')
mostraLinha()

# 2) Função COM parâmetro
def mensagem(msg):
    print("-="*30)
    print(msg)
    print("-="*30)

# Chamar função com parâmetro
mensagem("CAMILA ALVES")

# 3) Criar função
def titulo(txt):
    print(txt)


# Programa principal
titulo('Blumenau')

# 4) Criar função
def soma(a, b):
    print(f"A = {a} e B = {b}")
    s = a + b
    print(f"A soma A + B = {s}")


# Programa principal
soma(8, 9)
soma(13, 7)
soma(a=15, b=30)
soma(b=45, a=51)

# 5) Empacotar parâmetros (* desempacotar)

def contador(*num):
    print(num) # Na exibição, criará uma tupla com os parâmetros


# Programa principal
contador(4, 3, 5, 6, 9)
contador(1, 2, 7)
contador(8, 4)

# Exemplo 2 (fazer laço)
def contador2(* numeros):
    for valor in numeros:
        print(f"{valor} ", end="")
    print("FIM")


contador2(1,5,6,8,5,4,3,2,1)
contador2(9,8,6,3)

# Exemplo 3 (contar números)
def contador3(* num):
    tamanho = len(num)
    print(f"Recebi os valores: {num} e são ao todo '{tamanho}' números.")


contador3(5,4,3,2,1)
contador3(9,8,)

# 6) Criando funções com listas

def dobraValores(lista):
    posicao = 0
    while posicao < len(valores):
        valores[posicao] *= 2
        posicao += 1

valores = [7,8,9,3,6]
dobraValores(valores)
print(valores)


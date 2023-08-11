# Funções: DEFs Python - PARTE 2: Tópicos a serem abordados:
# Interactive help: utilizar a função interna help() no python
# docstrings: documentação de função
# Argumentos opcionais: funções com argumentos opcionais
# Escopo de variáveis: quando variável 'nasce', 'morre', em que momentos e posições elas são visíveis, isso funciona também para importação de bibliotecas
# Retorno de resultados: retornar resultado das funções

# 1) Interactive help
# help()
# print(input.__doc__)

# 2) DocStrings 

def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    Função criada por Gustavo Guanabara do canal CursoemVídeo.
    """
    c = i
    while c <= f:
        print(f"{c} ", end="")
        c += p
    print("FIM!")


help(contador)

# 3) Parâmetros opcionais

def soma(a=0, b=0, c=0):
    """
    -> Faz a soma de 3 valores e mostra o resultado na tela.
    :param a: o primeiro valor (parâmetro opcional)
    :param b: o segundo valor (parâmetro opcional)
    :param c: o terceiro valor (parâmetro opcional)
    :return: sem retorno
    Função criada por Guanabara.
    """
    s = a + b + c
    print(f"A soma vale {s}.")


soma(3, 2, 5)
soma(8, 4)
soma()
soma(a=3, b=5)

# 4) Escopo de variáveis (Escopo global e local)
# Local onde uma variável vai existir. Também pode ser onde ela não vai existir.

# Escopo LOCAL
def teste():
    x = 8
    print(f"No escopo LOCAL, função teste, n vale {n}.")
    print(f"No escopo LOCAL, função teste, x vale {x}.")


# Escopo GLOBAL
# Programa principal
n = 2
print(f"No escopo GLOBAL, n vale {n}.")
teste()
print(f"No escopo GLOBAL, x vale {x}.")
# n é uma variável GLOBAL
# x é uma variável LOCAL

# Outro exemplo 1:
def teste_escopo(b):
    a = 8
    b += 4
    c = 2
    print(f"A dentro vale {a}.")
    print(f"B dentro vale {b}.")
    print(f"C dentro vale {c}.")


a = 5
teste_escopo(a)
print(f"A fora vale {a}.")

# Outro exemplo 2:
def funcao():
    n = 4
    print(f"N1 dentro vale {n1}")


n1 = 2
funcao()
print(f"N1 fora vale {n1}")

# Aplicar escopo global dentro da função:

def teste(b):
    global a
    a = 8
    b += 4
    c = 2
    print(f"A dentro vale {a}")
    print(f"B dentro vale {b}")
    print(f"C dentro vale {c}")

a = 5
teste(a)
print(f"A fora vale {a}")

# 5) Retorno de valores
# Retornar 'print()' dentro delas OU usar o 'Return'

def somar(a=0, b=0, c=0):
    s = a + b + c
    return s

# Formas de usar o return - Opção1:
print(somar(3,2,5))
print(somar(2,2))
print(somar(6))

# Formas de usar o return - Opção2:

r1 = somar(3,2,5)
r2 = somar(2,2)
r3 = somar(6)
print(f"Os resultados foram: {r1}, {r2} e {r3}.")

# 6) Mais exemplos - Opção1 :

def fatorial(num=1):
    f = 1
    for c in range(num, 0 -1):
        f *= c
    return f

n = int(input("Digite um número: "))
print(f"O fatorial de {n} é igual a {fatorial(n)}.")

# 6) Mais exemplos - Opção2 :

def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False

num = int(input("Digite um número: "))
if par(num):
    print("É par!")
else:
    print("Não é par")

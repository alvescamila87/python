# Criando funções e usando assert para testes

from operator import add
def soma(x, y):
    return x + y

def sub(x, y):
    return  x - y

def mul(x, y):
    return x * y


# Gama de testes:

# 1) Teste soma:
assert soma(5,5) == add(5,5)
# 2) Teste sub:
assert sub(5,5) == -1, "Erro no resultado de sub: {}".format(sub(5,5))
# 3) Teste mul:
assert mul(3,3) == 9, "Erro de multiplicação"
# Funções #8 - HOFs e Módulo operator

"""Operator."""
from operator import add, mul, sub, floordiv, itemgetter
from functools import reduce

print("Utilizando lambda: ", lambda x, y: x + y, [1,2,3,4,5])
print("Utilizando reduce, operator add: ", reduce(add, [1,2,3,4,5]))
print("Utilizando reduce, operador sub: ", reduce(sub, [1,2,3,4,5]))
print("Utilizando reduce, operador mul: ", reduce(mul, [1,2,3,4,5]))
print("Utilizando reduce, operador div: ", reduce(floordiv, [200, 4, 5]))

# Opção 2

palavras = ["amar", "falar", "ler", "meditar", "rezar", "abacate"]

print("Modo exemplo 1 - lambda: ", sorted(palavras, key=lambda string: string[1]))
print("Modo exemplo 2 - itemgetter: ", sorted(palavras, key=itemgetter(1)))
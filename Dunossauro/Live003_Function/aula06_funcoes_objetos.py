# Funções #6 - Funções como objetos de primeira classe
# Função dentro de variável

# Opção 1
funcao = lambda : "resultado da função como objeto de primeira classe"

print(funcao)
print(funcao())

# Opção 2

from typing import Callable, Dict

calc: Dict[str, Callable] = {
    'soma': lambda x, y: x + y,
    'sub': lambda x, y: x - y,
    'mult': lambda x, y: x * y,
    'div': lambda x, y: x / y,
}

print("Verificar o que tem na função calc: ", calc)
print("Operação soma da função calc: ", calc['soma'](2,1))
print("Operação subtração da função calc: ", calc['sub'](3,1))
print("Operação multiplicação da função calc: ", calc['mult'](3,9))
print("Operação divisão da função calc: ", calc['div'](40,5))

# Opção 3 Criar calculadora com função nomeada e tipagem de parâmetros

from numbers import Number
def soma(a: Number, b: Number) -> Number:
    """Soma de dois números."""
    return a + b

def sub(a: Number, b: Number) -> Number:
    """Subtração de dois números."""
    return a - b

def mult(a: Number, b: Number) -> Number:
    """Multiplicação de dois números."""
    return a * b

def div(a: Number, b: Number) -> Number:
    """Divisão de dois números."""
    return a / b

calculadora_nomeada = {
    'soma': soma,
    'sub': sub,
    'multi': mult,
    'div': div,
}

print("Verificar função calculadora nomeada: ", calculadora_nomeada)
print("Calculadora nomeada -> Operação soma: ", calculadora_nomeada['soma'](10,5))
print("Calculadora nomeada -> Operação sub: ", calculadora_nomeada['sub'](50,15))
print("Calculadora nomeada -> Operação multi: ", calculadora_nomeada['multi'](8,8))
print("Calculadora nomeada -> Operação div: ", calculadora_nomeada['div'](15, 3))

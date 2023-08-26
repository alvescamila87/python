# Funções #4 - Anotações de tipos de argumentos
# PEP-484, mypy, monkeytype

# Exemplo 1:
def soma(x: int, y: int) -> int:
    """
    Função soma de números inteiros
    :param x: parâmetro obrigatório, com anotação de 'número inteiro'
    :param y: parâmetro obrigatório, com anotação de 'número inteiro'
    :return: retorna a soma de x + y
    """
    return x + y

print("Concaterou string: ", soma('a', 'b'))
print("Somou números: ", soma(5, 10))

# Exemplo 2 - Numbers and Typing

from numbers import Number
from typing import Union

somavel = Union[Number, str, list]
def soma2(x: somavel, y: somavel) -> somavel:
    return x + y

print(soma2("Camila ", "Blumenau"))
print(soma2(42, 13))

# Exemplo 3 - Typing

from typing import Any

def identidade(val: Any) -> Any:
    return val

print("Retorna algo informado como valor da varável Any: ", identidade(35))

# Exemplo 4 - Typing List

from typing import List

def meu_sum(l: List[int]) -> int:
    return meu_sum(l)

def meu_sum2(l: List[float]) -> int:
    return meu_sum(l)

def meu_sum3(l: List[Number]) -> Number:
    return meu_sum(l)

from typing import Dict
def cadastro_usuario(
        nome: str,
        idade: int,
        atividades: List[str]
) -> Dict[str, Union[str, int, List[str]]]:
    return {
        'nome': nome,
        'idade': idade,
        'atividades': atividades
    }

help(cadastro_usuario)
print("Dicionário: ", cadastro_usuario("Camila", 35, ["cachorro", "podcast", "livros"]))

from typing import Sequence
def meu_min(seq: Sequence):
    return min(seq)


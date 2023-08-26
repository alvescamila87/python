# Funções #3 - Empacotamento e desempacotamento de argumentos

# 1) Args só consegue trabalhar com argumentos posicionais, não nomeados
def minha_soma(*args):
    """
    Função para EMPACOTAR vários argumentos
    :param args: pode passar n argumentos
    :return: retorna soma dos argumentos.
    """
    print(args)
    print(type(args))
    return sum(args)

print("A soma de todos os números passados: ", minha_soma(1,2,3,6,5,4,8,9))

# 2) *args e **kwargs
# posicionais vira tupla e nomeado vira dict
# se usar grupos, não utilizar flags: x ou *

# def minha_soma2(*args, **kwargs):
def minha_soma2(*grupo_posicinais, **grupo_nomeados):
    "Função para EMPACOTAR argumentos"
    print(grupo_posicinais, grupo_nomeados)
    print(type(grupo_posicinais), type(grupo_nomeados))
    return grupo_posicinais, grupo_nomeados

print("Args = grupo posicional e Kwargs = grupo nomeado: ", minha_soma2(1,2,3,4,5))
print("Args = grupo posicional e Kwargs = grupo nomeado: ", minha_soma2(1,2,3,4,5, a=13, b=29))

# 3) Desempacotar

lista = [6,9,8,7,10,50,99]
def desempacotar_min(*args):
    return min(*args)

print("Desempacotar lista: o menor valor é: ", desempacotar_min(*lista))


dicionario = {'a': 1,
              'b': 2,
              'c': 3,
              'd': 4}
def desempacotar_max(a=0, b=0, c=0, d=0):
    return max(a, b, c, d)

print("Desempacotar dicionário: o maior valor é: ", desempacotar_max(**dicionario))

l = [10,20,30]
d = {'d': 40, 'e': 50}
def desempacotar_mix(a, b, c, d=0, e=0):
    return a, b, c, d, e

print("Desempacotar lista e dicionário: ", desempacotar_mix(*l, **d))

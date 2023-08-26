# Funções #2 - Argumentos posicionais, nomeados e o Python 3.8

# Opção de parâmetros com funções anônimas:

anonima = lambda param: param + 2
print("A função anônima de soma: ", anonima(2))

anonima_plus = lambda param1, param2: param1 + param2
print("A função anônima_plusde soma: ", anonima_plus(7, 7))

# Opção de parâmetros com funções defs (funcões nomeadas / normais):

def soma_posicional(x, y):
    """
    Função de soma posicional
    :param x: parâmetro posicional
    :param y: parâmetro posicional
    :return: retorna soma de x + y
    """
    return x + y
print(f"soma posicional: ", soma_posicional(50,13))
print(f"soma posicional: ", soma_posicional(x=5, y=10))
print(f"soma posicional: ", soma_posicional(y=15, x=25))

def soma_nomeados(a=10, b=10):
    """
    Função de soma com parâmetros nomeados, na falta de a ou b, o valor 10 será utilizado.
    :param a: parâmetro nomeado
    :param b: parâmetro nomeado
    :return: retorna soma de a + b
    """

    return a + b

print(f"soma nomeada: ", soma_nomeados())
print(f"soma nomeada: ", soma_nomeados(70,50))
print(f"soma nomeada: ", soma_nomeados(b=1))

# Com asterisco, os demais parâmetros nomeados se tornam obrigatório ao chamar a função
# a ordem de * importa
# só pode ser chamado posicional
# só enviar valores, não funciona, precisa determinar qual parâmetro recebe o valor

def soma_explicitamente_nomeados(*, a=5, b=5):
    """
    Função de soma com parâmetros nomeados, na falta de a ou b, o valor 10 será utilizado.
    :param a: parâmetro nomeado
    :param b: parâmetro nomeado
    :return: retorna soma de a + b
    """

    return a + b

print(f"Explicitamente nomeados: ", soma_explicitamente_nomeados())
print(f"Explicitamente nomeados: ",soma_explicitamente_nomeados(a=70,b=50))
print(f"Explicitamente nomeados: ", soma_explicitamente_nomeados(b=8,a=8))

# Com barra /, só pode chamar de forma posicional, sem informar de qual parâmetro pertence
def soma_explicitamente_posicional(a=2, b=2, /):
    return a + b

print(f"Explicitamente posicinal: ", soma_explicitamente_posicional(5,5))
print(f"Explicitamente posicinal: ", soma_explicitamente_posicional(50,70))

# Com / (antes da barra permite posicional) e * (após o astericso permite só nomeado), de forma mix

def soma_mix(d, e, /, f, *, g):
    """

    :param d: posicional
    :param e: posicional
    :param f: nomeado
    :param g: nomeado
    :return:
    """
    return sum((d, e, f, g))

print("soma mix: posicional e nomeado: ", soma_mix(1,2,f=3,g=5))